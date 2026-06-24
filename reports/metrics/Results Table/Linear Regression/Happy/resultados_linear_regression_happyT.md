# Resultados dos baselines — happyT — Linear Regression

Este arquivo resume os dois baselines de Regressão Linear avaliados no dataset `happyT`, separando os resultados por baseline e por conjunto de teste externo `B`, `C` e `D`.

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

## Comparação geral entre os baselines

| Teste | Baseline | MAE | RMSE | R² | Bias | NMAD | Outliers catastróficos | Predições negativas | N |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| B | `mag` | 0.0484 | 0.0767 | 0.8684 | -0.0003 | 0.0369 | 1.90% | 1631 | 74900 |
| B | `mag_err` | 0.0438 | 0.0728 | 0.8814 | -0.0002 | 0.0327 | 1.67% | 911 | 74900 |
| C | `mag` | 0.0995 | 0.1322 | 0.4775 | 0.0343 | 0.0779 | 11.05% | 163 | 60315 |
| C | `mag_err` | 0.0934 | 0.1289 | 0.5033 | 0.0200 | 0.0735 | 9.54% | 210 | 60315 |
| D | `mag` | 0.1363 | 0.1958 | 0.2129 | -0.0191 | 0.1059 | 18.11% | 485 | 74642 |
| D | `mag_err` | 0.1306 | 0.1946 | 0.2224 | 0.0007 | 0.0985 | 17.07% | 428 | 74642 |

## Leitura rápida

- O baseline `mag_err` melhora MAE, RMSE, R², NMAD e fração de outliers nos três testes B, C e D.
- A melhora é mais clara no teste B e continua presente nos testes C e D.
- O conjunto D continua sendo o mais difícil, com maior MAE, RMSE, NMAD e fração de outliers em ambos os baselines.
- Mesmo com erros fotométricos, o modelo ainda apresenta viés por faixa de redshift: tende a superestimar redshifts baixos e subestimar redshifts altos.

# Baseline 1 — Linear Regression com magnitudes (`mag`)

Usa apenas as magnitudes fotométricas: `u`, `g`, `r`, `i`, `z`.

- Modelo: `LinearRegression`
- Experimento: `linear_regression_mag`
- Dataset: `happyT`
- Alvo: `redshift`
- Número de features: `5`
- Parâmetros: `{'fit_intercept': True}`

## Resumo do baseline

| Teste | MAE | RMSE | R² | Bias | NMAD | Outliers catastróficos | Predições negativas | N |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| B | 0.0484 | 0.0767 | 0.8684 | -0.0003 | 0.0369 | 1.90% | 1631 | 74900 |
| C | 0.0995 | 0.1322 | 0.4775 | 0.0343 | 0.0779 | 11.05% | 163 | 60315 |
| D | 0.1363 | 0.1958 | 0.2129 | -0.0191 | 0.1059 | 18.11% | 485 | 74642 |

## Teste B

- MAE: `0.048444`
- RMSE: `0.076650`
- R²: `0.868445`
- Bias: `-0.000344`
- NMAD: `0.036939`
- Erro padrão do NMAD: `0.000158`
- Fração de outliers catastróficos: `1.9039%`
- Limiar de outlier catastrófico: `0.15`
- Predições negativas de redshift: `1631`
- N: `74900`

### Métricas por faixa de redshift

| Faixa de redshift | N | MAE | RMSE | Bias | NMAD | Predições negativas |
|---|---:|---:|---:|---:|---:|---:|
| z 0..0.1 | 12878 | 0.0556 | 0.0824 | 0.0198 | 0.0530 | 1586 |
| z 0.1..0.2 | 12719 | 0.0386 | 0.0660 | 0.0212 | 0.0327 | 25 |
| z 0.2..0.4 | 13434 | 0.0395 | 0.0653 | 0.0178 | 0.0292 | 9 |
| z 0.4..0.6 | 27319 | 0.0394 | 0.0551 | -0.0030 | 0.0301 | 8 |
| z 0.6..inf | 8550 | 0.0952 | 0.1355 | -0.0827 | 0.0477 | 3 |

### Métricas por magnitude `r`

