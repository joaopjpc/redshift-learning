# Desempenho por faixa de redshift - teddyT - Linear Regression

Resultados dos baselines `mag` e `mag_err` nos testes externos `B`, `C` e `D`. As métricas são calculadas separadamente dentro de cada faixa de redshift.

## Teste B

| Faixa | Baseline | N | MAE | RMSE | Bias | NMAD | Prev. negativas |
|---|---|---:|---:|---:|---:|---:|---:|
| z 0..0.1 | `mag` | 23 | 0.1304 | 0.1727 | 0.1304 | 0.0742 | 0 |
| z 0..0.1 | `mag_err` | 23 | 0.1401 | 0.1906 | 0.1401 | 0.0692 | 0 |
| z 0.1..0.2 | `mag` | 6306 | 0.0245 | 0.0364 | 0.0167 | 0.0193 | 0 |
| z 0.1..0.2 | `mag_err` | 6306 | 0.0224 | 0.0346 | 0.0143 | 0.0180 | 0 |
| z 0.2..0.4 | `mag` | 53153 | 0.0242 | 0.0334 | 0.0049 | 0.0206 | 0 |
| z 0.2..0.4 | `mag_err` | 53153 | 0.0234 | 0.0329 | 0.0053 | 0.0197 | 0 |
| z 0.4..0.6 | `mag` | 15002 | 0.0350 | 0.0475 | -0.0242 | 0.0232 | 0 |
| z 0.4..0.6 | `mag_err` | 15002 | 0.0344 | 0.0461 | -0.0242 | 0.0220 | 0 |
| z 0.6..inf | `mag` | 75 | 0.2010 | 0.2097 | -0.2010 | 0.0233 | 0 |
| z 0.6..inf | `mag_err` | 75 | 0.1885 | 0.1987 | -0.1885 | 0.0207 | 0 |

## Teste C

| Faixa | Baseline | N | MAE | RMSE | Bias | NMAD | Prev. negativas |
|---|---|---:|---:|---:|---:|---:|---:|
| z 0..0.1 | `mag` | 43 | 0.1500 | 0.1893 | 0.1462 | 0.1317 | 0 |
| z 0..0.1 | `mag_err` | 43 | 0.1560 | 0.1963 | 0.1528 | 0.1382 | 0 |
| z 0.1..0.2 | `mag` | 11889 | 0.0235 | 0.0343 | 0.0158 | 0.0191 | 0 |
| z 0.1..0.2 | `mag_err` | 11889 | 0.0216 | 0.0328 | 0.0133 | 0.0180 | 0 |
| z 0.2..0.4 | `mag` | 59116 | 0.0257 | 0.0363 | 0.0063 | 0.0214 | 0 |
| z 0.2..0.4 | `mag_err` | 59116 | 0.0250 | 0.0361 | 0.0068 | 0.0203 | 0 |
| z 0.4..0.6 | `mag` | 26778 | 0.0345 | 0.0473 | -0.0221 | 0.0237 | 0 |
| z 0.4..0.6 | `mag_err` | 26778 | 0.0340 | 0.0460 | -0.0222 | 0.0228 | 0 |
| z 0.6..inf | `mag` | 154 | 0.2094 | 0.2263 | -0.2094 | 0.0207 | 0 |
| z 0.6..inf | `mag_err` | 154 | 0.1975 | 0.2161 | -0.1975 | 0.0219 | 0 |

## Teste D

| Faixa | Baseline | N | MAE | RMSE | Bias | NMAD | Prev. negativas |
|---|---|---:|---:|---:|---:|---:|---:|
| z 0..0.1 | `mag` | 14096 | 0.0399 | 0.0953 | 0.0043 | 0.0406 | 1669 |
| z 0..0.1 | `mag_err` | 14096 | 0.0396 | 0.0972 | -0.0005 | 0.0368 | 1676 |
| z 0.1..0.2 | `mag` | 13431 | 0.0315 | 0.0801 | 0.0035 | 0.0274 | 43 |
| z 0.1..0.2 | `mag_err` | 13431 | 0.0339 | 0.0800 | -0.0047 | 0.0275 | 69 |
| z 0.2..0.4 | `mag` | 10761 | 0.0450 | 0.0959 | -0.0045 | 0.0286 | 48 |
| z 0.2..0.4 | `mag_err` | 10761 | 0.0439 | 0.0963 | 0.0043 | 0.0267 | 30 |
| z 0.4..0.6 | `mag` | 28349 | 0.0507 | 0.0703 | 0.0070 | 0.0374 | 6 |
| z 0.4..0.6 | `mag_err` | 28349 | 0.0487 | 0.0662 | 0.0161 | 0.0345 | 6 |
| z 0.6..inf | `mag` | 9288 | 0.1074 | 0.1603 | -0.0423 | 0.0680 | 13 |
| z 0.6..inf | `mag_err` | 9288 | 0.0945 | 0.1403 | -0.0305 | 0.0594 | 3 |

## Leitura rápida

- Nos testes B e C, `mag_err` traz ganhos pequenos e consistentes nas faixas com maior quantidade de objetos.
- As faixas extremas de B e C possuem apenas dezenas ou centenas de objetos e devem ser interpretadas com cautela.
- No teste D, `mag_err` ajuda principalmente em `z >= 0.2`, com a melhora mais clara em `z >= 0.6`.
