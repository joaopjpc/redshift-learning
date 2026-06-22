# Modelos e model selection

Este README documenta o pre-processamento, os modelos baseline e a selecao de
modelos para estimacao de redshift fotometrico.

## Estrutura

```text
src/redshift/
  data/
    preprocess.py
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

## Visao geral

Dois baselines de regressao sao comparados nos dois datasets COIN:

- **Datasets**: `happyT` (COIN/Happy) e `teddyT` (COIN/Teddy).
- **Modelos**: Regressao Linear e Polynomial Ridge (`PolynomialFeatures` + `Ridge`).
- **Conjuntos de features**:
  - `mag`: apenas magnitudes;
  - `mag_err`: magnitudes + erros fotometricos.

Fluxo de trabalho:

1. Pre-processar os dados (`data/preprocess.py`).
2. Selecionar hiperparametros na **validacao** (so o Polynomial Ridge tem busca).
3. Avaliar **uma unica vez** no teste externo (`B + C + D`).

`utils/modeling.py` concentra o codigo comum: leitura de `data/processed/`, selecao
de features e split de avaliacao, metricas na escala original do redshift, e os
caminhos padronizados de modelos, metricas, figuras e tabelas.

`evaluation/plots.py` salva o grafico de avaliacao (real vs previsto e residuos).
A geracao da figura e **nao-fatal**: se o backend do matplotlib estiver bloqueado
pelo sistema operacional, a execucao apenas avisa e continua, preservando metricas,
modelos e tabelas.

## Pre-processamento (`data/preprocess.py`)

**Os dois modelos consomem os splits ja preprocessados em
`data/processed/<dataset>/`.** O pre-processamento e ajustado **apenas no treino**
(sem vazamento) e depois aplicado a validacao e teste:

| Grupo de colunas      | Transformacao                  |
| --------------------- | ------------------------------ |
| magnitudes `u,g,r,i,z`| `StandardScaler`               |
| erros `uErr..zErr`    | `log1p` e depois `RobustScaler`|
| alvo `redshift`       | `log1p` (sem scaler)           |

- O `log1p` nos **erros** reduz a assimetria das medidas; o `log1p` no **alvo**
  lineariza a escala de redshift.
- Ponto importante: o `log1p` e aplicado nas **features brutas** (erros), **antes**
  de qualquer expansao polinomial. As metricas voltam para a escala original de
  redshift aplicando `expm1` nas predicoes e no alvo.

Split dos dados:

- conjunto `A` -> `train`/`validation` (80%/20%, estratificado por faixa de redshift);
- conjuntos `B`, `C`, `D` -> teste externo (concatenados).

Gerar os dados processados (uma vez por dataset):

```powershell
.\.venv\Scripts\python.exe src\redshift\data\preprocess.py --dataset happyT
.\.venv\Scripts\python.exe src\redshift\data\preprocess.py --dataset teddyT
```

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
avalia em: test externo (B + C + D)
```

Em outras palavras:

- `val`: o modelo e ajustado apenas em `X_train` e comparado em `X_val`;
- `test`: depois da selecao do modelo, o ajuste final usa `X_train + X_val` e a
  avaliacao acontece em `X_test`.

Se o split escolhido estiver vazio ou incompleto, a execucao falha com erro explicito.

## Metricas

As metricas sao calculadas sempre na **escala original do redshift**, aplicando
`expm1` nas predicoes e no alvo antes da avaliacao. Sao iguais para os dois modelos,
pois ambos usam a mesma funcao `evaluate_predictions`.

```text
mae
rmse
r2
bias
n
negative_redshift_predictions
catastrophic_outlier_fraction
catastrophic_outlier_threshold
nmad
nmad_se
```

Erro normalizado de redshift:

```text
dz = (z_pred - z_real) / (1 + z_real)
```

- **Fracao de outliers catastroficos**: proporcao de objetos com `|dz| > 0.15`.
- **NMAD** (dispersao robusta de photo-z): `1.4826 * mediana(|dz - mediana(dz)|)`.
  O fator `1.4826` faz o NMAD coincidir com o desvio-padrao sob residuos Gaussianos,
  mas sem ser afetado pelas caudas pesadas / outliers catastroficos.
- **`nmad_se`**: erro-padrao do NMAD estimado por **bootstrap** (reamostragem com
  reposicao, seed fixa), pois nao tem formula fechada simples sob a distribuicao de
  cauda pesada de `dz`. E usado na regra de 1 desvio-padrao da busca.

