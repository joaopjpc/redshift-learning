# Resultados dos baselines — teddyT — Linear Regression

Este arquivo resume os dois baselines de Regressão Linear avaliados no dataset `teddyT`, separando os resultados por baseline e por conjunto de teste externo `B`, `C` e `D`.

## Métricas reportadas

| Métrica | Interpretação | Melhor direção |
| --- | --- | --- |
| MAE | erro absoluto médio | menor |
| RMSE | raiz do erro quadrático médio; penaliza mais erros grandes | menor |
| R² | proporção da variância explicada | maior |
| Bias | média do erro de previsão | mais próximo de 0 |
| NMAD | métrica robusta de dispersão do erro | menor |
| Outliers catastróficos | fração de objetos com erro acima do limiar configurado | menor |
| Predições negativas | número de previsões de redshift negativo | menor |

## Comparação geral entre os baselines

| Teste | Baseline | MAE | RMSE | R² | Bias | NMAD | Outliers catastróficos | Predições negativas | N |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| B | `mag` | 0.0266 | 0.0377 | 0.8161 | -0.0001 | 0.0216 | 0.10% | 0 | 74559 |
| B | `mag_err` | 0.0257 | 0.0368 | 0.8244 | -0.0000 | 0.0205 | 0.11% | 0 | 74559 |
| C | `mag` | 0.0282 | 0.0406 | 0.8337 | -0.0006 | 0.0223 | 0.18% | 0 | 97980 |
| C | `mag_err` | 0.0273 | 0.0398 | 0.8398 | -0.0006 | 0.0212 | 0.19% | 0 | 97980 |
| D | `mag` | 0.0514 | 0.0955 | 0.8072 | -0.0018 | 0.0372 | 2.01% | 1779 | 75925 |
| D | `mag_err` | 0.0493 | 0.0908 | 0.8256 | 0.0020 | 0.0354 | 1.75% | 1784 | 75925 |

## Leitura rápida

- O baseline `mag_err` melhora MAE, RMSE, R² e NMAD nos três testes B, C e D.
- Nos testes B e C, a fração de outliers catastróficos aumenta levemente com `mag_err`, apesar da melhora nas demais métricas globais.
- No teste D, `mag_err` reduz MAE, RMSE, NMAD e outliers catastróficos, mas aumenta ligeiramente o número de predições negativas.
- O conjunto D continua sendo mais difícil que B e C, principalmente pela maior fração de outliers e maior erro nas faixas de maior erro fotométrico médio.
- Em ambos os baselines, o erro tende a aumentar para objetos mais fracos, isto é, nas maiores magnitudes `r`, e para faixas com maior erro fotométrico médio.

# Baseline 1 — Linear Regression com magnitudes (`mag`)

Usa apenas as magnitudes fotométricas: `u`, `g`, `r`, `i`, `z`.

- Modelo: `LinearRegression`
- Experimento: `linear_regression_mag`
- Dataset: `teddyT`
- Alvo: `redshift`
- Número de features: `5`
- Parâmetros: `{'fit_intercept': True}`

## Resumo do baseline

| Teste | MAE | RMSE | R² | Bias | NMAD | Outliers catastróficos | Predições negativas | N |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| B | 0.0266 | 0.0377 | 0.8161 | -0.0001 | 0.0216 | 0.10% | 0 | 74559 |
| C | 0.0282 | 0.0406 | 0.8337 | -0.0006 | 0.0223 | 0.18% | 0 | 97980 |
| D | 0.0514 | 0.0955 | 0.8072 | -0.0018 | 0.0372 | 2.01% | 1779 | 75925 |

## Teste B

- MAE: `0.026579`
- RMSE: `0.037651`
- R²: `0.816063`
- Bias: `-0.000113`
- NMAD: `0.021644`
- Erro padrão do NMAD: `0.000096`
- Fração de outliers catastróficos: `0.0993%`
- Limiar de outlier catastrófico: `0.15`
- Predições negativas de redshift: `0`
- N: `74559`

### Métricas por faixa de redshift

| Faixa de redshift | N | MAE | RMSE | Bias | NMAD | Predições negativas |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| z 0..0.1 | 23 | 0.1304 | 0.1727 | 0.1304 | 0.0742 | 0 |
| z 0.1..0.2 | 6306 | 0.0245 | 0.0364 | 0.0167 | 0.0193 | 0 |
| z 0.2..0.4 | 53153 | 0.0242 | 0.0334 | 0.0049 | 0.0206 | 0 |
| z 0.4..0.6 | 15002 | 0.0350 | 0.0475 | -0.0242 | 0.0232 | 0 |
| z 0.6..inf | 75 | 0.2010 | 0.2097 | -0.2010 | 0.0233 | 0 |

### Métricas por magnitude `r`

