# Resultados dos baselines - happyT - Linear Regression

Resultados dos baselines `mag`, `mag_err` e `gate-err` no dataset `happyT`, avaliados separadamente nos testes externos `B`, `C` e `D`.

Todos os valores foram extra?dos diretamente dos JSONs em `reports/metrics/Tests/`. Em cada teste, o melhor valor entre os tr?s baselines est? em **negrito**.

## M?tricas reportadas

| M?trica | Interpreta??o | Melhor dire??o |
|---|---|---|
| MAE | erro absoluto m?dio | menor |
| RMSE | raiz do erro quadr?tico m?dio; penaliza mais erros grandes | menor |
| R? | propor??o da vari?ncia explicada | maior |
| Bias | m?dia do erro de previs?o | mais pr?ximo de 0 |
| NMAD | m?trica robusta de dispers?o do erro | menor |
| Outliers catastr?ficos | fra??o de objetos com erro acima do limiar configurado | menor |
| Predi??es negativas | n?mero de previs?es de redshift negativo | menor |

## Compara??o geral entre os baselines

| Teste | Baseline | MAE | RMSE | R? | Bias | NMAD | Outliers catastr?ficos | Predi??es negativas | N |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| B | `mag` | 0.0484 | 0.0767 | 0.8684 | -0.0003 | 0.0369 | 1.90% | 1631 | 74900 |
| B | `mag_err` | **0.0438** | **0.0728** | **0.8814** | **-0.0002** | **0.0327** | **1.67%** | **911** | 74900 |
| B | `gate-err` | 0.0483 | 0.0765 | 0.8690 | -0.0004 | 0.0366 | 1.97% | 1765 | 74900 |
|  |  |  |  |  |  |  |  |  |  |
| C | `mag` | 0.0995 | 0.1322 | 0.4775 | 0.0343 | 0.0779 | 11.05% | **163** | 60315 |
| C | `mag_err` | **0.0934** | **0.1289** | **0.5033** | **0.0200** | **0.0735** | **9.54%** | 210 | 60315 |
| C | `gate-err` | 0.0991 | 0.1321 | 0.4786 | 0.0334 | 0.0778 | 11.02% | 175 | 60315 |
|  |  |  |  |  |  |  |  |  |  |
| D | `mag` | 0.1363 | 0.1958 | 0.2129 | -0.0191 | 0.1059 | 18.11% | 485 | 74642 |
| D | `mag_err` | **0.1306** | **0.1946** | **0.2224** | **0.0007** | **0.0985** | **17.07%** | **428** | 74642 |
| D | `gate-err` | 0.1367 | 0.1969 | 0.2043 | -0.0225 | 0.1057 | 18.31% | 493 | 74642 |

## Resultados por baseline e teste

## Baseline 1 - Linear Regression com magnitudes (`mag`)

- **Feature set:** `mag`
- **Features finais:** `u`, `g`, `r`, `i`, `z`
- **Par?metros selecionados:** fit_intercept=True

| Teste | N | MAE | RMSE | R? | Bias | NMAD | Outliers catastr?ficos | Predi??es negativas |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| B | 74900 | 0.0484 | 0.0767 | 0.8684 | -0.0003 | 0.0369 | 1.90% | 1631 |
| C | 60315 | 0.0995 | 0.1322 | 0.4775 | 0.0343 | 0.0779 | 11.05% | 163 |
| D | 74642 | 0.1363 | 0.1958 | 0.2129 | -0.0191 | 0.1059 | 18.11% | 485 |

### Teste B

- **Experimento:** `linear_regression_mag`
- **Par?metros:** fit_intercept=True

| M?trica | Valor |
|---|---:|
| N | 74900 |
| MAE | 0.048444 |
| RMSE | 0.076650 |
| R? | 0.868445 |
| Bias | -0.000344 |
| NMAD | 0.036939 |
| Erro-padr?o do NMAD | 0.000158 |
| Fra??o de outliers catastr?ficos | 1.90% |
| Limiar de outlier catastr?fico | 0.15 |
| Predi??es negativas de redshift | 1631 |

### Teste C

- **Experimento:** `linear_regression_mag`
- **Par?metros:** fit_intercept=True

| M?trica | Valor |
|---|---:|
| N | 60315 |
| MAE | 0.099514 |
| RMSE | 0.132226 |
| R? | 0.477471 |
| Bias | 0.034258 |
| NMAD | 0.077940 |
| Erro-padr?o do NMAD | 0.000400 |
| Fra??o de outliers catastr?ficos | 11.05% |
| Limiar de outlier catastr?fico | 0.15 |
| Predi??es negativas de redshift | 163 |

### Teste D

- **Experimento:** `linear_regression_mag`
- **Par?metros:** fit_intercept=True

| M?trica | Valor |
|---|---:|
| N | 74642 |
| MAE | 0.136347 |
| RMSE | 0.195824 |
| R? | 0.212852 |
| Bias | -0.019149 |
| NMAD | 0.105939 |
| Erro-padr?o do NMAD | 0.000450 |
| Fra??o de outliers catastr?ficos | 18.11% |
| Limiar de outlier catastr?fico | 0.15 |
| Predi??es negativas de redshift | 485 |

## Baseline 2 - Linear Regression com magnitudes + erros fotom?tricos (`mag_err`)

