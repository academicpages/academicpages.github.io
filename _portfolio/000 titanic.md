---
title: "Predicting Survival Rates on the Titanic"
collection: portfolio
---

In this project the Titanic survivor data set is used. The goal is to fit a model that
accurately predicts which passengers survived by learning
the relationships between the individual passenger-characteristics
and their survival rate. The data set is first studied to determine
what pre-processing procedures or ML methods are necessary. A
simple model with the original features and a complex model with
engineered features is applied to test for interactions or non-linear
relationships between the variables. Data is split into training and
testing using cross-validation-resampling. The models are tuned using
grid search and performance is measured using accuracy score.
An ensemble model combines all the models into one. A prediction
with the ensemble model is submitted to Kaggle.com using the provided
hold out set. 

[Working Paper](https://gzhelev2020.github.io/files/Titanic_Paper.pdf)

[Notebook in PDF-Version](https://gzhelev2020.github.io/files/Titanic_Jupyter.pdf)