| Faixa de magnitude r | N | MAE | RMSE | Bias | NMAD | Predições negativas |
|---|---:|---:|---:|---:|---:|---:|
| (9.805, 17.455] | 18725 | 0.0369 | 0.0568 | -0.0026 | 0.0377 | 1614 |
| (17.455, 19.256] | 18725 | 0.0404 | 0.0587 | 0.0175 | 0.0360 | 16 |
| (19.256, 20.4] | 18725 | 0.0499 | 0.0728 | -0.0122 | 0.0329 | 1 |
| (20.4, 27.587] | 18725 | 0.0665 | 0.1074 | -0.0040 | 0.0408 | 0 |

### Métricas por erro fotométrico médio

| Faixa de erro fotométrico médio | N | MAE | RMSE | Bias | NMAD | Predições negativas |
|---|---:|---:|---:|---:|---:|---:|
| (0.0331, 0.0758] | 18726 | 0.0370 | 0.0485 | 0.0204 | 0.0365 | 209 |
| (0.0758, 0.173] | 18724 | 0.0498 | 0.0751 | -0.0081 | 0.0389 | 1178 |
| (0.173, 0.266] | 18725 | 0.0507 | 0.0774 | -0.0061 | 0.0337 | 131 |
| (0.266, 12.53] | 18725 | 0.0563 | 0.0976 | -0.0076 | 0.0359 | 113 |

## Teste C

- MAE: `0.099514`
- RMSE: `0.132226`
- R²: `0.477471`
- Bias: `0.034258`
- NMAD: `0.077940`
- Erro padrão do NMAD: `0.000400`
- Fração de outliers catastróficos: `11.0503%`
- Limiar de outlier catastrófico: `0.15`
- Predições negativas de redshift: `163`
- N: `60315`

### Métricas por faixa de redshift

| Faixa de redshift | N | MAE | RMSE | Bias | NMAD | Predições negativas |
|---|---:|---:|---:|---:|---:|---:|
| z 0..0.1 | 3213 | 0.1868 | 0.2214 | 0.1755 | 0.1260 | 124 |
| z 0.1..0.2 | 7877 | 0.1363 | 0.1557 | 0.1323 | 0.0666 | 19 |
| z 0.2..0.4 | 21701 | 0.0861 | 0.1053 | 0.0753 | 0.0560 | 5 |
| z 0.4..0.6 | 20706 | 0.0659 | 0.0832 | -0.0063 | 0.0567 | 13 |
| z 0.6..inf | 6818 | 0.1606 | 0.2173 | -0.1531 | 0.0739 | 2 |

### Métricas por magnitude `r`

| Faixa de magnitude r | N | MAE | RMSE | Bias | NMAD | Predições negativas |
|---|---:|---:|---:|---:|---:|---:|
| (13.923, 19.754] | 15079 | 0.0814 | 0.1069 | 0.0521 | 0.0639 | 162 |
| (19.754, 20.47] | 15079 | 0.0980 | 0.1285 | 0.0443 | 0.0815 | 1 |
| (20.47, 21.016] | 15078 | 0.1039 | 0.1348 | 0.0298 | 0.0839 | 0 |
| (21.016, 22.683] | 15079 | 0.1148 | 0.1543 | 0.0108 | 0.0843 | 0 |

### Métricas por erro fotométrico médio

| Faixa de erro fotométrico médio | N | MAE | RMSE | Bias | NMAD | Predições negativas |
|---|---:|---:|---:|---:|---:|---:|
| (0.0329, 0.131] | 15079 | 0.0945 | 0.1259 | 0.0450 | 0.0740 | 137 |
| (0.131, 0.191] | 15079 | 0.1091 | 0.1457 | 0.0282 | 0.0927 | 19 |
| (0.191, 0.254] | 15078 | 0.1026 | 0.1346 | 0.0313 | 0.0782 | 5 |
| (0.254, 0.512] | 15079 | 0.0918 | 0.1214 | 0.0325 | 0.0667 | 2 |

## Teste D

- MAE: `0.136347`
- RMSE: `0.195824`
- R²: `0.212852`
- Bias: `-0.019149`
- NMAD: `0.105939`
- Erro padrão do NMAD: `0.000450`
- Fração de outliers catastróficos: `18.1091%`
- Limiar de outlier catastrófico: `0.15`
- Predições negativas de redshift: `485`
- N: `74642`

