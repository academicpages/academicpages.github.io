```python
import pandas as pd

data = pd.read_csv("clean_weather.csv", index_col=0)
data = data.ffill()

data.head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tmax</th>
      <th>tmin</th>
      <th>rain</th>
      <th>tmax_tomorrow</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1970-01-01</th>
      <td>60.0</td>
      <td>35.0</td>
      <td>0.0</td>
      <td>52.0</td>
    </tr>
    <tr>
      <th>1970-01-02</th>
      <td>52.0</td>
      <td>39.0</td>
      <td>0.0</td>
      <td>52.0</td>
    </tr>
    <tr>
      <th>1970-01-03</th>
      <td>52.0</td>
      <td>35.0</td>
      <td>0.0</td>
      <td>53.0</td>
    </tr>
    <tr>
      <th>1970-01-04</th>
      <td>53.0</td>
      <td>36.0</td>
      <td>0.0</td>
      <td>52.0</td>
    </tr>
    <tr>
      <th>1970-01-05</th>
      <td>52.0</td>
      <td>35.0</td>
      <td>0.0</td>
      <td>50.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.shape[1]
```




    4




```python
data.plot.scatter("tmax", "tmax_tomorrow")
```




    <Axes: xlabel='tmax', ylabel='tmax_tomorrow'>




    
![png](LR_GD_files/LR_GD_2_1.png)
    



```python
import matplotlib.pyplot as plt

data.plot.scatter("tmax", "tmax_tomorrow")
plt.plot([30,120],[30,120], 'red')
```




    [<matplotlib.lines.Line2D at 0x11e287640>]




    
![png](LR_GD_files/LR_GD_3_1.png)
    



```python
data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tmax</th>
      <th>tmin</th>
      <th>rain</th>
      <th>tmax_tomorrow</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1970-01-01</th>
      <td>60.0</td>
      <td>35.0</td>
      <td>0.0</td>
      <td>52.0</td>
    </tr>
    <tr>
      <th>1970-01-02</th>
      <td>52.0</td>
      <td>39.0</td>
      <td>0.0</td>
      <td>52.0</td>
    </tr>
    <tr>
      <th>1970-01-03</th>
      <td>52.0</td>
      <td>35.0</td>
      <td>0.0</td>
      <td>53.0</td>
    </tr>
    <tr>
      <th>1970-01-04</th>
      <td>53.0</td>
      <td>36.0</td>
      <td>0.0</td>
      <td>52.0</td>
    </tr>
    <tr>
      <th>1970-01-05</th>
      <td>52.0</td>
      <td>35.0</td>
      <td>0.0</td>
      <td>50.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2022-11-22</th>
      <td>62.0</td>
      <td>35.0</td>
      <td>0.0</td>
      <td>67.0</td>
    </tr>
    <tr>
      <th>2022-11-23</th>
      <td>67.0</td>
      <td>38.0</td>
      <td>0.0</td>
      <td>66.0</td>
    </tr>
    <tr>
      <th>2022-11-24</th>
      <td>66.0</td>
      <td>41.0</td>
      <td>0.0</td>
      <td>70.0</td>
    </tr>
    <tr>
      <th>2022-11-25</th>
      <td>70.0</td>
      <td>39.0</td>
      <td>0.0</td>
      <td>62.0</td>
    </tr>
    <tr>
      <th>2022-11-26</th>
      <td>62.0</td>
      <td>41.0</td>
      <td>0.0</td>
      <td>64.0</td>
    </tr>
  </tbody>
</table>
<p>13509 rows × 4 columns</p>
</div>




```python
import numpy as np
PREDICTORS = ["tmax", "tmin","rain"]
TARGET = "tmax_tomorrow"

np.random.seed(0)
split_data = np.split(data, [int(.7 * len(data)), int(.85 * len(data))])
(train_x,train_y), (valid_x, valid_y), (test_x, test_y) = [[d[PREDICTORS].to_numpy(), d[[TARGET]].to_numpy()] for d in split_data]

```


```python
import math

def init_params(predictors):
    np.random.seed(0)
    weights = np.random.rand(predictors, 1)
    biases = np.ones((1,1))
    return [weights, biases]