| Faixa de magnitude r | N | MAE | RMSE | Bias | NMAD | Predições negativas |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| (12.017000000000001, 17.942] | 18640 | 0.0193 | 0.0261 | -0.0007 | 0.0178 | 0 |
| (17.942, 18.619] | 18640 | 0.0242 | 0.0325 | 0.0007 | 0.0210 | 0 |
| (18.619, 19.174] | 18639 | 0.0257 | 0.0344 | -0.0007 | 0.0222 | 0 |
| (19.174, 20.985] | 18640 | 0.0371 | 0.0524 | 0.0002 | 0.0268 | 0 |

### Métricas por erro fotométrico médio

| Faixa de erro fotométrico médio | N | MAE | RMSE | Bias | NMAD | Predições negativas |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| (0.0457, 0.0941] | 18640 | 0.0195 | 0.0270 | 0.0037 | 0.0176 | 0 |
| (0.0941, 0.127] | 18640 | 0.0242 | 0.0331 | 0.0013 | 0.0208 | 0 |
| (0.127, 0.17] | 18639 | 0.0276 | 0.0378 | -0.0022 | 0.0228 | 0 |
| (0.17, 0.766] | 18640 | 0.0350 | 0.0491 | -0.0033 | 0.0265 | 0 |

## Teste C

- MAE: `0.028162`
- RMSE: `0.040598`
- R²: `0.833717`
- Bias: `-0.000601`
- NMAD: `0.022253`
- Erro padrão do NMAD: `0.000088`
- Fração de outliers catastróficos: `0.1776%`
- Limiar de outlier catastrófico: `0.15`
- Predições negativas de redshift: `0`
- N: `97980`

### Métricas por faixa de redshift

| Faixa de redshift | N | MAE | RMSE | Bias | NMAD | Predições negativas |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| z 0..0.1 | 43 | 0.1500 | 0.1893 | 0.1462 | 0.1317 | 0 |
| z 0.1..0.2 | 11889 | 0.0235 | 0.0343 | 0.0158 | 0.0191 | 0 |
| z 0.2..0.4 | 59116 | 0.0257 | 0.0363 | 0.0063 | 0.0214 | 0 |
| z 0.4..0.6 | 26778 | 0.0345 | 0.0473 | -0.0221 | 0.0237 | 0 |
| z 0.6..inf | 154 | 0.2094 | 0.2263 | -0.2094 | 0.0207 | 0 |

### Métricas por magnitude `r`

| Faixa de magnitude r | N | MAE | RMSE | Bias | NMAD | Predições negativas |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| (13.047, 17.852] | 24495 | 0.0192 | 0.0263 | 0.0006 | 0.0182 | 0 |
| (17.852, 18.722] | 24495 | 0.0252 | 0.0340 | 0.0007 | 0.0220 | 0 |
| (18.722, 19.352] | 24495 | 0.0267 | 0.0362 | -0.0004 | 0.0221 | 0 |
| (19.352, 22.289] | 24495 | 0.0416 | 0.0586 | -0.0033 | 0.0293 | 0 |

### Métricas por erro fotométrico médio

| Faixa de erro fotométrico médio | N | MAE | RMSE | Bias | NMAD | Predições negativas |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| (0.0453, 0.0929] | 24495 | 0.0196 | 0.0277 | 0.0040 | 0.0179 | 0 |
| (0.0929, 0.134] | 24495 | 0.0261 | 0.0363 | 0.0012 | 0.0219 | 0 |
| (0.134, 0.185] | 24495 | 0.0300 | 0.0420 | -0.0036 | 0.0234 | 0 |
| (0.185, 0.771] | 24495 | 0.0369 | 0.0524 | -0.0041 | 0.0270 | 0 |

## Teste D

- MAE: `0.051407`
- RMSE: `0.095472`
- R²: `0.807243`
- Bias: `-0.001801`
- NMAD: `0.037154`
- Erro padrão do NMAD: `0.000155`
- Fração de outliers catastróficos: `2.0125%`
- Limiar de outlier catastrófico: `0.15`
- Predições negativas de redshift: `1779`
- N: `75925`

### Métricas por faixa de redshift

| Faixa de redshift | N | MAE | RMSE | Bias | NMAD | Predições negativas |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| z 0..0.1 | 14096 | 0.0399 | 0.0953 | 0.0043 | 0.0406 | 1669 |
| z 0.1..0.2 | 13431 | 0.0315 | 0.0801 | 0.0035 | 0.0274 | 43 |
| z 0.2..0.4 | 10761 | 0.0450 | 0.0959 | -0.0045 | 0.0286 | 48 |
| z 0.4..0.6 | 28349 | 0.0507 | 0.0703 | 0.0070 | 0.0374 | 6 |
| z 0.6..inf | 9288 | 0.1074 | 0.1603 | -0.0423 | 0.0680 | 13 |

### Métricas por magnitude `r`