### Métricas por faixa de redshift

| Faixa de redshift | N | MAE | RMSE | Bias | NMAD | Predições negativas |
|---|---:|---:|---:|---:|---:|---:|
| z 0..0.1 | 3265 | 0.2541 | 0.3079 | 0.2044 | 0.1618 | 245 |
| z 0.1..0.2 | 5876 | 0.1684 | 0.1987 | 0.1551 | 0.0781 | 88 |
| z 0.2..0.4 | 20281 | 0.0988 | 0.1259 | 0.0825 | 0.0615 | 59 |
| z 0.4..0.6 | 26237 | 0.0799 | 0.1122 | -0.0230 | 0.0640 | 43 |
| z 0.6..inf | 18983 | 0.2243 | 0.2965 | -0.2148 | 0.0830 | 50 |

### Métricas por magnitude `r`

| Faixa de magnitude r | N | MAE | RMSE | Bias | NMAD | Predições negativas |
|---|---:|---:|---:|---:|---:|---:|
| (8.509, 20.635] | 18661 | 0.1082 | 0.1749 | 0.0257 | 0.0809 | 472 |
| (20.635, 21.377] | 18660 | 0.1215 | 0.1636 | 0.0004 | 0.0988 | 8 |
| (21.377, 21.87] | 18660 | 0.1430 | 0.2008 | -0.0357 | 0.1095 | 5 |
| (21.87, 30.481] | 18661 | 0.1727 | 0.2360 | -0.0670 | 0.1177 | 0 |

### Métricas por erro fotométrico médio

| Faixa de erro fotométrico médio | N | MAE | RMSE | Bias | NMAD | Predições negativas |
|---|---:|---:|---:|---:|---:|---:|
| (0.0339, 0.213] | 18661 | 0.1072 | 0.1430 | 0.0323 | 0.0876 | 111 |
| (0.213, 0.308] | 18660 | 0.1245 | 0.1703 | -0.0005 | 0.0966 | 42 |
| (0.308, 0.409] | 18660 | 0.1396 | 0.1964 | -0.0317 | 0.1051 | 20 |
| (0.409, 352.277] | 18661 | 0.1741 | 0.2556 | -0.0767 | 0.1173 | 312 |

# Baseline 2 — Linear Regression com magnitudes + erros (`mag_err`)

Usa magnitudes e erros fotométricos: `u`, `g`, `r`, `i`, `z`, `uErr`, `gErr`, `rErr`, `iErr`, `zErr`.

- Modelo: `LinearRegression`
- Experimento: `linear_regression_mag_err`
- Dataset: `happyT`
- Alvo: `redshift`
- Número de features: `10`
- Parâmetros: `{'fit_intercept': True}`

## Resumo do baseline

| Teste | MAE | RMSE | R² | Bias | NMAD | Outliers catastróficos | Predições negativas | N |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| B | 0.0438 | 0.0728 | 0.8814 | -0.0002 | 0.0327 | 1.67% | 911 | 74900 |
| C | 0.0934 | 0.1289 | 0.5033 | 0.0200 | 0.0735 | 9.54% | 210 | 60315 |
| D | 0.1306 | 0.1946 | 0.2224 | 0.0007 | 0.0985 | 17.07% | 428 | 74642 |

## Teste B

- MAE: `0.043827`
- RMSE: `0.072793`
- R²: `0.881351`
- Bias: `-0.000208`
- NMAD: `0.032730`
- Erro padrão do NMAD: `0.000140`
- Fração de outliers catastróficos: `1.6702%`
- Limiar de outlier catastrófico: `0.15`
- Predições negativas de redshift: `911`
- N: `74900`

### Métricas por faixa de redshift

