"""Funcoes compartilhadas entre scripts de modelos."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import joblib
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


PROJECT_ROOT = Path(__file__).resolve().parents[3]
PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"
MODELS_DIR = PROJECT_ROOT / "models"
METRICS_DIR = PROJECT_ROOT / "reports" / "metrics"
TABLES_DIR = PROJECT_ROOT / "reports" / "tables"

MAG_FEATURES = ["u", "g", "r", "i", "z"]
ERR_FEATURES = ["uErr", "gErr", "rErr", "iErr", "zErr"]
FEATURE_SETS = {
    "mag": MAG_FEATURES,
    "mag_err": MAG_FEATURES + ERR_FEATURES,
}
EVAL_SPLIT_PURPOSES = {
    "val": "model_selection",
    "test": "final_evaluation",
}
EVAL_SPLIT_METRICS_DIRS = {
    "val": "Model Selection",
    "test": "Tests",
}
DATASET_METRICS_DIRS = {
    "happyT": "happy",
    "teddyT": "teddy",
}
TARGET_TRANSFORM = "log1p(redshift)"
CATASTROPHIC_OUTLIER_THRESHOLD = 0.15


def model_artifacts_dir(model_name: str) -> Path:
    """Retorna a pasta padrao para artefatos de um modelo."""

    return MODELS_DIR / model_name


def model_metrics_dir(model_name: str) -> Path:
    """Retorna a pasta raiz das metricas.

    O argumento e mantido para usar a mesma assinatura dos scripts de modelo,
    mas a organizacao final fica:
    metrics/Model Selection ou Tests/dataset/feature_set/model.
    """

    return METRICS_DIR


def dataset_metrics_dir_name(dataset: str) -> str:
    """Retorna o nome da pasta de metricas para um dataset."""

    return DATASET_METRICS_DIRS.get(dataset, dataset)


def metrics_output_path(
    metrics_dir: Path,
    eval_split: str,
    feature_set: str,
    model_name: str,
    dataset: str,
    filename: str,
) -> Path:
    """Monta o caminho padrao de metricas para um experimento."""

    if eval_split not in EVAL_SPLIT_METRICS_DIRS:
        available = ", ".join(EVAL_SPLIT_METRICS_DIRS)
        raise ValueError(f"Split de avaliacao invalido: {eval_split}. Opcoes: {available}")

    return (
        metrics_dir
        / EVAL_SPLIT_METRICS_DIRS[eval_split]
        / dataset_metrics_dir_name(dataset)
        / feature_set
        / model_name
        / filename
    )


def table_output_path(
    tables_dir: Path,
    eval_split: str,
    feature_set: str,
    model_name: str,
    dataset: str,
    filename: str,
) -> Path:
    """Monta o caminho padrao de tabelas para uma busca/experimento."""

    if eval_split not in EVAL_SPLIT_METRICS_DIRS:
        available = ", ".join(EVAL_SPLIT_METRICS_DIRS)
        raise ValueError(f"Split de avaliacao invalido: {eval_split}. Opcoes: {available}")

    return (
        tables_dir
        / EVAL_SPLIT_METRICS_DIRS[eval_split]
        / dataset_metrics_dir_name(dataset)
        / feature_set
        / model_name
        / filename
    )


def load_processed_split(
    dataset_dir: Path,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.Series, pd.Series, pd.Series]:
    """Carrega os splits processados de um dataset."""

    X_train = pd.read_csv(dataset_dir / "X_train.csv")
    X_val = pd.read_csv(dataset_dir / "X_val.csv")
    X_test = pd.read_csv(dataset_dir / "X_test.csv")
    y_train = pd.read_csv(dataset_dir / "y_train.csv").squeeze("columns")
    y_val = pd.read_csv(dataset_dir / "y_val.csv").squeeze("columns")
    y_test = pd.read_csv(dataset_dir / "y_test.csv").squeeze("columns")

    return X_train, X_val, X_test, y_train, y_val, y_test


def validate_feature_columns(X: pd.DataFrame, feature_cols: list[str]) -> None:
    """Garante que as features esperadas existem no dataframe."""

    missing = [col for col in feature_cols if col not in X.columns]
    if missing:
        raise ValueError(f"Features ausentes: {', '.join(missing)}")


def get_feature_cols(feature_set: str) -> list[str]:
    """Retorna as colunas do conjunto de features escolhido."""

    if feature_set not in FEATURE_SETS:
        available = ", ".join(FEATURE_SETS)
        raise ValueError(f"Feature set invalido: {feature_set}. Opcoes: {available}")

    return FEATURE_SETS[feature_set]


def get_eval_data(
    eval_split: str,
    X_val: pd.DataFrame,
    y_val: pd.Series,
    X_test: pd.DataFrame,
    y_test: pd.Series,
) -> tuple[pd.DataFrame, pd.Series]:
    """Seleciona o split usado para avaliacao."""

    eval_data = {
        "val": (X_val, y_val),
        "test": (X_test, y_test),
    }
    if eval_split not in eval_data:
        available = ", ".join(eval_data)
        raise ValueError(f"Split de avaliacao invalido: {eval_split}. Opcoes: {available}")

    return eval_data[eval_split]


def regression_metrics(
    y_true: pd.Series | np.ndarray,
    y_pred: np.ndarray,
    prefix: str,
) -> dict[str, float | int]:
    """Calcula metricas basicas de regressao."""

    y_true_array = np.asarray(y_true)
    residuals = y_pred - y_true_array

    return {
        f"{prefix}_mae": float(mean_absolute_error(y_true_array, y_pred)),
        f"{prefix}_rmse": float(np.sqrt(mean_squared_error(y_true_array, y_pred))),
        f"{prefix}_r2": float(r2_score(y_true_array, y_pred)),
        f"{prefix}_bias": float(np.mean(residuals)),
        f"{prefix}_n": int(len(y_true_array)),
    }


def evaluate_predictions(
    y_true_log: pd.Series,
    y_pred_log: np.ndarray,
    split_name: str,
) -> dict[str, float | int]:
    """Avalia sempre na escala original de redshift."""

    y_true_redshift = np.expm1(y_true_log)
    y_pred_redshift = np.expm1(y_pred_log)
    metrics = regression_metrics(y_true_redshift, y_pred_redshift, split_name)
    normalized_abs_error = np.abs(y_pred_redshift - y_true_redshift) / (
        1 + y_true_redshift
    )
    catastrophic_outliers = (
        normalized_abs_error > CATASTROPHIC_OUTLIER_THRESHOLD
    )
    metrics[f"{split_name}_negative_redshift_predictions"] = int(np.sum(y_pred_redshift < 0))
    metrics[f"{split_name}_catastrophic_outlier_fraction"] = float(
        np.mean(catastrophic_outliers)
    )
    metrics[f"{split_name}_catastrophic_outlier_threshold"] = (
        CATASTROPHIC_OUTLIER_THRESHOLD
    )

    return metrics


def build_metadata(
    experiment_name: str,
    dataset: str,
    model_label: str,
    feature_set: str,
    eval_split: str,
    feature_cols: list[str],
    model_params: dict[str, Any],
) -> dict[str, Any]:
    """Monta metadados reprodutiveis do experimento."""

    return {
        "experiment_name": experiment_name,
        "dataset": dataset,
        "model": model_label,
        "feature_set": feature_set,
        "eval_split": eval_split,
        "evaluation_purpose": EVAL_SPLIT_PURPOSES[eval_split],
        "target": TARGET_TRANSFORM,
        "features": feature_cols,
        "n_features": len(feature_cols),
        "model_params": model_params,
        "created_at_utc": datetime.now(timezone.utc).strftime("%H:%M"),
    }


def save_json(data: dict[str, Any], path: Path) -> None:
    """Salva dicionario em JSON com indentacao."""

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def save_model_artifact(
    model: Any,
    feature_cols: list[str],
    metadata: dict[str, Any],
    path: Path,
) -> None:
    """Salva o modelo junto com colunas e metadados."""

    path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(
        {
            "model": model,
            "feature_cols": feature_cols,
            "target_transform": TARGET_TRANSFORM,
            "metadata": metadata,
        },
        path,
    )


def print_regression_summary(metrics: dict[str, Any]) -> None:
    """Mostra um resumo curto do experimento no terminal."""

    eval_split = metrics["eval_split"]
    mae_key = f"{eval_split}_mae"
    rmse_key = f"{eval_split}_rmse"

    print(f"Experimento: {metrics['experiment_name']}")
    print(f"Dataset: {metrics['dataset']}")
    print(f"Feature set: {metrics['feature_set']}")
    print(f"Eval split: {metrics['eval_split']} ({metrics['evaluation_purpose']})")
    print(f"Features: {', '.join(metrics['features'])}")
    print(f"{eval_split} MAE redshift: {metrics['metrics'][mae_key]:.6f}")
    print(f"{eval_split} RMSE redshift: {metrics['metrics'][rmse_key]:.6f}")