Observacao: quando `rmse` fica muito maior que `nmad`, isso normalmente indica
**poucos pontos catastroficos** (o RMSE e dominado por eles; o NMAD, baseado na
mediana, ignora a cauda).

## Organizacao de metricas, modelos, figuras e tabelas

```text
reports/metrics/<Model Selection ou Tests>/<dataset>/<feature_set>/<modelo>/
models/<Model Selection ou Tests>/<dataset>/<feature_set>/<modelo>/
reports/figures/<Model Selection ou Tests>/<dataset>/<feature_set>/<modelo>/
reports/tables/<Model Selection ou Tests>/<dataset>/<feature_set>/<modelo>/
```

Mapeamento de nomes de dataset nas pastas:

```text
happyT -> happy
teddyT -> teddy
```

Exemplos:

```text
reports/metrics/Model Selection/happy/mag/linear_regression/
reports/metrics/Tests/teddy/mag_err/polynomial_ridge/
reports/tables/Model Selection/happy/mag/polynomial_ridge/
```

## Regressao Linear

Script:

```text
src/redshift/models/linear_regression.py
```

Pipeline:

```text
data/processed -> LinearRegression
```

Le diretamente os arquivos de `data/processed/<dataset>/` (magnitudes com
`StandardScaler`, erros com `log1p` + `RobustScaler`, alvo com `log1p`) e ajusta uma
`LinearRegression`. Nao ha hiperparametro a buscar.

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

Saidas por execucao: modelo `.joblib`, metricas `.json` e grafico `.png`.

## Polynomial Ridge

Script:

```text
src/redshift/models/polynomial_ridge.py
```

Assim como a regressao linear, o Polynomial Ridge **consome `data/processed/<dataset>/`**
(nao usa mais dados brutos nem aplica `log1p` depois da expansao). O pipeline do modelo e:

```text
data/processed -> PolynomialFeatures -> StandardScaler -> Ridge
```

```python
PolynomialFeatures(degree=degree, include_bias=False)
StandardScaler()
Ridge(alpha=alpha)
```

### Escala em duas etapas

As features passam por `StandardScaler` **duas vezes**, em momentos diferentes e com
propositos diferentes:

1. **Antes do poly** (no pre-processamento, `data/processed`): magnitudes recebem
   `StandardScaler` e erros `log1p` + `RobustScaler`. Isso deixa as features ~O(1),
   entao termos como `u^2` ficam ~O(1) em vez de ~O(centenas) — o que reduz muito a
   tendencia de explosao na extrapolacao.
2. **Depois do poly** (no pipeline do modelo): o `StandardScaler` padroniza os termos
   **novos** (`u^2`, `u*g`, ...), para que a penalidade L2 do `Ridge` seja uniforme
   entre eles.

As duas passagens nao conflitam: re-padronizar os termos lineares (ja escalados na
etapa 1) e praticamente um no-op; o ganho real da etapa 2 e sobre os quadrados e
produtos. O alvo continua transformado com `log1p(redshift)` no pre-processamento.

Rodar uma configuracao especifica (MAG):

```powershell
.\.venv\Scripts\python.exe src\redshift\models\polynomial_ridge.py --dataset happyT --feature-set mag --eval-split val --degree 2 --alpha 1
```

Com MAG+ERR:

```powershell
.\.venv\Scripts\python.exe src\redshift\models\polynomial_ridge.py --dataset happyT --feature-set mag_err --eval-split val --degree 2 --alpha 1
```

Avaliacao final em teste, ja com o `degree` e o `alpha` escolhidos na validacao:

```powershell
.\.venv\Scripts\python.exe src\redshift\models\polynomial_ridge.py --dataset happyT --feature-set mag --eval-split test --degree 2 --alpha 5
```

## Busca de hiperparametros do Polynomial Ridge

Script:

```text
src/redshift/training/search_polynomial_ridge.py
```

Grade padrao:

```python
degrees = [1, 2]
alphas = [0.1, 0.5, 1, 2, 5, 10, 50, 100, 1000]
```

A busca treina cada combinacao em `train`, avalia em `validation` e salva uma tabela
resumo. A escolha do melhor conjunto de hiperparametros usa a **regra de 1 desvio-padrao**
(em ingles, *one-standard-error rule*) aplicada sobre o **NMAD** — nao o simples menor erro.

