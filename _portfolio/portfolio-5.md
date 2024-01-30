---
title: "Predicting Diabetes using a Neural Network Model Trained on Clinical Data"
excerpt: "Diabetes prediction is the use of data and algorithms to determine the likelihood of an individual developing diabetes. This helps with early detection and prevention of complications associated with the disease, allowing for improved patient outcomes.



<br/><img src='https://private-user-images.githubusercontent.com/75142232/237525868-6f8f0b5a-41b8-4518-b8df-eec991df8fce.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDY2NDA0NzEsIm5iZiI6MTcwNjY0MDE3MSwicGF0aCI6Ii83NTE0MjIzMi8yMzc1MjU4NjgtNmY4ZjBiNWEtNDFiOC00NTE4LWI4ZGYtZWVjOTkxZGY4ZmNlLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAxMzAlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMTMwVDE4NDI1MVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWI2YmMwMTM0ZDNjZmRhYjBiOThkMzQ2MmM4YzdkMzM3YzNlODJjM2IxZTQwYjNlYzQxNDI0MWVlZTY0NDg4MTImWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.eG_v-EnL5zyh_RnPaWP3p5kzLrKMlDxRWVJJNKdcwWk'>"
collection: portfolio
---

# Predicting Diabetes using a Neural Network Model Trained on Clinical Data
## An Evaluation of Accuracy, Precision, Recall, and F1 Score

> $By$ $Salar$ $Mokhtari$ $Laleh$ 

![Pink and Peach Technology LinkedIn Banner (2)](https://github.com/salarMokhtariL/Diabetes-prediction/assets/75142232/6f8f0b5a-41b8-4518-b8df-eec991df8fce)

# Introduction
This project aims to predict diabetes in individuals using a neural network model. The dataset used for training and testing the model is publicly available and contains information about eight medical predictors (e.g., glucose level, age, and blood pressure) and one target variable indicating whether or not the individual has diabetes.

# Dependencies

This code requires the following dependencies:

* torch
* numpy
* pandas
* scikit-learn


You can install them using pip:

```
pip install torch numpy pandas scikit-learn
```

# Usage
Clone the repository:

```
git clone https://github.com/salarMokhtariL/Diabetes-prediction.git
```
Navigate to the code directory:
```
cd Diabetes-prediction
```

Run the Jupyter Notebook file:

```
jupyter notebook diabetes_prediction.ipynb
```
Follow the instructions in the notebook to execute the code.


# Methods
## Data Preprocessing
The first step in building the model was to load the dataset and preprocess it for training and testing. The dataset was loaded from a remote source and stored in a pandas DataFrame. The input features (predictors) and target variable were then separated into different numpy arrays. To split the dataset into training and testing sets, we used the `train_test_split()` function from scikit-learn, which randomly divides the data into two sets with a specified test size and random state. Finally, the numpy arrays were converted to PyTorch tensors, which are required for training the neural network.

## Neural Network Model
The neural network model used for this task consists of three fully connected layers with 8, 32, and 16 neurons, respectively. Each layer is followed by a batch normalization layer and a ReLU activation function. Additionally, the second and third layers are followed by a dropout layer with a dropout probability of 0.2. The output layer has a single neuron with a sigmoid activation function, which produces a probability value that indicates the likelihood of a patient having diabetes.

The model is trained using the binary cross-entropy loss function and the Adam optimization algorithm.

The neural network model is defined using the following formula:

$y= \sigma(W_3.ReLU(BN_2(W_2.ReLU(BN_1(W_1.x))))$

where $x$ is the input feature vector, $W_1$, $W_2$, and $W_3$ are the weight matrices of the three fully connected layers, $BN_1$ and $BN_2$ are the batch normalization layers, and $\sigma$ is the sigmoid activation function.

## Loss Function and Optimization
We used the binary cross-entropy loss function, also known as the log loss, to calculate the error between the predicted and actual values. The Adam optimizer was used to minimize this loss function and update the model parameters during training.

## Training
The neural network model is trained on the diabetes dataset using the Adam optimizer with a learning rate of 0.001. The training process involves updating the weights of the neural network by minimizing the binary cross-entropy loss between the predicted labels and the ground truth labels. The binary cross-entropy loss is defined as follows:

$BinaryCrossEntropyLoss (y,\hat{y})= - \frac{1}{N} \displaystyle\sum_{i=1}^{N} [y_i \log(\hat{y_i})+(1-y_i) \log(1-\hat{y_i}]$

where $y$ is the ground truth label vector, $\hat{y}$ is the predicted label vector, and $N$ is the number of samples.

The neural network model is trained for 1000 epochs with a batch size of 1. During each epoch, the optimizer computes the gradients of the loss function with respect to the model parameters and updates the parameters accordingly. The training loss is monitored every 100 epochs to ensure that the model is converging.

## Evaluation
The trained neural network model is evaluated on a held-out test set using several evaluation metrics, including accuracy, precision, recall, and F1 score. The evaluation metrics are computed as follows:

$Accuracy = \frac{TP+TN}{TP+TN+FP+FN} $

$Precision = \frac{TP}{TP+FP} $

$Recall = \frac{TP}{TP+TN} $

$F1 Score = 2.{\frac{Precision⋅Recall}{Precision⋅Recall}} $

where $TP$ is the number of true positives, $TN$ is the number of true negatives, $FP$ is the number of false positives, and $FN$ is the number of false negatives.

The evaluation metrics provide a quantitative measure of the performance of the neural network model. A higher accuracy, precision, recall, and F1 score indicate better performance.
# Results
The trained model achieved an accuracy of 0.7792, a precision of 0.6818, a recall of 0.6571, and an F1 score of 0.6693 on the testing set. These results indicate that the model has a moderate predictive performance for diabetes in individuals.

# Conclusion
In this project, we developed a neural network model to predict diabetes in individuals using eight medical predictors. The model achieved moderate performance on the testing set, indicating that the predictors used in this study have some predictive value for diabetes. Further research could be conducted to explore the use of other predictors or models to improve the predictive performance.

# License
This project is licensed under the [Salar Mokhtari Laleh Open-Source License](https://github.com/salarMokhtariL/Salar-Mokhtari-Laleh-License). See the LICENSE file for details
