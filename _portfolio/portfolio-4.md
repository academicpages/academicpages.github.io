---
title: "PREDICTION WAGE: BASIC VS FLEXIBLE MODEL"
excerpt: "In this Python [Script](https://github.com/alexanderquispe/ECO224/blob/main/Labs/replication_2/Group5_Lab2_Python.ipynb), we use two different prediction rules for the hourly wage $Y$ using OLS: the basic model and the flexible model.  Also, we use the partilliang out using lasso tool in both models and the idea of sample splitting. "

collection: portfolio
---
[Script](https://github.com/alexanderquispe/ECO224/blob/main/Labs/replication_2/Group5_Lab2_Python.ipynb) : In the flexible model, in addition to the regressors of the basic model we add the occupation and industry indicators, the transformations and the interactions of experience with other regressors. As a result we find that in terms of prediction the flexible model performs better, as it has a high $R^2_{adjusted}$ and a low $MSE_{adjusted}$, in contrast to the basic one.