| Faixa de redshift | N | MAE | RMSE | Bias | NMAD | Predições negativas |
|---|---:|---:|---:|---:|---:|---:|
| z 0..0.1 | 12878 | 0.0445 | 0.0750 | 0.0233 | 0.0420 | 876 |
| z 0.1..0.2 | 12719 | 0.0327 | 0.0611 | 0.0120 | 0.0285 | 15 |
| z 0.2..0.4 | 13434 | 0.0387 | 0.0642 | 0.0105 | 0.0284 | 9 |
| z 0.4..0.6 | 27319 | 0.0378 | 0.0556 | 0.0014 | 0.0289 | 8 |
| z 0.6..inf | 8550 | 0.0867 | 0.1266 | -0.0759 | 0.0448 | 3 |

### Métricas por magnitude `r`

| Faixa de magnitude r | N | MAE | RMSE | Bias | NMAD | Predições negativas |
|---|---:|---:|---:|---:|---:|---:|
| (9.805, 17.455] | 18725 | 0.0296 | 0.0489 | -0.0006 | 0.0309 | 889 |
| (17.455, 19.256] | 18725 | 0.0350 | 0.0551 | 0.0078 | 0.0319 | 20 |
| (19.256, 20.4] | 18725 | 0.0461 | 0.0690 | -0.0073 | 0.0298 | 2 |
| (20.4, 27.587] | 18725 | 0.0646 | 0.1049 | -0.0007 | 0.0390 | 0 |

### Métricas por erro fotométrico médio

| Faixa de erro fotométrico médio | N | MAE | RMSE | Bias | NMAD | Predições negativas |
|---|---:|---:|---:|---:|---:|---:|
| (0.0331, 0.0758] | 18726 | 0.0303 | 0.0428 | 0.0081 | 0.0311 | 207 |
| (0.0758, 0.173] | 18724 | 0.0453 | 0.0718 | -0.0081 | 0.0342 | 604 |
| (0.173, 0.266] | 18725 | 0.0475 | 0.0743 | -0.0037 | 0.0314 | 60 |
| (0.266, 12.53] | 18725 | 0.0521 | 0.0933 | 0.0029 | 0.0327 | 40 |

## Teste C

- MAE: `0.093397`
- RMSE: `0.128912`
- R²: `0.503336`
- Bias: `0.019979`
- NMAD: `0.073490`
- Erro padrão do NMAD: `0.000418`
- Fração de outliers catastróficos: `9.5366%`
- Limiar de outlier catastrófico: `0.15`
- Predições negativas de redshift: `210`
- N: `60315`

### Métricas por faixa de redshift

| Faixa de redshift | N | MAE | RMSE | Bias | NMAD | Predições negativas |
|---|---:|---:|---:|---:|---:|---:|
| z 0..0.1 | 3213 | 0.1717 | 0.2101 | 0.1578 | 0.1267 | 111 |
| z 0.1..0.2 | 7877 | 0.1190 | 0.1432 | 0.1116 | 0.0691 | 49 |
| z 0.2..0.4 | 21701 | 0.0769 | 0.0989 | 0.0561 | 0.0569 | 31 |
| z 0.4..0.6 | 20706 | 0.0659 | 0.0853 | -0.0160 | 0.0552 | 15 |
| z 0.6..inf | 6818 | 0.1627 | 0.2220 | -0.1566 | 0.0729 | 4 |

### Métricas por magnitude `r`

| Faixa de magnitude r | N | MAE | RMSE | Bias | NMAD | Predições negativas |
|---|---:|---:|---:|---:|---:|---:|
| (13.923, 19.754] | 15079 | 0.0724 | 0.1045 | 0.0316 | 0.0598 | 204 |
| (19.754, 20.47] | 15079 | 0.0913 | 0.1239 | 0.0266 | 0.0777 | 6 |
| (20.47, 21.016] | 15078 | 0.0991 | 0.1310 | 0.0196 | 0.0797 | 0 |
| (21.016, 22.683] | 15079 | 0.1108 | 0.1518 | 0.0021 | 0.0798 | 0 |

### Métricas por erro fotométrico médio

| Faixa de erro fotométrico médio | N | MAE | RMSE | Bias | NMAD | Predições negativas |
|---|---:|---:|---:|---:|---:|---:|
| (0.0329, 0.131] | 15079 | 0.0867 | 0.1249 | 0.0184 | 0.0715 | 174 |
| (0.131, 0.191] | 15079 | 0.1037 | 0.1424 | 0.0134 | 0.0887 | 24 |
| (0.191, 0.254] | 15078 | 0.0961 | 0.1295 | 0.0208 | 0.0728 | 8 |
| (0.254, 0.512] | 15079 | 0.0871 | 0.1175 | 0.0273 | 0.0623 | 4 |