| Faixa de magnitude r | N | MAE | RMSE | Bias | NMAD | Predições negativas |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| (11.487, 17.412] | 18982 | 0.0305 | 0.0659 | -0.0035 | 0.0310 | 1492 |
| (17.412, 19.394] | 18981 | 0.0368 | 0.0734 | -0.0066 | 0.0319 | 167 |
| (19.394, 20.44] | 18981 | 0.0551 | 0.0850 | -0.0110 | 0.0359 | 43 |
| (20.44, 29.999] | 18981 | 0.0833 | 0.1396 | 0.0139 | 0.0463 | 77 |

### Métricas por erro fotométrico médio

| Faixa de erro fotométrico médio | N | MAE | RMSE | Bias | NMAD | Predições negativas |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| (0.0347, 0.0738] | 18982 | 0.0305 | 0.0444 | 0.0047 | 0.0301 | 450 |
| (0.0738, 0.182] | 18981 | 0.0484 | 0.0814 | -0.0182 | 0.0350 | 1041 |
| (0.182, 0.272] | 18981 | 0.0564 | 0.0876 | 0.0005 | 0.0390 | 147 |
| (0.272, 6.578] | 18981 | 0.0704 | 0.1421 | 0.0057 | 0.0436 | 141 |

# Baseline 2 — Linear Regression com magnitudes + erros (`mag_err`)

Usa magnitudes e erros fotométricos: `u`, `g`, `r`, `i`, `z`, `uErr`, `gErr`, `rErr`, `iErr`, `zErr`.

- Modelo: `LinearRegression`
- Experimento: `linear_regression_mag_err`
- Dataset: `teddyT`
- Alvo: `redshift`
- Número de features: `10`
- Parâmetros: `{'fit_intercept': True}`

## Resumo do baseline

| Teste | MAE | RMSE | R² | Bias | NMAD | Outliers catastróficos | Predições negativas | N |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| B | 0.0257 | 0.0368 | 0.8244 | -0.0000 | 0.0205 | 0.11% | 0 | 74559 |
| C | 0.0273 | 0.0398 | 0.8398 | -0.0006 | 0.0212 | 0.19% | 0 | 97980 |
| D | 0.0493 | 0.0908 | 0.8256 | 0.0020 | 0.0354 | 1.75% | 1784 | 75925 |

## Teste B

- MAE: `0.025709`
- RMSE: `0.036790`
- R²: `0.824378`
- Bias: `-0.000015`
- NMAD: `0.020548`
- Erro padrão do NMAD: `0.000089`
- Fração de outliers catastróficos: `0.1113%`
- Limiar de outlier catastrófico: `0.15`
- Predições negativas de redshift: `0`
- N: `74559`

### Métricas por faixa de redshift

| Faixa de redshift | N | MAE | RMSE | Bias | NMAD | Predições negativas |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| z 0..0.1 | 23 | 0.1401 | 0.1906 | 0.1401 | 0.0692 | 0 |
| z 0.1..0.2 | 6306 | 0.0224 | 0.0346 | 0.0143 | 0.0180 | 0 |
| z 0.2..0.4 | 53153 | 0.0234 | 0.0329 | 0.0053 | 0.0197 | 0 |
| z 0.4..0.6 | 15002 | 0.0344 | 0.0461 | -0.0242 | 0.0220 | 0 |
| z 0.6..inf | 75 | 0.1885 | 0.1987 | -0.1885 | 0.0207 | 0 |

### Métricas por magnitude `r`

| Faixa de magnitude r | N | MAE | RMSE | Bias | NMAD | Predições negativas |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| (12.017000000000001, 17.942] | 18640 | 0.0178 | 0.0247 | -0.0007 | 0.0160 | 0 |
| (17.942, 18.619] | 18640 | 0.0229 | 0.0311 | 0.0014 | 0.0198 | 0 |
| (18.619, 19.174] | 18639 | 0.0253 | 0.0338 | -0.0007 | 0.0217 | 0 |
| (19.174, 20.985] | 18640 | 0.0368 | 0.0519 | -0.0001 | 0.0265 | 0 |

### Métricas por erro fotométrico médio

| Faixa de erro fotométrico médio | N | MAE | RMSE | Bias | NMAD | Predições negativas |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| (0.0457, 0.0941] | 18640 | 0.0183 | 0.0257 | 0.0002 | 0.0164 | 0 |
| (0.0941, 0.127] | 18640 | 0.0233 | 0.0323 | 0.0013 | 0.0198 | 0 |
| (0.127, 0.17] | 18639 | 0.0270 | 0.0372 | -0.0014 | 0.0221 | 0 |
| (0.17, 0.766] | 18640 | 0.0342 | 0.0482 | -0.0001 | 0.0255 | 0 |

## Teste C

