# Test Global Baseline Results

## Dataset Happy

| Modelo            | Baseline | test_nmad  |  test_rmse | Config          |
|-------------------|----------|------------|------------|-----------------|
| Linear Regression |   MAG    |  0.066074  |  0.144629  | -               |
| Polynomial Ridge  |   MAG    |  0.059798  |**0.135730**| degree2 alpha10 |

| Linear Regression | MAG_ERR  |  0.059604  |  0.161276  | -               |
| Polynomial Ridge  | MAG_ERR  |**0.051158**|  13.43771  | degree2 alpha5  |



## Dataset Teddy

| Modelo            | Baseline | test_nmad  |  test_rmse  |    Config        |
|-------------------|----------|------------|-------------|------------------|
| Linear Regression |   MAG    | 0.025870   | **0.104229**| -                |
| Polynomial Ridge  |   MAG    | 0.025419** | 1.156255e+22| degree2 alpha0.5 |

| Linear Regression | MAG_ERR  | 0.024444   |   0.150902  | -                |
| Polynomial Ridge  | MAG_ERR  |**0.022682**| 4.024657e+09| degree2 alpha5   |





Com NMAD, MAG_ERR + Polynomial Ridge vence sempre
Com RMSE, MAG vence sempre