```


```python
init_params(3)
```




    [array([[0.5488135 ],
            [0.71518937],
            [0.60276338]]),
     array([[1.]])]




```python
def forward(params, x):
    weights, biases = params
    prediction = x @ weights + biases
    return prediction
```


```python
def mse(actual, predicted):
    return np.mean((actual-predicted) ** 2)

def mse_grad(actual, predicted):
    return predicted - actual
```


```python
def backward(params, x, lr, grad):
    w_grad = (x.T / x.shape[0]) @ grad
    b_grad = np.mean(grad, axis=0)

    params[0] -= w_grad * lr
    params[1] -= b_grad * lr

    return params
```


```python
lr = 1e-4
epochs = 1000000

params = init_params(train_x.shape[1])

for i in range(epochs):
    predictions = forward(params, train_x)
    grad = mse_grad(train_y, predictions)

    params = backward(params, train_x, lr, grad)

    if i % 100000 == 0:
        predictions = forward(params, valid_x)
        valid_loss = mse(valid_y, predictions)

        print(f"Epoch {i} loss: {valid_loss}")
```

    Epoch 0 loss: 31.564020597420274
    Epoch 100000 loss: 22.334538322879986
    Epoch 200000 loss: 22.091830904025493
    Epoch 300000 loss: 21.90086363406021
    Epoch 400000 loss: 21.7495164452107
    Epoch 500000 loss: 21.628818306812136
    Epoch 600000 loss: 21.532024522869786
    Epoch 700000 loss: 21.454001309402106
    Epoch 800000 loss: 21.39080287641205
    Epoch 900000 loss: 21.339372947459434



```python
params
```




    [array([[ 0.73472903],
            [ 0.20396443],
            [-1.62813009]]),
     array([[7.09116813]])]




```python
print(f"Param 1: {params[0][0]}")
print(f"Param 2: {params[0][1]}")
print(f"Param 3: {params[0][2]}")
print(f"Bias: {params[1][0]}")
```

    Param 1: [0.73472903]
    Param 2: [0.20396443]
    Param 3: [-1.62813009]
    Bias: [7.09116813]



```python
test_y
```




    array([[68.],
           [67.],
           [67.],
           ...,
           [70.],
           [62.],
           [64.]])




```python
new_predictions = forward(params, test_x)
```


```python
new_predictions
```




    array([[66.59736354],
           [68.0668216 ],
           [67.33209257],
           ...,
           [63.94582594],
           [66.47681321],
           [61.00690981]])




```python
from sklearn.metrics import precision_score

new_predictions = new_predictions.round()
```


```python
new_predictions
```




    array([[67.],
           [68.],
           [67.],
           ...,
           [64.],
           [66.],
           [61.]])




```python
from sklearn.metrics import r2_score

r2 = r2_score(test_y, new_predictions)
print("R-squared:", r2)
```

    R-squared: 0.6763452148780562



```python
from sklearn.linear_model import LinearRegression

lr_model = LinearRegression()
```


```python
lr_model.fit(train_x, train_y)
```




<style>#sk-container-id-1 {color: black;}#sk-container-id-1 pre{padding: 0;}#sk-container-id-1 div.sk-toggleable {background-color: white;}#sk-container-id-1 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-1 label.sk-toggleable__label-arrow:before {content: "▸";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-1 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-1 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-1 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: "▾";}#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-1 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-1 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-1 div.sk-parallel-item::after {content: "";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-serial::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-1 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-1 div.sk-item {position: relative;z-index: 1;}#sk-container-id-1 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-1 div.sk-item::before, #sk-container-id-1 div.sk-parallel-item::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-1 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-1 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-1 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-1 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-1 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-1 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-1 div.sk-label-container {text-align: center;}#sk-container-id-1 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-1 div.sk-text-repr-fallback {display: none;}</style><div id="sk-container-id-1" class="sk-top-container"><div class="sk-text-repr-fallback"><pre>LinearRegression()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class="sk-container" hidden><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-1" type="checkbox" checked><label for="sk-estimator-id-1" class="sk-toggleable__label sk-toggleable__label-arrow">LinearRegression</label><div class="sk-toggleable__content"><pre>LinearRegression()</pre></div></div></div></div></div>




```python
lr_model.intercept_
```




    array([9.53979018])




```python
lr_model.coef_
```




    array([[ 0.71161936,  0.18644815, -2.18382429]])




```python

```