## Teste D

- MAE: `0.130637`
- RMSE: `0.194628`
- R²: `0.222434`
- Bias: `0.000686`
- NMAD: `0.098518`
- Erro padrão do NMAD: `0.000457`
- Fração de outliers catastróficos: `17.0735%`
- Limiar de outlier catastrófico: `0.15`
- Predições negativas de redshift: `428`
- N: `74642`

### Métricas por faixa de redshift

| Faixa de redshift | N | MAE | RMSE | Bias | NMAD | Predições negativas |
|---|---:|---:|---:|---:|---:|---:|
| z 0..0.1 | 3265 | 0.2661 | 0.3228 | 0.2295 | 0.2005 | 177 |
| z 0.1..0.2 | 5876 | 0.1779 | 0.2229 | 0.1623 | 0.1042 | 94 |
| z 0.2..0.4 | 20281 | 0.1140 | 0.1489 | 0.0977 | 0.0699 | 73 |
| z 0.4..0.6 | 26237 | 0.0699 | 0.1159 | -0.0022 | 0.0566 | 37 |
| z 0.6..inf | 18983 | 0.1945 | 0.2709 | -0.1883 | 0.0706 | 47 |

### Métricas por magnitude `r`

| Faixa de magnitude r | N | MAE | RMSE | Bias | NMAD | Predições negativas |
|---|---:|---:|---:|---:|---:|---:|
| (8.509, 20.635] | 18661 | 0.1021 | 0.1968 | 0.0152 | 0.0757 | 420 |
| (20.635, 21.377] | 18660 | 0.1166 | 0.1571 | 0.0159 | 0.0939 | 2 |
| (21.377, 21.87] | 18660 | 0.1382 | 0.1927 | 0.0011 | 0.1053 | 4 |
| (21.87, 30.481] | 18661 | 0.1656 | 0.2258 | -0.0294 | 0.1155 | 2 |

### Métricas por erro fotométrico médio

| Faixa de erro fotométrico médio | N | MAE | RMSE | Bias | NMAD | Predições negativas |
|---|---:|---:|---:|---:|---:|---:|
| (0.0339, 0.213] | 18661 | 0.1008 | 0.1413 | 0.0153 | 0.0835 | 107 |
| (0.213, 0.308] | 18660 | 0.1207 | 0.1687 | 0.0033 | 0.0912 | 37 |
| (0.308, 0.409] | 18660 | 0.1351 | 0.1914 | -0.0090 | 0.1014 | 14 |
| (0.409, 352.277] | 18661 | 0.1659 | 0.2578 | -0.0068 | 0.1165 | 270 |

# Comparação direta: `mag_err` - `mag`

Valores negativos em MAE, RMSE, NMAD e outliers indicam melhora do baseline com erros fotométricos. Valores positivos em R² indicam melhora.

| Teste | Δ MAE | Δ RMSE | Δ R² | Δ Bias abs. | Δ NMAD | Δ Outliers | Δ Predições negativas |
|---|---:|---:|---:|---:|---:|---:|---:|
| B | -0.0046 | -0.0039 | 0.0129 | -0.0001 | -0.0042 | -0.234% | -720 |
| C | -0.0061 | -0.0033 | 0.0259 | -0.0143 | -0.0044 | -1.514% | 47 |
| D | -0.0057 | -0.0012 | 0.0096 | -0.0185 | -0.0074 | -1.036% | -57 |

## Conclusão curta

Para o dataset `happyT`, a Regressão Linear com magnitudes + erros fotométricos (`mag_err`) foi superior à versão com apenas magnitudes (`mag`) nos três testes externos. A melhora aparece nas principais métricas globais, incluindo MAE, RMSE, R², NMAD e fração de outliers catastróficos. Ainda assim, o teste D permanece o cenário mais difícil, sugerindo maior diferença de distribuição ou maior presença de objetos problemáticos nesse split.