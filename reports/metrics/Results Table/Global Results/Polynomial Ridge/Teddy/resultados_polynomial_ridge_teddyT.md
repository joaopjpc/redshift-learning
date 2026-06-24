# Polinomial Ridge - Resultados dos baselines — TeddyT

Este arquivo resume os dois baselines testados nos conjuntos externos B, C e D com 
Linear Regression + Polynomial Features + Regularization Ridge no dataset TEDDY

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
| B | `mag` | 74559 | 0.0240 | 0.0350 | 0.8411 | -0.0000 | 0.0190 | 0.14% | 0 |
| B | `mag_err` | 74559 | 0.0233 | 0.0345 | 0.8456 | 0.0000 | 0.0181 | 0.15% | 1 |
| C | `mag` | 97980 | 0.0254 | 0.0376 | 0.8571 | -0.0005 | 0.0195 | 0.23% | 0 |
| C | `mag_err` | 97980 | 0.0246 | 0.0372 | 0.8604 | -0.0007 | 0.0185 | 0.24% | 1 |
| D | `mag` | 75925 | 0.1076 | 0.5041 | -4.3740 | 0.0817 | 0.0663 | 11.55% | 1903 |
| D | `mag_err` | 75925 | 0.1006 | 0.5427 | -5.2294 | 0.0050 | 0.0441 | 8.11% | 1187 |



## Resultados por baseline e teste

## Baseline 1 — Polynomial Ridge com magnitudes

- **Feature set:** `mag`
- **Transformações do modelo:** PolynomialFeatures, StandardScaler
- **Features usadas:** `u`, `g`, `r`, `i`, `z`

| Teste | n | MAE | RMSE | R² | Bias | NMAD | Outliers catastróficos | Previsões negativas |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| B | 74559 | 0.0240 | 0.0350 | 0.8411 | -0.0000 | 0.0190 | 0.14% | 0 |
| C | 97980 | 0.0254 | 0.0376 | 0.8571 | -0.0005 | 0.0195 | 0.23% | 0 |
| D | 75925 | 0.1076 | 0.5041 | -4.3740 | 0.0817 | 0.0663 | 11.55% | 1903 |

### Teste B

- **Experimento:** `polynomial_ridge_mag_degree2_alpha0.5`
- **Modelo:** PolynomialFeatures+Ridge
- **Features:** `u`, `g`, `r`, `i`, `z`
- **Grau polynomial:** 2
- **Alpha Ridge:** 0.5

| Métrica | Valor |
|---|---:|
| n | 74559 |
| MAE | 0.024039 |
| RMSE | 0.034996 |
| R² | 0.841087 |
| Bias | -0.000039 |
| NMAD | 0.019048 |
| Erro-padrão do NMAD | 0.000088 |
| Fração de outliers catastróficos | 0.14% |
| Limiar de outlier catastrófico | 0.15 |
| Previsões negativas de redshift | 0 |

### Teste C

- **Experimento:** `polynomial_ridge_mag_degree2_alpha0.5`
- **Modelo:** PolynomialFeatures+Ridge
- **Features:** `u`, `g`, `r`, `i`, `z`
- **Grau polynomial:** 2
- **Alpha Ridge:** 0.5

| Métrica | Valor |
|---|---:|
| n | 97980 |
| MAE | 0.025375 |
| RMSE | 0.037640 |
| R² | 0.857064 |
| Bias | -0.000539 |
| NMAD | 0.019521 |
| Erro-padrão do NMAD | 0.000075 |
| Fração de outliers catastróficos | 0.23% |
| Limiar de outlier catastrófico | 0.15 |
| Previsões negativas de redshift | 0 |

### Teste D

- **Experimento:** `polynomial_ridge_mag_degree2_alpha0.5`
- **Modelo:** PolynomialFeatures+Ridge
- **Features:** `u`, `g`, `r`, `i`, `z`
- **Grau polynomial:** 2
- **Alpha Ridge:** 0.5

