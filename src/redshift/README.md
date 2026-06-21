# Modelos e model selection

Este README documenta apenas os scripts de modelagem e selecao de modelos criados ate agora.

## Estrutura

```text
src/redshift/
  evaluation/
    plots.py
  models/
    linear_regression.py
    polynomial_ridge.py
  training/
    search_polynomial_ridge.py
  utils/
    modeling.py
```

`utils/modeling.py` concentra codigo comum aos modelos:

- leitura de `data/processed/<dataset>/` para modelos que usam os splits ja preprocessados;
- selecao de features `mag` ou `mag_err`;
- selecao de split de avaliacao `val` ou `test`;
- caminhos padronizados para modelos `.joblib`;
- metricas na escala original do redshift;
- caminhos padronizados para figuras `.png`;
- salvamento de metricas `.json`;
- caminhos padronizados para tabelas `.csv`.

`evaluation/plots.py` concentra visualizacoes de avaliacao. No momento, ele salva um grafico com:

- dispersao de redshift real vs previsto;
- dispersao de residuos (`previsto - real`) vs redshift previsto.

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
treina em: train + validation
avalia em: test externo
```

Em outras palavras:

- `val`: o modelo e ajustado apenas em `X_train` e comparado em `X_val`;
- `test`: depois da selecao do modelo, o ajuste final usa `X_train + X_val` e a avaliacao acontece em `X_test`.

Se o split escolhido estiver vazio ou incompleto, a execucao falha com erro explicito.
Isso e importante especialmente para datasets em que `y_test.csv` possa estar ausente ou vazio:

- `--eval-split val` continua funcionando, pois `y_test` nao e usado;
- `--eval-split test` exige `X_test` e `y_test` validos.

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

Os arquivos `.json` de metricas incluem o dataset no nome. Exemplos:

```text
linear_regression_happy_mag_val_metrics.json
polynomial_ridge_teddy_mag_err_degree2_alpha10_val_metrics.json
```

## Organizacao dos modelos

Os artefatos `.joblib` sao salvos em:

```text
models/<Model Selection ou Tests>/<dataset>/<feature_set>/<modelo>/
```

Exemplos:

```text
models/Model Selection/happy/mag/linear_regression/
models/Model Selection/happy/mag_err/polynomial_ridge/
models/Tests/teddy/mag/linear_regression/
```

## Organizacao das figuras

Os graficos de avaliacao sao salvos em:

```text
reports/figures/<Model Selection ou Tests>/<dataset>/<feature_set>/<modelo>/
```

Exemplos:

```text
reports/figures/Model Selection/happy/mag/linear_regression/
reports/figures/Model Selection/happy/mag_err/polynomial_ridge/
```

## Regressao Linear

Script:

```text
src/redshift/models/linear_regression.py
```

A regressao linear continua usando diretamente os arquivos de `data/processed/<dataset>/`.

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

Saidas geradas por execucao:

- modelo `.joblib` em `models/...`;
- metricas `.json` em `reports/metrics/...`;
- grafico de residuos `.png` em `reports/figures/...`.

## Polynomial Ridge

Script:

```text
src/redshift/models/polynomial_ridge.py
```

O pipeline do Polynomial Ridge foi invertido.

Antes:

```text
dados preprocessados -> PolynomialFeatures -> Ridge
```

Agora:

```text
dados brutos -> PolynomialFeatures -> log1p nas features expandidas -> StandardScaler -> Ridge
```

O alvo continua sendo transformado com `log1p(redshift)`.

Por isso, diferentemente da regressao linear, o `polynomial_ridge.py` nao depende mais de `data/processed/<dataset>/` para montar as features de entrada. Ele recria internamente os splits a partir de `data/raw/`, usando:

- `A` para `train/validation`;
- `B + C + D` para `test`;
- o mesmo split estratificado de `A` para separar `train` e `validation`.

O modelo usa:

```python
PolynomialFeatures(degree=degree, include_bias=False)
FunctionTransformer(np.log1p, validate=False)
StandardScaler()
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

Se quiser apontar outra pasta com os arquivos brutos:

```powershell
.\.venv\Scripts\python.exe src\redshift\models\polynomial_ridge.py --dataset happyT --feature-set mag --eval-split val --degree 2 --alpha 1 --raw-data-dir data\raw
```

Cada execucao do `polynomial_ridge.py` tambem salva automaticamente um grafico `.png` com:

- redshift real vs previsto;
- residuos (`previsto - real`) vs previsto.

## Busca de hiperparametros do Polynomial Ridge

Script:

```text
src/redshift/training/search_polynomial_ridge.py
```

Grid padrao:

```python
degrees = [1, 2, 3]
alphas = [0.1, 0.5, 1, 2, 5, 10, 50, 100, 1000]
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

Se quiser usar outra pasta com os arquivos brutos:

```powershell
.\.venv\Scripts\python.exe src\redshift\training\search_polynomial_ridge.py --dataset happyT --feature-set mag --eval-split val --raw-data-dir data\raw
```

A busca salva:

- JSON individual para cada combinacao em `reports/metrics/...`;
- grafico individual para cada combinacao em `reports/figures/...`;
- tabela resumo ordenada por `rmse` e depois `mae` em `reports/tables/...`.

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
