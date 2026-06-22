# Test MAE by Redshift Results

## Dataset Happy MAE

|       Modelo      | Baseline|  z 0..0.1  | z 0.1..0.2 | z 0.2..0.4  |  z 0.4..0.6 |  z 0.6..inf |
| Linear Regression |   MAG   |  0.100708  |  0.087383  |   0.074546  |   0.067365  |  0.186509   |
| Polynomial Ridge  |   MAG   |  0.097750  |  0.088276  |   0.087157  |   0.061626  | **0.148454**| -> degree2 alpha10

| Linear Regression | MAG_ERR |**0.094631**| 0.083698   |   0.076146  |   0.060635  |   0.170060  |
| Polynomial Ridge  | MAG_ERR |  0.102011  |**0.070548**| **0.070082**| **0.058569**|   0.350185  | -> degree2 alpha5



## Dataset Teddy MAE

|      Modelo       | Baseline|  z 0..0.1  | z 0.1..0.2  |  z 0.2..0.4 |  z 0.4..0.6 | z 0.6..inf  |
| Linear Regression |   MAG   |**0.036790**|   0.025594  |   0.026589  |   0.045865  |   0.132788  |
| Polynomial Ridge  |   MAG   |4.222807e+08| 3.301872e+06| 4.684618e+19|   0.076631  |   0.433570  | -> degree2 alpha0.5

| Linear Regression | MAG_ERR |  0.037517  | **0.025197**| **0.026065**| **0.043504**| **0.112485**|
| Polynomial Ridge  | MAG_ERR |4.591390e+06| 5.920451e+04| 1.994189e+07|   0.068914  |   0.260127  | -> degree2 alpha5




## Dataset Happy MAE
|     z 0..0.1     |     z 0.1..0.2     |    z 0.2..0.4    |    z 0.4..0.6    |    z 0.6..inf    |
| Linear + MAG_ERR |    Poly + MAG_ERR  |  Poly + MAG_ERR  |  Poly + MAG_ERR  |    Poly + MAG    |


## Dataset Teddy MAE
|     z 0..0.1     |     z 0.1..0.2     |   z 0.2..0.4     |    z 0.4..0.6    |    z 0.6..inf    |
|  Linear + MAG    | Linear + MAG_ERR   | Linear + MAG_ERR | Linear + MAG_ERR | Linear + MAG_ERR |