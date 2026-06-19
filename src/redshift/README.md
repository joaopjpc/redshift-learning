# Modelos e model selection

Este README documenta apenas os scripts de modelagem e selecao de modelos criados ate agora.

## Estrutura

```text
src/redshift/
  models/
    linear_regression.py
    polynomial_ridge.py
  training/
    search_polynomial_ridge.py
  utils/
    modeling.py
```

`utils/modeling.py` concentra codigo comum aos modelos:

- leitura de `data/processed/<dataset>/`;
- selecao de features `mag` ou `mag_err`;
- selecao de split de avaliacao `val` ou `test`;
- metricas na escala original do redshift;
- salvamento de modelos `.joblib`;
- salvamento de metricas `.json`;
- caminhos padronizados para tabelas `.csv`.

## Feature sets

`mag` usa apenas magnitudes:

```text
u, g, r, i, z
```

`mag_err` usa magnitudes e erros fotometricos:

```text
u, g, r, i, z, uErr, gErr, rErr, iErr, zErr
```

## Splits de avaliacao

`--eval-split val` deve ser usado para model selection.

```text
treina em: train
avalia em: validation
```

`--eval-split test` deve ser usado apenas para avaliacao final.

```text
treina em: train
avalia em: test externo
```

Por decisao do projeto, mesmo em `--eval-split test`, o conjunto de validacao nao e adicionado ao treino.

## Metricas

As metricas sao calculadas sempre na escala original do redshift, aplicando `expm1` nas predicoes e no alvo antes da avaliacao.

Metricas salvas:

```text
mae
rmse
r2
bias
n
negative_redshift_predictions
catastrophic_outlier_fraction
catastrophic_outlier_threshold
```

A fracao de outliers catastroficos usa:

```text
abs(z_pred - z_real) / (1 + z_real) > 0.15
```

## Organizacao das metricas

As metricas sao salvas em:

```text
reports/metrics/<Model Selection ou Tests>/<dataset>/<feature_set>/<modelo>/
```

Mapeamento de nomes de dataset nas pastas:

```text
happyT -> happy
teddyT -> teddy
```

Exemplos:

```text
reports/metrics/Model Selection/happy/mag/linear_regression/
reports/metrics/Model Selection/happy/mag_err/polynomial_ridge/
reports/metrics/Tests/teddy/mag/polynomial_ridge/
```

## Regressao Linear

Script:

```text
src/redshift/models/linear_regression.py
```

Rodar MAG em validacao:

```powershell
.\.venv\Scripts\python.exe src\redshift\models\linear_regression.py --dataset happyT --feature-set mag --eval-split val
```

Rodar MAG+ERR em validacao:

```powershell
.\.venv\Scripts\python.exe src\redshift\models\linear_regression.py --dataset happyT --feature-set mag_err --eval-split val
```

Rodar avaliacao final em teste:

```powershell
.\.venv\Scripts\python.exe src\redshift\models\linear_regression.py --dataset happyT --feature-set mag --eval-split test
```

## Polynomial Ridge

Script:

```text
src/redshift/models/polynomial_ridge.py
```

O modelo usa:

```python
PolynomialFeatures(degree=degree, include_bias=False)
Ridge(alpha=alpha)
```

Rodar uma configuracao especifica:

```powershell
.\.venv\Scripts\python.exe src\redshift\models\polynomial_ridge.py --dataset happyT --feature-set mag --eval-split val --degree 2 --alpha 1
```

Com MAG+ERR:

```powershell
.\.venv\Scripts\python.exe src\redshift\models\polynomial_ridge.py --dataset happyT --feature-set mag_err --eval-split val --degree 2 --alpha 1
```

## Busca de hiperparametros do Polynomial Ridge

Script:

```text
src/redshift/training/search_polynomial_ridge.py
```

Grid padrao:

```python
degrees = [1, 2, 3]
alphas = [1, 10, 100, 1000, 10000, 100000]
```

Rodar busca em MAG:

```powershell
.\.venv\Scripts\python.exe src\redshift\training\search_polynomial_ridge.py --dataset happyT --feature-set mag --eval-split val
```

Rodar busca em MAG+ERR:

```powershell
.\.venv\Scripts\python.exe src\redshift\training\search_polynomial_ridge.py --dataset happyT --feature-set mag_err --eval-split val
```

Customizar a grade:

```powershell
.\.venv\Scripts\python.exe src\redshift\training\search_polynomial_ridge.py --dataset happyT --feature-set mag --eval-split val --degrees 1 2 3 --alphas 1 10 100
```

A busca salva:

- JSON individual para cada combinacao em `reports/metrics/...`;
- tabela resumo ordenada por `mae` e depois `rmse` em `reports/tables/...`.

Exemplo de tabela:

```text
reports/tables/Model Selection/happy/mag/polynomial_ridge/polynomial_ridge_mag_val_search.csv
```

## Teddy

Para rodar qualquer comando no Teddy, troque:

```powershell
--dataset happyT
```

por:

```powershell
--dataset teddyT
```