- MAE: `0.027349`
- RMSE: `0.039844`
- R²: `0.839833`
- Bias: `-0.000591`
- NMAD: `0.021178`
- Erro padrão do NMAD: `0.000085`
- Fração de outliers catastróficos: `0.1868%`
- Limiar de outlier catastrófico: `0.15`
- Predições negativas de redshift: `0`
- N: `97980`

### Métricas por faixa de redshift

| Faixa de redshift | N | MAE | RMSE | Bias | NMAD | Predições negativas |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| z 0..0.1 | 43 | 0.1560 | 0.1963 | 0.1528 | 0.1382 | 0 |
| z 0.1..0.2 | 11889 | 0.0216 | 0.0328 | 0.0133 | 0.0180 | 0 |
| z 0.2..0.4 | 59116 | 0.0250 | 0.0361 | 0.0068 | 0.0203 | 0 |
| z 0.4..0.6 | 26778 | 0.0340 | 0.0460 | -0.0222 | 0.0228 | 0 |
| z 0.6..inf | 154 | 0.1975 | 0.2161 | -0.1975 | 0.0219 | 0 |

### Métricas por magnitude `r`

| Faixa de magnitude r | N | MAE | RMSE | Bias | NMAD | Predições negativas |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| (13.047, 17.852] | 24495 | 0.0178 | 0.0250 | 0.0000 | 0.0163 | 0 |
| (17.852, 18.722] | 24495 | 0.0239 | 0.0326 | 0.0015 | 0.0205 | 0 |
| (18.722, 19.352] | 24495 | 0.0266 | 0.0360 | -0.0008 | 0.0221 | 0 |
| (19.352, 22.289] | 24495 | 0.0411 | 0.0580 | -0.0031 | 0.0290 | 0 |

### Métricas por erro fotométrico médio

| Faixa de erro fotométrico médio | N | MAE | RMSE | Bias | NMAD | Predições negativas |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| (0.0453, 0.0929] | 24495 | 0.0183 | 0.0264 | 0.0004 | 0.0165 | 0 |
| (0.0929, 0.134] | 24495 | 0.0253 | 0.0357 | 0.0014 | 0.0207 | 0 |
| (0.134, 0.185] | 24495 | 0.0297 | 0.0418 | -0.0034 | 0.0229 | 0 |
| (0.185, 0.771] | 24495 | 0.0360 | 0.0514 | -0.0008 | 0.0262 | 0 |

## Teste D

- MAE: `0.049321`
- RMSE: `0.090807`
- R²: `0.825618`
- Bias: `0.001960`
- NMAD: `0.035395`
- Erro padrão do NMAD: `0.000159`
- Fração de outliers catastróficos: `1.7544%`
- Limiar de outlier catastrófico: `0.15`
- Predições negativas de redshift: `1784`
- N: `75925`

### Métricas por faixa de redshift

| Faixa de redshift | N | MAE | RMSE | Bias | NMAD | Predições negativas |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| z 0..0.1 | 14096 | 0.0396 | 0.0972 | -0.0005 | 0.0368 | 1676 |
| z 0.1..0.2 | 13431 | 0.0339 | 0.0800 | -0.0047 | 0.0275 | 69 |
| z 0.2..0.4 | 10761 | 0.0439 | 0.0963 | 0.0043 | 0.0267 | 30 |
| z 0.4..0.6 | 28349 | 0.0487 | 0.0662 | 0.0161 | 0.0345 | 6 |
| z 0.6..inf | 9288 | 0.0945 | 0.1403 | -0.0305 | 0.0594 | 3 |

### Métricas por magnitude `r`

| Faixa de magnitude r | N | MAE | RMSE | Bias | NMAD | Predições negativas |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| (11.487, 17.412] | 18982 | 0.0301 | 0.0584 | -0.0098 | 0.0279 | 1459 |
| (17.412, 19.394] | 18981 | 0.0348 | 0.0648 | -0.0079 | 0.0291 | 273 |
| (19.394, 20.44] | 18981 | 0.0522 | 0.0799 | -0.0008 | 0.0327 | 31 |
| (20.44, 29.999] | 18981 | 0.0802 | 0.1378 | 0.0264 | 0.0415 | 21 |

### Métricas por erro fotométrico médio

| Faixa de erro fotométrico médio | N | MAE | RMSE | Bias | NMAD | Predições negativas |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| (0.0347, 0.0738] | 18982 | 0.0324 | 0.0485 | -0.0123 | 0.0313 | 976 |
| (0.0738, 0.182] | 18981 | 0.0462 | 0.0784 | -0.0132 | 0.0325 | 726 |
| (0.182, 0.272] | 18981 | 0.0538 | 0.0817 | 0.0125 | 0.0355 | 34 |
| (0.272, 6.578] | 18981 | 0.0650 | 0.1334 | 0.0208 | 0.0403 | 48 |
