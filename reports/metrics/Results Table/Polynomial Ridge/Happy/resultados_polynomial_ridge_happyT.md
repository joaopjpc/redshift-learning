# Resultados dos baselines — HappyT

Este arquivo resume os dois baselines testados nos conjuntos externos B, C e D com 
Linear Regression + Polynomial Features + Regularization Ridge no dataset HAPPY

## Métricas reportadas

| Métrica | Interpretação | Melhor direção |
|---|---|---|
| MAE | erro absoluto médio | menor |
| RMSE | raiz do erro quadrático médio; penaliza mais erros grandes | menor |
| R² | proporção da variância explicada | maior |
| Bias | média do erro de previsão | mais próximo de 0 |
| NMAD | métrica robusta de dispersão do erro | menor |
| Outliers catastróficos | fração de objetos com erro acima do limiar configurado | menor |
| Predições negativas | número de previsões de redshift negativo | menor |

## Resumo comparativo

| Teste | Baseline | n | MAE | RMSE | R² | Bias | NMAD | Out Cat | Prev neg |
|:---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| B | `mag` | 74900 | 0.0429 | 0.0703 | 0.8892 | -0.0001 | 0.0321 | 1.57% | 805 |
| B | `mag_err` | 74900 | 0.0378 | 0.0660 | 0.9025 | 0.0000 | 0.0269 | 1.31% | 267 |
| C | `mag` | 60315 | 0.0975 | 0.1311 | 0.4862 | 0.0422 | 0.0732 | 10.97% | 202 |
| C | `mag_err` | 60315 | 0.0842 | 0.1206 | 0.5652 | 0.0209 | 0.0636 | 7.62% | 187 |
| D | `mag` | 74642 | 0.1328 | 0.1880 | 0.2741 | 0.0254 | 0.0989 | 18.08% | 447 |
| D | `mag_err` | 74642 | 0.1252 | 0.2157 | 0.0451 | -0.0010 | 0.0905 | 15.18% | 301 |



## Resultados por baseline e teste

## Baseline 1 — Polynomial Ridge com magnitudes

- **Feature set:** `mag`
- **Transformações do modelo:** PolynomialFeatures, StandardScaler
- **Features usadas:** `u`, `g`, `r`, `i`, `z`

| Teste | n | MAE | RMSE | R² | Bias | NMAD | Outliers catastróficos | Previsões negativas |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| B | 74900 | 0.0429 | 0.0703 | 0.8892 | -0.0001 | 0.0321 | 1.57% | 805 |
| C | 60315 | 0.0975 | 0.1311 | 0.4862 | 0.0422 | 0.0732 | 10.97% | 202 |
| D | 74642 | 0.1328 | 0.1880 | 0.2741 | 0.0254 | 0.0989 | 18.08% | 447 |

### Teste B

- **Experimento:** `polynomial_ridge_mag_degree2_alpha10`
- **Modelo:** PolynomialFeatures+Ridge
- **Features:** `u`, `g`, `r`, `i`, `z`
- **Grau polynomial:** 2
- **Alpha Ridge:** 10.0

| Métrica | Valor |
|---|---:|
| n | 74900 |
| MAE | 0.042944 |
| RMSE | 0.070340 |
| R² | 0.889212 |
| Bias | -0.000118 |
| NMAD | 0.032135 |
| Erro-padrão do NMAD | 0.000143 |
| Fração de outliers catastróficos | 1.57% |
| Limiar de outlier catastrófico | 0.15 |
| Previsões negativas de redshift | 805 |

### Teste C

- **Experimento:** `polynomial_ridge_mag_degree2_alpha10`
- **Modelo:** PolynomialFeatures+Ridge
- **Features:** `u`, `g`, `r`, `i`, `z`
- **Grau polynomial:** 2
- **Alpha Ridge:** 10.0

| Métrica | Valor |
|---|---:|
| n | 60315 |
| MAE | 0.097463 |
| RMSE | 0.131120 |
| R² | 0.486171 |
| Bias | 0.042194 |
| NMAD | 0.073189 |
| Erro-padrão do NMAD | 0.000367 |
| Fração de outliers catastróficos | 10.97% |
| Limiar de outlier catastrófico | 0.15 |
| Previsões negativas de redshift | 202 |

### Teste D

