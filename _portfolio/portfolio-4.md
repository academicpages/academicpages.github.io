---
title: "House Price Prediction Regression Modeling"
excerpt: "This notebook provides an implementation of a recommender system using PyTorch and demonstrates how to train and evaluate the model on a dataset of grocery transactions. The system utilizes item embeddings to represent the items in the dataset and computes their similarity to make recommendations.

<br/><img src='https://private-user-images.githubusercontent.com/75142232/240875224-0a2891df-3ecf-4702-9cbc-f57f55286884.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDY2NDAzNTksIm5iZiI6MTcwNjY0MDA1OSwicGF0aCI6Ii83NTE0MjIzMi8yNDA4NzUyMjQtMGEyODkxZGYtM2VjZi00NzAyLTljYmMtZjU3ZjU1Mjg2ODg0LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAxMzAlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMTMwVDE4NDA1OVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTYxZTBmNzA5ODg1NmEyNmI3YWMwZDdkM2ZiOWY1OTY3ZjVhNGIyM2NhZWNjNzhiZDZmMDY3ZGU5NTFmMTU0NGEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.oWouFq2wBOJh9kYsZhjLjXqhr2HSC1nnE8EbcQVRcxg'>"
collection: portfolio
---

# Groceries Recommender System
## Scalable Recommender System Development with PyTorch and Pandas for Enhanced Personalization

> By $Salar$ $Mokhtari$ $Laleh$


![Pink and Peach Technology LinkedIn Banner (3)](https://github.com/salarMokhtariL/salarMokhtariL/assets/75142232/0a2891df-3ecf-4702-9cbc-f57f55286884)



# Introduction
This notebook provides an implementation of a recommender system using PyTorch and demonstrates how to train and evaluate the model on a dataset of grocery transactions. The system utilizes item embeddings to represent the items in the dataset and computes their similarity to make recommendations.

# Dataset
The dataset used in this notebook is a list of grocery transactions. Each transaction consists of a list of items purchased by a customer. The dataset is available at the following URL:

https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/groceries.csv

# Implementation
The implementation consists of the following steps:

Load the dataset using pandas and convert it to a list of lists.
Create a dictionary to map each item to a unique integer.
Convert the dataset to a list of lists of integers using the mapping dictionary.
Convert the dataset to a PyTorch tensor.
Define the model architecture using PyTorch.
Train the model on the dataset using PyTorch.
Compute the item embeddings and similarity matrix.
Generate recommendations for each item using the similarity matrix.