| Métrica | Valor |
|---|---:|
| n | 75925 |
| MAE | 0.107609 |
| RMSE | 0.504102 |
| R² | -4.373959 |
| Bias | 0.081716 |
| NMAD | 0.066268 |
| Erro-padrão do NMAD | 0.000339 |
| Fração de outliers catastróficos | 11.55% |
| Limiar de outlier catastrófico | 0.15 |
| Previsões negativas de redshift | 1903 |

## Baseline 2 — Polynomial Ridge com magnitudes + erros fotométricos

- **Feature set:** `mag_err`
- **Transformações do modelo:** PolynomialFeatures, StandardScaler
- **Features usadas:** `u`, `g`, `r`, `i`, `z`, `uErr`, `gErr`, `rErr`, `iErr`, `zErr`

| Teste | n | MAE | RMSE | R² | Bias | NMAD | Outliers catastróficos | Previsões negativas |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| B | 74559 | 0.0233 | 0.0345 | 0.8456 | 0.0000 | 0.0181 | 0.15% | 1 |
| C | 97980 | 0.0246 | 0.0372 | 0.8604 | -0.0007 | 0.0185 | 0.24% | 1 |
| D | 75925 | 0.1006 | 0.5427 | -5.2294 | 0.0050 | 0.0441 | 8.11% | 1187 |

### Teste B

- **Experimento:** `polynomial_ridge_mag_err_degree2_alpha5`
- **Modelo:** PolynomialFeatures+Ridge
- **Features:** `u`, `g`, `r`, `i`, `z`, `uErr`, `gErr`, `rErr`, `iErr`, `zErr`
- **Grau polynomial:** 2
- **Alpha Ridge:** 5.0

| Métrica | Valor |
|---|---:|
| n | 74559 |
| MAE | 0.023330 |
| RMSE | 0.034491 |
| R² | 0.845646 |
| Bias | 0.000021 |
| NMAD | 0.018135 |
| Erro-padrão do NMAD | 0.000084 |
| Fração de outliers catastróficos | 0.15% |
| Limiar de outlier catastrófico | 0.15 |
| Previsões negativas de redshift | 1 |

### Teste C

- **Experimento:** `polynomial_ridge_mag_err_degree2_alpha5`
- **Modelo:** PolynomialFeatures+Ridge
- **Features:** `u`, `g`, `r`, `i`, `z`, `uErr`, `gErr`, `rErr`, `iErr`, `zErr`
- **Grau polynomial:** 2
- **Alpha Ridge:** 5.0

| Métrica | Valor |
|---|---:|
| n | 97980 |
| MAE | 0.024649 |
| RMSE | 0.037192 |
| R² | 0.860448 |
| Bias | -0.000655 |
| NMAD | 0.018469 |
| Erro-padrão do NMAD | 0.000081 |
| Fração de outliers catastróficos | 0.24% |
| Limiar de outlier catastrófico | 0.15 |
| Previsões negativas de redshift | 1 |

### Teste D

- **Experimento:** `polynomial_ridge_mag_err_degree2_alpha5`
- **Modelo:** PolynomialFeatures+Ridge
- **Features:** `u`, `g`, `r`, `i`, `z`, `uErr`, `gErr`, `rErr`, `iErr`, `zErr`
- **Grau polynomial:** 2
- **Alpha Ridge:** 5.0

| Métrica | Valor |
|---|---:|
| n | 75925 |
| MAE | 0.100568 |
| RMSE | 0.542741 |
| R² | -5.229365 |
| Bias | 0.004982 |
| NMAD | 0.044098 |
| Erro-padrão do NMAD | 0.000251 |
| Fração de outliers catastróficos | 8.11% |
| Limiar de outlier catastrófico | 0.15 |
| Previsões negativas de redshift | 1187 |

## Observação geral

No teddyT, o baseline com erros fotométricos (`mag_err`) traz ganhos pequenos em B e C e uma melhora bem clara em NMAD, bias e outliers no teste D. Ainda assim, no D o RMSE piora, o que sugere presença de poucos erros extremos muito grandes.
