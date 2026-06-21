"""Regressao polinomial com regularizacao Ridge para redshift fotometrico."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer, PolynomialFeatures, StandardScaler

SRC_DIR = Path(__file__).resolve().parents[2]
if str(SRC_DIR) not in sys.path:
    sys.path.append(str(SRC_DIR))

from redshift.utils.modeling import (
    FEATURE_SETS,
    build_metadata,
    dataset_metrics_dir_name,
    evaluate_predictions,
    figure_output_path,
    get_feature_cols,
    metrics_output_path,
    model_artifacts_dir,
    model_output_path,
    model_figures_dir,
    model_metrics_dir,
    print_regression_summary,
    save_json,
    save_model_artifact,
    validate_feature_columns,
)
from redshift.evaluation.plots import save_redshift_residual_plot
from redshift.data.preprocess import (
    RAW_DATA_DIR,
    load_raw_datasets,
    split_features_target,
    split_train_validation_from_a,
    transform_target,
)


MODEL_NAME = "polynomial_ridge"
MODEL_LABEL = "PolynomialFeatures+Ridge"
MODELS_DIR = model_artifacts_dir(MODEL_NAME)
FIGURES_DIR = model_figures_dir(MODEL_NAME)
METRICS_DIR = model_metrics_dir(MODEL_NAME)


def train_polynomial_ridge(
    X_train: pd.DataFrame,
    y_train: pd.Series,
    feature_cols: list[str],
    degree: int = 2,
    alpha: float = 1.0,
) -> Pipeline:
    """Treina PolynomialFeatures seguido de Ridge."""

    validate_feature_columns(X_train, feature_cols)

    model = Pipeline(
        steps=[
            ("poly", PolynomialFeatures(degree=degree, include_bias=False)),
            ("log1p", FunctionTransformer(np.log1p, validate=False)),
            ("scaler", StandardScaler()),
            ("ridge", Ridge(alpha=alpha)),
        ]
    )
    model.fit(X_train.loc[:, feature_cols], y_train)

    return model


def run_experiment(
    dataset: str,
    feature_set: str = "mag",
    eval_split: str = "val",
    degree: int = 2,
    alpha: float = 1.0,
    raw_data_dir: Path = RAW_DATA_DIR,
    models_dir: Path = MODELS_DIR,
    figures_dir: Path = FIGURES_DIR,
    metrics_dir: Path = METRICS_DIR,
) -> dict[str, Any]:
    """Executa o experimento Polynomial Ridge e salva artefatos."""

    train_val_df, test_dfs = load_raw_datasets(dataset_name=dataset, raw_dir=raw_data_dir)
    train_df, val_df = split_train_validation_from_a(train_val_df)
    test_df = pd.concat(test_dfs.values(), axis=0, ignore_index=True)

    X_train, y_train_raw = split_features_target(train_df)
    X_val, y_val_raw = split_features_target(val_df)
    X_test, y_test_raw = split_features_target(test_df)

    y_train = transform_target(y_train_raw)
    y_val = transform_target(y_val_raw)
    y_test = transform_target(y_test_raw)
    feature_cols = get_feature_cols(feature_set)
    validate_feature_columns(X_train, feature_cols)
    validate_feature_columns(X_val, feature_cols)
    validate_feature_columns(X_test, feature_cols)

    X_fit = X_train
    y_fit = y_train
    X_eval = X_val
    y_eval = y_val
    if eval_split == "test":
        X_fit = pd.concat([X_train, X_val], axis=0, ignore_index=True)
        y_fit = pd.concat([y_train, y_val], axis=0, ignore_index=True)
        X_eval = X_test
        y_eval = y_test

    model = train_polynomial_ridge(
        X_train=X_fit,
        y_train=y_fit,
        feature_cols=feature_cols,
        degree=degree,
        alpha=alpha,
    )
    eval_pred = model.predict(X_eval.loc[:, feature_cols])

    experiment_name = f"{MODEL_NAME}_{feature_set}_degree{degree}_alpha{alpha:g}"
    metadata = build_metadata(
        experiment_name=experiment_name,
        dataset=dataset,
        model_label=MODEL_LABEL,
        feature_set=feature_set,
        eval_split=eval_split,
        feature_cols=feature_cols,
        model_params={
            "degree": degree,
            "include_bias": False,
            "alpha": alpha,
            "feature_transform": [
                "PolynomialFeatures",
                "log1p",
                "StandardScaler",
            ],
        },
    )
    metrics: dict[str, Any] = {
        **metadata,
        "metrics": evaluate_predictions(y_eval, eval_pred, eval_split),
    }

    save_model_artifact(
        model=model,
        feature_cols=feature_cols,
        metadata=metadata,
        path=model_output_path(
            models_dir=models_dir,
            eval_split=eval_split,
            feature_set=feature_set,
            model_name=MODEL_NAME,
            dataset=dataset,
            filename=f"{experiment_name}_{eval_split}.joblib",
        ),
    )
    save_json(
        metrics,
        metrics_output_path(
            metrics_dir=metrics_dir,
            eval_split=eval_split,
            feature_set=feature_set,
            model_name=MODEL_NAME,
            dataset=dataset,
            filename=(
                f"{MODEL_NAME}_{dataset_metrics_dir_name(dataset)}_"
                f"{feature_set}_degree{degree}_alpha{alpha:g}_{eval_split}_metrics.json"
            ),
        ),
    )
    save_redshift_residual_plot(
        y_true=np.expm1(y_eval),
        y_pred=np.expm1(eval_pred),
        path=figure_output_path(
            figures_dir=figures_dir,
            eval_split=eval_split,
            feature_set=feature_set,
            model_name=MODEL_NAME,
            dataset=dataset,
            filename=f"{experiment_name}_{eval_split}_residuals.png",
        ),
        title=f"{MODEL_LABEL} | {dataset} | {feature_set} | {eval_split}",
    )

    return metrics


def parse_args() -> argparse.Namespace:
    """Define argumentos de linha de comando."""

    parser = argparse.ArgumentParser(
        description="Treina Regressao Polinomial com regularizacao Ridge."
    )
    parser.add_argument(
        "--dataset",
        choices=["happyT", "teddyT"],
        default="happyT",
        help="Dataset bruto em data/raw.",
    )
    parser.add_argument(
        "--feature-set",
        choices=list(FEATURE_SETS),
        default="mag",
        help="Conjunto de features: mag usa magnitudes; mag_err usa magnitudes e erros.",
    )
    parser.add_argument(
        "--eval-split",
        choices=["val", "test"],
        default="val",
        help="Split usado para avaliacao: val para selecao de modelo; test para avaliacao final.",
    )
    parser.add_argument(
        "--degree",
        type=int,
        default=2,
        help="Grau das PolynomialFeatures.",
    )
    parser.add_argument(
        "--alpha",
        type=float,
        default=1.0,
        help="Forca da regularizacao Ridge.",
    )
    parser.add_argument(
        "--raw-data-dir",
        type=Path,
        default=RAW_DATA_DIR,
        help="Diretorio base com datasets brutos.",
    )
    parser.add_argument(
        "--models-dir",
        type=Path,
        default=MODELS_DIR,
        help="Diretorio para salvar modelos.",
    )
    parser.add_argument(
        "--metrics-dir",
        type=Path,
        default=METRICS_DIR,
        help="Diretorio para salvar metricas.",
    )
    parser.add_argument(
        "--figures-dir",
        type=Path,
        default=FIGURES_DIR,
        help="Diretorio para salvar figuras de avaliacao.",
    )

    return parser.parse_args()


def main() -> None:
    """Executa o modelo pelo terminal."""

    args = parse_args()
    metrics = run_experiment(
        dataset=args.dataset,
        feature_set=args.feature_set,
        eval_split=args.eval_split,
        degree=args.degree,
        alpha=args.alpha,
        raw_data_dir=args.raw_data_dir,
        models_dir=args.models_dir,
        figures_dir=args.figures_dir,
        metrics_dir=args.metrics_dir,
    )
    print_regression_summary(metrics)


if __name__ == "__main__":
    main()
