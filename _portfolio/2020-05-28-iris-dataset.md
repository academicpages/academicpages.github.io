---
title: "The Iris dataset"
excerpt: "The iris dataset is quite famouse in the machine learning world. Introduced by the British statistician and biologist Ronald fisher, it quantifies the morphologic variation for three related species of Iris flowers. [Read more..](/portfolio/2020-05-28-iris-dataset/)<br><img src='/images/2020-05-28-iris-dataset/iris&me.png' style='max-width: 500px;' height='300'/><br>"
collection: portfolio
---

# 1. Import the data


```python
from sklearn.datasets import load_iris

iris = load_iris()

```

We can assume with scikit learn that it's clean data. So after importing we need to split the data into training and test sets. In order to do this we can use the concept of X and Y in ML. X = input we want to give
Y is going to be the target.


```python
X = iris.data
y = iris.target

feature_names = iris.feature_names
target_names = iris.target_names

```


```python
type(X)
```




    numpy.ndarray



# 2. Split the data 


```python
from sklearn.model_selection import train_test_split
```


```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)
```


```python
#return the dimensions (how many rows and colums)
print(X_train.shape)
print(X_test.shape)
```

    (135, 4)
    (15, 4)


# 3. Create the model


```python
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
```




    KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
               metric_params=None, n_jobs=1, n_neighbors=3, p=2,
               weights='uniform')



# 4. Check the output.

[Understanding the algorithm](https://www.analyticsvidhya.com/blog/2018/08/k-nearest-neighbor-introduction-regression-python/)


```python
# predict what type of flowers there are based on the model we gave 
y_pred = knn.predict(X_test)
```


```python
from sklearn import metrics
print(metrics.accuracy_score(y_test, y_pred))
```

    1.0


# 5. Improve

This can be done in a few ways: 
* Give more data for trainng data. Con: can't be certain for accuracy of model because not enough testing. 
* Parameters can be changed - creates segments to evaluate
* Have more features/columns/parameters. The more features to look at the more information to look at. 
* Change the algorithm? E.g a Descion Tree classifier


```python
sample = [[3,4,5,2], [2,3,5,4]]
```


```python
predictions = knn.predict(sample)
predict_species = [iris.target_names[p] for p in predictions]
print(f"predictions: , {predict_species}")
```

    predictions: , ['versicolor', 'virginica']



```python
# Model persistence 
from sklearn.externals import joblib 
# dump the model somewhere for later access. 
joblib.dump(knn, 'mlbrain.joblib')
```




    ['mlbrain.joblib']




```python
model = joblib.load('mlbrain.joblib')
model.predict(X_test)
```




    array([2, 0, 2, 1, 1, 2, 0, 1, 0, 1, 1, 2, 1, 1, 1])




```python

```