- **Feature set:** `mag_err`
- **Features finais:** `u`, `g`, `r`, `i`, `z`, `uErr`, `gErr`, `rErr`, `iErr`, `zErr`
- **Par?metros selecionados:** fit_intercept=True

| Teste | N | MAE | RMSE | R? | Bias | NMAD | Outliers catastr?ficos | Predi??es negativas |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| B | 74900 | 0.0438 | 0.0728 | 0.8814 | -0.0002 | 0.0327 | 1.67% | 911 |
| C | 60315 | 0.0934 | 0.1289 | 0.5033 | 0.0200 | 0.0735 | 9.54% | 210 |
| D | 74642 | 0.1306 | 0.1946 | 0.2224 | 0.0007 | 0.0985 | 17.07% | 428 |

### Teste B

- **Experimento:** `linear_regression_mag_err`
- **Par?metros:** fit_intercept=True

| M?trica | Valor |
|---|---:|
| N | 74900 |
| MAE | 0.043827 |
| RMSE | 0.072793 |
| R? | 0.881351 |
| Bias | -0.000208 |
| NMAD | 0.032730 |
| Erro-padr?o do NMAD | 0.000140 |
| Fra??o de outliers catastr?ficos | 1.67% |
| Limiar de outlier catastr?fico | 0.15 |
| Predi??es negativas de redshift | 911 |

### Teste C

- **Experimento:** `linear_regression_mag_err`
- **Par?metros:** fit_intercept=True

| M?trica | Valor |
|---|---:|
| N | 60315 |
| MAE | 0.093397 |
| RMSE | 0.128912 |
| R? | 0.503336 |
| Bias | 0.019979 |
| NMAD | 0.073490 |
| Erro-padr?o do NMAD | 0.000418 |
| Fra??o de outliers catastr?ficos | 9.54% |
| Limiar de outlier catastr?fico | 0.15 |
| Predi??es negativas de redshift | 210 |

### Teste D

- **Experimento:** `linear_regression_mag_err`
- **Par?metros:** fit_intercept=True

| M?trica | Valor |
|---|---:|
| N | 74642 |
| MAE | 0.130637 |
| RMSE | 0.194628 |
| R? | 0.222434 |
| Bias | 0.000686 |
| NMAD | 0.098518 |
| Erro-padr?o do NMAD | 0.000457 |
| Fra??o de outliers catastr?ficos | 17.07% |
| Limiar de outlier catastr?fico | 0.15 |
| Predi??es negativas de redshift | 428 |

## Baseline 3 - Linear Regression com magnitudes ponderadas pelos erros (`gate-err`)

- **Feature set:** `gate_err_manual`
- **Features finais:** `u_gate`, `g_gate`, `r_gate`, `i_gate`, `z_gate`
- **Par?metros selecionados:** gate_strength=0.1, fit_intercept=True

| Teste | N | MAE | RMSE | R? | Bias | NMAD | Outliers catastr?ficos | Predi??es negativas |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| B | 74900 | 0.0483 | 0.0765 | 0.8690 | -0.0004 | 0.0366 | 1.97% | 1765 |
| C | 60315 | 0.0991 | 0.1321 | 0.4786 | 0.0334 | 0.0778 | 11.02% | 175 |
| D | 74642 | 0.1367 | 0.1969 | 0.2043 | -0.0225 | 0.1057 | 18.31% | 493 |

### Teste B

- **Experimento:** `linear_regression_gate_err_manual_strength0.1`
- **Par?metros:** gate_strength=0.1, fit_intercept=True

| M?trica | Valor |
|---|---:|
| N | 74900 |
| MAE | 0.048318 |
| RMSE | 0.076502 |
| R? | 0.868952 |
| Bias | -0.000379 |
| NMAD | 0.036614 |
| Erro-padr?o do NMAD | 0.000166 |
| Fra??o de outliers catastr?ficos | 1.97% |
| Limiar de outlier catastr?fico | 0.15 |
| Predi??es negativas de redshift | 1765 |

### Teste C

- **Experimento:** `linear_regression_gate_err_manual_strength0.1`
- **Par?metros:** gate_strength=0.1, fit_intercept=True

| M?trica | Valor |
|---|---:|
| N | 60315 |
| MAE | 0.099115 |
| RMSE | 0.132084 |
| R? | 0.478586 |
| Bias | 0.033373 |
| NMAD | 0.077833 |
| Erro-padr?o do NMAD | 0.000416 |
| Fra??o de outliers catastr?ficos | 11.02% |
| Limiar de outlier catastr?fico | 0.15 |
| Predi??es negativas de redshift | 175 |

### Teste D

- **Experimento:** `linear_regression_gate_err_manual_strength0.1`
- **Par?metros:** gate_strength=0.1, fit_intercept=True

| M?trica | Valor |
|---|---:|
| N | 74642 |
| MAE | 0.136742 |
| RMSE | 0.196890 |
| R? | 0.204258 |
| Bias | -0.022522 |
| NMAD | 0.105738 |
| Erro-padr?o do NMAD | 0.000446 |
| Fra??o de outliers catastr?ficos | 18.31% |
| Limiar de outlier catastr?fico | 0.15 |
| Predi??es negativas de redshift | 493 |