### Por que nao pegar simplesmente o menor erro

A metrica de validacao e uma **estimativa ruidosa**: se a amostra de validacao fosse um
pouco diferente, o valor mudaria. Pegar cegamente a config de menor erro quase sempre
premia a mais complexa (maior `degree`, menor `alpha`) por uma diferenca que cabe **dentro
do ruido**, sem ganho real de generalizacao. Pior: modelos pouco regularizados extrapolam
mal no teste externo (`B, C, D`). Queremos o oposto: o modelo **mais simples que ainda seja
estatisticamente equivalente ao melhor**.

### O que e o "1 desvio-padrao" aqui

Para saber se duas configs sao "iguais dentro do ruido", precisamos medir o quanto a
metrica oscilaria por puro acaso — o **desvio-padrao da estimativa** do NMAD (em ingles,
*standard error*, SE). Como a distribuicao do erro normalizado `dz` tem cauda pesada e o
NMAD nao tem formula fechada simples, esse desvio-padrao e estimado por **bootstrap**:
reamostramos os residuos com reposicao varias vezes, recalculamos o NMAD em cada
reamostra, e o desvio-padrao desses valores e o `nmad_se`. Ele responde: "se a amostra de
validacao fosse outra, quanto o NMAD do melhor modelo balancaria?".

### Passo a passo da regra

1. acha a config de **menor NMAD** (o "melhor"; coluna `nmad`);
2. pega o **desvio-padrao** do NMAD dessa config (`nmad_se`, via bootstrap);
3. define a faixa de tolerancia: `limite = melhor_NMAD + 1 desvio-padrao`
   (coluna `selection_threshold`). Toda config com `nmad <= limite` recebe
   `within_1se = True` — sao **indistinguiveis** do melhor, pois a diferenca cabe dentro
   do desvio-padrao;
4. dentre as indistinguiveis, escolhe a **mais simples / mais regularizada**: menor
   `degree` e, em seguida, maior `alpha` (coluna `selected_1se = True`).

Ou seja, abrimos mao de um ganho de erro que e so ruido em troca de **robustez**: o modelo
escolhido tem NMAD de validacao praticamente igual ao do minimo, porem mais regularizado,
o que generaliza melhor sob mudanca de distribuicao.

### Exemplo concreto (teddy / mag_err)

Com os numeros reais da tabela:

```text
melhor NMAD               = 0.018033   (degree 2, alpha 0.1)
desvio-padrao (bootstrap) = 0.000198
limite 1-SE               = 0.018033 + 0.000198 = 0.018231
```

5 configs ficam dentro do limite (todas `degree 2`, com `alpha` de 0.1 a 5). Como todas
tem o mesmo degree, o desempate vai pelo maior `alpha`: a escolhida e **degree 2, alpha 5**
— 50x mais regularizada que o minimo cru, com NMAD praticamente identico.

### Por que NMAD e nao RMSE

O RMSE e dominado por poucos outliers catastroficos e tende a apontar sempre o maior
`degree` e o menor `alpha` por margem dentro do ruido. O NMAD e robusto (baseado na
mediana) e seleciona pela qualidade do **nucleo** da distribuicao, que e o que queremos
comparar entre modelos.

Colunas relevantes na tabela: `nmad`, `nmad_se`, `selection_metric`, `selection_se`,
`selection_threshold`, `within_1se`, `selected_1se`. A config recomendada fica na
primeira linha (`selected_1se = True`).

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

A busca salva: JSON individual por combinacao, grafico individual por combinacao e a
tabela resumo ordenada pela regra de 1-SE em `reports/tables/...`.

## Teddy

Para rodar qualquer comando no Teddy, troque `--dataset happyT` por `--dataset teddyT`.

## Aviso sobre limitacao conhecida

No teste externo (`B + C + D`), modelos polinomiais podem produzir predicoes
extremas para objetos que caem fora do suporte do treino (extrapolacao sob mudanca de
distribuicao). Como o alvo usa `log1p`, uma predicao moderadamente alta no espaco
transformado vira um redshift enorme apos `expm1`, inflando RMSE/MAE enquanto o NMAD
permanece comportado. Esse efeito nao e corrigido pela selecao de hiperparametros; um
guarda-corpo possivel e clipar a predicao em uma faixa fisica de redshift antes do
`expm1`.
```

