---
title: "Model Resuability in SparkML Library"
excerpt: "Custom Transformer and Model Reusability in sparkML Library"
collection: portfolio
---
<div style="float: right; margin-left: 20px; width: 33%;">
    <img src='/images/sparkMLPipelineFlow.webp' style="width: 100%;display: block;">
</div>

This project demonstrates the development and integration of custom estimators and transformers within the SparkML pipeline framework.

Using a loan prediction dataset, I perform exploratory data analysis to understand the raw data. The preprocessing steps include:

    - Converting feature data types using custom estimators and transformers
    - Imputing missing values with custom estimators and transformers
    - Indexing categorical feature levels using StringIndexer
    - Encoding categorical features using OneHotEncoder
    - Assembling input features into a vector using VectorAssembler

I then build a logistic regression model and interpret the results. A pipeline is created, encompassing all preprocessing stages and model building steps. The final PipelineModel is used to save the model artifact, which can be reloaded to score new or unseen data without retraining.

This project showcases the flexibility of SparkML, the power of custom components, and the efficiency of model reusability in machine learning workflows.

[Git Repository](https://github.com/ryputtam/misc_learn_lab/tree/main/02_LR_spakMLlib) 