- **Experimento:** `polynomial_ridge_mag_degree2_alpha10`
- **Modelo:** PolynomialFeatures+Ridge
- **Features:** `u`, `g`, `r`, `i`, `z`
- **Grau polynomial:** 2
- **Alpha Ridge:** 10.0

| Métrica | Valor |
|---|---:|
| n | 74642 |
| MAE | 0.132776 |
| RMSE | 0.188046 |
| R² | 0.274136 |
| Bias | 0.025431 |
| NMAD | 0.098914 |
| Erro-padrão do NMAD | 0.000457 |
| Fração de outliers catastróficos | 18.08% |
| Limiar de outlier catastrófico | 0.15 |
| Previsões negativas de redshift | 447 |

## Baseline 2 — Polynomial Ridge com magnitudes + erros fotométricos

- **Feature set:** `mag_err`
- **Transformações do modelo:** PolynomialFeatures, StandardScaler
- **Features usadas:** `u`, `g`, `r`, `i`, `z`, `uErr`, `gErr`, `rErr`, `iErr`, `zErr`

| Teste | n | MAE | RMSE | R² | Bias | NMAD | Outliers catastróficos | Previsões negativas |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| B | 74900 | 0.0378 | 0.0660 | 0.9025 | 0.0000 | 0.0269 | 1.31% | 267 |
| C | 60315 | 0.0842 | 0.1206 | 0.5652 | 0.0209 | 0.0636 | 7.62% | 187 |
| D | 74642 | 0.1252 | 0.2157 | 0.0451 | -0.0010 | 0.0905 | 15.18% | 301 |

### Teste B

- **Experimento:** `polynomial_ridge_mag_err_degree2_alpha10`
- **Modelo:** PolynomialFeatures+Ridge
- **Features:** `u`, `g`, `r`, `i`, `z`, `uErr`, `gErr`, `rErr`, `iErr`, `zErr`
- **Grau polynomial:** 2
- **Alpha Ridge:** 10.0

| Métrica | Valor |
|---|---:|
| n | 74900 |
| MAE | 0.037758 |
| RMSE | 0.065973 |
| R² | 0.902543 |
| Bias | 0.000049 |
| NMAD | 0.026896 |
| Erro-padrão do NMAD | 0.000118 |
| Fração de outliers catastróficos | 1.31% |
| Limiar de outlier catastrófico | 0.15 |
| Previsões negativas de redshift | 267 |

### Teste C

- **Experimento:** `polynomial_ridge_mag_err_degree2_alpha10`
- **Modelo:** PolynomialFeatures+Ridge
- **Features:** `u`, `g`, `r`, `i`, `z`, `uErr`, `gErr`, `rErr`, `iErr`, `zErr`
- **Grau polynomial:** 2
- **Alpha Ridge:** 10.0

| Métrica | Valor |
|---|---:|
| n | 60315 |
| MAE | 0.084209 |
| RMSE | 0.120613 |
| R² | 0.565221 |
| Bias | 0.020909 |
| NMAD | 0.063603 |
| Erro-padrão do NMAD | 0.000329 |
| Fração de outliers catastróficos | 7.62% |
| Limiar de outlier catastrófico | 0.15 |
| Previsões negativas de redshift | 187 |

### Teste D

- **Experimento:** `polynomial_ridge_mag_err_degree2_alpha10`
- **Modelo:** PolynomialFeatures+Ridge
- **Features:** `u`, `g`, `r`, `i`, `z`, `uErr`, `gErr`, `rErr`, `iErr`, `zErr`
- **Grau polynomial:** 2
- **Alpha Ridge:** 10.0

| Métrica | Valor |
|---|---:|
| n | 74642 |
| MAE | 0.125183 |
| RMSE | 0.215681 |
| R² | 0.045117 |
| Bias | -0.001023 |
| NMAD | 0.090485 |
| Erro-padrão do NMAD | 0.000437 |
| Fração de outliers catastróficos | 15.18% |
| Limiar de outlier catastrófico | 0.15 |
| Previsões negativas de redshift | 301 |

## Observação geral

No happyT, o baseline com erros fotométricos (`mag_err`) melhora MAE, NMAD e fração de outliers nos três testes. No teste D, porém, o RMSE piora em relação ao baseline apenas com magnitudes, indicando maior sensibilidade a alguns erros extremos.
