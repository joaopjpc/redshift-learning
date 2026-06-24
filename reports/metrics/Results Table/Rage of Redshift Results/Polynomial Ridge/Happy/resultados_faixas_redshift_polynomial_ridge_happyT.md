# Desempenho por faixa de redshift - happyT - Polynomial Ridge

Resultados dos baselines `mag` e `mag_err` nos testes externos `B`, `C` e `D`. As métricas são calculadas separadamente dentro de cada faixa de redshift.

## Teste B

| Faixa | Baseline | N | MAE | RMSE | Bias | NMAD | Prev. negativas |
|---|---|---:|---:|---:|---:|---:|---:|
| z 0..0.1 | `mag` | 12878 | 0.0406 | 0.0765 | 0.0207 | 0.0373 | 764 |
| z 0..0.1 | `mag_err` | 12878 | 0.0304 | 0.0642 | 0.0166 | 0.0265 | 233 |
| z 0.1..0.2 | `mag` | 12719 | 0.0315 | 0.0560 | 0.0144 | 0.0267 | 23 |
| z 0.1..0.2 | `mag_err` | 12719 | 0.0267 | 0.0529 | 0.0039 | 0.0216 | 19 |
| z 0.2..0.4 | `mag` | 13434 | 0.0386 | 0.0611 | 0.0112 | 0.0288 | 8 |
| z 0.2..0.4 | `mag_err` | 13434 | 0.0367 | 0.0615 | 0.0155 | 0.0261 | 10 |
| z 0.4..0.6 | `mag` | 27319 | 0.0383 | 0.0525 | 0.0017 | 0.0300 | 7 |
| z 0.4..0.6 | `mag_err` | 27319 | 0.0351 | 0.0532 | 0.0023 | 0.0267 | 2 |
| z 0.6..inf | `mag` | 8550 | 0.0852 | 0.1233 | -0.0767 | 0.0431 | 3 |
| z 0.6..inf | `mag_err` | 8550 | 0.0753 | 0.1130 | -0.0619 | 0.0384 | 3 |

## Teste C

| Faixa | Baseline | N | MAE | RMSE | Bias | NMAD | Prev. negativas |
|---|---|---:|---:|---:|---:|---:|---:|
| z 0..0.1 | `mag` | 3213 | 0.1812 | 0.2254 | 0.1659 | 0.1452 | 141 |
| z 0..0.1 | `mag_err` | 3213 | 0.1480 | 0.1951 | 0.1351 | 0.1183 | 119 |
| z 0.1..0.2 | `mag` | 7877 | 0.1308 | 0.1569 | 0.1250 | 0.0753 | 35 |
| z 0.1..0.2 | `mag_err` | 7877 | 0.1001 | 0.1299 | 0.0920 | 0.0665 | 33 |
| z 0.2..0.4 | `mag` | 21701 | 0.0907 | 0.1117 | 0.0804 | 0.0592 | 8 |
| z 0.2..0.4 | `mag_err` | 21701 | 0.0720 | 0.0964 | 0.0518 | 0.0532 | 25 |
| z 0.4..0.6 | `mag` | 20706 | 0.0643 | 0.0817 | 0.0089 | 0.0529 | 15 |
| z 0.4..0.6 | `mag_err` | 20706 | 0.0628 | 0.0820 | -0.0080 | 0.0504 | 7 |
| z 0.6..inf | `mag` | 6818 | 0.1416 | 0.1994 | -0.1323 | 0.0675 | 3 |
| z 0.6..inf | `mag_err` | 6818 | 0.1398 | 0.2032 | -0.1254 | 0.0703 | 3 |

## Teste D

| Faixa | Baseline | N | MAE | RMSE | Bias | NMAD | Prev. negativas |
|---|---|---:|---:|---:|---:|---:|---:|
| z 0..0.1 | `mag` | 3265 | 0.2832 | 0.3605 | 0.2283 | 0.2263 | 252 |
| z 0..0.1 | `mag_err` | 3265 | 0.2518 | 0.3769 | 0.2239 | 0.1997 | 146 |
| z 0.1..0.2 | `mag` | 5876 | 0.1872 | 0.2282 | 0.1717 | 0.1101 | 82 |
| z 0.1..0.2 | `mag_err` | 5876 | 0.1540 | 0.2159 | 0.1410 | 0.0990 | 54 |
| z 0.2..0.4 | `mag` | 20281 | 0.1309 | 0.1631 | 0.1204 | 0.0743 | 46 |
| z 0.2..0.4 | `mag_err` | 20281 | 0.1045 | 0.1495 | 0.0853 | 0.0698 | 50 |
| z 0.4..0.6 | `mag` | 26237 | 0.0776 | 0.1041 | 0.0255 | 0.0608 | 37 |
| z 0.4..0.6 | `mag_err` | 26237 | 0.0753 | 0.1465 | -0.0054 | 0.0592 | 23 |
| z 0.6..inf | `mag` | 18983 | 0.1683 | 0.2391 | -0.1563 | 0.0739 | 30 |
| z 0.6..inf | `mag_err` | 18983 | 0.1855 | 0.3008 | -0.1698 | 0.0763 | 28 |

## Leitura rápida

- No teste B, `mag_err` melhora principalmente MAE e NMAD em todas as faixas.
- No teste C, `mag_err` é especialmente útil abaixo de `z = 0.4`; acima disso, as diferenças são menores e o RMSE nem sempre melhora.
- No teste D, `mag_err` reduz o MAE até `z = 0.6`, mas há piora importante de RMSE nas faixas extremas e piora geral em `z >= 0.6`.
