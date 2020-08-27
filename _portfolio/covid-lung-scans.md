
---
title: "COVID-19 CT scans"
excerpt: "Using Lung CT scans to create prediction models for indicating the presence of COVID-19 infections<br/><img src='images/pneumonia.png'>"
collection: portfolio
---


# COVID-19 CT scans
> Use of Lung CT scans to create prediction models that indicate the presence of COVID-19 infections

CT scans plays a supportive role in the diagnosis of COVID-19 and is a key procedure for determining the severity that the patient finds himself in.
Models that can find evidence of COVID-19 and/or characterize its findings can play a crucial role in optimizing diagnosis and treatment, especially in areas with a shortage of expert radiologists.
This dataset contains 20 CT scans of patients diagnosed with COVID-19 as well as segmentations of lungs and infections made by experts.


```python
import glob 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
```


```python
# As the raw data files are in the *.nii format we need to import the nibabel 
import nibabel as nib 
```


```python
import os
cwd = os.getcwd()
print(cwd)
```

    /Users/arcadekwaku/A.Code/fast_pages_datascience/_notebooks


Within the dataset provided by kaggle there is a a metadata csv file which provides all of the file paths for sub directories.


```python
raw_df = pd.read_csv('input/covid19-ct-scans/metadata.csv')
```


```python
#The metadata csv file contains all of the file paths for each of the CT images within the dataset provided by kaggle. 
# Loading the data frame head to get an ouline of the data.
raw_df.head()
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
      <th>ct_scan</th>
      <th>lung_mask</th>
      <th>infection_mask</th>
      <th>lung_and_infection_mask</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>../input/covid19-ct-scans/ct_scans/coronacases...</td>
      <td>../input/covid19-ct-scans/lung_mask/coronacase...</td>
      <td>../input/covid19-ct-scans/infection_mask/coron...</td>
      <td>../input/covid19-ct-scans/lung_and_infection_m...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>../input/covid19-ct-scans/ct_scans/coronacases...</td>
      <td>../input/covid19-ct-scans/lung_mask/coronacase...</td>
      <td>../input/covid19-ct-scans/infection_mask/coron...</td>
      <td>../input/covid19-ct-scans/lung_and_infection_m...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>../input/covid19-ct-scans/ct_scans/coronacases...</td>
      <td>../input/covid19-ct-scans/lung_mask/coronacase...</td>
      <td>../input/covid19-ct-scans/infection_mask/coron...</td>
      <td>../input/covid19-ct-scans/lung_and_infection_m...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>../input/covid19-ct-scans/ct_scans/coronacases...</td>
      <td>../input/covid19-ct-scans/lung_mask/coronacase...</td>
      <td>../input/covid19-ct-scans/infection_mask/coron...</td>
      <td>../input/covid19-ct-scans/lung_and_infection_m...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>../input/covid19-ct-scans/ct_scans/coronacases...</td>
      <td>../input/covid19-ct-scans/lung_mask/coronacase...</td>
      <td>../input/covid19-ct-scans/infection_mask/coron...</td>
      <td>../input/covid19-ct-scans/lung_and_infection_m...</td>
    </tr>
  </tbody>
</table>
</div>



First, to ensure we're able to load each image file by reading the file path and using the nibel package to load the data. 


```python
#select the first file path in the first column
first_scan = raw_df['ct_scan'][0]
print(first_scan)
```

    input/covid19-ct-scans/ct_scans/coronacases_org_001.nii



```python
# As all the data has the "../" prefix in the dataframe this cause in an error with loading it.
# Use of a lambda function to strip this from the front of the string
raw_df['ct_scan'] = raw_df['ct_scan'].map(lambda x: x.lstrip('../').rstrip('aAbBcC'))
```


```python
print(first_scan)
```

    input/covid19-ct-scans/ct_scans/coronacases_org_001.nii



```python
ct_scan = nib.load(first_scan)
```


```python
array = ct_scan.get_fdata()
```


```python
# refactor the above code into a function:
def read_nii(filepath):
    '''
    Reads .nii file and returns pixel array
    '''
    ct_scan = nib.load(filepath)
    ct_array   = ct_scan.get_fdata()
    ct_array = ct_array.T
    # Return an image using maplot lib 
    return plt.imshow(ct_array[200])
```


```python
read_nii(first_scan)
```




    <matplotlib.image.AxesImage at 0x7fe8867b9518>




![png](output_15_1.png)



```python

```
