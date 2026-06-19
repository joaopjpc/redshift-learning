"""Busca de hiperparametros para Polynomial Ridge."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

import pandas as pd

SRC_DIR = Path(__file__).resolve().parents[2]
if str(SRC_DIR) not in sys.path:
    sys.path.append(str(SRC_DIR))

from redshift.models.polynomial_ridge import (  # noqa: E402
    METRICS_DIR,
    MODEL_NAME,
    MODELS_DIR,
    run_experiment,
)
from redshift.utils.modeling import (  # noqa: E402
    FEATURE_SETS,
    PROCESSED_DATA_DIR,
    TABLES_DIR,
    table_output_path,
)


DEFAULT_DEGREES = [1, 2, 3]
DEFAULT_ALPHAS = [1, 10, 100, 1000, 10000, 100000]


def summarize_metrics(metrics: dict[str, Any]) -> dict[str, Any]:
    """Achata o JSON de metricas em uma linha tabular."""

    eval_split = metrics["eval_split"]
    model_params = metrics["model_params"]
    split_metrics = metrics["metrics"]

    return {
        "experiment_name": metrics["experiment_name"],
        "dataset": metrics["dataset"],
        "feature_set": metrics["feature_set"],
        "eval_split": eval_split,
        "degree": model_params["degree"],
        "alpha": model_params["alpha"],
        "mae": split_metrics[f"{eval_split}_mae"],
        "rmse": split_metrics[f"{eval_split}_rmse"],
        "r2": split_metrics[f"{eval_split}_r2"],
        "bias": split_metrics[f"{eval_split}_bias"],
        "n": split_metrics[f"{eval_split}_n"],
        "catastrophic_outlier_fraction": split_metrics[
            f"{eval_split}_catastrophic_outlier_fraction"
        ],
        "negative_redshift_predictions": split_metrics[
            f"{eval_split}_negative_redshift_predictions"
        ],
    }


def run_search(
    dataset: str,
    feature_set: str = "mag",
    eval_split: str = "val",
    degrees: list[int] | None = None,
    alphas: list[float] | None = None,
    processed_data_dir: Path = PROCESSED_DATA_DIR,
    models_dir: Path = MODELS_DIR,
    metrics_dir: Path = METRICS_DIR,
    tables_dir: Path = TABLES_DIR,
) -> pd.DataFrame:
    """Executa a busca em grade e salva uma tabela resumo."""

    degrees = degrees or DEFAULT_DEGREES
    alphas = alphas or DEFAULT_ALPHAS

    rows = []
    for degree in degrees:
        for alpha in alphas:
            metrics = run_experiment(
                dataset=dataset,
                feature_set=feature_set,
                eval_split=eval_split,
                degree=degree,
                alpha=alpha,
                processed_data_dir=processed_data_dir,
                models_dir=models_dir,
                metrics_dir=metrics_dir,
            )
            rows.append(summarize_metrics(metrics))

    results = pd.DataFrame(rows).sort_values(
        by=["mae", "rmse"],
        ascending=[True, True],
    )

    output_path = table_output_path(
        tables_dir=tables_dir,
        eval_split=eval_split,
        feature_set=feature_set,
        model_name=MODEL_NAME,
        dataset=dataset,
        filename=f"{MODEL_NAME}_{feature_set}_{eval_split}_search.csv",
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    results.to_csv(output_path, index=False)

    return results


def parse_args() -> argparse.Namespace:
    """Define argumentos de linha de comando."""

    parser = argparse.ArgumentParser(
        description="Busca hiperparametros de Polynomial Ridge."
    )
    parser.add_argument(
        "--dataset",
        choices=["happyT", "teddyT"],
        default="happyT",
        help="Dataset processado em data/processed.",
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
        help="Split usado para avaliacao. Para busca, use val.",
    )
    parser.add_argument(
        "--degrees",
        type=int,
        nargs="+",
        default=DEFAULT_DEGREES,
        help="Graus testados nas PolynomialFeatures.",
    )
    parser.add_argument(
        "--alphas",
        type=float,
        nargs="+",
        default=DEFAULT_ALPHAS,
        help="Valores de alpha testados no Ridge.",
    )
    parser.add_argument(
        "--processed-data-dir",
        type=Path,
        default=PROCESSED_DATA_DIR,
        help="Diretorio base com datasets processados.",
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
        "--tables-dir",
        type=Path,
        default=TABLES_DIR,
        help="Diretorio para salvar tabelas resumo.",
    )

    return parser.parse_args()


def main() -> None:
    """Executa a busca pelo terminal."""

    args = parse_args()
    results = run_search(
        dataset=args.dataset,
        feature_set=args.feature_set,
        eval_split=args.eval_split,
        degrees=args.degrees,
        alphas=args.alphas,
        processed_data_dir=args.processed_data_dir,
        models_dir=args.models_dir,
        metrics_dir=args.metrics_dir,
        tables_dir=args.tables_dir,
    )

    print("Melhores combinacoes por MAE:")
    print(results.head(10).to_string(index=False))


if __name__ == "__main__":
    main()
