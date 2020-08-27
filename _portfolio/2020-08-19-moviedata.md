---
title: "Analysing movie data"
excerpt: "Analyzing data associated with information from 10,000 movies collected from the Movie Database (TMDb<br/><img src='/images/.png'>"
collection: portfolio
---



# Project: TMDb Movie Data Analysis

## Table of Contents
<ul>
<li><a>Introduction</a></li>
<li><a>Data Wrangling</a></li>
<li><a>Exploratory Data Analysis</a></li>
<li><a>Conclusions</a></li>
</ul>

<a></a>
## Introduction

In this project I'll be analyzing data associated with information from 10,000 movies collected from the Movie Database (TMDb).In particular this anaysis is focused on distinguishing movies that are popular from year to year, and the genre of movies that incure high revenues. To start first the  necessary packages need to be imported in order to analyze this data set. 

The questions I will be trying to answer are the following:
1. What is the average profit earned for each movie?
2. Which movie earned the most profit?
3. Which movie earned the least profit?
4. What was the average budget for each movie?
5. Which movie had the lowest budget?
6. Which movie had the highest budget?
7. What was the average run time for all the movies?
8. Which movie had the longest run time?
9. Which movie had the shortest run time?
10. Which movie had the highest rating (with respect to average vote count)?
11. Which movie had the lowest ratiing (with respect to average vote count)?

## Data acquisition is an important step in any data analysis process. 
In this case the data was provided courtsey of Udacity via a cleaned Kaggle database. 
The data was aquired by downloading a CSV file and put in the same directory as this notebook.
The csv file can be read with pandas read_csv function as shown below. 
The first step in the Data analysis process is to import pandas, matplob lib and any other helpful packages.


```python
import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 
%matplotlib inline

```

In order to give quick access to the csv file associated with the datafrane, it is possible to download it using the kernel without having to commit it. This is shown blow, with the download link in Out[8]:


```python
# import the modules we'll need
from IPython.display import HTML
import base64

# function that takes in a dataframe and creates a text link to  
# download it (will only work for files < 2MB or so)
def create_download_link(df, title = "Download CSV file", filename = "tmdb-movies.csv"):  
    csv = df.to_csv()
    b64 = base64.b64encode(csv.encode())
    payload = b64.decode()
    html = '<a download="{filename}" href="data:text/csv;base64,{payload}" target="_blank">{title}</a>'
    html = html.format(payload=payload,title=title,filename=filename)
    return HTML(html)

# create a random sample dataframe
df = pd.DataFrame(np.random.randn(50, 4), columns=list('ABCD'))

# create a link to download the dataframe
create_download_link(df)

```




<a>Download CSV file</a>



<a></a>
# Data Wrangling

In this section of the report we will load the data in order to better inspect and understand the information presented. The dataset will also be checked for cleanliness, and then trimmed and cleaned for analysis. Only relevant data will be kept, usefull for any calculations. 
### General Properties


```python
df = pd.read_csv('tmdb-movies.csv')
```


```python
#once the data has been importanted, to quickly test to see whether there is the correct information in the dataset
#the df.head() function is useful. This generates the first n rows for the dataset (n=5 usually).
#df.head() also gives us a summary of how many columns are in the dataframe - 21. 
df.head()
```




<div>
<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>imdb_id</th>
      <th>popularity</th>
      <th>budget</th>
      <th>revenue</th>
      <th>original_title</th>
      <th>cast</th>
      <th>homepage</th>
      <th>director</th>
      <th>tagline</th>
      <th>...</th>
      <th>overview</th>
      <th>runtime</th>
      <th>genres</th>
      <th>production_companies</th>
      <th>release_date</th>
      <th>vote_count</th>
      <th>vote_average</th>
      <th>release_year</th>
      <th>budget_adj</th>
      <th>revenue_adj</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>135397</td>
      <td>tt0369610</td>
      <td>32.985763</td>
      <td>150000000</td>
      <td>1513528810</td>
      <td>Jurassic World</td>
      <td>Chris Pratt|Bryce Dallas Howard|Irrfan Khan|Vi...</td>
      <td>http://www.jurassicworld.com/</td>
      <td>Colin Trevorrow</td>
      <td>The park is open.</td>
      <td>...</td>
      <td>Twenty-two years after the events of Jurassic ...</td>
      <td>124</td>
      <td>Action|Adventure|Science Fiction|Thriller</td>
      <td>Universal Studios|Amblin Entertainment|Legenda...</td>
      <td>6/9/15</td>
      <td>5562</td>
      <td>6.5</td>
      <td>2015</td>
      <td>1.379999e+08</td>
      <td>1.392446e+09</td>
    </tr>
    <tr>
      <th>1</th>
      <td>76341</td>
      <td>tt1392190</td>
      <td>28.419936</td>
      <td>150000000</td>
      <td>378436354</td>
      <td>Mad Max: Fury Road</td>
      <td>Tom Hardy|Charlize Theron|Hugh Keays-Byrne|Nic...</td>
      <td>http://www.madmaxmovie.com/</td>
      <td>George Miller</td>
      <td>What a Lovely Day.</td>
      <td>...</td>
      <td>An apocalyptic story set in the furthest reach...</td>
      <td>120</td>
      <td>Action|Adventure|Science Fiction|Thriller</td>
      <td>Village Roadshow Pictures|Kennedy Miller Produ...</td>
      <td>5/13/15</td>
      <td>6185</td>
      <td>7.1</td>
      <td>2015</td>
      <td>1.379999e+08</td>
      <td>3.481613e+08</td>
    </tr>
    <tr>
      <th>2</th>
      <td>262500</td>
      <td>tt2908446</td>
      <td>13.112507</td>
      <td>110000000</td>
      <td>295238201</td>
      <td>Insurgent</td>
      <td>Shailene Woodley|Theo James|Kate Winslet|Ansel...</td>
      <td>http://www.thedivergentseries.movie/#insurgent</td>
      <td>Robert Schwentke</td>
      <td>One Choice Can Destroy You</td>
      <td>...</td>
      <td>Beatrice Prior must confront her inner demons ...</td>
      <td>119</td>
      <td>Adventure|Science Fiction|Thriller</td>
      <td>Summit Entertainment|Mandeville Films|Red Wago...</td>
      <td>3/18/15</td>
      <td>2480</td>
      <td>6.3</td>
      <td>2015</td>
      <td>1.012000e+08</td>
      <td>2.716190e+08</td>
    </tr>
    <tr>
      <th>3</th>
      <td>140607</td>
      <td>tt2488496</td>
      <td>11.173104</td>
      <td>200000000</td>
      <td>2068178225</td>
      <td>Star Wars: The Force Awakens</td>
      <td>Harrison Ford|Mark Hamill|Carrie Fisher|Adam D...</td>
      <td>http://www.starwars.com/films/star-wars-episod...</td>
      <td>J.J. Abrams</td>
      <td>Every generation has a story.</td>
      <td>...</td>
      <td>Thirty years after defeating the Galactic Empi...</td>
      <td>136</td>
      <td>Action|Adventure|Science Fiction|Fantasy</td>
      <td>Lucasfilm|Truenorth Productions|Bad Robot</td>
      <td>12/15/15</td>
      <td>5292</td>
      <td>7.5</td>
      <td>2015</td>
      <td>1.839999e+08</td>
      <td>1.902723e+09</td>
    </tr>
    <tr>
      <th>4</th>
      <td>168259</td>
      <td>tt2820852</td>
      <td>9.335014</td>
      <td>190000000</td>
      <td>1506249360</td>
      <td>Furious 7</td>
      <td>Vin Diesel|Paul Walker|Jason Statham|Michelle ...</td>
      <td>http://www.furious7.com/</td>
      <td>James Wan</td>
      <td>Vengeance Hits Home</td>
      <td>...</td>
      <td>Deckard Shaw seeks revenge against Dominic Tor...</td>
      <td>137</td>
      <td>Action|Crime|Thriller</td>
      <td>Universal Pictures|Original Film|Media Rights ...</td>
      <td>4/1/15</td>
      <td>2947</td>
      <td>7.3</td>
      <td>2015</td>
      <td>1.747999e+08</td>
      <td>1.385749e+09</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 21 columns</p>
</div>



Observations:
1. There are 21 columns in the data frame. 
2. From the information presented above, we can see that there are no units given to any values across the 21 columns. 
In order to make the budget and revenue tangible, I will use american currency of dollars, as the imbd dataset is predominantly hollywood production. 


```python
#The function df.shape returns the number of rows and columns in the dataset.
df.shape
```




    (10866, 21)




```python
#The function below returns descriptive statistics useful for indicating hat summarize the central tendency, 
#dispersion and shape of a dataset’s distribution, excluding NaN values.
df.describe()
```




<div>
<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>popularity</th>
      <th>budget</th>
      <th>revenue</th>
      <th>runtime</th>
      <th>vote_count</th>
      <th>vote_average</th>
      <th>release_year</th>
      <th>budget_adj</th>
      <th>revenue_adj</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>10866.000000</td>
      <td>10866.000000</td>
      <td>1.086600e+04</td>
      <td>1.086600e+04</td>
      <td>10866.000000</td>
      <td>10866.000000</td>
      <td>10866.000000</td>
      <td>10866.000000</td>
      <td>1.086600e+04</td>
      <td>1.086600e+04</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>66064.177434</td>
      <td>0.646441</td>
      <td>1.462570e+07</td>
      <td>3.982332e+07</td>
      <td>102.070863</td>
      <td>217.389748</td>
      <td>5.974922</td>
      <td>2001.322658</td>
      <td>1.755104e+07</td>
      <td>5.136436e+07</td>
    </tr>
    <tr>
      <th>std</th>
      <td>92130.136561</td>
      <td>1.000185</td>
      <td>3.091321e+07</td>
      <td>1.170035e+08</td>
      <td>31.381405</td>
      <td>575.619058</td>
      <td>0.935142</td>
      <td>12.812941</td>
      <td>3.430616e+07</td>
      <td>1.446325e+08</td>
    </tr>
    <tr>
      <th>min</th>
      <td>5.000000</td>
      <td>0.000065</td>
      <td>0.000000e+00</td>
      <td>0.000000e+00</td>
      <td>0.000000</td>
      <td>10.000000</td>
      <td>1.500000</td>
      <td>1960.000000</td>
      <td>0.000000e+00</td>
      <td>0.000000e+00</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>10596.250000</td>
      <td>0.207583</td>
      <td>0.000000e+00</td>
      <td>0.000000e+00</td>
      <td>90.000000</td>
      <td>17.000000</td>
      <td>5.400000</td>
      <td>1995.000000</td>
      <td>0.000000e+00</td>
      <td>0.000000e+00</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>20669.000000</td>
      <td>0.383856</td>
      <td>0.000000e+00</td>
      <td>0.000000e+00</td>
      <td>99.000000</td>
      <td>38.000000</td>
      <td>6.000000</td>
      <td>2006.000000</td>
      <td>0.000000e+00</td>
      <td>0.000000e+00</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>75610.000000</td>
      <td>0.713817</td>
      <td>1.500000e+07</td>
      <td>2.400000e+07</td>
      <td>111.000000</td>
      <td>145.750000</td>
      <td>6.600000</td>
      <td>2011.000000</td>
      <td>2.085325e+07</td>
      <td>3.369710e+07</td>
    </tr>
    <tr>
      <th>max</th>
      <td>417859.000000</td>
      <td>32.985763</td>
      <td>4.250000e+08</td>
      <td>2.781506e+09</td>
      <td>900.000000</td>
      <td>9767.000000</td>
      <td>9.200000</td>
      <td>2015.000000</td>
      <td>4.250000e+08</td>
      <td>2.827124e+09</td>
    </tr>
  </tbody>
</table>
</div>



## Data Cleaning 

After gathering and assessing the general properties of the data the second and crucially important step is to clean the dataset. In order to make and further investigations easier. Accuracy is important and can be affected by issues such as missing data, duplicates, or structural problems.

#### Important observations and clearning processes
1.  Missing data: Identify and remove any catagorical values while imputing  numerical data with the mean where possible. 
2. Cleaning: removing any irrelevant information in analysing our data (certain unused/unclear colunns) 
3. Duplicates: Identifying and removing any duplicated data.
4. Drop Nulls: Identifing movies with values of 0 for the budget and/ore revenue, and removing them.
5. Incorrect data types a: changing the release date column into date format. 
6. Incorrect data type b: Changining the format of budget and revenue column. 


##  1. Missing data: removing missing/irrelevant data


```python
#The function below is helpful for exploratory analysis of the data. As we can see from the output, 
#the summary includes list of all columns with their data types and the number of non-null values in each column. 
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 10866 entries, 0 to 10865
    Data columns (total 21 columns):
    id                      10866 non-null int64
    imdb_id                 10856 non-null object
    popularity              10866 non-null float64
    budget                  10866 non-null int64
    revenue                 10866 non-null int64
    original_title          10866 non-null object
    cast                    10790 non-null object
    homepage                2936 non-null object
    director                10822 non-null object
    tagline                 8042 non-null object
    keywords                9373 non-null object
    overview                10862 non-null object
    runtime                 10866 non-null int64
    genres                  10843 non-null object
    production_companies    9836 non-null object
    release_date            10866 non-null object
    vote_count              10866 non-null int64
    vote_average            10866 non-null float64
    release_year            10866 non-null int64
    budget_adj              10866 non-null float64
    revenue_adj             10866 non-null float64
    dtypes: float64(4), int64(6), object(11)
    memory usage: 1.7+ MB


Using Numpy and Pandas to provide insight into the data, the key attributes from this data frame are as follows: 
* There are records 10,866 different films.
*


```python
#df.info also shows which columns haeve missing data. Simply by observing where the number of entries for each column,
#is mistatched with the value for total entries. 
```

From the data above we can see that there are 10,866 total entries of data and 21 coulmns in the csv file. From the information it is apparent that there is missing data. The features with missing data, in order of apperance, are as follows:
* Cast - 10790 
* Homepage - 2936
* Director - 10822
* Tagline - 8042
* Keywords - 9372
* overview - 10862
* genres - 10843
* Production_companies - 9836

Usually to solve the problem of missing data is solved by imputing the mean using the fill.na function in pandas. However, the variables with missing data are not numerical but catagorical. 
One way to  solve this problem is by removing Unused or irrelevant columns. Columns that need to be deleted are - id, imdb_id, popularity, budget_adj, revenue_adj, homepage, cast, director, keywords, tagline, overview, production_companies, vote_count, vote_average.
 

## 2. Cleaning: removing any irrelevant information in analysing our data (certain unused/unclear colunns) 


```python
#creating a list of columns for deleting
del_col=[ 'imdb_id', 'popularity', 'budget_adj', 'revenue_adj', 'homepage', 'cast', 'director', 'keywords', 'tagline', 'overview', 'production_companies', 'vote_count', 'vote_average']

#deleting the columns
df = df.drop(del_col,1)

#previewing the new dataset
df.head(4)
```




<div>
<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>budget</th>
      <th>revenue</th>
      <th>original_title</th>
      <th>runtime</th>
      <th>genres</th>
      <th>release_date</th>
      <th>release_year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>135397</td>
      <td>150000000</td>
      <td>1513528810</td>
      <td>Jurassic World</td>
      <td>124</td>
      <td>Action|Adventure|Science Fiction|Thriller</td>
      <td>6/9/15</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>1</th>
      <td>76341</td>
      <td>150000000</td>
      <td>378436354</td>
      <td>Mad Max: Fury Road</td>
      <td>120</td>
      <td>Action|Adventure|Science Fiction|Thriller</td>
      <td>5/13/15</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>2</th>
      <td>262500</td>
      <td>110000000</td>
      <td>295238201</td>
      <td>Insurgent</td>
      <td>119</td>
      <td>Adventure|Science Fiction|Thriller</td>
      <td>3/18/15</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>3</th>
      <td>140607</td>
      <td>200000000</td>
      <td>2068178225</td>
      <td>Star Wars: The Force Awakens</td>
      <td>136</td>
      <td>Action|Adventure|Science Fiction|Fantasy</td>
      <td>12/15/15</td>
      <td>2015</td>
    </tr>
  </tbody>
</table>
</div>



So now we can see all irrelevant columns, or columns with missing data have been removed from the data frame.

## 3. Duplicates: identifying and removing duplicated data. 
The second issue is duplicated data. This dataset is too large to find any duplicates visually. To find any duplicate rows the function df.duplicated() is useful.


```python
#To return duplicated data:
df.duplicated()
```




    0        False
    1        False
    2        False
    3        False
    4        False
    5        False
    6        False
    7        False
    8        False
    9        False
    10       False
    11       False
    12       False
    13       False
    14       False
    15       False
    16       False
    17       False
    18       False
    19       False
    20       False
    21       False
    22       False
    23       False
    24       False
    25       False
    26       False
    27       False
    28       False
    29       False
             ...  
    10836    False
    10837    False
    10838    False
    10839    False
    10840    False
    10841    False
    10842    False
    10843    False
    10844    False
    10845    False
    10846    False
    10847    False
    10848    False
    10849    False
    10850    False
    10851    False
    10852    False
    10853    False
    10854    False
    10855    False
    10856    False
    10857    False
    10858    False
    10859    False
    10860    False
    10861    False
    10862    False
    10863    False
    10864    False
    10865    False
    dtype: bool




```python
#By defult this pandas function marks any duplicates as true. We can keep any 'false' statements. 
#The function below returns any duplicated data.
df[df.duplicated(keep=False)]
```




<div>
<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>budget</th>
      <th>revenue</th>
      <th>original_title</th>
      <th>runtime</th>
      <th>genres</th>
      <th>release_date</th>
      <th>release_year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2089</th>
      <td>42194</td>
      <td>30000000</td>
      <td>967000</td>
      <td>TEKKEN</td>
      <td>92</td>
      <td>Crime|Drama|Action|Thriller|Science Fiction</td>
      <td>3/20/10</td>
      <td>2010</td>
    </tr>
    <tr>
      <th>2090</th>
      <td>42194</td>
      <td>30000000</td>
      <td>967000</td>
      <td>TEKKEN</td>
      <td>92</td>
      <td>Crime|Drama|Action|Thriller|Science Fiction</td>
      <td>3/20/10</td>
      <td>2010</td>
    </tr>
  </tbody>
</table>
</div>



#### The code executed above returned duplicate data in rows 2089 and 2090


```python
rows, col = df.shape
#we need to reduce the row count by one. 
print('There are {} total movie entries and {} no.of colums in it'.format(rows -1, col))
```

    There are 10865 total movie entries and 8 no.of colums in it


#In order to fix this problem the drop duplicates function in pandas is ideal.
[df.drop_duplicates(inplace=True)]


```python
df.drop_duplicates(keep ='first', inplace=True)
rows, col = df.shape
```


```python
#Use the df duplicated function to check if duplicates have been dropped. 
df[df.duplicated(keep=False)]
```




<div>
<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>budget</th>
      <th>revenue</th>
      <th>original_title</th>
      <th>runtime</th>
      <th>genres</th>
      <th>release_date</th>
      <th>release_year</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
</div>



No duplicate rows were returned, so this is proof that the previously duplicated data was removed. 


```python

rows, col = df.shape 
print('There are now {} total movie entries and {} no.of columns in it.'.format(rows-1, col))
```

    There are now 10864 total movie entries and 8 no.of columns in it.


## 4. Drop null: identifing movies with values of 0 for the budget and/ore revenue,  and removing them. 


```python
# creating a seperate list of revenue and budget column
temp_list=['budget', 'revenue']

#this will replace all the value from '0' to NAN in the list
df[temp_list] = df[temp_list].replace(0, np.NAN)

#Removing all the row which has NaN value in temp_list 
df.dropna(subset = temp_list, inplace = True)

rows, col = df.shape
print('So after removing such entries, we now have only {} no.of movies.'.format(rows-1))
```

    So after removing such entries, we now have only 3853 no.of movies.


## 5. Incorrect data types a:  changing the release date column into date format.



```python
df.info ()
```

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 3854 entries, 0 to 10848
    Data columns (total 8 columns):
    id                3854 non-null int64
    budget            3854 non-null float64
    revenue           3854 non-null float64
    original_title    3854 non-null object
    runtime           3854 non-null int64
    genres            3854 non-null object
    release_date      3854 non-null object
    release_year      3854 non-null int64
    dtypes: float64(2), int64(3), object(3)
    memory usage: 271.0+ KB


We can see that release_date is represetned as an object (string) when ideally it sould be represented as a date-time object. Whilst this isn't a big issue, date-time is more convienient work with for filtering or extracting specific information. We can use the to_datetime function to convert the column. 


```python
df.release_date = pd.to_datetime(df['release_date'])
```


```python
#We can now print the changed data frame to check whether this change worked.
df.info ()
```

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 3854 entries, 0 to 10848
    Data columns (total 8 columns):
    id                3854 non-null int64
    budget            3854 non-null float64
    revenue           3854 non-null float64
    original_title    3854 non-null object
    runtime           3854 non-null int64
    genres            3854 non-null object
    release_date      3854 non-null datetime64[ns]
    release_year      3854 non-null int64
    dtypes: datetime64[ns](1), float64(2), int64(3), object(2)
    memory usage: 271.0+ KB


Now we can see that the timestamp is represented as a datetime. 

## 6. Incorrect data type b: Changining the format of budget and revenue column.

We can see a similar issue for the budget and revenue folumns. They are represented as a float instead of integers.  


```python
#print the data type of the current data frame. 
df.dtypes
```




    id                         int64
    budget                   float64
    revenue                  float64
    original_title            object
    runtime                    int64
    genres                    object
    release_date      datetime64[ns]
    release_year               int64
    dtype: object




```python
change_type=['budget', 'revenue']
df[change_type]=df[change_type].applymap(np.int64)
```


```python
#we can now print the data types again to check if the information has changed. 
df.dtypes
```




    id                         int64
    budget                     int64
    revenue                    int64
    original_title            object
    runtime                    int64
    genres                    object
    release_date      datetime64[ns]
    release_year               int64
    dtype: object



The data type for budget and revenue has now been changed to intgers. 

<a></a>
# Exploratory Data Analysis

&gt; Now that the data has been trimmed and cleaned, the next step is exploration. In this section I will compute statistics and create visualizations with the goal of addressing the research questions posed in the Introduction section. I will look at each variable independently and then follow up by looking at any correlations/relationships between variables. 



### Research Question 1: Which movies had the lowest and highest budget?


```python
import pprint
#defining the function
def calculate(column):
    #for highest earned profit
    high= df[column].idxmax()
    high_details=pd.DataFrame(df.loc[high])
    
    #for lowest earned profit
    low= df[column].idxmin()
    low_details=pd.DataFrame(df.loc[low])
    
    #collectin data in one place
    info=pd.concat([high_details, low_details], axis=1)
    
    return info

calculate('budget')
```




<div>
<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>2244</th>
      <th>2618</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>id</th>
      <td>46528</td>
      <td>39964</td>
    </tr>
    <tr>
      <th>budget</th>
      <td>425000000</td>
      <td>1</td>
    </tr>
    <tr>
      <th>profit_earned</th>
      <td>-413912431</td>
      <td>99</td>
    </tr>
    <tr>
      <th>revenue</th>
      <td>11087569</td>
      <td>100</td>
    </tr>
    <tr>
      <th>original_title</th>
      <td>The Warrior's Way</td>
      <td>Lost &amp; Found</td>
    </tr>
    <tr>
      <th>runtime</th>
      <td>100</td>
      <td>95</td>
    </tr>
    <tr>
      <th>genres</th>
      <td>Adventure|Fantasy|Action|Western|Thriller</td>
      <td>Comedy|Romance</td>
    </tr>
    <tr>
      <th>release_date</th>
      <td>2010-12-02 00:00:00</td>
      <td>1999-04-23 00:00:00</td>
    </tr>
    <tr>
      <th>release_year</th>
      <td>2010</td>
      <td>1999</td>
    </tr>
  </tbody>
</table>
</div>



The film with the highest budget was 'The Warrior's Way' and ironically, this film also had the lowest profit as mentioned earlier. The film with the highest budge of only $1 was 'Lost &amp; Found' released in 1999.

### Research Question 2: How do we calcuate the profit for each movie?

As there is no column that presents profit in this data set from the original csv file, in order to calulate profit, the budget of each movie must be subtracted from the revenue and allocated to a new column. 

To create a new column, it must be indexed and to look at the current index (row labels) we can use the DataFrame.index function.


```python
df.index
```




    Int64Index([    0,     1,     2,     3,     4,     5,     6,     7,     8,
                    9,
                ...
                10779, 10780, 10788, 10791, 10793, 10822, 10828, 10829, 10835,
                10848],
               dtype='int64', length=3854)




```python
#look at the original dataframe to choose, where best to put the new column.
df.head()
```




<div>
<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>budget</th>
      <th>revenue</th>
      <th>original_title</th>
      <th>runtime</th>
      <th>genres</th>
      <th>release_date</th>
      <th>release_year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>135397</td>
      <td>150000000</td>
      <td>1513528810</td>
      <td>Jurassic World</td>
      <td>124</td>
      <td>Action|Adventure|Science Fiction|Thriller</td>
      <td>2015-06-09</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>1</th>
      <td>76341</td>
      <td>150000000</td>
      <td>378436354</td>
      <td>Mad Max: Fury Road</td>
      <td>120</td>
      <td>Action|Adventure|Science Fiction|Thriller</td>
      <td>2015-05-13</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>2</th>
      <td>262500</td>
      <td>110000000</td>
      <td>295238201</td>
      <td>Insurgent</td>
      <td>119</td>
      <td>Adventure|Science Fiction|Thriller</td>
      <td>2015-03-18</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>3</th>
      <td>140607</td>
      <td>200000000</td>
      <td>2068178225</td>
      <td>Star Wars: The Force Awakens</td>
      <td>136</td>
      <td>Action|Adventure|Science Fiction|Fantasy</td>
      <td>2015-12-15</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>4</th>
      <td>168259</td>
      <td>190000000</td>
      <td>1506249360</td>
      <td>Furious 7</td>
      <td>137</td>
      <td>Action|Crime|Thriller</td>
      <td>2015-04-01</td>
      <td>2015</td>
    </tr>
  </tbody>
</table>
</div>




```python
#The most appropriate place would be after index 2 - revenue
```


```python
#insert function with three prameters (index of the column in the dataset, name of the colum, value to be inserted)
df.insert(2,'profit_earned',df['revenue']-df['budget'])

#Check for changes in the data frame
df.head()
```




<div>
<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>budget</th>
      <th>profit_earned</th>
      <th>revenue</th>
      <th>original_title</th>
      <th>runtime</th>
      <th>genres</th>
      <th>release_date</th>
      <th>release_year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>135397</td>
      <td>150000000</td>
      <td>1363528810</td>
      <td>1513528810</td>
      <td>Jurassic World</td>
      <td>124</td>
      <td>Action|Adventure|Science Fiction|Thriller</td>
      <td>2015-06-09</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>1</th>
      <td>76341</td>
      <td>150000000</td>
      <td>228436354</td>
      <td>378436354</td>
      <td>Mad Max: Fury Road</td>
      <td>120</td>
      <td>Action|Adventure|Science Fiction|Thriller</td>
      <td>2015-05-13</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>2</th>
      <td>262500</td>
      <td>110000000</td>
      <td>185238201</td>
      <td>295238201</td>
      <td>Insurgent</td>
      <td>119</td>
      <td>Adventure|Science Fiction|Thriller</td>
      <td>2015-03-18</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>3</th>
      <td>140607</td>
      <td>200000000</td>
      <td>1868178225</td>
      <td>2068178225</td>
      <td>Star Wars: The Force Awakens</td>
      <td>136</td>
      <td>Action|Adventure|Science Fiction|Fantasy</td>
      <td>2015-12-15</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>4</th>
      <td>168259</td>
      <td>190000000</td>
      <td>1316249360</td>
      <td>1506249360</td>
      <td>Furious 7</td>
      <td>137</td>
      <td>Action|Crime|Thriller</td>
      <td>2015-04-01</td>
      <td>2015</td>
    </tr>
  </tbody>
</table>
</div>



Now there is a column that shows the profit earned for each individual film. 

### Research Question 3: What is the average profit earned for each movie?


```python
#Here is how to calculate the mean of each df column. 
df.mean()
```




    id               3.988819e+04
    budget           3.720370e+07
    profit_earned    7.048292e+07
    revenue          1.076866e+08
    runtime          1.092203e+02
    release_year     2.001261e+03
    dtype: float64



I wanted to find out the available methods for analysis of data for the data frame. The dir function is useful for this. 


```python
dir(pd.DataFrame)
```




    ['T',
     '_AXIS_ALIASES',
     '_AXIS_IALIASES',
     '_AXIS_LEN',
     '_AXIS_NAMES',
     '_AXIS_NUMBERS',
     '_AXIS_ORDERS',
     '_AXIS_REVERSED',
     '_AXIS_SLICEMAP',
     '__abs__',
     '__add__',
     '__and__',
     '__array__',
     '__array_wrap__',
     '__bool__',
     '__bytes__',
     '__class__',
     '__contains__',
     '__delattr__',
     '__delitem__',
     '__dict__',
     '__dir__',
     '__div__',
     '__doc__',
     '__eq__',
     '__finalize__',
     '__floordiv__',
     '__format__',
     '__ge__',
     '__getattr__',
     '__getattribute__',
     '__getitem__',
     '__getstate__',
     '__gt__',
     '__hash__',
     '__iadd__',
     '__imul__',
     '__init__',
     '__invert__',
     '__ipow__',
     '__isub__',
     '__iter__',
     '__itruediv__',
     '__le__',
     '__len__',
     '__lt__',
     '__mod__',
     '__module__',
     '__mul__',
     '__ne__',
     '__neg__',
     '__new__',
     '__nonzero__',
     '__or__',
     '__pow__',
     '__radd__',
     '__rand__',
     '__rdiv__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__rfloordiv__',
     '__rmod__',
     '__rmul__',
     '__ror__',
     '__round__',
     '__rpow__',
     '__rsub__',
     '__rtruediv__',
     '__rxor__',
     '__setattr__',
     '__setitem__',
     '__setstate__',
     '__sizeof__',
     '__str__',
     '__sub__',
     '__subclasshook__',
     '__truediv__',
     '__unicode__',
     '__weakref__',
     '__xor__',
     '_accessors',
     '_add_numeric_operations',
     '_add_series_only_operations',
     '_add_series_or_dataframe_operations',
     '_agg_by_level',
     '_align_frame',
     '_align_series',
     '_apply_broadcast',
     '_apply_empty_result',
     '_apply_raw',
     '_apply_standard',
     '_at',
     '_box_col_values',
     '_box_item_values',
     '_check_inplace_setting',
     '_check_is_chained_assignment_possible',
     '_check_percentile',
     '_check_setitem_copy',
     '_clear_item_cache',
     '_combine_const',
     '_combine_frame',
     '_combine_match_columns',
     '_combine_match_index',
     '_combine_series',
     '_combine_series_infer',
     '_compare_frame',
     '_compare_frame_evaluate',
     '_consolidate_inplace',
     '_construct_axes_dict',
     '_construct_axes_dict_for_slice',
     '_construct_axes_dict_from',
     '_construct_axes_from_arguments',
     '_constructor',
     '_constructor_expanddim',
     '_constructor_sliced',
     '_convert',
     '_count_level',
     '_create_indexer',
     '_dir_additions',
     '_dir_deletions',
     '_ensure_valid_index',
     '_expand_axes',
     '_flex_compare_frame',
     '_from_arrays',
     '_from_axes',
     '_get_agg_axis',
     '_get_axis',
     '_get_axis_name',
     '_get_axis_number',
     '_get_axis_resolvers',
     '_get_block_manager_axis',
     '_get_bool_data',
     '_get_cacher',
     '_get_index_resolvers',
     '_get_item_cache',
     '_get_numeric_data',
     '_get_values',
     '_getitem_array',
     '_getitem_column',
     '_getitem_frame',
     '_getitem_multilevel',
     '_getitem_slice',
     '_iat',
     '_iget_item_cache',
     '_iloc',
     '_indexed_same',
     '_info_axis',
     '_info_axis_name',
     '_info_axis_number',
     '_info_repr',
     '_init_dict',
     '_init_mgr',
     '_init_ndarray',
     '_internal_names',
     '_internal_names_set',
     '_is_cached',
     '_is_datelike_mixed_type',
     '_is_mixed_type',
     '_is_numeric_mixed_type',
     '_is_view',
     '_ix',
     '_ixs',
     '_join_compat',
     '_loc',
     '_maybe_cache_changed',
     '_maybe_update_cacher',
     '_metadata',
     '_needs_reindex_multi',
     '_protect_consolidate',
     '_reduce',
     '_reindex_axes',
     '_reindex_axis',
     '_reindex_columns',
     '_reindex_index',
     '_reindex_multi',
     '_reindex_with_indexers',
     '_repr_fits_horizontal_',
     '_repr_fits_vertical_',
     '_repr_html_',
     '_repr_latex_',
     '_reset_cache',
     '_reset_cacher',
     '_sanitize_column',
     '_series',
     '_set_as_cached',
     '_set_axis',
     '_set_axis_name',
     '_set_is_copy',
     '_set_item',
     '_setitem_array',
     '_setitem_frame',
     '_setitem_slice',
     '_setup_axes',
     '_slice',
     '_stat_axis',
     '_stat_axis_name',
     '_stat_axis_number',
     '_typ',
     '_unpickle_frame_compat',
     '_unpickle_matrix_compat',
     '_update_inplace',
     '_validate_dtype',
     '_values',
     '_where',
     '_xs',
     'abs',
     'add',
     'add_prefix',
     'add_suffix',
     'align',
     'all',
     'any',
     'append',
     'apply',
     'applymap',
     'as_blocks',
     'as_matrix',
     'asfreq',
     'asof',
     'assign',
     'astype',
     'at',
     'at_time',
     'axes',
     'between_time',
     'bfill',
     'blocks',
     'bool',
     'boxplot',
     'clip',
     'clip_lower',
     'clip_upper',
     'columns',
     'combine',
     'combineAdd',
     'combineMult',
     'combine_first',
     'compound',
     'consolidate',
     'convert_objects',
     'copy',
     'corr',
     'corrwith',
     'count',
     'cov',
     'cummax',
     'cummin',
     'cumprod',
     'cumsum',
     'describe',
     'diff',
     'div',
     'divide',
     'dot',
     'drop',
     'drop_duplicates',
     'dropna',
     'dtypes',
     'duplicated',
     'empty',
     'eq',
     'equals',
     'eval',
     'ewm',
     'expanding',
     'ffill',
     'fillna',
     'filter',
     'first',
     'first_valid_index',
     'floordiv',
     'from_csv',
     'from_dict',
     'from_items',
     'from_records',
     'ftypes',
     'ge',
     'get',
     'get_dtype_counts',
     'get_ftype_counts',
     'get_value',
     'get_values',
     'groupby',
     'gt',
     'head',
     'hist',
     'iat',
     'icol',
     'idxmax',
     'idxmin',
     'iget_value',
     'iloc',
     'index',
     'info',
     'insert',
     'interpolate',
     'irow',
     'is_copy',
     'isin',
     'isnull',
     'items',
     'iteritems',
     'iterkv',
     'iterrows',
     'itertuples',
     'ix',
     'join',
     'keys',
     'kurt',
     'kurtosis',
     'last',
     'last_valid_index',
     'le',
     'loc',
     'lookup',
     'lt',
     'mad',
     'mask',
     'max',
     'mean',
     'median',
     'memory_usage',
     'merge',
     'min',
     'mod',
     'mode',
     'mul',
     'multiply',
     'ndim',
     'ne',
     'nlargest',
     'notnull',
     'nsmallest',
     'pct_change',
     'pipe',
     'pivot',
     'pivot_table',
     'plot',
     'pop',
     'pow',
     'prod',
     'product',
     'quantile',
     'query',
     'radd',
     'rank',
     'rdiv',
     'reindex',
     'reindex_axis',
     'reindex_like',
     'rename',
     'rename_axis',
     'reorder_levels',
     'replace',
     'resample',
     'reset_index',
     'rfloordiv',
     'rmod',
     'rmul',
     'rolling',
     'round',
     'rpow',
     'rsub',
     'rtruediv',
     'sample',
     'select',
     'select_dtypes',
     'sem',
     'set_axis',
     'set_index',
     'set_value',
     'shape',
     'shift',
     'size',
     'skew',
     'slice_shift',
     'sort',
     'sort_index',
     'sort_values',
     'sortlevel',
     'squeeze',
     'stack',
     'std',
     'style',
     'sub',
     'subtract',
     'sum',
     'swapaxes',
     'swaplevel',
     'tail',
     'take',
     'to_clipboard',
     'to_csv',
     'to_dense',
     'to_dict',
     'to_excel',
     'to_gbq',
     'to_hdf',
     'to_html',
     'to_json',
     'to_latex',
     'to_msgpack',
     'to_panel',
     'to_period',
     'to_pickle',
     'to_records',
     'to_sparse',
     'to_sql',
     'to_stata',
     'to_string',
     'to_timestamp',
     'to_xarray',
     'transpose',
     'truediv',
     'truncate',
     'tshift',
     'tz_convert',
     'tz_localize',
     'unstack',
     'update',
     'values',
     'var',
     'where',
     'xs']



the help function outputs a decsription of each method. 


```python
help(pd.DataFrame)
```

    Help on class DataFrame in module pandas.core.frame:
    
    class DataFrame(pandas.core.generic.NDFrame)
     |  Two-dimensional size-mutable, potentially heterogeneous tabular data
     |  structure with labeled axes (rows and columns). Arithmetic operations
     |  align on both row and column labels. Can be thought of as a dict-like
     |  container for Series objects. The primary pandas data structure
     |  
     |  Parameters
     |  ----------
     |  data : numpy ndarray (structured or homogeneous), dict, or DataFrame
     |      Dict can contain Series, arrays, constants, or list-like objects
     |  index : Index or array-like
     |      Index to use for resulting frame. Will default to np.arange(n) if
     |      no indexing information part of input data and no index provided
     |  columns : Index or array-like
     |      Column labels to use for resulting frame. Will default to
     |      np.arange(n) if no column labels are provided
     |  dtype : dtype, default None
     |      Data type to force, otherwise infer
     |  copy : boolean, default False
     |      Copy data from inputs. Only affects DataFrame / 2d ndarray input
     |  
     |  Examples
     |  --------
     |  >>> d = {'col1': ts1, 'col2': ts2}
     |  >>> df = DataFrame(data=d, index=index)
     |  >>> df2 = DataFrame(np.random.randn(10, 5))
     |  >>> df3 = DataFrame(np.random.randn(10, 5),
     |  ...                 columns=['a', 'b', 'c', 'd', 'e'])
     |  
     |  See also
     |  --------
     |  DataFrame.from_records : constructor from tuples, also record arrays
     |  DataFrame.from_dict : from dicts of Series, arrays, or dicts
     |  DataFrame.from_items : from sequence of (key, value) pairs
     |  pandas.read_csv, pandas.read_table, pandas.read_clipboard
     |  
     |  Method resolution order:
     |      DataFrame
     |      pandas.core.generic.NDFrame
     |      pandas.core.base.PandasObject
     |      pandas.core.base.StringMixin
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __add__(self, other, axis=None, level=None, fill_value=None)
     |      Binary operator __add__ with support to substitute a fill_value for missing data in
     |      one of the inputs
     |      
     |      Parameters
     |      ----------
     |      other : Series, DataFrame, or constant
     |      axis : {0, 1, 'index', 'columns'}
     |          For Series input, axis to match Series index on
     |      fill_value : None or float value, default None
     |          Fill missing (NaN) values with this value. If both DataFrame locations are
     |          missing, the result will be missing
     |      level : int or name
     |          Broadcast across a level, matching Index values on the
     |          passed MultiIndex level
     |      
     |      Notes
     |      -----
     |      Mismatched indices will be unioned together
     |      
     |      Returns
     |      -------
     |      result : DataFrame
     |  
     |  __and__(self, other, axis='columns', level=None, fill_value=None)
     |      Binary operator __and__ with support to substitute a fill_value for missing data in
     |      one of the inputs
     |      
     |      Parameters
     |      ----------
     |      other : Series, DataFrame, or constant
     |      axis : {0, 1, 'index', 'columns'}
     |          For Series input, axis to match Series index on
     |      fill_value : None or float value, default None
     |          Fill missing (NaN) values with this value. If both DataFrame locations are
     |          missing, the result will be missing
     |      level : int or name
     |          Broadcast across a level, matching Index values on the
     |          passed MultiIndex level
     |      
     |      Notes
     |      -----
     |      Mismatched indices will be unioned together
     |      
     |      Returns
     |      -------
     |      result : DataFrame
     |  
     |  __div__ = __truediv__(self, other, axis=None, level=None, fill_value=None)
     |  
     |  __eq__(self, other)
     |      Wrapper for comparison method __eq__
     |  
     |  __floordiv__(self, other, axis=None, level=None, fill_value=None)
     |      Binary operator __floordiv__ with support to substitute a fill_value for missing data in
     |      one of the inputs
     |      
     |      Parameters
     |      ----------
     |      other : Series, DataFrame, or constant
     |      axis : {0, 1, 'index', 'columns'}
     |          For Series input, axis to match Series index on
     |      fill_value : None or float value, default None
     |          Fill missing (NaN) values with this value. If both DataFrame locations are
     |          missing, the result will be missing
     |      level : int or name
     |          Broadcast across a level, matching Index values on the
     |          passed MultiIndex level
     |      
     |      Notes
     |      -----
     |      Mismatched indices will be unioned together
     |      
     |      Returns
     |      -------
     |      result : DataFrame
     |  
     |  __ge__(self, other)
     |      Wrapper for comparison method __ge__
     |  
     |  __getitem__(self, key)
     |  
     |  __gt__(self, other)
     |      Wrapper for comparison method __gt__
     |  
     |  __iadd__ = f(self, other)
     |  
     |  __imul__ = f(self, other)
     |  
     |  __init__(self, data=None, index=None, columns=None, dtype=None, copy=False)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __ipow__ = f(self, other)
     |  
     |  __isub__ = f(self, other)
     |  
     |  __itruediv__ = f(self, other)
     |  
     |  __le__(self, other)
     |      Wrapper for comparison method __le__
     |  
     |  __len__(self)
     |      Returns length of info axis, but here we use the index
     |  
     |  __lt__(self, other)
     |      Wrapper for comparison method __lt__
     |  
     |  __mod__(self, other, axis=None, level=None, fill_value=None)
     |      Binary operator __mod__ with support to substitute a fill_value for missing data in
     |      one of the inputs
     |      
     |      Parameters
     |      ----------
     |      other : Series, DataFrame, or constant
     |      axis : {0, 1, 'index', 'columns'}
     |          For Series input, axis to match Series index on
     |      fill_value : None or float value, default None
     |          Fill missing (NaN) values with this value. If both DataFrame locations are
     |          missing, the result will be missing
     |      level : int or name
     |          Broadcast across a level, matching Index values on the
     |          passed MultiIndex level
     |      
     |      Notes
     |      -----
     |      Mismatched indices will be unioned together
     |      
     |      Returns
     |      -------
     |      result : DataFrame
     |  
     |  __mul__(self, other, axis=None, level=None, fill_value=None)
     |      Binary operator __mul__ with support to substitute a fill_value for missing data in
     |      one of the inputs
     |      
     |      Parameters
     |      ----------
     |      other : Series, DataFrame, or constant
     |      axis : {0, 1, 'index', 'columns'}
     |          For Series input, axis to match Series index on
     |      fill_value : None or float value, default None
     |          Fill missing (NaN) values with this value. If both DataFrame locations are
     |          missing, the result will be missing
     |      level : int or name
     |          Broadcast across a level, matching Index values on the
     |          passed MultiIndex level
     |      
     |      Notes
     |      -----
     |      Mismatched indices will be unioned together
     |      
     |      Returns
     |      -------
     |      result : DataFrame
     |  
     |  __ne__(self, other)
     |      Wrapper for comparison method __ne__
     |  
     |  __or__(self, other, axis='columns', level=None, fill_value=None)
     |      Binary operator __or__ with support to substitute a fill_value for missing data in
     |      one of the inputs
     |      
     |      Parameters
     |      ----------
     |      other : Series, DataFrame, or constant
     |      axis : {0, 1, 'index', 'columns'}
     |          For Series input, axis to match Series index on
     |      fill_value : None or float value, default None
     |          Fill missing (NaN) values with this value. If both DataFrame locations are
     |          missing, the result will be missing
     |      level : int or name
     |          Broadcast across a level, matching Index values on the
     |          passed MultiIndex level
     |      
     |      Notes
     |      -----
     |      Mismatched indices will be unioned together
     |      
     |      Returns
     |      -------
     |      result : DataFrame
     |  
     |  __pow__(self, other, axis=None, level=None, fill_value=None)
     |      Binary operator __pow__ with support to substitute a fill_value for missing data in
     |      one of the inputs
     |      
     |      Parameters
     |      ----------
     |      other : Series, DataFrame, or constant
     |      axis : {0, 1, 'index', 'columns'}
     |          For Series input, axis to match Series index on
     |      fill_value : None or float value, default None
     |          Fill missing (NaN) values with this value. If both DataFrame locations are
     |          missing, the result will be missing
     |      level : int or name
     |          Broadcast across a level, matching Index values on the
     |          passed MultiIndex level
     |      
     |      Notes
     |      -----
     |      Mismatched indices will be unioned together
     |      
     |      Returns
     |      -------
     |      result : DataFrame
     |  
     |  __radd__(self, other, axis=None, level=None, fill_value=None)
     |      Binary operator __radd__ with support to substitute a fill_value for missing data in
     |      one of the inputs
     |      
     |      Parameters
     |      ----------
     |      other : Series, DataFrame, or constant
     |      axis : {0, 1, 'index', 'columns'}
     |          For Series input, axis to match Series index on
     |      fill_value : None or float value, default None
     |          Fill missing (NaN) values with this value. If both DataFrame locations are
     |          missing, the result will be missing
     |      level : int or name
     |          Broadcast across a level, matching Index values on the
     |          passed MultiIndex level
     |      
     |      Notes
     |      -----
     |      Mismatched indices will be unioned together
     |      
     |      Returns
     |      -------
     |      result : DataFrame
     |  
     |  __rand__(self, other, axis='columns', level=None, fill_value=None)
     |      Binary operator __rand__ with support to substitute a fill_value for missing data in
     |      one of the inputs
     |      
     |      Parameters
     |      ----------
     |      other : Series, DataFrame, or constant
     |      axis : {0, 1, 'index', 'columns'}
     |          For Series input, axis to match Series index on
     |      fill_value : None or float value, default None
     |          Fill missing (NaN) values with this value. If both DataFrame locations are
     |          missing, the result will be missing
     |      level : int or name
     |          Broadcast across a level, matching Index values on the
     |          passed MultiIndex level
     |      
     |      Notes
     |      -----
     |      Mismatched indices will be unioned together
     |      
     |      Returns
     |      -------
     |      result : DataFrame
     |  
     |  __rdiv__ = __rtruediv__(self, other, axis=None, level=None, fill_value=None)
     |  
     |  __rfloordiv__(self, other, axis=None, level=None, fill_value=None)
     |      Binary operator __rfloordiv__ with support to substitute a fill_value for missing data in
     |      one of the inputs
     |      
     |      Parameters
     |      ----------
     |      other : Series, DataFrame, or constant
     |      axis : {0, 1, 'index', 'columns'}
     |          For Series input, axis to match Series index on
     |      fill_value : None or float value, default None
     |          Fill missing (NaN) values with this value. If both DataFrame locations are
     |          missing, the result will be missing
     |      level : int or name
     |          Broadcast across a level, matching Index values on the
     |          passed MultiIndex level
     |      
     |      Notes
     |      -----
     |      Mismatched indices will be unioned together
     |      
     |      Returns
     |      -------
     |      result : DataFrame
     |  
     |  __rmod__(self, other, axis=None, level=None, fill_value=None)
     |      Binary operator __rmod__ with support to substitute a fill_value for missing data in
     |      one of the inputs
     |      
     |      Parameters
     |      ----------
     |      other : Series, DataFrame, or constant
     |      axis : {0, 1, 'index', 'columns'}
     |          For Series input, axis to match Series index on
     |      fill_value : None or float value, default None
     |          Fill missing (NaN) values with this value. If both DataFrame locations are
     |          missing, the result will be missing
     |      level : int or name
     |          Broadcast across a level, matching Index values on the
     |          passed MultiIndex level
     |      
     |      Notes
     |      -----
     |      Mismatched indices will be unioned together
     |      
     |      Returns
     |      -------
     |      result : DataFrame
     |  
     |  __rmul__(self, other, axis=None, level=None, fill_value=None)
     |      Binary operator __rmul__ with support to substitute a fill_value for missing data in
     |      one of the inputs
     |      
     |      Parameters
     |      ----------
     |      other : Series, DataFrame, or constant
     |      axis : {0, 1, 'index', 'columns'}
     |          For Series input, axis to match Series index on
     |      fill_value : None or float value, default None
     |          Fill missing (NaN) values with this value. If both DataFrame locations are
     |          missing, the result will be missing
     |      level : int or name
     |          Broadcast across a level, matching Index values on the
     |          passed MultiIndex level
     |      
     |      Notes
     |      -----
     |      Mismatched indices will be unioned together
     |      
     |      Returns
     |      -------
     |      result : DataFrame
     |  
     |  __ror__(self, other, axis='columns', level=None, fill_value=None)
     |      Binary operator __ror__ with support to substitute a fill_value for missing data in
     |      one of the inputs
     |      
     |      Parameters
     |      ----------
     |      other : Series, DataFrame, or constant
     |      axis : {0, 1, 'index', 'columns'}
     |          For Series input, axis to match Series index on
     |      fill_value : None or float value, default None
     |          Fill missing (NaN) values with this value. If both DataFrame locations are
     |          missing, the result will be missing
     |      level : int or name
     |          Broadcast across a level, matching Index values on the
     |          passed MultiIndex level
     |      
     |      Notes
     |      -----
     |      Mismatched indices will be unioned together
     |      
     |      Returns
     |      -------
     |      result : DataFrame
     |  
     |  __rpow__(self, other, axis=None, level=None, fill_value=None)
     |      Binary operator __rpow__ with support to substitute a fill_value for missing data in
     |      one of the inputs
     |      
     |      Parameters
     |      ----------
     |      other : Series, DataFrame, or constant
     |      axis : {0, 1, 'index', 'columns'}
     |          For Series input, axis to match Series index on
     |      fill_value : None or float value, default None
     |          Fill missing (NaN) values with this value. If both DataFrame locations are
     |          missing, the result will be missing
     |      level : int or name
     |          Broadcast across a level, matching Index values on the
     |          passed MultiIndex level
     |      
     |      Notes
     |      -----
     |      Mismatched indices will be unioned together
     |      
     |      Returns
     |      -------
     |      result : DataFrame
     |  
     |  __rsub__(self, other, axis=None, level=None, fill_value=None)
     |      Binary operator __rsub__ with support to substitute a fill_value for missing data in
     |      one of the inputs
     |      
     |      Parameters
     |      ----------
     |      other : Series, DataFrame, or constant
     |      axis : {0, 1, 'index', 'columns'}
     |          For Series input, axis to match Series index on
     |      fill_value : None or float value, default None
     |          Fill missing (NaN) values with this value. If both DataFrame locations are
     |          missing, the result will be missing
     |      level : int or name
     |          Broadcast across a level, matching Index values on the
     |          passed MultiIndex level
     |      
     |      Notes
     |      -----
     |      Mismatched indices will be unioned together
     |      
     |      Returns
     |      -------
     |      result : DataFrame
     |  
     |  __rtruediv__(self, other, axis=None, level=None, fill_value=None)
     |      Binary operator __rtruediv__ with support to substitute a fill_value for missing data in
     |      one of the inputs
     |      
     |      Parameters
     |      ----------
     |      other : Series, DataFrame, or constant
     |      axis : {0, 1, 'index', 'columns'}
     |          For Series input, axis to match Series index on
     |      fill_value : None or float value, default None
     |          Fill missing (NaN) values with this value. If both DataFrame locations are
     |          missing, the result will be missing
     |      level : int or name
     |          Broadcast across a level, matching Index values on the
     |          passed MultiIndex level
     |      
     |      Notes
     |      -----
     |      Mismatched indices will be unioned together
     |      
     |      Returns
     |      -------
     |      result : DataFrame
     |  
     |  __rxor__(self, other, axis='columns', level=None, fill_value=None)
     |      Binary operator __rxor__ with support to substitute a fill_value for missing data in
     |      one of the inputs
     |      
     |      Parameters
     |      ----------
     |      other : Series, DataFrame, or constant
     |      axis : {0, 1, 'index', 'columns'}
     |          For Series input, axis to match Series index on
     |      fill_value : None or float value, default None
     |          Fill missing (NaN) values with this value. If both DataFrame locations are
     |          missing, the result will be missing
     |      level : int or name
     |          Broadcast across a level, matching Index values on the
     |          passed MultiIndex level
     |      
     |      Notes
     |      -----
     |      Mismatched indices will be unioned together
     |      
     |      Returns
     |      -------
     |      result : DataFrame
     |  
     |  __setitem__(self, key, value)
     |  
     |  __sub__(self, other, axis=None, level=None, fill_value=None)
     |      Binary operator __sub__ with support to substitute a fill_value for missing data in
     |      one of the inputs
     |      
     |      Parameters
     |      ----------
     |      other : Series, DataFrame, or constant
     |      axis : {0, 1, 'index', 'columns'}
     |          For Series input, axis to match Series index on
     |      fill_value : None or float value, default None
     |          Fill missing (NaN) values with this value. If both DataFrame locations are
     |          missing, the result will be missing
     |      level : int or name
     |          Broadcast across a level, matching Index values on the
     |          passed MultiIndex level
     |      
     |      Notes
     |      -----
     |      Mismatched indices will be unioned together
     |      
     |      Returns
     |      -------
     |      result : DataFrame
     |  
     |  __truediv__(self, other, axis=None, level=None, fill_value=None)
     |      Binary operator __truediv__ with support to substitute a fill_value for missing data in
     |      one of the inputs
     |      
     |      Parameters
     |      ----------
     |      other : Series, DataFrame, or constant
     |      axis : {0, 1, 'index', 'columns'}
     |          For Series input, axis to match Series index on
     |      fill_value : None or float value, default None
     |          Fill missing (NaN) values with this value. If both DataFrame locations are
     |          missing, the result will be missing
     |      level : int or name
     |          Broadcast across a level, matching Index values on the
     |          passed MultiIndex level
     |      
     |      Notes
     |      -----
     |      Mismatched indices will be unioned together
     |      
     |      Returns
     |      -------
     |      result : DataFrame
     |  
     |  __unicode__(self)
     |      Return a string representation for a particular DataFrame
     |      
     |      Invoked by unicode(df) in py2 only. Yields a Unicode String in both
     |      py2/py3.
     |  
     |  __xor__(self, other, axis='columns', level=None, fill_value=None)
     |      Binary operator __xor__ with support to substitute a fill_value for missing data in
     |      one of the inputs
     |      
     |      Parameters
     |      ----------
     |      other : Series, DataFrame, or constant
     |      axis : {0, 1, 'index', 'columns'}
     |          For Series input, axis to match Series index on
     |      fill_value : None or float value, default None
     |          Fill missing (NaN) values with this value. If both DataFrame locations are
     |          missing, the result will be missing
     |      level : int or name
     |          Broadcast across a level, matching Index values on the
     |          passed MultiIndex level
     |      
     |      Notes
     |      -----
     |      Mismatched indices will be unioned together
     |      
     |      Returns
     |      -------
     |      result : DataFrame
     |  
     |  add(self, other, axis='columns', level=None, fill_value=None)
     |      Addition of dataframe and other, element-wise (binary operator `add`).
     |      
     |      Equivalent to ``dataframe + other``, but with support to substitute a fill_value for
     |      missing data in one of the inputs.
     |      
     |      Parameters
     |      ----------
     |      other : Series, DataFrame, or constant
     |      axis : {0, 1, 'index', 'columns'}
     |          For Series input, axis to match Series index on
     |      fill_value : None or float value, default None
     |          Fill missing (NaN) values with this value. If both DataFrame
     |          locations are missing, the result will be missing
     |      level : int or name
     |          Broadcast across a level, matching Index values on the
     |          passed MultiIndex level
     |      
     |      Notes
     |      -----
     |      Mismatched indices will be unioned together
     |      
     |      Returns
     |      -------
     |      result : DataFrame
     |      
     |      See also
     |      --------
     |      DataFrame.radd
     |  
     |  align(self, other, join='outer', axis=None, level=None, copy=True, fill_value=None, method=None, limit=None, fill_axis=0, broadcast_axis=None)
     |      Align two object on their axes with the
     |      specified join method for each axis Index
     |      
     |      Parameters
     |      ----------
     |      other : DataFrame or Series
     |      join : {'outer', 'inner', 'left', 'right'}, default 'outer'
     |      axis : allowed axis of the other object, default None
     |          Align on index (0), columns (1), or both (None)
     |      level : int or level name, default None
     |          Broadcast across a level, matching Index values on the
     |          passed MultiIndex level
     |      copy : boolean, default True
     |          Always returns new objects. If copy=False and no reindexing is
     |          required then original objects are returned.
     |      fill_value : scalar, default np.NaN
     |          Value to use for missing values. Defaults to NaN, but can be any
     |          "compatible" value
     |      method : str, default None
     |      limit : int, default None
     |      fill_axis : {0 or 'index', 1 or 'columns'}, default 0
     |          Filling axis, method and limit
     |      broadcast_axis : {0 or 'index', 1 or 'columns'}, default None
     |          Broadcast values along this axis, if aligning two objects of
     |          different dimensions
     |      
     |          .. versionadded:: 0.17.0
     |      
     |      Returns
     |      -------
     |      (left, right) : (DataFrame, type of other)
     |          Aligned objects
     |  
     |  all(self, axis=None, bool_only=None, skipna=None, level=None, **kwargs)
     |      Return whether all elements are True over requested axis
     |      
     |      Parameters
     |      ----------
     |      axis : {index (0), columns (1)}
     |      skipna : boolean, default True
     |          Exclude NA/null values. If an entire row/column is NA, the result
     |          will be NA
     |      level : int or level name, default None
     |          If the axis is a MultiIndex (hierarchical), count along a
     |          particular level, collapsing into a Series
     |      bool_only : boolean, default None
     |          Include only boolean columns. If None, will attempt to use everything,
     |          then use only boolean data. Not implemented for Series.
     |      
     |      Returns
     |      -------
     |      all : Series or DataFrame (if level specified)
     |  
     |  any(self, axis=None, bool_only=None, skipna=None, level=None, **kwargs)
     |      Return whether any element is True over requested axis
     |      
     |      Parameters
     |      ----------
     |      axis : {index (0), columns (1)}
     |      skipna : boolean, default True
     |          Exclude NA/null values. If an entire row/column is NA, the result
     |          will be NA
     |      level : int or level name, default None
     |          If the axis is a MultiIndex (hierarchical), count along a
     |          particular level, collapsing into a Series
     |      bool_only : boolean, default None
     |          Include only boolean columns. If None, will attempt to use everything,
     |          then use only boolean data. Not implemented for Series.
     |      
     |      Returns
     |      -------
     |      any : Series or DataFrame (if level specified)
     |  
     |  append(self, other, ignore_index=False, verify_integrity=False)
     |      Append rows of `other` to the end of this frame, returning a new
     |      object. Columns not in this frame are added as new columns.
     |      
     |      Parameters
     |      ----------
     |      other : DataFrame or Series/dict-like object, or list of these
     |          The data to append.
     |      ignore_index : boolean, default False
     |          If True, do not use the index labels.
     |      verify_integrity : boolean, default False
     |          If True, raise ValueError on creating index with duplicates.
     |      
     |      Returns
     |      -------
     |      appended : DataFrame
     |      
     |      Notes
     |      -----
     |      If a list of dict/series is passed and the keys are all contained in
     |      the DataFrame's index, the order of the columns in the resulting
     |      DataFrame will be unchanged.
     |      
     |      See also
     |      --------
     |      pandas.concat : General function to concatenate DataFrame, Series
     |          or Panel objects
     |      
     |      Examples
     |      --------
     |      
     |      >>> df = pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'))
     |      >>> df
     |         A  B
     |      0  1  2
     |      1  3  4
     |      >>> df2 = pd.DataFrame([[5, 6], [7, 8]], columns=list('AB'))
     |      >>> df.append(df2)
     |         A  B
     |      0  1  2
     |      1  3  4
     |      0  5  6
     |      1  7  8
     |      
     |      With `ignore_index` set to True:
     |      
     |      >>> df.append(df2, ignore_index=True)
     |         A  B
     |      0  1  2
     |      1  3  4
     |      2  5  6
     |      3  7  8
     |  
     |  apply(self, func, axis=0, broadcast=False, raw=False, reduce=None, args=(), **kwds)
     |      Applies function along input axis of DataFrame.
     |      
     |      Objects passed to functions are Series objects having index
     |      either the DataFrame's index (axis=0) or the columns (axis=1).
     |      Return type depends on whether passed function aggregates, or the
     |      reduce argument if the DataFrame is empty.
     |      
     |      Parameters
     |      ----------
     |      func : function
     |          Function to apply to each column/row
     |      axis : {0 or 'index', 1 or 'columns'}, default 0
     |          * 0 or 'index': apply function to each column
     |          * 1 or 'columns': apply function to each row
     |      broadcast : boolean, default False
     |          For aggregation functions, return object of same size with values
     |          propagated
     |      raw : boolean, default False
     |          If False, convert each row or column into a Series. If raw=True the
     |          passed function will receive ndarray objects instead. If you are
     |          just applying a NumPy reduction function this will achieve much
     |          better performance
     |      reduce : boolean or None, default None
     |          Try to apply reduction procedures. If the DataFrame is empty,
     |          apply will use reduce to determine whether the result should be a
     |          Series or a DataFrame. If reduce is None (the default), apply's
     |          return value will be guessed by calling func an empty Series (note:
     |          while guessing, exceptions raised by func will be ignored). If
     |          reduce is True a Series will always be returned, and if False a
     |          DataFrame will always be returned.
     |      args : tuple
     |          Positional arguments to pass to function in addition to the
     |          array/series
     |      Additional keyword arguments will be passed as keywords to the function
     |      
     |      Notes
     |      -----
     |      In the current implementation apply calls func twice on the
     |      first column/row to decide whether it can take a fast or slow
     |      code path. This can lead to unexpected behavior if func has
     |      side-effects, as they will take effect twice for the first
     |      column/row.
     |      
     |      Examples
     |      --------
     |      >>> df.apply(numpy.sqrt) # returns DataFrame
     |      >>> df.apply(numpy.sum, axis=0) # equiv to df.sum(0)
     |      >>> df.apply(numpy.sum, axis=1) # equiv to df.sum(1)
     |      
     |      See also
     |      --------
     |      DataFrame.applymap: For elementwise operations
     |      
     |      Returns
     |      -------
     |      applied : Series or DataFrame
     |  
     |  applymap(self, func)
     |      Apply a function to a DataFrame that is intended to operate
     |      elementwise, i.e. like doing map(func, series) for each series in the
     |      DataFrame
     |      
     |      Parameters
     |      ----------
     |      func : function
     |          Python function, returns a single value from a single value
     |      
     |      Examples
     |      --------
     |      
     |      >>> df = pd.DataFrame(np.random.randn(3, 3))
     |      >>> df
     |          0         1          2
     |      0  -0.029638  1.081563   1.280300
     |      1   0.647747  0.831136  -1.549481
     |      2   0.513416 -0.884417   0.195343
     |      >>> df = df.applymap(lambda x: '%.2f' % x)
     |      >>> df
     |          0         1          2
     |      0  -0.03      1.08       1.28
     |      1   0.65      0.83      -1.55
     |      2   0.51     -0.88       0.20
     |      
     |      Returns
     |      -------
     |      applied : DataFrame
     |      
     |      See also
     |      --------
     |      DataFrame.apply : For operations on rows/columns
     |  
     |  assign(self, **kwargs)
     |      Assign new columns to a DataFrame, returning a new object
     |      (a copy) with all the original columns in addition to the new ones.
     |      
     |      .. versionadded:: 0.16.0
     |      
     |      Parameters
     |      ----------
     |      kwargs : keyword, value pairs
     |          keywords are the column names. If the values are
     |          callable, they are computed on the DataFrame and
     |          assigned to the new columns. The callable must not
     |          change input DataFrame (though pandas doesn't check it).
     |          If the values are not callable, (e.g. a Series, scalar, or array),
     |          they are simply assigned.
     |      
     |      Returns
     |      -------
     |      df : DataFrame
     |          A new DataFrame with the new columns in addition to
     |          all the existing columns.
     |      
     |      Notes
     |      -----
     |      Since ``kwargs`` is a dictionary, the order of your
     |      arguments may not be preserved. The make things predicatable,
     |      the columns are inserted in alphabetical order, at the end of
     |      your DataFrame. Assigning multiple columns within the same
     |      ``assign`` is possible, but you cannot reference other columns
     |      created within the same ``assign`` call.
     |      
     |      Examples
     |      --------
     |      >>> df = DataFrame({'A': range(1, 11), 'B': np.random.randn(10)})
     |      
     |      Where the value is a callable, evaluated on `df`:
     |      
     |      >>> df.assign(ln_A = lambda x: np.log(x.A))
     |          A         B      ln_A
     |      0   1  0.426905  0.000000
     |      1   2 -0.780949  0.693147
     |      2   3 -0.418711  1.098612
     |      3   4 -0.269708  1.386294
     |      4   5 -0.274002  1.609438
     |      5   6 -0.500792  1.791759
     |      6   7  1.649697  1.945910
     |      7   8 -1.495604  2.079442
     |      8   9  0.549296  2.197225
     |      9  10 -0.758542  2.302585
     |      
     |      Where the value already exists and is inserted:
     |      
     |      >>> newcol = np.log(df['A'])
     |      >>> df.assign(ln_A=newcol)
     |          A         B      ln_A
     |      0   1  0.426905  0.000000
     |      1   2 -0.780949  0.693147
     |      2   3 -0.418711  1.098612
     |      3   4 -0.269708  1.386294
     |      4   5 -0.274002  1.609438
     |      5   6 -0.500792  1.791759
     |      6   7  1.649697  1.945910
     |      7   8 -1.495604  2.079442
     |      8   9  0.549296  2.197225
     |      9  10 -0.758542  2.302585
     |  
     |  boxplot(self, column=None, by=None, ax=None, fontsize=None, rot=0, grid=True, figsize=None, layout=None, return_type=None, **kwds)
     |      Make a box plot from DataFrame column optionally grouped by some columns or
     |      other inputs
     |      
     |      Parameters
     |      ----------
     |      data : the pandas object holding the data
     |      column : column name or list of names, or vector
     |          Can be any valid input to groupby
     |      by : string or sequence
     |          Column in the DataFrame to group by
     |      ax : Matplotlib axes object, optional
     |      fontsize : int or string
     |      rot : label rotation angle
     |      figsize : A tuple (width, height) in inches
     |      grid : Setting this to True will show the grid
     |      layout : tuple (optional)
     |          (rows, columns) for the layout of the plot
     |      return_type : {None, 'axes', 'dict', 'both'}, default None
     |          The kind of object to return. The default is ``axes``
     |          'axes' returns the matplotlib axes the boxplot is drawn on;
     |          'dict' returns a dictionary  whose values are the matplotlib
     |          Lines of the boxplot;
     |          'both' returns a namedtuple with the axes and dict.
     |      
     |          When grouping with ``by``, a Series mapping columns to ``return_type``
     |          is returned, unless ``return_type`` is None, in which case a NumPy
     |          array of axes is returned with the same shape as ``layout``.
     |          See the prose documentation for more.
     |      
     |      kwds : other plotting keyword arguments to be passed to matplotlib boxplot
     |             function
     |      
     |      Returns
     |      -------
     |      lines : dict
     |      ax : matplotlib Axes
     |      (ax, lines): namedtuple
     |      
     |      Notes
     |      -----
     |      Use ``return_type='dict'`` when you want to tweak the appearance
     |      of the lines after plotting. In this case a dict containing the Lines
     |      making up the boxes, caps, fliers, medians, and whiskers is returned.
     |  
     |  combine(self, other, func, fill_value=None, overwrite=True)
     |      Add two DataFrame objects and do not propagate NaN values, so if for a
     |      (column, time) one frame is missing a value, it will default to the
     |      other frame's value (which might be NaN as well)
     |      
     |      Parameters
     |      ----------
     |      other : DataFrame
     |      func : function
     |      fill_value : scalar value
     |      overwrite : boolean, default True
     |          If True then overwrite values for common keys in the calling frame
     |      
     |      Returns
     |      -------
     |      result : DataFrame
     |  
     |  combineAdd(self, other)
     |      DEPRECATED. Use ``DataFrame.add(other, fill_value=0.)`` instead.
     |      
     |      Add two DataFrame objects and do not propagate
     |      NaN values, so if for a (column, time) one frame is missing a
     |      value, it will default to the other frame's value (which might
     |      be NaN as well)
     |      
     |      Parameters
     |      ----------
     |      other : DataFrame
     |      
     |      Returns
     |      -------
     |      DataFrame
     |      
     |      See also
     |      --------
     |      DataFrame.add
     |  
     |  combineMult(self, other)
     |      DEPRECATED. Use ``DataFrame.mul(other, fill_value=1.)`` instead.
     |      
     |      Multiply two DataFrame objects and do not propagate NaN values, so if
     |      for a (column, time) one frame is missing a value, it will default to
     |      the other frame's value (which might be NaN as well)
     |      
     |      Parameters
     |      ----------
     |      other : DataFrame
     |      
     |      Returns
     |      -------
     |      DataFrame
     |      
     |      See also
     |      --------
     |      DataFrame.mul
     |  
     |  combine_first(self, other)
     |      Combine two DataFrame objects and default to non-null values in frame
     |      calling the method. Result index columns will be the union of the
     |      respective indexes and columns
     |      
     |      Parameters
     |      ----------
     |      other : DataFrame
     |      
     |      Examples
     |      --------
     |      a's values prioritized, use values from b to fill holes:
     |      
     |      >>> a.combine_first(b)
     |      
     |      
     |      Returns
     |      -------
     |      combined : DataFrame
     |  
     |  compound(self, axis=None, skipna=None, level=None)
     |      Return the compound percentage of the values for the requested axis
     |      
     |      Parameters
     |      ----------
     |      axis : {index (0), columns (1)}
     |      skipna : boolean, default True
     |          Exclude NA/null values. If an entire row/column is NA, the result
     |          will be NA
     |      level : int or level name, default None
     |          If the axis is a MultiIndex (hierarchical), count along a
     |          particular level, collapsing into a Series
     |      numeric_only : boolean, default None
     |          Include only float, int, boolean columns. If None, will attempt to use
     |          everything, then use only numeric data. Not implemented for Series.
     |      
     |      Returns
     |      -------
     |      compounded : Series or DataFrame (if level specified)
     |  
     |  corr(self, method='pearson', min_periods=1)
     |      Compute pairwise correlation of columns, excluding NA/null values
     |      
     |      Parameters
     |      ----------
     |      method : {'pearson', 'kendall', 'spearman'}
     |          * pearson : standard correlation coefficient
     |          * kendall : Kendall Tau correlation coefficient
     |          * spearman : Spearman rank correlation
     |      min_periods : int, optional
     |          Minimum number of observations required per pair of columns
     |          to have a valid result. Currently only available for pearson
     |          and spearman correlation
     |      
     |      Returns
     |      -------
     |      y : DataFrame
     |  
     |  corrwith(self, other, axis=0, drop=False)
     |      Compute pairwise correlation between rows or columns of two DataFrame
     |      objects.
     |      
     |      Parameters
     |      ----------
     |      other : DataFrame
     |      axis : {0 or 'index', 1 or 'columns'}, default 0
     |          0 or 'index' to compute column-wise, 1 or 'columns' for row-wise
     |      drop : boolean, default False
     |          Drop missing indices from result, default returns union of all
     |      
     |      Returns
     |      -------
     |      correls : Series
     |  
     |  count(self, axis=0, level=None, numeric_only=False)
     |      Return Series with number of non-NA/null observations over requested
     |      axis. Works with non-floating point data as well (detects NaN and None)
     |      
     |      Parameters
     |      ----------
     |      axis : {0 or 'index', 1 or 'columns'}, default 0
     |          0 or 'index' for row-wise, 1 or 'columns' for column-wise
     |      level : int or level name, default None
     |          If the axis is a MultiIndex (hierarchical), count along a
     |          particular level, collapsing into a DataFrame
     |      numeric_only : boolean, default False
     |          Include only float, int, boolean data
     |      
     |      Returns
     |      -------
     |      count : Series (or DataFrame if level specified)
     |  
     |  cov(self, min_periods=None)
     |      Compute pairwise covariance of columns, excluding NA/null values
     |      
     |      Parameters
     |      ----------
     |      min_periods : int, optional
     |          Minimum number of observations required per pair of columns
     |          to have a valid result.
     |      
     |      Returns
     |      -------
     |      y : DataFrame
     |      
     |      Notes
     |      -----
     |      `y` contains the covariance matrix of the DataFrame's time series.
     |      The covariance is normalized by N-1 (unbiased estimator).
     |  
     |  cummax(self, axis=None, skipna=True, *args, **kwargs)
     |      Return cumulative max over requested axis.
     |      
     |      Parameters
     |      ----------
     |      axis : {index (0), columns (1)}
     |      skipna : boolean, default True
     |          Exclude NA/null values. If an entire row/column is NA, the result
     |          will be NA
     |      
     |      Returns
     |      -------
     |      cummax : Series
     |  
     |  cummin(self, axis=None, skipna=True, *args, **kwargs)
     |      Return cumulative minimum over requested axis.
     |      
     |      Parameters
     |      ----------
     |      axis : {index (0), columns (1)}
     |      skipna : boolean, default True
     |          Exclude NA/null values. If an entire row/column is NA, the result
     |          will be NA
     |      
     |      Returns
     |      -------
     |      cummin : Series
     |  
     |  cumprod(self, axis=None, skipna=True, *args, **kwargs)
     |      Return cumulative product over requested axis.
     |      
     |      Parameters
     |      ----------
     |      axis : {index (0), columns (1)}
     |      skipna : boolean, default True
     |          Exclude NA/null values. If an entire row/column is NA, the result
     |          will be NA
     |      
     |      Returns
     |      -------
     |      cumprod : Series
     |  
     |  cumsum(self, axis=None, skipna=True, *args, **kwargs)
     |      Return cumulative sum over requested axis.
     |      
     |      Parameters
     |      ----------
     |      axis : {index (0), columns (1)}
     |      skipna : boolean, default True
     |          Exclude NA/null values. If an entire row/column is NA, the result
     |          will be NA
     |      
     |      Returns
     |      -------
     |      cumsum : Series
     |  
     |  diff(self, periods=1, axis=0)
     |      1st discrete difference of object
     |      
     |      Parameters
     |      ----------
     |      periods : int, default 1
     |          Periods to shift for forming difference
     |      axis : {0 or 'index', 1 or 'columns'}, default 0
     |          Take difference over rows (0) or columns (1).
     |      
     |          .. versionadded: 0.16.1
     |      
     |      Returns
     |      -------
     |      diffed : DataFrame
     |  
     |  div = truediv(self, other, axis='columns', level=None, fill_value=None)
     |  
     |  divide = truediv(self, other, axis='columns', level=None, fill_value=None)
     |  
     |  dot(self, other)
     |      Matrix multiplication with DataFrame or Series objects
     |      
     |      Parameters
     |      ----------
     |      other : DataFrame or Series
     |      
     |      Returns
     |      -------
     |      dot_product : DataFrame or Series
     |  
     |  drop_duplicates(self, subset=None, keep='first', inplace=False)
     |      Return DataFrame with duplicate rows removed, optionally only
     |      considering certain columns
     |      
     |      Parameters
     |      ----------
     |      subset : column label or sequence of labels, optional
     |          Only consider certain columns for identifying duplicates, by
     |          default use all of the columns
     |      keep : {'first', 'last', False}, default 'first'
     |          - ``first`` : Drop duplicates except for the first occurrence.
     |          - ``last`` : Drop duplicates except for the last occurrence.
     |          - False : Drop all duplicates.
     |      take_last : deprecated
     |      inplace : boolean, default False
     |          Whether to drop duplicates in place or to return a copy
     |      
     |      Returns
     |      -------
     |      deduplicated : DataFrame
     |  
     |  dropna(self, axis=0, how='any', thresh=None, subset=None, inplace=False)
     |      Return object with labels on given axis omitted where alternately any
     |      or all of the data are missing
     |      
     |      Parameters
     |      ----------
     |      axis : {0 or 'index', 1 or 'columns'}, or tuple/list thereof
     |          Pass tuple or list to drop on multiple axes
     |      how : {'any', 'all'}
     |          * any : if any NA values are present, drop that label
     |          * all : if all values are NA, drop that label
     |      thresh : int, default None
     |          int value : require that many non-NA values
     |      subset : array-like
     |          Labels along other axis to consider, e.g. if you are dropping rows
     |          these would be a list of columns to include
     |      inplace : boolean, default False
     |          If True, do operation inplace and return None.
     |      
     |      Returns
     |      -------
     |      dropped : DataFrame
     |  
     |  duplicated(self, subset=None, keep='first')
     |      Return boolean Series denoting duplicate rows, optionally only
     |      considering certain columns
     |      
     |      Parameters
     |      ----------
     |      subset : column label or sequence of labels, optional
     |          Only consider certain columns for identifying duplicates, by
     |          default use all of the columns
     |      keep : {'first', 'last', False}, default 'first'
     |          - ``first`` : Mark duplicates as ``True`` except for the
     |            first occurrence.
     |          - ``last`` : Mark duplicates as ``True`` except for the
     |            last occurrence.
     |          - False : Mark all duplicates as ``True``.
     |      take_last : deprecated
     |      
     |      Returns
     |      -------
     |      duplicated : Series
     |  
     |  eq(self, other, axis='columns', level=None)
     |      Wrapper for flexible comparison methods eq
     |  
     |  eval(self, expr, inplace=None, **kwargs)
     |      Evaluate an expression in the context of the calling DataFrame
     |      instance.
     |      
     |      Parameters
     |      ----------
     |      expr : string
     |          The expression string to evaluate.
     |      inplace : bool
     |          If the expression contains an assignment, whether to return a new
     |          DataFrame or mutate the existing.
     |      
     |          WARNING: inplace=None currently falls back to to True, but
     |          in a future version, will default to False.  Use inplace=True
     |          explicitly rather than relying on the default.
     |      
     |          .. versionadded:: 0.18.0
     |      
     |      kwargs : dict
     |          See the documentation for :func:`~pandas.eval` for complete details
     |          on the keyword arguments accepted by
     |          :meth:`~pandas.DataFrame.query`.
     |      
     |      Returns
     |      -------
     |      ret : ndarray, scalar, or pandas object
     |      
     |      See Also
     |      --------
     |      pandas.DataFrame.query
     |      pandas.DataFrame.assign
     |      pandas.eval
     |      
     |      Notes
     |      -----
     |      For more details see the API documentation for :func:`~pandas.eval`.
     |      For detailed examples see :ref:`enhancing performance with eval
     |      <enhancingperf.eval>`.
     |      
     |      Examples
     |      --------
     |      >>> from numpy.random import randn
     |      >>> from pandas import DataFrame
     |      >>> df = DataFrame(randn(10, 2), columns=list('ab'))
     |      >>> df.eval('a + b')
     |      >>> df.eval('c = a + b')
     |  
     |  ewm(self, com=None, span=None, halflife=None, alpha=None, min_periods=0, freq=None, adjust=True, ignore_na=False, axis=0)
     |      Provides exponential weighted functions
     |      
     |      .. versionadded:: 0.18.0
     |      
     |      Parameters
     |      ----------
     |      com : float, optional
     |          Specify decay in terms of center of mass,
     |          :math:`\alpha = 1 / (1 + com),\text{ for } com \geq 0`
     |      span : float, optional
     |          Specify decay in terms of span,
     |          :math:`\alpha = 2 / (span + 1),\text{ for } span \geq 1`
     |      halflife : float, optional
     |          Specify decay in terms of half-life,
     |          :math:`\alpha = 1 - exp(log(0.5) / halflife),\text{ for } halflife > 0`
     |      alpha : float, optional
     |          Specify smoothing factor :math:`\alpha` directly,
     |          :math:`0 < \alpha \leq 1`
     |      
     |          .. versionadded:: 0.18.0
     |      
     |      min_periods : int, default 0
     |          Minimum number of observations in window required to have a value
     |          (otherwise result is NA).
     |      freq : None or string alias / date offset object, default=None (DEPRECATED)
     |          Frequency to conform to before computing statistic
     |      adjust : boolean, default True
     |          Divide by decaying adjustment factor in beginning periods to account
     |          for imbalance in relative weightings (viewing EWMA as a moving average)
     |      ignore_na : boolean, default False
     |          Ignore missing values when calculating weights;
     |          specify True to reproduce pre-0.15.0 behavior
     |      
     |      Returns
     |      -------
     |      a Window sub-classed for the particular operation
     |      
     |      Examples
     |      --------
     |      
     |      >>> df = DataFrame({'B': [0, 1, 2, np.nan, 4]})
     |           B
     |      0  0.0
     |      1  1.0
     |      2  2.0
     |      3  NaN
     |      4  4.0
     |      
     |      >>> df.ewm(com=0.5).mean()
     |                B
     |      0  0.000000
     |      1  0.750000
     |      2  1.615385
     |      3  1.615385
     |      4  3.670213
     |      
     |      Notes
     |      -----
     |      Exactly one of center of mass, span, half-life, and alpha must be provided.
     |      Allowed values and relationship between the parameters are specified in the
     |      parameter descriptions above; see the link at the end of this section for
     |      a detailed explanation.
     |      
     |      The `freq` keyword is used to conform time series data to a specified
     |      frequency by resampling the data. This is done with the default parameters
     |      of :meth:`~pandas.Series.resample` (i.e. using the `mean`).
     |      
     |      When adjust is True (default), weighted averages are calculated using
     |      weights (1-alpha)**(n-1), (1-alpha)**(n-2), ..., 1-alpha, 1.
     |      
     |      When adjust is False, weighted averages are calculated recursively as:
     |         weighted_average[0] = arg[0];
     |         weighted_average[i] = (1-alpha)*weighted_average[i-1] + alpha*arg[i].
     |      
     |      When ignore_na is False (default), weights are based on absolute positions.
     |      For example, the weights of x and y used in calculating the final weighted
     |      average of [x, None, y] are (1-alpha)**2 and 1 (if adjust is True), and
     |      (1-alpha)**2 and alpha (if adjust is False).
     |      
     |      When ignore_na is True (reproducing pre-0.15.0 behavior), weights are based
     |      on relative positions. For example, the weights of x and y used in
     |      calculating the final weighted average of [x, None, y] are 1-alpha and 1
     |      (if adjust is True), and 1-alpha and alpha (if adjust is False).
     |      
     |      More details can be found at
     |      http://pandas.pydata.org/pandas-docs/stable/computation.html#exponentially-weighted-windows
     |  
     |  expanding(self, min_periods=1, freq=None, center=False, axis=0)
     |      Provides expanding transformations.
     |      
     |      .. versionadded:: 0.18.0
     |      
     |      Parameters
     |      ----------
     |      min_periods : int, default None
     |          Minimum number of observations in window required to have a value
     |          (otherwise result is NA).
     |      freq : string or DateOffset object, optional (default None) (DEPRECATED)
     |          Frequency to conform the data to before computing the statistic.
     |          Specified as a frequency string or DateOffset object.
     |      center : boolean, default False
     |          Set the labels at the center of the window.
     |      axis : int or string, default 0
     |      
     |      Returns
     |      -------
     |      a Window sub-classed for the particular operation
     |      
     |      Examples
     |      --------
     |      
     |      >>> df = DataFrame({'B': [0, 1, 2, np.nan, 4]})
     |           B
     |      0  0.0
     |      1  1.0
     |      2  2.0
     |      3  NaN
     |      4  4.0
     |      
     |      >>> df.expanding(2).sum()
     |           B
     |      0  NaN
     |      1  1.0
     |      2  3.0
     |      3  3.0
     |      4  7.0
     |      
     |      Notes
     |      -----
     |      By default, the result is set to the right edge of the window. This can be
     |      changed to the center of the window by setting ``center=True``.
     |      
     |      The `freq` keyword is used to conform time series data to a specified
     |      frequency by resampling the data. This is done with the default parameters
     |      of :meth:`~pandas.Series.resample` (i.e. using the `mean`).
     |  
     |  fillna(self, value=None, method=None, axis=None, inplace=False, limit=None, downcast=None, **kwargs)
     |      Fill NA/NaN values using the specified method
     |      
     |      Parameters
     |      ----------
     |      value : scalar, dict, Series, or DataFrame
     |          Value to use to fill holes (e.g. 0), alternately a
     |          dict/Series/DataFrame of values specifying which value to use for
     |          each index (for a Series) or column (for a DataFrame). (values not
     |          in the dict/Series/DataFrame will not be filled). This value cannot
     |          be a list.
     |      method : {'backfill', 'bfill', 'pad', 'ffill', None}, default None
     |          Method to use for filling holes in reindexed Series
     |          pad / ffill: propagate last valid observation forward to next valid
     |          backfill / bfill: use NEXT valid observation to fill gap
     |      axis : {0 or 'index', 1 or 'columns'}
     |      inplace : boolean, default False
     |          If True, fill in place. Note: this will modify any
     |          other views on this object, (e.g. a no-copy slice for a column in a
     |          DataFrame).
     |      limit : int, default None
     |          If method is specified, this is the maximum number of consecutive
     |          NaN values to forward/backward fill. In other words, if there is
     |          a gap with more than this number of consecutive NaNs, it will only
     |          be partially filled. If method is not specified, this is the
     |          maximum number of entries along the entire axis where NaNs will be
     |          filled.
     |      downcast : dict, default is None
     |          a dict of item->dtype of what to downcast if possible,
     |          or the string 'infer' which will try to downcast to an appropriate
     |          equal type (e.g. float64 to int64 if possible)
     |      
     |      See Also
     |      --------
     |      reindex, asfreq
     |      
     |      Returns
     |      -------
     |      filled : DataFrame
     |  
     |  first_valid_index(self)
     |      Return label for first non-NA/null value
     |  
     |  floordiv(self, other, axis='columns', level=None, fill_value=None)
     |      Integer division of dataframe and other, element-wise (binary operator `floordiv`).
     |      
     |      Equivalent to ``dataframe // other``, but with support to substitute a fill_value for
     |      missing data in one of the inputs.
     |      
     |      Parameters
     |      ----------
     |      other : Series, DataFrame, or constant
     |      axis : {0, 1, 'index', 'columns'}
     |          For Series input, axis to match Series index on
     |      fill_value : None or float value, default None
     |          Fill missing (NaN) values with this value. If both DataFrame
     |          locations are missing, the result will be missing
     |      level : int or name
     |          Broadcast across a level, matching Index values on the
     |          passed MultiIndex level
     |      
     |      Notes
     |      -----
     |      Mismatched indices will be unioned together
     |      
     |      Returns
     |      -------
     |      result : DataFrame
     |      
     |      See also
     |      --------
     |      DataFrame.rfloordiv
     |  
     |  ge(self, other, axis='columns', level=None)
     |      Wrapper for flexible comparison methods ge
     |  
     |  get_value(self, index, col, takeable=False)
     |      Quickly retrieve single value at passed column and index
     |      
     |      Parameters
     |      ----------
     |      index : row label
     |      col : column label
     |      takeable : interpret the index/col as indexers, default False
     |      
     |      Returns
     |      -------
     |      value : scalar value
     |  
     |  gt(self, other, axis='columns', level=None)
     |      Wrapper for flexible comparison methods gt
     |  
     |  hist = hist_frame(data, column=None, by=None, grid=True, xlabelsize=None, xrot=None, ylabelsize=None, yrot=None, ax=None, sharex=False, sharey=False, figsize=None, layout=None, bins=10, **kwds)
     |      Draw histogram of the DataFrame's series using matplotlib / pylab.
     |      
     |      Parameters
     |      ----------
     |      data : DataFrame
     |      column : string or sequence
     |          If passed, will be used to limit data to a subset of columns
     |      by : object, optional
     |          If passed, then used to form histograms for separate groups
     |      grid : boolean, default True
     |          Whether to show axis grid lines
     |      xlabelsize : int, default None
     |          If specified changes the x-axis label size
     |      xrot : float, default None
     |          rotation of x axis labels
     |      ylabelsize : int, default None
     |          If specified changes the y-axis label size
     |      yrot : float, default None
     |          rotation of y axis labels
     |      ax : matplotlib axes object, default None
     |      sharex : boolean, default True if ax is None else False
     |          In case subplots=True, share x axis and set some x axis labels to
     |          invisible; defaults to True if ax is None otherwise False if an ax
     |          is passed in; Be aware, that passing in both an ax and sharex=True
     |          will alter all x axis labels for all subplots in a figure!
     |      sharey : boolean, default False
     |          In case subplots=True, share y axis and set some y axis labels to
     |          invisible
     |      figsize : tuple
     |          The size of the figure to create in inches by default
     |      layout: (optional) a tuple (rows, columns) for the layout of the histograms
     |      bins: integer, default 10
     |          Number of histogram bins to be used
     |      kwds : other plotting keyword arguments
     |          To be passed to hist function
     |  
     |  icol(self, i)
     |      DEPRECATED. Use ``.iloc[:, i]`` instead
     |  
     |  idxmax(self, axis=0, skipna=True)
     |      Return index of first occurrence of maximum over requested axis.
     |      NA/null values are excluded.
     |      
     |      Parameters
     |      ----------
     |      axis : {0 or 'index', 1 or 'columns'}, default 0
     |          0 or 'index' for row-wise, 1 or 'columns' for column-wise
     |      skipna : boolean, default True
     |          Exclude NA/null values. If an entire row/column is NA, the result
     |          will be first index.
     |      
     |      Returns
     |      -------
     |      idxmax : Series
     |      
     |      Notes
     |      -----
     |      This method is the DataFrame version of ``ndarray.argmax``.
     |      
     |      See Also
     |      --------
     |      Series.idxmax
     |  
     |  idxmin(self, axis=0, skipna=True)
     |      Return index of first occurrence of minimum over requested axis.
     |      NA/null values are excluded.
     |      
     |      Parameters
     |      ----------
     |      axis : {0 or 'index', 1 or 'columns'}, default 0
     |          0 or 'index' for row-wise, 1 or 'columns' for column-wise
     |      skipna : boolean, default True
     |          Exclude NA/null values. If an entire row/column is NA, the result
     |          will be NA
     |      
     |      Returns
     |      -------
     |      idxmin : Series
     |      
     |      Notes
     |      -----
     |      This method is the DataFrame version of ``ndarray.argmin``.
     |      
     |      See Also
     |      --------
     |      Series.idxmin
     |  
     |  iget_value(self, i, j)
     |      DEPRECATED. Use ``.iat[i, j]`` instead
     |  
     |  info(self, verbose=None, buf=None, max_cols=None, memory_usage=None, null_counts=None)
     |      Concise summary of a DataFrame.
     |      
     |      Parameters
     |      ----------
     |      verbose : {None, True, False}, optional
     |          Whether to print the full summary.
     |          None follows the `display.max_info_columns` setting.
     |          True or False overrides the `display.max_info_columns` setting.
     |      buf : writable buffer, defaults to sys.stdout
     |      max_cols : int, default None
     |          Determines whether full summary or short summary is printed.
     |          None follows the `display.max_info_columns` setting.
     |      memory_usage : boolean/string, default None
     |          Specifies whether total memory usage of the DataFrame
     |          elements (including index) should be displayed. None follows
     |          the `display.memory_usage` setting. True or False overrides
     |          the `display.memory_usage` setting. A value of 'deep' is equivalent
     |          of True, with deep introspection. Memory usage is shown in
     |          human-readable units (base-2 representation).
     |      null_counts : boolean, default None
     |          Whether to show the non-null counts
     |      
     |          - If None, then only show if the frame is smaller than
     |            max_info_rows and max_info_columns.
     |          - If True, always show counts.
     |          - If False, never show counts.
     |  
     |  insert(self, loc, column, value, allow_duplicates=False)
     |      Insert column into DataFrame at specified location.
     |      
     |      If `allow_duplicates` is False, raises Exception if column
     |      is already contained in the DataFrame.
     |      
     |      Parameters
     |      ----------
     |      loc : int
     |          Must have 0 <= loc <= len(columns)
     |      column : object
     |      value : scalar, Series, or array-like
     |  
     |  irow(self, i, copy=False)
     |      DEPRECATED. Use ``.iloc[i]`` instead
     |  
     |  isin(self, values)
     |      Return boolean DataFrame showing whether each element in the
     |      DataFrame is contained in values.
     |      
     |      Parameters
     |      ----------
     |      values : iterable, Series, DataFrame or dictionary
     |          The result will only be true at a location if all the
     |          labels match. If `values` is a Series, that's the index. If
     |          `values` is a dictionary, the keys must be the column names,
     |          which must match. If `values` is a DataFrame,
     |          then both the index and column labels must match.
     |      
     |      Returns
     |      -------
     |      
     |      DataFrame of booleans
     |      
     |      Examples
     |      --------
     |      When ``values`` is a list:
     |      
     |      >>> df = DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'f']})
     |      >>> df.isin([1, 3, 12, 'a'])
     |             A      B
     |      0   True   True
     |      1  False  False
     |      2   True  False
     |      
     |      When ``values`` is a dict:
     |      
     |      >>> df = DataFrame({'A': [1, 2, 3], 'B': [1, 4, 7]})
     |      >>> df.isin({'A': [1, 3], 'B': [4, 7, 12]})
     |             A      B
     |      0   True  False  # Note that B didn't match the 1 here.
     |      1  False   True
     |      2   True   True
     |      
     |      When ``values`` is a Series or DataFrame:
     |      
     |      >>> df = DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'f']})
     |      >>> other = DataFrame({'A': [1, 3, 3, 2], 'B': ['e', 'f', 'f', 'e']})
     |      >>> df.isin(other)
     |             A      B
     |      0   True  False
     |      1  False  False  # Column A in `other` has a 3, but not at index 1.
     |      2   True   True
     |  
     |  items = iteritems(self)
     |  
     |  iteritems(self)
     |      Iterator over (column name, Series) pairs.
     |      
     |      See also
     |      --------
     |      iterrows : Iterate over DataFrame rows as (index, Series) pairs.
     |      itertuples : Iterate over DataFrame rows as namedtuples of the values.
     |  
     |  iterrows(self)
     |      Iterate over DataFrame rows as (index, Series) pairs.
     |      
     |      Notes
     |      -----
     |      
     |      1. Because ``iterrows`` returns a Series for each row,
     |         it does **not** preserve dtypes across the rows (dtypes are
     |         preserved across columns for DataFrames). For example,
     |      
     |         >>> df = pd.DataFrame([[1, 1.5]], columns=['int', 'float'])
     |         >>> row = next(df.iterrows())[1]
     |         >>> row
     |         int      1.0
     |         float    1.5
     |         Name: 0, dtype: float64
     |         >>> print(row['int'].dtype)
     |         float64
     |         >>> print(df['int'].dtype)
     |         int64
     |      
     |         To preserve dtypes while iterating over the rows, it is better
     |         to use :meth:`itertuples` which returns namedtuples of the values
     |         and which is generally faster than ``iterrows``.
     |      
     |      2. You should **never modify** something you are iterating over.
     |         This is not guaranteed to work in all cases. Depending on the
     |         data types, the iterator returns a copy and not a view, and writing
     |         to it will have no effect.
     |      
     |      Returns
     |      -------
     |      it : generator
     |          A generator that iterates over the rows of the frame.
     |      
     |      See also
     |      --------
     |      itertuples : Iterate over DataFrame rows as namedtuples of the values.
     |      iteritems : Iterate over (column name, Series) pairs.
     |  
     |  itertuples(self, index=True, name='Pandas')
     |      Iterate over DataFrame rows as namedtuples, with index value as first
     |      element of the tuple.
     |      
     |      Parameters
     |      ----------
     |      index : boolean, default True
     |          If True, return the index as the first element of the tuple.
     |      name : string, default "Pandas"
     |          The name of the returned namedtuples or None to return regular
     |          tuples.
     |      
     |      Notes
     |      -----
     |      The column names will be renamed to positional names if they are
     |      invalid Python identifiers, repeated, or start with an underscore.
     |      With a large number of columns (>255), regular tuples are returned.
     |      
     |      See also
     |      --------
     |      iterrows : Iterate over DataFrame rows as (index, Series) pairs.
     |      iteritems : Iterate over (column name, Series) pairs.
     |      
     |      Examples
     |      --------
     |      
     |      >>> df = pd.DataFrame({'col1': [1, 2], 'col2': [0.1, 0.2]},
     |                            index=['a', 'b'])
     |      >>> df
     |         col1  col2
     |      a     1   0.1
     |      b     2   0.2
     |      >>> for row in df.itertuples():
     |      ...     print(row)
     |      ...
     |      Pandas(Index='a', col1=1, col2=0.10000000000000001)
     |      Pandas(Index='b', col1=2, col2=0.20000000000000001)
     |  
     |  join(self, other, on=None, how='left', lsuffix='', rsuffix='', sort=False)
     |      Join columns with other DataFrame either on index or on a key
     |      column. Efficiently Join multiple DataFrame objects by index at once by
     |      passing a list.
     |      
     |      Parameters
     |      ----------
     |      other : DataFrame, Series with name field set, or list of DataFrame
     |          Index should be similar to one of the columns in this one. If a
     |          Series is passed, its name attribute must be set, and that will be
     |          used as the column name in the resulting joined DataFrame
     |      on : column name, tuple/list of column names, or array-like
     |          Column(s) in the caller to join on the index in other,
     |          otherwise joins index-on-index. If multiples
     |          columns given, the passed DataFrame must have a MultiIndex. Can
     |          pass an array as the join key if not already contained in the
     |          calling DataFrame. Like an Excel VLOOKUP operation
     |      how : {'left', 'right', 'outer', 'inner'}, default: 'left'
     |          How to handle the operation of the two objects.
     |      
     |          * left: use calling frame's index (or column if on is specified)
     |          * right: use other frame's index
     |          * outer: form union of calling frame's index (or column if on is
     |              specified) with other frame's index
     |          * inner: form intersection of calling frame's index (or column if
     |              on is specified) with other frame's index
     |      lsuffix : string
     |          Suffix to use from left frame's overlapping columns
     |      rsuffix : string
     |          Suffix to use from right frame's overlapping columns
     |      sort : boolean, default False
     |          Order result DataFrame lexicographically by the join key. If False,
     |          preserves the index order of the calling (left) DataFrame
     |      
     |      Notes
     |      -----
     |      on, lsuffix, and rsuffix options are not supported when passing a list
     |      of DataFrame objects
     |      
     |      Examples
     |      --------
     |      >>> caller = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3', 'K4', 'K5'],
     |      ...                        'A': ['A0', 'A1', 'A2', 'A3', 'A4', 'A5']})
     |      
     |      >>> caller
     |          A key
     |      0  A0  K0
     |      1  A1  K1
     |      2  A2  K2
     |      3  A3  K3
     |      4  A4  K4
     |      5  A5  K5
     |      
     |      >>> other = pd.DataFrame({'key': ['K0', 'K1', 'K2'],
     |      ...                       'B': ['B0', 'B1', 'B2']})
     |      
     |      >>> other
     |          B key
     |      0  B0  K0
     |      1  B1  K1
     |      2  B2  K2
     |      
     |      Join DataFrames using their indexes.
     |      
     |      >>> caller.join(other, lsuffix='_caller', rsuffix='_other')
     |      
     |      >>>     A key_caller    B key_other
     |          0  A0         K0   B0        K0
     |          1  A1         K1   B1        K1
     |          2  A2         K2   B2        K2
     |          3  A3         K3  NaN       NaN
     |          4  A4         K4  NaN       NaN
     |          5  A5         K5  NaN       NaN
     |      
     |      
     |      If we want to join using the key columns, we need to set key to be
     |      the index in both caller and other. The joined DataFrame will have
     |      key as its index.
     |      
     |      >>> caller.set_index('key').join(other.set_index('key'))
     |      
     |      >>>      A    B
     |          key
     |          K0   A0   B0
     |          K1   A1   B1
     |          K2   A2   B2
     |          K3   A3  NaN
     |          K4   A4  NaN
     |          K5   A5  NaN
     |      
     |      Another option to join using the key columns is to use the on
     |      parameter. DataFrame.join always uses other's index but we can use any
     |      column in the caller. This method preserves the original caller's
     |      index in the result.
     |      
     |      >>> caller.join(other.set_index('key'), on='key')
     |      
     |      >>>     A key    B
     |          0  A0  K0   B0
     |          1  A1  K1   B1
     |          2  A2  K2   B2
     |          3  A3  K3  NaN
     |          4  A4  K4  NaN
     |          5  A5  K5  NaN
     |      
     |      
     |      See also
     |      --------
     |      DataFrame.merge : For column(s)-on-columns(s) operations
     |      
     |      Returns
     |      -------
     |      joined : DataFrame
     |  
     |  kurt(self, axis=None, skipna=None, level=None, numeric_only=None, **kwargs)
     |      Return unbiased kurtosis over requested axis using Fisher's definition of
     |      kurtosis (kurtosis of normal == 0.0). Normalized by N-1
     |      
     |      
     |      Parameters
     |      ----------
     |      axis : {index (0), columns (1)}
     |      skipna : boolean, default True
     |          Exclude NA/null values. If an entire row/column is NA, the result
     |          will be NA
     |      level : int or level name, default None
     |          If the axis is a MultiIndex (hierarchical), count along a
     |          particular level, collapsing into a Series
     |      numeric_only : boolean, default None
     |          Include only float, int, boolean columns. If None, will attempt to use
     |          everything, then use only numeric data. Not implemented for Series.
     |      
     |      Returns
     |      -------
     |      kurt : Series or DataFrame (if level specified)
     |  
     |  kurtosis = kurt(self, axis=None, skipna=None, level=None, numeric_only=None, **kwargs)
     |  
     |  last_valid_index(self)
     |      Return label for last non-NA/null value
     |  
     |  le(self, other, axis='columns', level=None)
     |      Wrapper for flexible comparison methods le
     |  
     |  lookup(self, row_labels, col_labels)
     |      Label-based "fancy indexing" function for DataFrame.
     |      Given equal-length arrays of row and column labels, return an
     |      array of the values corresponding to each (row, col) pair.
     |      
     |      Parameters
     |      ----------
     |      row_labels : sequence
     |          The row labels to use for lookup
     |      col_labels : sequence
     |          The column labels to use for lookup
     |      
     |      Notes
     |      -----
     |      Akin to::
     |      
     |          result = []
     |          for row, col in zip(row_labels, col_labels):
     |              result.append(df.get_value(row, col))
     |      
     |      Examples
     |      --------
     |      values : ndarray
     |          The found values
     |  
     |  lt(self, other, axis='columns', level=None)
     |      Wrapper for flexible comparison methods lt
     |  
     |  mad(self, axis=None, skipna=None, level=None)
     |      Return the mean absolute deviation of the values for the requested axis
     |      
     |      Parameters
     |      ----------
     |      axis : {index (0), columns (1)}
     |      skipna : boolean, default True
     |          Exclude NA/null values. If an entire row/column is NA, the result
     |          will be NA
     |      level : int or level name, default None
     |          If the axis is a MultiIndex (hierarchical), count along a
     |          particular level, collapsing into a Series
     |      numeric_only : boolean, default None
     |          Include only float, int, boolean columns. If None, will attempt to use
     |          everything, then use only numeric data. Not implemented for Series.
     |      
     |      Returns
     |      -------
     |      mad : Series or DataFrame (if level specified)
     |  
     |  max(self, axis=None, skipna=None, level=None, numeric_only=None, **kwargs)
     |      This method returns the maximum of the values in the object.
     |                  If you want the *index* of the maximum, use ``idxmax``. This is
     |                  the equivalent of the ``numpy.ndarray`` method ``argmax``.
     |      
     |      Parameters
     |      ----------
     |      axis : {index (0), columns (1)}
     |      skipna : boolean, default True
     |          Exclude NA/null values. If an entire row/column is NA, the result
     |          will be NA
     |      level : int or level name, default None
     |          If the axis is a MultiIndex (hierarchical), count along a
     |          particular level, collapsing into a Series
     |      numeric_only : boolean, default None
     |          Include only float, int, boolean columns. If None, will attempt to use
     |          everything, then use only numeric data. Not implemented for Series.
     |      
     |      Returns
     |      -------
     |      max : Series or DataFrame (if level specified)
     |  
     |  mean(self, axis=None, skipna=None, level=None, numeric_only=None, **kwargs)
     |      Return the mean of the values for the requested axis
     |      
     |      Parameters
     |      ----------
     |      axis : {index (0), columns (1)}
     |      skipna : boolean, default True
     |          Exclude NA/null values. If an entire row/column is NA, the result
     |          will be NA
     |      level : int or level name, default None
     |          If the axis is a MultiIndex (hierarchical), count along a
     |          particular level, collapsing into a Series
     |      numeric_only : boolean, default None
     |          Include only float, int, boolean columns. If None, will attempt to use
     |          everything, then use only numeric data. Not implemented for Series.
     |      
     |      Returns
     |      -------
     |      mean : Series or DataFrame (if level specified)
     |  
     |  median(self, axis=None, skipna=None, level=None, numeric_only=None, **kwargs)
     |      Return the median of the values for the requested axis
     |      
     |      Parameters
     |      ----------
     |      axis : {index (0), columns (1)}
     |      skipna : boolean, default True
     |          Exclude NA/null values. If an entire row/column is NA, the result
     |          will be NA
     |      level : int or level name, default None
     |          If the axis is a MultiIndex (hierarchical), count along a
     |          particular level, collapsing into a Series
     |      numeric_only : boolean, default None
     |          Include only float, int, boolean columns. If None, will attempt to use
     |          everything, then use only numeric data. Not implemented for Series.
     |      
     |      Returns
     |      -------
     |      median : Series or DataFrame (if level specified)
     |  
     |  memory_usage(self, index=True, deep=False)
     |      Memory usage of DataFrame columns.
     |      
     |      Parameters
     |      ----------
     |      index : bool
     |          Specifies whether to include memory usage of DataFrame's
     |          index in returned Series. If `index=True` (default is False)
     |          the first index of the Series is `Index`.
     |      deep : bool
     |          Introspect the data deeply, interrogate
     |          `object` dtypes for system-level memory consumption
     |      
     |      Returns
     |      -------
     |      sizes : Series
     |          A series with column names as index and memory usage of
     |          columns with units of bytes.
     |      
     |      Notes
     |      -----
     |      Memory usage does not include memory consumed by elements that
     |      are not components of the array if deep=False
     |      
     |      See Also
     |      --------
     |      numpy.ndarray.nbytes
     |  
     |  merge(self, right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, sort=False, suffixes=('_x', '_y'), copy=True, indicator=False)
     |      Merge DataFrame objects by performing a database-style join operation by
     |      columns or indexes.
     |      
     |      If joining columns on columns, the DataFrame indexes *will be
     |      ignored*. Otherwise if joining indexes on indexes or indexes on a column or
     |      columns, the index will be passed on.
     |      
     |      Parameters
     |      ----------
     |      right : DataFrame
     |      how : {'left', 'right', 'outer', 'inner'}, default 'inner'
     |          * left: use only keys from left frame (SQL: left outer join)
     |          * right: use only keys from right frame (SQL: right outer join)
     |          * outer: use union of keys from both frames (SQL: full outer join)
     |          * inner: use intersection of keys from both frames (SQL: inner join)
     |      on : label or list
     |          Field names to join on. Must be found in both DataFrames. If on is
     |          None and not merging on indexes, then it merges on the intersection of
     |          the columns by default.
     |      left_on : label or list, or array-like
     |          Field names to join on in left DataFrame. Can be a vector or list of
     |          vectors of the length of the DataFrame to use a particular vector as
     |          the join key instead of columns
     |      right_on : label or list, or array-like
     |          Field names to join on in right DataFrame or vector/list of vectors per
     |          left_on docs
     |      left_index : boolean, default False
     |          Use the index from the left DataFrame as the join key(s). If it is a
     |          MultiIndex, the number of keys in the other DataFrame (either the index
     |          or a number of columns) must match the number of levels
     |      right_index : boolean, default False
     |          Use the index from the right DataFrame as the join key. Same caveats as
     |          left_index
     |      sort : boolean, default False
     |          Sort the join keys lexicographically in the result DataFrame
     |      suffixes : 2-length sequence (tuple, list, ...)
     |          Suffix to apply to overlapping column names in the left and right
     |          side, respectively
     |      copy : boolean, default True
     |          If False, do not copy data unnecessarily
     |      indicator : boolean or string, default False
     |          If True, adds a column to output DataFrame called "_merge" with
     |          information on the source of each row.
     |          If string, column with information on source of each row will be added to
     |          output DataFrame, and column will be named value of string.
     |          Information column is Categorical-type and takes on a value of "left_only"
     |          for observations whose merge key only appears in 'left' DataFrame,
     |          "right_only" for observations whose merge key only appears in 'right'
     |          DataFrame, and "both" if the observation's merge key is found in both.
     |      
     |          .. versionadded:: 0.17.0
     |      
     |      Examples
     |      --------
     |      
     |      >>> A              >>> B
     |          lkey value         rkey value
     |      0   foo  1         0   foo  5
     |      1   bar  2         1   bar  6
     |      2   baz  3         2   qux  7
     |      3   foo  4         3   bar  8
     |      
     |      >>> A.merge(B, left_on='lkey', right_on='rkey', how='outer')
     |         lkey  value_x  rkey  value_y
     |      0  foo   1        foo   5
     |      1  foo   4        foo   5
     |      2  bar   2        bar   6
     |      3  bar   2        bar   8
     |      4  baz   3        NaN   NaN
     |      5  NaN   NaN      qux   7
     |      
     |      Returns
     |      -------
     |      merged : DataFrame
     |          The output type will the be same as 'left', if it is a subclass
     |          of DataFrame.
     |      
     |      See also
     |      --------
     |      merge_ordered
     |      merge_asof
     |  
     |  min(self, axis=None, skipna=None, level=None, numeric_only=None, **kwargs)
     |      This method returns the minimum of the values in the object.
     |                  If you want the *index* of the minimum, use ``idxmin``. This is
     |                  the equivalent of the ``numpy.ndarray`` method ``argmin``.
     |      
     |      Parameters
     |      ----------
     |      axis : {index (0), columns (1)}
     |      skipna : boolean, default True
     |          Exclude NA/null values. If an entire row/column is NA, the result
     |          will be NA
     |      level : int or level name, default None
     |          If the axis is a MultiIndex (hierarchical), count along a
     |          particular level, collapsing into a Series
     |      numeric_only : boolean, default None
     |          Include only float, int, boolean columns. If None, will attempt to use
     |          everything, then use only numeric data. Not implemented for Series.
     |      
     |      Returns
     |      -------
     |      min : Series or DataFrame (if level specified)
     |  
     |  mod(self, other, axis='columns', level=None, fill_value=None)
     |      Modulo of dataframe and other, element-wise (binary operator `mod`).
     |      
     |      Equivalent to ``dataframe % other``, but with support to substitute a fill_value for
     |      missing data in one of the inputs.
     |      
     |      Parameters
     |      ----------
     |      other : Series, DataFrame, or constant
     |      axis : {0, 1, 'index', 'columns'}
     |          For Series input, axis to match Series index on
     |      fill_value : None or float value, default None
     |          Fill missing (NaN) values with this value. If both DataFrame
     |          locations are missing, the result will be missing
     |      level : int or name
     |          Broadcast across a level, matching Index values on the
     |          passed MultiIndex level
     |      
     |      Notes
     |      -----
     |      Mismatched indices will be unioned together
     |      
     |      Returns
     |      -------
     |      result : DataFrame
     |      
     |      See also
     |      --------
     |      DataFrame.rmod
     |  
     |  mode(self, axis=0, numeric_only=False)
     |      Gets the mode(s) of each element along the axis selected. Empty if
     |      nothing has 2+ occurrences. Adds a row for each mode per label, fills
     |      in gaps with nan.
     |      
     |      Note that there could be multiple values returned for the selected
     |      axis (when more than one item share the maximum frequency), which is
     |      the reason why a dataframe is returned. If you want to impute missing
     |      values with the mode in a dataframe ``df``, you can just do this:
     |      ``df.fillna(df.mode().iloc[0])``
     |      
     |      Parameters
     |      ----------
     |      axis : {0 or 'index', 1 or 'columns'}, default 0
     |          * 0 or 'index' : get mode of each column
     |          * 1 or 'columns' : get mode of each row
     |      numeric_only : boolean, default False
     |          if True, only apply to numeric columns
     |      
     |      Returns
     |      -------
     |      modes : DataFrame (sorted)
     |      
     |      Examples
     |      --------
     |      >>> df = pd.DataFrame({'A': [1, 2, 1, 2, 1, 2, 3]})
     |      >>> df.mode()
     |         A
     |      0  1
     |      1  2
     |  
     |  mul(self, other, axis='columns', level=None, fill_value=None)
     |      Multiplication of dataframe and other, element-wise (binary operator `mul`).
     |      
     |      Equivalent to ``dataframe * other``, but with support to substitute a fill_value for
     |      missing data in one of the inputs.
     |      
     |      Parameters
     |      ----------
     |      other : Series, DataFrame, or constant
     |      axis : {0, 1, 'index', 'columns'}
     |          For Series input, axis to match Series index on
     |      fill_value : None or float value, default None
     |          Fill missing (NaN) values with this value. If both DataFrame
     |          locations are missing, the result will be missing
     |      level : int or name
     |          Broadcast across a level, matching Index values on the
     |          passed MultiIndex level
     |      
     |      Notes
     |      -----
     |      Mismatched indices will be unioned together
     |      
     |      Returns
     |      -------
     |      result : DataFrame
     |      
     |      See also
     |      --------
     |      DataFrame.rmul
     |  
     |  multiply = mul(self, other, axis='columns', level=None, fill_value=None)
     |  
     |  ne(self, other, axis='columns', level=None)
     |      Wrapper for flexible comparison methods ne
     |  
     |  nlargest(self, n, columns, keep='first')
     |      Get the rows of a DataFrame sorted by the `n` largest
     |      values of `columns`.
     |      
     |      .. versionadded:: 0.17.0
     |      
     |      Parameters
     |      ----------
     |      n : int
     |          Number of items to retrieve
     |      columns : list or str
     |          Column name or names to order by
     |      keep : {'first', 'last', False}, default 'first'
     |          Where there are duplicate values:
     |          - ``first`` : take the first occurrence.
     |          - ``last`` : take the last occurrence.
     |      
     |      Returns
     |      -------
     |      DataFrame
     |      
     |      Examples
     |      --------
     |      >>> df = DataFrame({'a': [1, 10, 8, 11, -1],
     |      ...                 'b': list('abdce'),
     |      ...                 'c': [1.0, 2.0, np.nan, 3.0, 4.0]})
     |      >>> df.nlargest(3, 'a')
     |          a  b   c
     |      3  11  c   3
     |      1  10  b   2
     |      2   8  d NaN
     |  
     |  nsmallest(self, n, columns, keep='first')
     |      Get the rows of a DataFrame sorted by the `n` smallest
     |      values of `columns`.
     |      
     |      .. versionadded:: 0.17.0
     |      
     |      Parameters
     |      ----------
     |      n : int
     |          Number of items to retrieve
     |      columns : list or str
     |          Column name or names to order by
     |      keep : {'first', 'last', False}, default 'first'
     |          Where there are duplicate values:
     |          - ``first`` : take the first occurrence.
     |          - ``last`` : take the last occurrence.
     |      
     |      Returns
     |      -------
     |      DataFrame
     |      
     |      Examples
     |      --------
     |      >>> df = DataFrame({'a': [1, 10, 8, 11, -1],
     |      ...                 'b': list('abdce'),
     |      ...                 'c': [1.0, 2.0, np.nan, 3.0, 4.0]})
     |      >>> df.nsmallest(3, 'a')
     |         a  b   c
     |      4 -1  e   4
     |      0  1  a   1
     |      2  8  d NaN
     |  
     |  pivot(self, index=None, columns=None, values=None)
     |      Reshape data (produce a "pivot" table) based on column values. Uses
     |      unique values from index / columns to form axes of the resulting
     |      DataFrame.
     |      
     |      Parameters
     |      ----------
     |      index : string or object, optional
     |          Column name to use to make new frame's index. If None, uses
     |          existing index.
     |      columns : string or object
     |          Column name to use to make new frame's columns
     |      values : string or object, optional
     |          Column name to use for populating new frame's values. If not
     |          specified, all remaining columns will be used and the result will
     |          have hierarchically indexed columns
     |      
     |      Returns
     |      -------
     |      pivoted : DataFrame
     |      
     |      See also
     |      --------
     |      DataFrame.pivot_table : generalization of pivot that can handle
     |          duplicate values for one index/column pair
     |      DataFrame.unstack : pivot based on the index values instead of a
     |          column
     |      
     |      Notes
     |      -----
     |      For finer-tuned control, see hierarchical indexing documentation along
     |      with the related stack/unstack methods
     |      
     |      Examples
     |      --------
     |      
     |      >>> df = pd.DataFrame({'foo': ['one','one','one','two','two','two'],
     |                             'bar': ['A', 'B', 'C', 'A', 'B', 'C'],
     |                             'baz': [1, 2, 3, 4, 5, 6]})
     |      >>> df
     |          foo   bar  baz
     |      0   one   A    1
     |      1   one   B    2
     |      2   one   C    3
     |      3   two   A    4
     |      4   two   B    5
     |      5   two   C    6
     |      
     |      >>> df.pivot(index='foo', columns='bar', values='baz')
     |           A   B   C
     |      one  1   2   3
     |      two  4   5   6
     |      
     |      >>> df.pivot(index='foo', columns='bar')['baz']
     |           A   B   C
     |      one  1   2   3
     |      two  4   5   6
     |  
     |  pivot_table(data, values=None, index=None, columns=None, aggfunc='mean', fill_value=None, margins=False, dropna=True, margins_name='All')
     |      Create a spreadsheet-style pivot table as a DataFrame. The levels in the
     |      pivot table will be stored in MultiIndex objects (hierarchical indexes) on
     |      the index and columns of the result DataFrame
     |      
     |      Parameters
     |      ----------
     |      data : DataFrame
     |      values : column to aggregate, optional
     |      index : column, Grouper, array, or list of the previous
     |          If an array is passed, it must be the same length as the data. The list
     |          can contain any of the other types (except list).
     |          Keys to group by on the pivot table index.  If an array is passed, it
     |          is being used as the same manner as column values.
     |      columns : column, Grouper, array, or list of the previous
     |          If an array is passed, it must be the same length as the data. The list
     |          can contain any of the other types (except list).
     |          Keys to group by on the pivot table column.  If an array is passed, it
     |          is being used as the same manner as column values.
     |      aggfunc : function or list of functions, default numpy.mean
     |          If list of functions passed, the resulting pivot table will have
     |          hierarchical columns whose top level are the function names (inferred
     |          from the function objects themselves)
     |      fill_value : scalar, default None
     |          Value to replace missing values with
     |      margins : boolean, default False
     |          Add all row / columns (e.g. for subtotal / grand totals)
     |      dropna : boolean, default True
     |          Do not include columns whose entries are all NaN
     |      margins_name : string, default 'All'
     |          Name of the row / column that will contain the totals
     |          when margins is True.
     |      
     |      Examples
     |      --------
     |      >>> df
     |         A   B   C      D
     |      0  foo one small  1
     |      1  foo one large  2
     |      2  foo one large  2
     |      3  foo two small  3
     |      4  foo two small  3
     |      5  bar one large  4
     |      6  bar one small  5
     |      7  bar two small  6
     |      8  bar two large  7
     |      
     |      >>> table = pivot_table(df, values='D', index=['A', 'B'],
     |      ...                     columns=['C'], aggfunc=np.sum)
     |      >>> table
     |                small  large
     |      foo  one  1      4
     |           two  6      NaN
     |      bar  one  5      4
     |           two  6      7
     |      
     |      Returns
     |      -------
     |      table : DataFrame
     |  
     |  pow(self, other, axis='columns', level=None, fill_value=None)
     |      Exponential power of dataframe and other, element-wise (binary operator `pow`).
     |      
     |      Equivalent to ``dataframe ** other``, but with support to substitute a fill_value for
     |      missing data in one of the inputs.
     |      
     |      Parameters
     |      ----------
     |      other : Series, DataFrame, or constant
     |      axis : {0, 1, 'index', 'columns'}
     |          For Series input, axis to match Series index on
     |      fill_value : None or float value, default None
     |          Fill missing (NaN) values with this value. If both DataFrame
     |          locations are missing, the result will be missing
     |      level : int or name
     |          Broadcast across a level, matching Index values on the
     |          passed MultiIndex level
     |      
     |      Notes
     |      -----
     |      Mismatched indices will be unioned together
     |      
     |      Returns
     |      -------
     |      result : DataFrame
     |      
     |      See also
     |      --------
     |      DataFrame.rpow
     |  
     |  prod(self, axis=None, skipna=None, level=None, numeric_only=None, **kwargs)
     |      Return the product of the values for the requested axis
     |      
     |      Parameters
     |      ----------
     |      axis : {index (0), columns (1)}
     |      skipna : boolean, default True
     |          Exclude NA/null values. If an entire row/column is NA, the result
     |          will be NA
     |      level : int or level name, default None
     |          If the axis is a MultiIndex (hierarchical), count along a
     |          particular level, collapsing into a Series
     |      numeric_only : boolean, default None
     |          Include only float, int, boolean columns. If None, will attempt to use
     |          everything, then use only numeric data. Not implemented for Series.
     |      
     |      Returns
     |      -------
     |      prod : Series or DataFrame (if level specified)
     |  
     |  product = prod(self, axis=None, skipna=None, level=None, numeric_only=None, **kwargs)
     |  
     |  quantile(self, q=0.5, axis=0, numeric_only=True, interpolation='linear')
     |      Return values at the given quantile over requested axis, a la
     |      numpy.percentile.
     |      
     |      Parameters
     |      ----------
     |      q : float or array-like, default 0.5 (50% quantile)
     |          0 <= q <= 1, the quantile(s) to compute
     |      axis : {0, 1, 'index', 'columns'} (default 0)
     |          0 or 'index' for row-wise, 1 or 'columns' for column-wise
     |      interpolation : {'linear', 'lower', 'higher', 'midpoint', 'nearest'}
     |          .. versionadded:: 0.18.0
     |      
     |          This optional parameter specifies the interpolation method to use,
     |          when the desired quantile lies between two data points `i` and `j`:
     |      
     |          * linear: `i + (j - i) * fraction`, where `fraction` is the
     |            fractional part of the index surrounded by `i` and `j`.
     |          * lower: `i`.
     |          * higher: `j`.
     |          * nearest: `i` or `j` whichever is nearest.
     |          * midpoint: (`i` + `j`) / 2.
     |      
     |      Returns
     |      -------
     |      quantiles : Series or DataFrame
     |      
     |          - If ``q`` is an array, a DataFrame will be returned where the
     |            index is ``q``, the columns are the columns of self, and the
     |            values are the quantiles.
     |          - If ``q`` is a float, a Series will be returned where the
     |            index is the columns of self and the values are the quantiles.
     |      
     |      Examples
     |      --------
     |      
     |      >>> df = DataFrame(np.array([[1, 1], [2, 10], [3, 100], [4, 100]]),
     |                         columns=['a', 'b'])
     |      >>> df.quantile(.1)
     |      a    1.3
     |      b    3.7
     |      dtype: float64
     |      >>> df.quantile([.1, .5])
     |             a     b
     |      0.1  1.3   3.7
     |      0.5  2.5  55.0
     |  
     |  query(self, expr, inplace=False, **kwargs)
     |      Query the columns of a frame with a boolean expression.
     |      
     |      .. versionadded:: 0.13
     |      
     |      Parameters
     |      ----------
     |      expr : string
     |          The query string to evaluate.  You can refer to variables
     |          in the environment by prefixing them with an '@' character like
     |          ``@a + b``.
     |      inplace : bool
     |          Whether the query should modify the data in place or return
     |          a modified copy
     |      
     |          .. versionadded:: 0.18.0
     |      
     |      kwargs : dict
     |          See the documentation for :func:`pandas.eval` for complete details
     |          on the keyword arguments accepted by :meth:`DataFrame.query`.
     |      
     |      Returns
     |      -------
     |      q : DataFrame
     |      
     |      Notes
     |      -----
     |      The result of the evaluation of this expression is first passed to
     |      :attr:`DataFrame.loc` and if that fails because of a
     |      multidimensional key (e.g., a DataFrame) then the result will be passed
     |      to :meth:`DataFrame.__getitem__`.
     |      
     |      This method uses the top-level :func:`pandas.eval` function to
     |      evaluate the passed query.
     |      
     |      The :meth:`~pandas.DataFrame.query` method uses a slightly
     |      modified Python syntax by default. For example, the ``&`` and ``|``
     |      (bitwise) operators have the precedence of their boolean cousins,
     |      :keyword:`and` and :keyword:`or`. This *is* syntactically valid Python,
     |      however the semantics are different.
     |      
     |      You can change the semantics of the expression by passing the keyword
     |      argument ``parser='python'``. This enforces the same semantics as
     |      evaluation in Python space. Likewise, you can pass ``engine='python'``
     |      to evaluate an expression using Python itself as a backend. This is not
     |      recommended as it is inefficient compared to using ``numexpr`` as the
     |      engine.
     |      
     |      The :attr:`DataFrame.index` and
     |      :attr:`DataFrame.columns` attributes of the
     |      :class:`~pandas.DataFrame` instance are placed in the query namespace
     |      by default, which allows you to treat both the index and columns of the
     |      frame as a column in the frame.
     |      The identifier ``index`` is used for the frame index; you can also
     |      use the name of the index to identify it in a query.
     |      
     |      For further details and examples see the ``query`` documentation in
     |      :ref:`indexing <indexing.query>`.
     |      
     |      See Also
     |      --------
     |      pandas.eval
     |      DataFrame.eval
     |      
     |      Examples
     |      --------
     |      >>> from numpy.random import randn
     |      >>> from pandas import DataFrame
     |      >>> df = DataFrame(randn(10, 2), columns=list('ab'))
     |      >>> df.query('a > b')
     |      >>> df[df.a > df.b]  # same result as the previous expression
     |  
     |  radd(self, other, axis='columns', level=None, fill_value=None)
     |      Addition of dataframe and other, element-wise (binary operator `radd`).
     |      
     |      Equivalent to ``other + dataframe``, but with support to substitute a fill_value for
     |      missing data in one of the inputs.
     |      
     |      Parameters
     |      ----------
     |      other : Series, DataFrame, or constant
     |      axis : {0, 1, 'index', 'columns'}
     |          For Series input, axis to match Series index on
     |      fill_value : None or float value, default None
     |          Fill missing (NaN) values with this value. If both DataFrame
     |          locations are missing, the result will be missing
     |      level : int or name
     |          Broadcast across a level, matching Index values on the
     |          passed MultiIndex level
     |      
     |      Notes
     |      -----
     |      Mismatched indices will be unioned together
     |      
     |      Returns
     |      -------
     |      result : DataFrame
     |      
     |      See also
     |      --------
     |      DataFrame.add
     |  
     |  rdiv = rtruediv(self, other, axis='columns', level=None, fill_value=None)
     |  
     |  reindex(self, index=None, columns=None, **kwargs)
     |      Conform DataFrame to new index with optional filling logic, placing
     |      NA/NaN in locations having no value in the previous index. A new object
     |      is produced unless the new index is equivalent to the current one and
     |      copy=False
     |      
     |      Parameters
     |      ----------
     |      index, columns : array-like, optional (can be specified in order, or as
     |          keywords)
     |          New labels / index to conform to. Preferably an Index object to
     |          avoid duplicating data
     |      method : {None, 'backfill'/'bfill', 'pad'/'ffill', 'nearest'}, optional
     |          method to use for filling holes in reindexed DataFrame.
     |          Please note: this is only  applicable to DataFrames/Series with a
     |          monotonically increasing/decreasing index.
     |      
     |          * default: don't fill gaps
     |          * pad / ffill: propagate last valid observation forward to next
     |            valid
     |          * backfill / bfill: use next valid observation to fill gap
     |          * nearest: use nearest valid observations to fill gap
     |      
     |      copy : boolean, default True
     |          Return a new object, even if the passed indexes are the same
     |      level : int or name
     |          Broadcast across a level, matching Index values on the
     |          passed MultiIndex level
     |      fill_value : scalar, default np.NaN
     |          Value to use for missing values. Defaults to NaN, but can be any
     |          "compatible" value
     |      limit : int, default None
     |          Maximum number of consecutive elements to forward or backward fill
     |      tolerance : optional
     |          Maximum distance between original and new labels for inexact
     |          matches. The values of the index at the matching locations most
     |          satisfy the equation ``abs(index[indexer] - target) <= tolerance``.
     |      
     |          .. versionadded:: 0.17.0
     |      
     |      Examples
     |      --------
     |      
     |      Create a dataframe with some fictional data.
     |      
     |      >>> index = ['Firefox', 'Chrome', 'Safari', 'IE10', 'Konqueror']
     |      >>> df = pd.DataFrame({
     |      ...      'http_status': [200,200,404,404,301],
     |      ...      'response_time': [0.04, 0.02, 0.07, 0.08, 1.0]},
     |      ...       index=index)
     |      >>> df
     |                  http_status  response_time
     |      Firefox            200           0.04
     |      Chrome             200           0.02
     |      Safari             404           0.07
     |      IE10               404           0.08
     |      Konqueror          301           1.00
     |      
     |      Create a new index and reindex the dataframe. By default
     |      values in the new index that do not have corresponding
     |      records in the dataframe are assigned ``NaN``.
     |      
     |      >>> new_index= ['Safari', 'Iceweasel', 'Comodo Dragon', 'IE10',
     |      ...             'Chrome']
     |      >>> df.reindex(new_index)
     |                     http_status  response_time
     |      Safari                 404           0.07
     |      Iceweasel              NaN            NaN
     |      Comodo Dragon          NaN            NaN
     |      IE10                   404           0.08
     |      Chrome                 200           0.02
     |      
     |      We can fill in the missing values by passing a value to
     |      the keyword ``fill_value``. Because the index is not monotonically
     |      increasing or decreasing, we cannot use arguments to the keyword
     |      ``method`` to fill the ``NaN`` values.
     |      
     |      >>> df.reindex(new_index, fill_value=0)
     |                     http_status  response_time
     |      Safari                 404           0.07
     |      Iceweasel                0           0.00
     |      Comodo Dragon            0           0.00
     |      IE10                   404           0.08
     |      Chrome                 200           0.02
     |      
     |      >>> df.reindex(new_index, fill_value='missing')
     |                    http_status response_time
     |      Safari                404          0.07
     |      Iceweasel         missing       missing
     |      Comodo Dragon     missing       missing
     |      IE10                  404          0.08
     |      Chrome                200          0.02
     |      
     |      To further illustrate the filling functionality in
     |      ``reindex``, we will create a dataframe with a
     |      monotonically increasing index (for example, a sequence
     |      of dates).
     |      
     |      >>> date_index = pd.date_range('1/1/2010', periods=6, freq='D')
     |      >>> df2 = pd.DataFrame({"prices": [100, 101, np.nan, 100, 89, 88]},
     |      ...                    index=date_index)
     |      >>> df2
     |                  prices
     |      2010-01-01     100
     |      2010-01-02     101
     |      2010-01-03     NaN
     |      2010-01-04     100
     |      2010-01-05      89
     |      2010-01-06      88
     |      
     |      Suppose we decide to expand the dataframe to cover a wider
     |      date range.
     |      
     |      >>> date_index2 = pd.date_range('12/29/2009', periods=10, freq='D')
     |      >>> df2.reindex(date_index2)
     |                  prices
     |      2009-12-29     NaN
     |      2009-12-30     NaN
     |      2009-12-31     NaN
     |      2010-01-01     100
     |      2010-01-02     101
     |      2010-01-03     NaN
     |      2010-01-04     100
     |      2010-01-05      89
     |      2010-01-06      88
     |      2010-01-07     NaN
     |      
     |      The index entries that did not have a value in the original data frame
     |      (for example, '2009-12-29') are by default filled with ``NaN``.
     |      If desired, we can fill in the missing values using one of several
     |      options.
     |      
     |      For example, to backpropagate the last valid value to fill the ``NaN``
     |      values, pass ``bfill`` as an argument to the ``method`` keyword.
     |      
     |      >>> df2.reindex(date_index2, method='bfill')
     |                  prices
     |      2009-12-29     100
     |      2009-12-30     100
     |      2009-12-31     100
     |      2010-01-01     100
     |      2010-01-02     101
     |      2010-01-03     NaN
     |      2010-01-04     100
     |      2010-01-05      89
     |      2010-01-06      88
     |      2010-01-07     NaN
     |      
     |      Please note that the ``NaN`` value present in the original dataframe
     |      (at index value 2010-01-03) will not be filled by any of the
     |      value propagation schemes. This is because filling while reindexing
     |      does not look at dataframe values, but only compares the original and
     |      desired indexes. If you do want to fill in the ``NaN`` values present
     |      in the original dataframe, use the ``fillna()`` method.
     |      
     |      Returns
     |      -------
     |      reindexed : DataFrame
     |  
     |  reindex_axis(self, labels, axis=0, method=None, level=None, copy=True, limit=None, fill_value=nan)
     |      Conform input object to new index with optional
     |      filling logic, placing NA/NaN in locations having no value in the
     |      previous index. A new object is produced unless the new index is
     |      equivalent to the current one and copy=False
     |      
     |      Parameters
     |      ----------
     |      labels : array-like
     |          New labels / index to conform to. Preferably an Index object to
     |          avoid duplicating data
     |      axis : {0 or 'index', 1 or 'columns'}
     |      method : {None, 'backfill'/'bfill', 'pad'/'ffill', 'nearest'}, optional
     |          Method to use for filling holes in reindexed DataFrame:
     |      
     |          * default: don't fill gaps
     |          * pad / ffill: propagate last valid observation forward to next
     |            valid
     |          * backfill / bfill: use next valid observation to fill gap
     |          * nearest: use nearest valid observations to fill gap
     |      
     |      copy : boolean, default True
     |          Return a new object, even if the passed indexes are the same
     |      level : int or name
     |          Broadcast across a level, matching Index values on the
     |          passed MultiIndex level
     |      limit : int, default None
     |          Maximum number of consecutive elements to forward or backward fill
     |      tolerance : optional
     |          Maximum distance between original and new labels for inexact
     |          matches. The values of the index at the matching locations most
     |          satisfy the equation ``abs(index[indexer] - target) <= tolerance``.
     |      
     |          .. versionadded:: 0.17.0
     |      
     |      Examples
     |      --------
     |      >>> df.reindex_axis(['A', 'B', 'C'], axis=1)
     |      
     |      See Also
     |      --------
     |      reindex, reindex_like
     |      
     |      Returns
     |      -------
     |      reindexed : DataFrame
     |  
     |  rename(self, index=None, columns=None, **kwargs)
     |      Alter axes input function or functions. Function / dict values must be
     |      unique (1-to-1). Labels not contained in a dict / Series will be left
     |      as-is. Extra labels listed don't throw an error. Alternatively, change
     |      ``Series.name`` with a scalar value (Series only).
     |      
     |      Parameters
     |      ----------
     |      index, columns : scalar, list-like, dict-like or function, optional
     |          Scalar or list-like will alter the ``Series.name`` attribute,
     |          and raise on DataFrame or Panel.
     |          dict-like or functions are transformations to apply to
     |          that axis' values
     |      copy : boolean, default True
     |          Also copy underlying data
     |      inplace : boolean, default False
     |          Whether to return a new DataFrame. If True then value of copy is
     |          ignored.
     |      
     |      Returns
     |      -------
     |      renamed : DataFrame (new object)
     |      
     |      See Also
     |      --------
     |      pandas.NDFrame.rename_axis
     |      
     |      Examples
     |      --------
     |      >>> s = pd.Series([1, 2, 3])
     |      >>> s
     |      0    1
     |      1    2
     |      2    3
     |      dtype: int64
     |      >>> s.rename("my_name") # scalar, changes Series.name
     |      0    1
     |      1    2
     |      2    3
     |      Name: my_name, dtype: int64
     |      >>> s.rename(lambda x: x ** 2)  # function, changes labels
     |      0    1
     |      1    2
     |      4    3
     |      dtype: int64
     |      >>> s.rename({1: 3, 2: 5})  # mapping, changes labels
     |      0    1
     |      3    2
     |      5    3
     |      dtype: int64
     |      >>> df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
     |      >>> df.rename(2)
     |      ...
     |      TypeError: 'int' object is not callable
     |      >>> df.rename(index=str, columns={"A": "a", "B": "c"})
     |         a  c
     |      0  1  4
     |      1  2  5
     |      2  3  6
     |      >>> df.rename(index=str, columns={"A": "a", "C": "c"})
     |         a  B
     |      0  1  4
     |      1  2  5
     |      2  3  6
     |  
     |  reorder_levels(self, order, axis=0)
     |      Rearrange index levels using input order.
     |      May not drop or duplicate levels
     |      
     |      Parameters
     |      ----------
     |      order : list of int or list of str
     |          List representing new level order. Reference level by number
     |          (position) or by key (label).
     |      axis : int
     |          Where to reorder levels.
     |      
     |      Returns
     |      -------
     |      type of caller (new object)
     |  
     |  reset_index(self, level=None, drop=False, inplace=False, col_level=0, col_fill='')
     |      For DataFrame with multi-level index, return new DataFrame with
     |      labeling information in the columns under the index names, defaulting
     |      to 'level_0', 'level_1', etc. if any are None. For a standard index,
     |      the index name will be used (if set), otherwise a default 'index' or
     |      'level_0' (if 'index' is already taken) will be used.
     |      
     |      Parameters
     |      ----------
     |      level : int, str, tuple, or list, default None
     |          Only remove the given levels from the index. Removes all levels by
     |          default
     |      drop : boolean, default False
     |          Do not try to insert index into dataframe columns. This resets
     |          the index to the default integer index.
     |      inplace : boolean, default False
     |          Modify the DataFrame in place (do not create a new object)
     |      col_level : int or str, default 0
     |          If the columns have multiple levels, determines which level the
     |          labels are inserted into. By default it is inserted into the first
     |          level.
     |      col_fill : object, default ''
     |          If the columns have multiple levels, determines how the other
     |          levels are named. If None then the index name is repeated.
     |      
     |      Returns
     |      -------
     |      resetted : DataFrame
     |  
     |  rfloordiv(self, other, axis='columns', level=None, fill_value=None)
     |      Integer division of dataframe and other, element-wise (binary operator `rfloordiv`).
     |      
     |      Equivalent to ``other // dataframe``, but with support to substitute a fill_value for
     |      missing data in one of the inputs.
     |      
     |      Parameters
     |      ----------
     |      other : Series, DataFrame, or constant
     |      axis : {0, 1, 'index', 'columns'}
     |          For Series input, axis to match Series index on
     |      fill_value : None or float value, default None
     |          Fill missing (NaN) values with this value. If both DataFrame
     |          locations are missing, the result will be missing
     |      level : int or name
     |          Broadcast across a level, matching Index values on the
     |          passed MultiIndex level
     |      
     |      Notes
     |      -----
     |      Mismatched indices will be unioned together
     |      
     |      Returns
     |      -------
     |      result : DataFrame
     |      
     |      See also
     |      --------
     |      DataFrame.floordiv
     |  
     |  rmod(self, other, axis='columns', level=None, fill_value=None)
     |      Modulo of dataframe and other, element-wise (binary operator `rmod`).
     |      
     |      Equivalent to ``other % dataframe``, but with support to substitute a fill_value for
     |      missing data in one of the inputs.
     |      
     |      Parameters
     |      ----------
     |      other : Series, DataFrame, or constant
     |      axis : {0, 1, 'index', 'columns'}
     |          For Series input, axis to match Series index on
     |      fill_value : None or float value, default None
     |          Fill missing (NaN) values with this value. If both DataFrame
     |          locations are missing, the result will be missing
     |      level : int or name
     |          Broadcast across a level, matching Index values on the
     |          passed MultiIndex level
     |      
     |      Notes
     |      -----
     |      Mismatched indices will be unioned together
     |      
     |      Returns
     |      -------
     |      result : DataFrame
     |      
     |      See also
     |      --------
     |      DataFrame.mod
     |  
     |  rmul(self, other, axis='columns', level=None, fill_value=None)
     |      Multiplication of dataframe and other, element-wise (binary operator `rmul`).
     |      
     |      Equivalent to ``other * dataframe``, but with support to substitute a fill_value for
     |      missing data in one of the inputs.
     |      
     |      Parameters
     |      ----------
     |      other : Series, DataFrame, or constant
     |      axis : {0, 1, 'index', 'columns'}
     |          For Series input, axis to match Series index on
     |      fill_value : None or float value, default None
     |          Fill missing (NaN) values with this value. If both DataFrame
     |          locations are missing, the result will be missing
     |      level : int or name
     |          Broadcast across a level, matching Index values on the
     |          passed MultiIndex level
     |      
     |      Notes
     |      -----
     |      Mismatched indices will be unioned together
     |      
     |      Returns
     |      -------
     |      result : DataFrame
     |      
     |      See also
     |      --------
     |      DataFrame.mul
     |  
     |  rolling(self, window, min_periods=None, freq=None, center=False, win_type=None, on=None, axis=0)
     |      Provides rolling window calculcations.
     |      
     |      .. versionadded:: 0.18.0
     |      
     |      Parameters
     |      ----------
     |      window : int, or offset
     |          Size of the moving window. This is the number of observations used for
     |          calculating the statistic. Each window will be a fixed size.
     |      
     |          If its an offset then this will be the time period of each window. Each
     |          window will be a variable sized based on the observations included in
     |          the time-period. This is only valid for datetimelike indexes. This is
     |          new in 0.19.0
     |      min_periods : int, default None
     |          Minimum number of observations in window required to have a value
     |          (otherwise result is NA). For a window that is specified by an offset,
     |          this will default to 1.
     |      freq : string or DateOffset object, optional (default None) (DEPRECATED)
     |          Frequency to conform the data to before computing the statistic.
     |          Specified as a frequency string or DateOffset object.
     |      center : boolean, default False
     |          Set the labels at the center of the window.
     |      win_type : string, default None
     |          Provide a window type. See the notes below.
     |      on : string, optional
     |          For a DataFrame, column on which to calculate
     |          the rolling window, rather than the index
     |      
     |          .. versionadded:: 0.19.0
     |      
     |      axis : int or string, default 0
     |      
     |      Returns
     |      -------
     |      a Window or Rolling sub-classed for the particular operation
     |      
     |      Examples
     |      --------
     |      
     |      >>> df = pd.DataFrame({'B': [0, 1, 2, np.nan, 4]})
     |      >>> df
     |           B
     |      0  0.0
     |      1  1.0
     |      2  2.0
     |      3  NaN
     |      4  4.0
     |      
     |      Rolling sum with a window length of 2, using the 'triang'
     |      window type.
     |      
     |      >>> df.rolling(2, win_type='triang').sum()
     |           B
     |      0  NaN
     |      1  1.0
     |      2  2.5
     |      3  NaN
     |      4  NaN
     |      
     |      Rolling sum with a window length of 2, min_periods defaults
     |      to the window length.
     |      
     |      >>> df.rolling(2).sum()
     |           B
     |      0  NaN
     |      1  1.0
     |      2  3.0
     |      3  NaN
     |      4  NaN
     |      
     |      Same as above, but explicity set the min_periods
     |      
     |      >>> df.rolling(2, min_periods=1).sum()
     |           B
     |      0  0.0
     |      1  1.0
     |      2  3.0
     |      3  2.0
     |      4  4.0
     |      
     |      A ragged (meaning not-a-regular frequency), time-indexed DataFrame
     |      
     |      >>> df = pd.DataFrame({'B': [0, 1, 2, np.nan, 4]},
     |      ....:                 index = [pd.Timestamp('20130101 09:00:00'),
     |      ....:                          pd.Timestamp('20130101 09:00:02'),
     |      ....:                          pd.Timestamp('20130101 09:00:03'),
     |      ....:                          pd.Timestamp('20130101 09:00:05'),
     |      ....:                          pd.Timestamp('20130101 09:00:06')])
     |      
     |      >>> df
     |                             B
     |      2013-01-01 09:00:00  0.0
     |      2013-01-01 09:00:02  1.0
     |      2013-01-01 09:00:03  2.0
     |      2013-01-01 09:00:05  NaN
     |      2013-01-01 09:00:06  4.0
     |      
     |      
     |      Contrasting to an integer rolling window, this will roll a variable
     |      length window corresponding to the time period.
     |      The default for min_periods is 1.
     |      
     |      >>> df.rolling('2s').sum()
     |                             B
     |      2013-01-01 09:00:00  0.0
     |      2013-01-01 09:00:02  1.0
     |      2013-01-01 09:00:03  3.0
     |      2013-01-01 09:00:05  NaN
     |      2013-01-01 09:00:06  4.0
     |      
     |      Notes
     |      -----
     |      By default, the result is set to the right edge of the window. This can be
     |      changed to the center of the window by setting ``center=True``.
     |      
     |      The `freq` keyword is used to conform time series data to a specified
     |      frequency by resampling the data. This is done with the default parameters
     |      of :meth:`~pandas.Series.resample` (i.e. using the `mean`).
     |      
     |      To learn more about the offsets & frequency strings, please see `this link
     |      <http://pandas.pydata.org/pandas-docs/stable/timeseries.html#offset-aliases>`__.
     |      
     |      The recognized win_types are:
     |      
     |      * ``boxcar``
     |      * ``triang``
     |      * ``blackman``
     |      * ``hamming``
     |      * ``bartlett``
     |      * ``parzen``
     |      * ``bohman``
     |      * ``blackmanharris``
     |      * ``nuttall``
     |      * ``barthann``
     |      * ``kaiser`` (needs beta)
     |      * ``gaussian`` (needs std)
     |      * ``general_gaussian`` (needs power, width)
     |      * ``slepian`` (needs width).
     |  
     |  round(self, decimals=0, *args, **kwargs)
     |      Round a DataFrame to a variable number of decimal places.
     |      
     |      .. versionadded:: 0.17.0
     |      
     |      Parameters
     |      ----------
     |      decimals : int, dict, Series
     |          Number of decimal places to round each column to. If an int is
     |          given, round each column to the same number of places.
     |          Otherwise dict and Series round to variable numbers of places.
     |          Column names should be in the keys if `decimals` is a
     |          dict-like, or in the index if `decimals` is a Series. Any
     |          columns not included in `decimals` will be left as is. Elements
     |          of `decimals` which are not columns of the input will be
     |          ignored.
     |      
     |      Examples
     |      --------
     |      >>> df = pd.DataFrame(np.random.random([3, 3]),
     |      ...     columns=['A', 'B', 'C'], index=['first', 'second', 'third'])
     |      >>> df
     |                     A         B         C
     |      first   0.028208  0.992815  0.173891
     |      second  0.038683  0.645646  0.577595
     |      third   0.877076  0.149370  0.491027
     |      >>> df.round(2)
     |                 A     B     C
     |      first   0.03  0.99  0.17
     |      second  0.04  0.65  0.58
     |      third   0.88  0.15  0.49
     |      >>> df.round({'A': 1, 'C': 2})
     |                A         B     C
     |      first   0.0  0.992815  0.17
     |      second  0.0  0.645646  0.58
     |      third   0.9  0.149370  0.49
     |      >>> decimals = pd.Series([1, 0, 2], index=['A', 'B', 'C'])
     |      >>> df.round(decimals)
     |                A  B     C
     |      first   0.0  1  0.17
     |      second  0.0  1  0.58
     |      third   0.9  0  0.49
     |      
     |      Returns
     |      -------
     |      DataFrame object
     |      
     |      See Also
     |      --------
     |      numpy.around
     |      Series.round
     |  
     |  rpow(self, other, axis='columns', level=None, fill_value=None)
     |      Exponential power of dataframe and other, element-wise (binary operator `rpow`).
     |      
     |      Equivalent to ``other ** dataframe``, but with support to substitute a fill_value for
     |      missing data in one of the inputs.
     |      
     |      Parameters
     |      ----------
     |      other : Series, DataFrame, or constant
     |      axis : {0, 1, 'index', 'columns'}
     |          For Series input, axis to match Series index on
     |      fill_value : None or float value, default None
     |          Fill missing (NaN) values with this value. If both DataFrame
     |          locations are missing, the result will be missing
     |      level : int or name
     |          Broadcast across a level, matching Index values on the
     |          passed MultiIndex level
     |      
     |      Notes
     |      -----
     |      Mismatched indices will be unioned together
     |      
     |      Returns
     |      -------
     |      result : DataFrame
     |      
     |      See also
     |      --------
     |      DataFrame.pow
     |  
     |  rsub(self, other, axis='columns', level=None, fill_value=None)
     |      Subtraction of dataframe and other, element-wise (binary operator `rsub`).
     |      
     |      Equivalent to ``other - dataframe``, but with support to substitute a fill_value for
     |      missing data in one of the inputs.
     |      
     |      Parameters
     |      ----------
     |      other : Series, DataFrame, or constant
     |      axis : {0, 1, 'index', 'columns'}
     |          For Series input, axis to match Series index on
     |      fill_value : None or float value, default None
     |          Fill missing (NaN) values with this value. If both DataFrame
     |          locations are missing, the result will be missing
     |      level : int or name
     |          Broadcast across a level, matching Index values on the
     |          passed MultiIndex level
     |      
     |      Notes
     |      -----
     |      Mismatched indices will be unioned together
     |      
     |      Returns
     |      -------
     |      result : DataFrame
     |      
     |      See also
     |      --------
     |      DataFrame.sub
     |  
     |  rtruediv(self, other, axis='columns', level=None, fill_value=None)
     |      Floating division of dataframe and other, element-wise (binary operator `rtruediv`).
     |      
     |      Equivalent to ``other / dataframe``, but with support to substitute a fill_value for
     |      missing data in one of the inputs.
     |      
     |      Parameters
     |      ----------
     |      other : Series, DataFrame, or constant
     |      axis : {0, 1, 'index', 'columns'}
     |          For Series input, axis to match Series index on
     |      fill_value : None or float value, default None
     |          Fill missing (NaN) values with this value. If both DataFrame
     |          locations are missing, the result will be missing
     |      level : int or name
     |          Broadcast across a level, matching Index values on the
     |          passed MultiIndex level
     |      
     |      Notes
     |      -----
     |      Mismatched indices will be unioned together
     |      
     |      Returns
     |      -------
     |      result : DataFrame
     |      
     |      See also
     |      --------
     |      DataFrame.truediv
     |  
     |  select_dtypes(self, include=None, exclude=None)
     |      Return a subset of a DataFrame including/excluding columns based on
     |      their ``dtype``.
     |      
     |      Parameters
     |      ----------
     |      include, exclude : list-like
     |          A list of dtypes or strings to be included/excluded. You must pass
     |          in a non-empty sequence for at least one of these.
     |      
     |      Raises
     |      ------
     |      ValueError
     |          * If both of ``include`` and ``exclude`` are empty
     |          * If ``include`` and ``exclude`` have overlapping elements
     |          * If any kind of string dtype is passed in.
     |      TypeError
     |          * If either of ``include`` or ``exclude`` is not a sequence
     |      
     |      Returns
     |      -------
     |      subset : DataFrame
     |          The subset of the frame including the dtypes in ``include`` and
     |          excluding the dtypes in ``exclude``.
     |      
     |      Notes
     |      -----
     |      * To select all *numeric* types use the numpy dtype ``numpy.number``
     |      * To select strings you must use the ``object`` dtype, but note that
     |        this will return *all* object dtype columns
     |      * See the `numpy dtype hierarchy
     |        <http://docs.scipy.org/doc/numpy/reference/arrays.scalars.html>`__
     |      * To select Pandas categorical dtypes, use 'category'
     |      
     |      Examples
     |      --------
     |      >>> df = pd.DataFrame({'a': np.random.randn(6).astype('f4'),
     |      ...                    'b': [True, False] * 3,
     |      ...                    'c': [1.0, 2.0] * 3})
     |      >>> df
     |              a      b  c
     |      0  0.3962   True  1
     |      1  0.1459  False  2
     |      2  0.2623   True  1
     |      3  0.0764  False  2
     |      4 -0.9703   True  1
     |      5 -1.2094  False  2
     |      >>> df.select_dtypes(include=['float64'])
     |         c
     |      0  1
     |      1  2
     |      2  1
     |      3  2
     |      4  1
     |      5  2
     |      >>> df.select_dtypes(exclude=['floating'])
     |             b
     |      0   True
     |      1  False
     |      2   True
     |      3  False
     |      4   True
     |      5  False
     |  
     |  sem(self, axis=None, skipna=None, level=None, ddof=1, numeric_only=None, **kwargs)
     |      Return unbiased standard error of the mean over requested axis.
     |      
     |      Normalized by N-1 by default. This can be changed using the ddof argument
     |      
     |      Parameters
     |      ----------
     |      axis : {index (0), columns (1)}
     |      skipna : boolean, default True
     |          Exclude NA/null values. If an entire row/column is NA, the result
     |          will be NA
     |      level : int or level name, default None
     |          If the axis is a MultiIndex (hierarchical), count along a
     |          particular level, collapsing into a Series
     |      ddof : int, default 1
     |          degrees of freedom
     |      numeric_only : boolean, default None
     |          Include only float, int, boolean columns. If None, will attempt to use
     |          everything, then use only numeric data. Not implemented for Series.
     |      
     |      Returns
     |      -------
     |      sem : Series or DataFrame (if level specified)
     |  
     |  set_index(self, keys, drop=True, append=False, inplace=False, verify_integrity=False)
     |      Set the DataFrame index (row labels) using one or more existing
     |      columns. By default yields a new object.
     |      
     |      Parameters
     |      ----------
     |      keys : column label or list of column labels / arrays
     |      drop : boolean, default True
     |          Delete columns to be used as the new index
     |      append : boolean, default False
     |          Whether to append columns to existing index
     |      inplace : boolean, default False
     |          Modify the DataFrame in place (do not create a new object)
     |      verify_integrity : boolean, default False
     |          Check the new index for duplicates. Otherwise defer the check until
     |          necessary. Setting to False will improve the performance of this
     |          method
     |      
     |      Examples
     |      --------
     |      >>> indexed_df = df.set_index(['A', 'B'])
     |      >>> indexed_df2 = df.set_index(['A', [0, 1, 2, 0, 1, 2]])
     |      >>> indexed_df3 = df.set_index([[0, 1, 2, 0, 1, 2]])
     |      
     |      Returns
     |      -------
     |      dataframe : DataFrame
     |  
     |  set_value(self, index, col, value, takeable=False)
     |      Put single value at passed column and index
     |      
     |      Parameters
     |      ----------
     |      index : row label
     |      col : column label
     |      value : scalar value
     |      takeable : interpret the index/col as indexers, default False
     |      
     |      Returns
     |      -------
     |      frame : DataFrame
     |          If label pair is contained, will be reference to calling DataFrame,
     |          otherwise a new object
     |  
     |  shift(self, periods=1, freq=None, axis=0)
     |      Shift index by desired number of periods with an optional time freq
     |      
     |      Parameters
     |      ----------
     |      periods : int
     |          Number of periods to move, can be positive or negative
     |      freq : DateOffset, timedelta, or time rule string, optional
     |          Increment to use from the tseries module or time rule (e.g. 'EOM').
     |          See Notes.
     |      axis : {0 or 'index', 1 or 'columns'}
     |      
     |      Notes
     |      -----
     |      If freq is specified then the index values are shifted but the data
     |      is not realigned. That is, use freq if you would like to extend the
     |      index when shifting and preserve the original data.
     |      
     |      Returns
     |      -------
     |      shifted : DataFrame
     |  
     |  skew(self, axis=None, skipna=None, level=None, numeric_only=None, **kwargs)
     |      Return unbiased skew over requested axis
     |      Normalized by N-1
     |      
     |      Parameters
     |      ----------
     |      axis : {index (0), columns (1)}
     |      skipna : boolean, default True
     |          Exclude NA/null values. If an entire row/column is NA, the result
     |          will be NA
     |      level : int or level name, default None
     |          If the axis is a MultiIndex (hierarchical), count along a
     |          particular level, collapsing into a Series
     |      numeric_only : boolean, default None
     |          Include only float, int, boolean columns. If None, will attempt to use
     |          everything, then use only numeric data. Not implemented for Series.
     |      
     |      Returns
     |      -------
     |      skew : Series or DataFrame (if level specified)
     |  
     |  sort(self, columns=None, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last', **kwargs)
     |      DEPRECATED: use :meth:`DataFrame.sort_values`
     |      
     |      Sort DataFrame either by labels (along either axis) or by the values in
     |      column(s)
     |      
     |      Parameters
     |      ----------
     |      columns : object
     |          Column name(s) in frame. Accepts a column name or a list
     |          for a nested sort. A tuple will be interpreted as the
     |          levels of a multi-index.
     |      ascending : boolean or list, default True
     |          Sort ascending vs. descending. Specify list for multiple sort
     |          orders
     |      axis : {0 or 'index', 1 or 'columns'}, default 0
     |          Sort index/rows versus columns
     |      inplace : boolean, default False
     |          Sort the DataFrame without creating a new instance
     |      kind : {'quicksort', 'mergesort', 'heapsort'}, optional
     |          This option is only applied when sorting on a single column or
     |          label.
     |      na_position : {'first', 'last'} (optional, default='last')
     |          'first' puts NaNs at the beginning
     |          'last' puts NaNs at the end
     |      
     |      Examples
     |      --------
     |      >>> result = df.sort(['A', 'B'], ascending=[1, 0])
     |      
     |      Returns
     |      -------
     |      sorted : DataFrame
     |  
     |  sort_index(self, axis=0, level=None, ascending=True, inplace=False, kind='quicksort', na_position='last', sort_remaining=True, by=None)
     |      Sort object by labels (along an axis)
     |      
     |      Parameters
     |      ----------
     |      axis : index, columns to direct sorting
     |      level : int or level name or list of ints or list of level names
     |          if not None, sort on values in specified index level(s)
     |      ascending : boolean, default True
     |          Sort ascending vs. descending
     |      inplace : bool, default False
     |          if True, perform operation in-place
     |      kind : {'quicksort', 'mergesort', 'heapsort'}, default 'quicksort'
     |           Choice of sorting algorithm. See also ndarray.np.sort for more
     |           information.  `mergesort` is the only stable algorithm. For
     |           DataFrames, this option is only applied when sorting on a single
     |           column or label.
     |      na_position : {'first', 'last'}, default 'last'
     |           `first` puts NaNs at the beginning, `last` puts NaNs at the end
     |      sort_remaining : bool, default True
     |          if true and sorting by level and index is multilevel, sort by other
     |          levels too (in order) after sorting by specified level
     |      
     |      Returns
     |      -------
     |      sorted_obj : DataFrame
     |  
     |  sort_values(self, by, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last')
     |      Sort by the values along either axis
     |      
     |      .. versionadded:: 0.17.0
     |      
     |      Parameters
     |      ----------
     |      by : str or list of str
     |          Name or list of names which refer to the axis items.
     |      axis : {0 or 'index', 1 or 'columns'}, default 0
     |          Axis to direct sorting
     |      ascending : bool or list of bool, default True
     |           Sort ascending vs. descending. Specify list for multiple sort
     |           orders.  If this is a list of bools, must match the length of
     |           the by.
     |      inplace : bool, default False
     |           if True, perform operation in-place
     |      kind : {'quicksort', 'mergesort', 'heapsort'}, default 'quicksort'
     |           Choice of sorting algorithm. See also ndarray.np.sort for more
     |           information.  `mergesort` is the only stable algorithm. For
     |           DataFrames, this option is only applied when sorting on a single
     |           column or label.
     |      na_position : {'first', 'last'}, default 'last'
     |           `first` puts NaNs at the beginning, `last` puts NaNs at the end
     |      
     |      Returns
     |      -------
     |      sorted_obj : DataFrame
     |  
     |  sortlevel(self, level=0, axis=0, ascending=True, inplace=False, sort_remaining=True)
     |      Sort multilevel index by chosen axis and primary level. Data will be
     |      lexicographically sorted by the chosen level followed by the other
     |      levels (in order)
     |      
     |      Parameters
     |      ----------
     |      level : int
     |      axis : {0 or 'index', 1 or 'columns'}, default 0
     |      ascending : boolean, default True
     |      inplace : boolean, default False
     |          Sort the DataFrame without creating a new instance
     |      sort_remaining : boolean, default True
     |          Sort by the other levels too.
     |      
     |      Returns
     |      -------
     |      sorted : DataFrame
     |      
     |      See Also
     |      --------
     |      DataFrame.sort_index(level=...)
     |  
     |  stack(self, level=-1, dropna=True)
     |      Pivot a level of the (possibly hierarchical) column labels, returning a
     |      DataFrame (or Series in the case of an object with a single level of
     |      column labels) having a hierarchical index with a new inner-most level
     |      of row labels.
     |      The level involved will automatically get sorted.
     |      
     |      Parameters
     |      ----------
     |      level : int, string, or list of these, default last level
     |          Level(s) to stack, can pass level name
     |      dropna : boolean, default True
     |          Whether to drop rows in the resulting Frame/Series with no valid
     |          values
     |      
     |      Examples
     |      ----------
     |      >>> s
     |           a   b
     |      one  1.  2.
     |      two  3.  4.
     |      
     |      >>> s.stack()
     |      one a    1
     |          b    2
     |      two a    3
     |          b    4
     |      
     |      Returns
     |      -------
     |      stacked : DataFrame or Series
     |  
     |  std(self, axis=None, skipna=None, level=None, ddof=1, numeric_only=None, **kwargs)
     |      Return sample standard deviation over requested axis.
     |      
     |      Normalized by N-1 by default. This can be changed using the ddof argument
     |      
     |      Parameters
     |      ----------
     |      axis : {index (0), columns (1)}
     |      skipna : boolean, default True
     |          Exclude NA/null values. If an entire row/column is NA, the result
     |          will be NA
     |      level : int or level name, default None
     |          If the axis is a MultiIndex (hierarchical), count along a
     |          particular level, collapsing into a Series
     |      ddof : int, default 1
     |          degrees of freedom
     |      numeric_only : boolean, default None
     |          Include only float, int, boolean columns. If None, will attempt to use
     |          everything, then use only numeric data. Not implemented for Series.
     |      
     |      Returns
     |      -------
     |      std : Series or DataFrame (if level specified)
     |  
     |  sub(self, other, axis='columns', level=None, fill_value=None)
     |      Subtraction of dataframe and other, element-wise (binary operator `sub`).
     |      
     |      Equivalent to ``dataframe - other``, but with support to substitute a fill_value for
     |      missing data in one of the inputs.
     |      
     |      Parameters
     |      ----------
     |      other : Series, DataFrame, or constant
     |      axis : {0, 1, 'index', 'columns'}
     |          For Series input, axis to match Series index on
     |      fill_value : None or float value, default None
     |          Fill missing (NaN) values with this value. If both DataFrame
     |          locations are missing, the result will be missing
     |      level : int or name
     |          Broadcast across a level, matching Index values on the
     |          passed MultiIndex level
     |      
     |      Notes
     |      -----
     |      Mismatched indices will be unioned together
     |      
     |      Returns
     |      -------
     |      result : DataFrame
     |      
     |      See also
     |      --------
     |      DataFrame.rsub
     |  
     |  subtract = sub(self, other, axis='columns', level=None, fill_value=None)
     |  
     |  sum(self, axis=None, skipna=None, level=None, numeric_only=None, **kwargs)
     |      Return the sum of the values for the requested axis
     |      
     |      Parameters
     |      ----------
     |      axis : {index (0), columns (1)}
     |      skipna : boolean, default True
     |          Exclude NA/null values. If an entire row/column is NA, the result
     |          will be NA
     |      level : int or level name, default None
     |          If the axis is a MultiIndex (hierarchical), count along a
     |          particular level, collapsing into a Series
     |      numeric_only : boolean, default None
     |          Include only float, int, boolean columns. If None, will attempt to use
     |          everything, then use only numeric data. Not implemented for Series.
     |      
     |      Returns
     |      -------
     |      sum : Series or DataFrame (if level specified)
     |  
     |  swaplevel(self, i=-2, j=-1, axis=0)
     |      Swap levels i and j in a MultiIndex on a particular axis
     |      
     |      Parameters
     |      ----------
     |      i, j : int, string (can be mixed)
     |          Level of index to be swapped. Can pass level name as string.
     |      
     |      Returns
     |      -------
     |      swapped : type of caller (new object)
     |      
     |      .. versionchanged:: 0.18.1
     |      
     |         The indexes ``i`` and ``j`` are now optional, and default to
     |         the two innermost levels of the index.
     |  
     |  to_csv(self, path_or_buf=None, sep=',', na_rep='', float_format=None, columns=None, header=True, index=True, index_label=None, mode='w', encoding=None, compression=None, quoting=None, quotechar='"', line_terminator='\n', chunksize=None, tupleize_cols=False, date_format=None, doublequote=True, escapechar=None, decimal='.')
     |      Write DataFrame to a comma-separated values (csv) file
     |      
     |      Parameters
     |      ----------
     |      path_or_buf : string or file handle, default None
     |          File path or object, if None is provided the result is returned as
     |          a string.
     |      sep : character, default ','
     |          Field delimiter for the output file.
     |      na_rep : string, default ''
     |          Missing data representation
     |      float_format : string, default None
     |          Format string for floating point numbers
     |      columns : sequence, optional
     |          Columns to write
     |      header : boolean or list of string, default True
     |          Write out column names. If a list of string is given it is assumed
     |          to be aliases for the column names
     |      index : boolean, default True
     |          Write row names (index)
     |      index_label : string or sequence, or False, default None
     |          Column label for index column(s) if desired. If None is given, and
     |          `header` and `index` are True, then the index names are used. A
     |          sequence should be given if the DataFrame uses MultiIndex.  If
     |          False do not print fields for index names. Use index_label=False
     |          for easier importing in R
     |      mode : str
     |          Python write mode, default 'w'
     |      encoding : string, optional
     |          A string representing the encoding to use in the output file,
     |          defaults to 'ascii' on Python 2 and 'utf-8' on Python 3.
     |      compression : string, optional
     |          a string representing the compression to use in the output file,
     |          allowed values are 'gzip', 'bz2', 'xz',
     |          only used when the first argument is a filename
     |      line_terminator : string, default ``'\n'``
     |          The newline character or character sequence to use in the output
     |          file
     |      quoting : optional constant from csv module
     |          defaults to csv.QUOTE_MINIMAL. If you have set a `float_format`
     |          then floats are comverted to strings and thus csv.QUOTE_NONNUMERIC
     |          will treat them as non-numeric
     |      quotechar : string (length 1), default '\"'
     |          character used to quote fields
     |      doublequote : boolean, default True
     |          Control quoting of `quotechar` inside a field
     |      escapechar : string (length 1), default None
     |          character used to escape `sep` and `quotechar` when appropriate
     |      chunksize : int or None
     |          rows to write at a time
     |      tupleize_cols : boolean, default False
     |          write multi_index columns as a list of tuples (if True)
     |          or new (expanded format) if False)
     |      date_format : string, default None
     |          Format string for datetime objects
     |      decimal: string, default '.'
     |          Character recognized as decimal separator. E.g. use ',' for
     |          European data
     |      
     |          .. versionadded:: 0.16.0
     |  
     |  to_dict(self, orient='dict')
     |      Convert DataFrame to dictionary.
     |      
     |      Parameters
     |      ----------
     |      orient : str {'dict', 'list', 'series', 'split', 'records', 'index'}
     |          Determines the type of the values of the dictionary.
     |      
     |          - dict (default) : dict like {column -> {index -> value}}
     |          - list : dict like {column -> [values]}
     |          - series : dict like {column -> Series(values)}
     |          - split : dict like
     |            {index -> [index], columns -> [columns], data -> [values]}
     |          - records : list like
     |            [{column -> value}, ... , {column -> value}]
     |          - index : dict like {index -> {column -> value}}
     |      
     |            .. versionadded:: 0.17.0
     |      
     |          Abbreviations are allowed. `s` indicates `series` and `sp`
     |          indicates `split`.
     |      
     |      Returns
     |      -------
     |      result : dict like {column -> {index -> value}}
     |  
     |  to_excel(self, excel_writer, sheet_name='Sheet1', na_rep='', float_format=None, columns=None, header=True, index=True, index_label=None, startrow=0, startcol=0, engine=None, merge_cells=True, encoding=None, inf_rep='inf', verbose=True)
     |      Write DataFrame to a excel sheet
     |      
     |      Parameters
     |      ----------
     |      excel_writer : string or ExcelWriter object
     |          File path or existing ExcelWriter
     |      sheet_name : string, default 'Sheet1'
     |          Name of sheet which will contain DataFrame
     |      na_rep : string, default ''
     |          Missing data representation
     |      float_format : string, default None
     |          Format string for floating point numbers
     |      columns : sequence, optional
     |          Columns to write
     |      header : boolean or list of string, default True
     |          Write out column names. If a list of string is given it is
     |          assumed to be aliases for the column names
     |      index : boolean, default True
     |          Write row names (index)
     |      index_label : string or sequence, default None
     |          Column label for index column(s) if desired. If None is given, and
     |          `header` and `index` are True, then the index names are used. A
     |          sequence should be given if the DataFrame uses MultiIndex.
     |      startrow :
     |          upper left cell row to dump data frame
     |      startcol :
     |          upper left cell column to dump data frame
     |      engine : string, default None
     |          write engine to use - you can also set this via the options
     |          ``io.excel.xlsx.writer``, ``io.excel.xls.writer``, and
     |          ``io.excel.xlsm.writer``.
     |      merge_cells : boolean, default True
     |          Write MultiIndex and Hierarchical Rows as merged cells.
     |      encoding: string, default None
     |          encoding of the resulting excel file. Only necessary for xlwt,
     |          other writers support unicode natively.
     |      inf_rep : string, default 'inf'
     |          Representation for infinity (there is no native representation for
     |          infinity in Excel)
     |      
     |      Notes
     |      -----
     |      If passing an existing ExcelWriter object, then the sheet will be added
     |      to the existing workbook.  This can be used to save different
     |      DataFrames to one workbook:
     |      
     |      >>> writer = ExcelWriter('output.xlsx')
     |      >>> df1.to_excel(writer,'Sheet1')
     |      >>> df2.to_excel(writer,'Sheet2')
     |      >>> writer.save()
     |      
     |      For compatibility with to_csv, to_excel serializes lists and dicts to
     |      strings before writing.
     |  
     |  to_gbq(self, destination_table, project_id, chunksize=10000, verbose=True, reauth=False, if_exists='fail', private_key=None)
     |      Write a DataFrame to a Google BigQuery table.
     |      
     |      THIS IS AN EXPERIMENTAL LIBRARY
     |      
     |      Parameters
     |      ----------
     |      dataframe : DataFrame
     |          DataFrame to be written
     |      destination_table : string
     |          Name of table to be written, in the form 'dataset.tablename'
     |      project_id : str
     |          Google BigQuery Account project ID.
     |      chunksize : int (default 10000)
     |          Number of rows to be inserted in each chunk from the dataframe.
     |      verbose : boolean (default True)
     |          Show percentage complete
     |      reauth : boolean (default False)
     |          Force Google BigQuery to reauthenticate the user. This is useful
     |          if multiple accounts are used.
     |      if_exists : {'fail', 'replace', 'append'}, default 'fail'
     |          'fail': If table exists, do nothing.
     |          'replace': If table exists, drop it, recreate it, and insert data.
     |          'append': If table exists, insert data. Create if does not exist.
     |      private_key : str (optional)
     |          Service account private key in JSON format. Can be file path
     |          or string contents. This is useful for remote server
     |          authentication (eg. jupyter iPython notebook on remote host)
     |      
     |          .. versionadded:: 0.17.0
     |  
     |  to_html(self, buf=None, columns=None, col_space=None, header=True, index=True, na_rep='NaN', formatters=None, float_format=None, sparsify=None, index_names=True, justify=None, bold_rows=True, classes=None, escape=True, max_rows=None, max_cols=None, show_dimensions=False, notebook=False, decimal='.', border=None)
     |      Render a DataFrame as an HTML table.
     |      
     |      `to_html`-specific options:
     |      
     |      bold_rows : boolean, default True
     |          Make the row labels bold in the output
     |      classes : str or list or tuple, default None
     |          CSS class(es) to apply to the resulting html table
     |      escape : boolean, default True
     |          Convert the characters <, >, and & to HTML-safe sequences.=
     |      max_rows : int, optional
     |          Maximum number of rows to show before truncating. If None, show
     |          all.
     |      max_cols : int, optional
     |          Maximum number of columns to show before truncating. If None, show
     |          all.
     |      decimal : string, default '.'
     |          Character recognized as decimal separator, e.g. ',' in Europe
     |      
     |          .. versionadded:: 0.18.0
     |      border : int
     |          A ``border=border`` attribute is included in the opening
     |          `<table>` tag. Default ``pd.options.html.border``.
     |      
     |          .. versionadded:: 0.19.0
     |      
     |      Parameters
     |      ----------
     |      buf : StringIO-like, optional
     |          buffer to write to
     |      columns : sequence, optional
     |          the subset of columns to write; default None writes all columns
     |      col_space : int, optional
     |          the minimum width of each column
     |      header : bool, optional
     |          whether to print column labels, default True
     |      index : bool, optional
     |          whether to print index (row) labels, default True
     |      na_rep : string, optional
     |          string representation of NAN to use, default 'NaN'
     |      formatters : list or dict of one-parameter functions, optional
     |          formatter functions to apply to columns' elements by position or name,
     |          default None. The result of each function must be a unicode string.
     |          List must be of length equal to the number of columns.
     |      float_format : one-parameter function, optional
     |          formatter function to apply to columns' elements if they are floats,
     |          default None. The result of this function must be a unicode string.
     |      sparsify : bool, optional
     |          Set to False for a DataFrame with a hierarchical index to print every
     |          multiindex key at each row, default True
     |      index_names : bool, optional
     |          Prints the names of the indexes, default True
     |      line_width : int, optional
     |          Width to wrap a line in characters, default no wrap
     |      justify : {'left', 'right'}, default None
     |          Left or right-justify the column labels. If None uses the option from
     |          the print configuration (controlled by set_option), 'right' out
     |          of the box.
     |      
     |      Returns
     |      -------
     |      formatted : string (or unicode, depending on data and options)
     |  
     |  to_latex(self, buf=None, columns=None, col_space=None, header=True, index=True, na_rep='NaN', formatters=None, float_format=None, sparsify=None, index_names=True, bold_rows=True, column_format=None, longtable=None, escape=None, encoding=None, decimal='.')
     |      Render a DataFrame to a tabular environment table. You can splice
     |      this into a LaTeX document. Requires \usepackage{booktabs}.
     |      
     |      `to_latex`-specific options:
     |      
     |      bold_rows : boolean, default True
     |          Make the row labels bold in the output
     |      column_format : str, default None
     |          The columns format as specified in `LaTeX table format
     |          <https://en.wikibooks.org/wiki/LaTeX/Tables>`__ e.g 'rcl' for 3
     |          columns
     |      longtable : boolean, default will be read from the pandas config module
     |          default: False
     |          Use a longtable environment instead of tabular. Requires adding
     |          a \usepackage{longtable} to your LaTeX preamble.
     |      escape : boolean, default will be read from the pandas config module
     |          default: True
     |          When set to False prevents from escaping latex special
     |          characters in column names.
     |      encoding : str, default None
     |          A string representing the encoding to use in the output file,
     |          defaults to 'ascii' on Python 2 and 'utf-8' on Python 3.
     |      decimal : string, default '.'
     |          Character recognized as decimal separator, e.g. ',' in Europe
     |      
     |          .. versionadded:: 0.18.0
     |      
     |      
     |      Parameters
     |      ----------
     |      buf : StringIO-like, optional
     |          buffer to write to
     |      columns : sequence, optional
     |          the subset of columns to write; default None writes all columns
     |      col_space : int, optional
     |          the minimum width of each column
     |      header : bool, optional
     |          whether to print column labels, default True
     |      index : bool, optional
     |          whether to print index (row) labels, default True
     |      na_rep : string, optional
     |          string representation of NAN to use, default 'NaN'
     |      formatters : list or dict of one-parameter functions, optional
     |          formatter functions to apply to columns' elements by position or name,
     |          default None. The result of each function must be a unicode string.
     |          List must be of length equal to the number of columns.
     |      float_format : one-parameter function, optional
     |          formatter function to apply to columns' elements if they are floats,
     |          default None. The result of this function must be a unicode string.
     |      sparsify : bool, optional
     |          Set to False for a DataFrame with a hierarchical index to print every
     |          multiindex key at each row, default True
     |      index_names : bool, optional
     |          Prints the names of the indexes, default True
     |      line_width : int, optional
     |          Width to wrap a line in characters, default no wrap
     |      
     |      Returns
     |      -------
     |      formatted : string (or unicode, depending on data and options)
     |  
     |  to_panel(self)
     |      Transform long (stacked) format (DataFrame) into wide (3D, Panel)
     |      format.
     |      
     |      Currently the index of the DataFrame must be a 2-level MultiIndex. This
     |      may be generalized later
     |      
     |      Returns
     |      -------
     |      panel : Panel
     |  
     |  to_period(self, freq=None, axis=0, copy=True)
     |      Convert DataFrame from DatetimeIndex to PeriodIndex with desired
     |      frequency (inferred from index if not passed)
     |      
     |      Parameters
     |      ----------
     |      freq : string, default
     |      axis : {0 or 'index', 1 or 'columns'}, default 0
     |          The axis to convert (the index by default)
     |      copy : boolean, default True
     |          If False then underlying input data is not copied
     |      
     |      Returns
     |      -------
     |      ts : TimeSeries with PeriodIndex
     |  
     |  to_records(self, index=True, convert_datetime64=True)
     |      Convert DataFrame to record array. Index will be put in the
     |      'index' field of the record array if requested
     |      
     |      Parameters
     |      ----------
     |      index : boolean, default True
     |          Include index in resulting record array, stored in 'index' field
     |      convert_datetime64 : boolean, default True
     |          Whether to convert the index to datetime.datetime if it is a
     |          DatetimeIndex
     |      
     |      Returns
     |      -------
     |      y : recarray
     |  
     |  to_sparse(self, fill_value=None, kind='block')
     |      Convert to SparseDataFrame
     |      
     |      Parameters
     |      ----------
     |      fill_value : float, default NaN
     |      kind : {'block', 'integer'}
     |      
     |      Returns
     |      -------
     |      y : SparseDataFrame
     |  
     |  to_stata(self, fname, convert_dates=None, write_index=True, encoding='latin-1', byteorder=None, time_stamp=None, data_label=None, variable_labels=None)
     |      A class for writing Stata binary dta files from array-like objects
     |      
     |      Parameters
     |      ----------
     |      fname : str or buffer
     |          String path of file-like object
     |      convert_dates : dict
     |          Dictionary mapping columns containing datetime types to stata
     |          internal format to use when wirting the dates. Options are 'tc',
     |          'td', 'tm', 'tw', 'th', 'tq', 'ty'. Column can be either an integer
     |          or a name. Datetime columns that do not have a conversion type
     |          specified will be converted to 'tc'. Raises NotImplementedError if
     |          a datetime column has timezone information
     |      write_index : bool
     |          Write the index to Stata dataset.
     |      encoding : str
     |          Default is latin-1. Unicode is not supported
     |      byteorder : str
     |          Can be ">", "<", "little", or "big". default is `sys.byteorder`
     |      time_stamp : datetime
     |          A datetime to use as file creation date.  Default is the current
     |          time.
     |      dataset_label : str
     |          A label for the data set.  Must be 80 characters or smaller.
     |      variable_labels : dict
     |          Dictionary containing columns as keys and variable labels as
     |          values. Each label must be 80 characters or smaller.
     |      
     |          .. versionadded:: 0.19.0
     |      
     |      Raises
     |      ------
     |      NotImplementedError
     |          * If datetimes contain timezone information
     |          * Column dtype is not representable in Stata
     |      ValueError
     |          * Columns listed in convert_dates are noth either datetime64[ns]
     |            or datetime.datetime
     |          * Column listed in convert_dates is not in DataFrame
     |          * Categorical label contains more than 32,000 characters
     |      
     |          .. versionadded:: 0.19.0
     |      
     |      Examples
     |      --------
     |      >>> writer = StataWriter('./data_file.dta', data)
     |      >>> writer.write_file()
     |      
     |      Or with dates
     |      
     |      >>> writer = StataWriter('./date_data_file.dta', data, {2 : 'tw'})
     |      >>> writer.write_file()
     |  
     |  to_string(self, buf=None, columns=None, col_space=None, header=True, index=True, na_rep='NaN', formatters=None, float_format=None, sparsify=None, index_names=True, justify=None, line_width=None, max_rows=None, max_cols=None, show_dimensions=False)
     |      Render a DataFrame to a console-friendly tabular output.
     |      
     |      Parameters
     |      ----------
     |      buf : StringIO-like, optional
     |          buffer to write to
     |      columns : sequence, optional
     |          the subset of columns to write; default None writes all columns
     |      col_space : int, optional
     |          the minimum width of each column
     |      header : bool, optional
     |          whether to print column labels, default True
     |      index : bool, optional
     |          whether to print index (row) labels, default True
     |      na_rep : string, optional
     |          string representation of NAN to use, default 'NaN'
     |      formatters : list or dict of one-parameter functions, optional
     |          formatter functions to apply to columns' elements by position or name,
     |          default None. The result of each function must be a unicode string.
     |          List must be of length equal to the number of columns.
     |      float_format : one-parameter function, optional
     |          formatter function to apply to columns' elements if they are floats,
     |          default None. The result of this function must be a unicode string.
     |      sparsify : bool, optional
     |          Set to False for a DataFrame with a hierarchical index to print every
     |          multiindex key at each row, default True
     |      index_names : bool, optional
     |          Prints the names of the indexes, default True
     |      line_width : int, optional
     |          Width to wrap a line in characters, default no wrap
     |      justify : {'left', 'right'}, default None
     |          Left or right-justify the column labels. If None uses the option from
     |          the print configuration (controlled by set_option), 'right' out
     |          of the box.
     |      
     |      Returns
     |      -------
     |      formatted : string (or unicode, depending on data and options)
     |  
     |  to_timestamp(self, freq=None, how='start', axis=0, copy=True)
     |      Cast to DatetimeIndex of timestamps, at *beginning* of period
     |      
     |      Parameters
     |      ----------
     |      freq : string, default frequency of PeriodIndex
     |          Desired frequency
     |      how : {'s', 'e', 'start', 'end'}
     |          Convention for converting period to timestamp; start of period
     |          vs. end
     |      axis : {0 or 'index', 1 or 'columns'}, default 0
     |          The axis to convert (the index by default)
     |      copy : boolean, default True
     |          If false then underlying input data is not copied
     |      
     |      Returns
     |      -------
     |      df : DataFrame with DatetimeIndex
     |  
     |  transpose(self, *args, **kwargs)
     |      Transpose index and columns
     |  
     |  truediv(self, other, axis='columns', level=None, fill_value=None)
     |      Floating division of dataframe and other, element-wise (binary operator `truediv`).
     |      
     |      Equivalent to ``dataframe / other``, but with support to substitute a fill_value for
     |      missing data in one of the inputs.
     |      
     |      Parameters
     |      ----------
     |      other : Series, DataFrame, or constant
     |      axis : {0, 1, 'index', 'columns'}
     |          For Series input, axis to match Series index on
     |      fill_value : None or float value, default None
     |          Fill missing (NaN) values with this value. If both DataFrame
     |          locations are missing, the result will be missing
     |      level : int or name
     |          Broadcast across a level, matching Index values on the
     |          passed MultiIndex level
     |      
     |      Notes
     |      -----
     |      Mismatched indices will be unioned together
     |      
     |      Returns
     |      -------
     |      result : DataFrame
     |      
     |      See also
     |      --------
     |      DataFrame.rtruediv
     |  
     |  unstack(self, level=-1, fill_value=None)
     |      Pivot a level of the (necessarily hierarchical) index labels, returning
     |      a DataFrame having a new level of column labels whose inner-most level
     |      consists of the pivoted index labels. If the index is not a MultiIndex,
     |      the output will be a Series (the analogue of stack when the columns are
     |      not a MultiIndex).
     |      The level involved will automatically get sorted.
     |      
     |      Parameters
     |      ----------
     |      level : int, string, or list of these, default -1 (last level)
     |          Level(s) of index to unstack, can pass level name
     |      fill_value : replace NaN with this value if the unstack produces
     |          missing values
     |      
     |          .. versionadded: 0.18.0
     |      
     |      See also
     |      --------
     |      DataFrame.pivot : Pivot a table based on column values.
     |      DataFrame.stack : Pivot a level of the column labels (inverse operation
     |          from `unstack`).
     |      
     |      Examples
     |      --------
     |      >>> index = pd.MultiIndex.from_tuples([('one', 'a'), ('one', 'b'),
     |      ...                                    ('two', 'a'), ('two', 'b')])
     |      >>> s = pd.Series(np.arange(1.0, 5.0), index=index)
     |      >>> s
     |      one  a   1.0
     |           b   2.0
     |      two  a   3.0
     |           b   4.0
     |      dtype: float64
     |      
     |      >>> s.unstack(level=-1)
     |           a   b
     |      one  1.0  2.0
     |      two  3.0  4.0
     |      
     |      >>> s.unstack(level=0)
     |         one  two
     |      a  1.0   3.0
     |      b  2.0   4.0
     |      
     |      >>> df = s.unstack(level=0)
     |      >>> df.unstack()
     |      one  a  1.0
     |           b  2.0
     |      two  a  3.0
     |           b  4.0
     |      dtype: float64
     |      
     |      Returns
     |      -------
     |      unstacked : DataFrame or Series
     |  
     |  update(self, other, join='left', overwrite=True, filter_func=None, raise_conflict=False)
     |      Modify DataFrame in place using non-NA values from passed
     |      DataFrame. Aligns on indices
     |      
     |      Parameters
     |      ----------
     |      other : DataFrame, or object coercible into a DataFrame
     |      join : {'left'}, default 'left'
     |      overwrite : boolean, default True
     |          If True then overwrite values for common keys in the calling frame
     |      filter_func : callable(1d-array) -> 1d-array<boolean>, default None
     |          Can choose to replace values other than NA. Return True for values
     |          that should be updated
     |      raise_conflict : boolean
     |          If True, will raise an error if the DataFrame and other both
     |          contain data in the same place.
     |  
     |  var(self, axis=None, skipna=None, level=None, ddof=1, numeric_only=None, **kwargs)
     |      Return unbiased variance over requested axis.
     |      
     |      Normalized by N-1 by default. This can be changed using the ddof argument
     |      
     |      Parameters
     |      ----------
     |      axis : {index (0), columns (1)}
     |      skipna : boolean, default True
     |          Exclude NA/null values. If an entire row/column is NA, the result
     |          will be NA
     |      level : int or level name, default None
     |          If the axis is a MultiIndex (hierarchical), count along a
     |          particular level, collapsing into a Series
     |      ddof : int, default 1
     |          degrees of freedom
     |      numeric_only : boolean, default None
     |          Include only float, int, boolean columns. If None, will attempt to use
     |          everything, then use only numeric data. Not implemented for Series.
     |      
     |      Returns
     |      -------
     |      var : Series or DataFrame (if level specified)
     |  
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |  
     |  from_csv(path, header=0, sep=',', index_col=0, parse_dates=True, encoding=None, tupleize_cols=False, infer_datetime_format=False) from builtins.type
     |      Read CSV file (DISCOURAGED, please use :func:`pandas.read_csv`
     |      instead).
     |      
     |      It is preferable to use the more powerful :func:`pandas.read_csv`
     |      for most general purposes, but ``from_csv`` makes for an easy
     |      roundtrip to and from a file (the exact counterpart of
     |      ``to_csv``), especially with a DataFrame of time series data.
     |      
     |      This method only differs from the preferred :func:`pandas.read_csv`
     |      in some defaults:
     |      
     |      - `index_col` is ``0`` instead of ``None`` (take first column as index
     |        by default)
     |      - `parse_dates` is ``True`` instead of ``False`` (try parsing the index
     |        as datetime by default)
     |      
     |      So a ``pd.DataFrame.from_csv(path)`` can be replaced by
     |      ``pd.read_csv(path, index_col=0, parse_dates=True)``.
     |      
     |      Parameters
     |      ----------
     |      path : string file path or file handle / StringIO
     |      header : int, default 0
     |          Row to use as header (skip prior rows)
     |      sep : string, default ','
     |          Field delimiter
     |      index_col : int or sequence, default 0
     |          Column to use for index. If a sequence is given, a MultiIndex
     |          is used. Different default from read_table
     |      parse_dates : boolean, default True
     |          Parse dates. Different default from read_table
     |      tupleize_cols : boolean, default False
     |          write multi_index columns as a list of tuples (if True)
     |          or new (expanded format) if False)
     |      infer_datetime_format: boolean, default False
     |          If True and `parse_dates` is True for a column, try to infer the
     |          datetime format based on the first datetime string. If the format
     |          can be inferred, there often will be a large parsing speed-up.
     |      
     |      See also
     |      --------
     |      pandas.read_csv
     |      
     |      Returns
     |      -------
     |      y : DataFrame
     |  
     |  from_dict(data, orient='columns', dtype=None) from builtins.type
     |      Construct DataFrame from dict of array-like or dicts
     |      
     |      Parameters
     |      ----------
     |      data : dict
     |          {field : array-like} or {field : dict}
     |      orient : {'columns', 'index'}, default 'columns'
     |          The "orientation" of the data. If the keys of the passed dict
     |          should be the columns of the resulting DataFrame, pass 'columns'
     |          (default). Otherwise if the keys should be rows, pass 'index'.
     |      dtype : dtype, default None
     |          Data type to force, otherwise infer
     |      
     |      Returns
     |      -------
     |      DataFrame
     |  
     |  from_items(items, columns=None, orient='columns') from builtins.type
     |      Convert (key, value) pairs to DataFrame. The keys will be the axis
     |      index (usually the columns, but depends on the specified
     |      orientation). The values should be arrays or Series.
     |      
     |      Parameters
     |      ----------
     |      items : sequence of (key, value) pairs
     |          Values should be arrays or Series.
     |      columns : sequence of column labels, optional
     |          Must be passed if orient='index'.
     |      orient : {'columns', 'index'}, default 'columns'
     |          The "orientation" of the data. If the keys of the
     |          input correspond to column labels, pass 'columns'
     |          (default). Otherwise if the keys correspond to the index,
     |          pass 'index'.
     |      
     |      Returns
     |      -------
     |      frame : DataFrame
     |  
     |  from_records(data, index=None, exclude=None, columns=None, coerce_float=False, nrows=None) from builtins.type
     |      Convert structured or record ndarray to DataFrame
     |      
     |      Parameters
     |      ----------
     |      data : ndarray (structured dtype), list of tuples, dict, or DataFrame
     |      index : string, list of fields, array-like
     |          Field of array to use as the index, alternately a specific set of
     |          input labels to use
     |      exclude : sequence, default None
     |          Columns or fields to exclude
     |      columns : sequence, default None
     |          Column names to use. If the passed data do not have names
     |          associated with them, this argument provides names for the
     |          columns. Otherwise this argument indicates the order of the columns
     |          in the result (any names not found in the data will become all-NA
     |          columns)
     |      coerce_float : boolean, default False
     |          Attempt to convert values to non-string, non-numeric objects (like
     |          decimal.Decimal) to floating point, useful for SQL result sets
     |      
     |      Returns
     |      -------
     |      df : DataFrame
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  T
     |      Transpose index and columns
     |  
     |  axes
     |      Return a list with the row axis labels and column axis labels as the
     |      only members. They are returned in that order.
     |  
     |  columns
     |  
     |  index
     |  
     |  shape
     |      Return a tuple representing the dimensionality of the DataFrame.
     |  
     |  style
     |      Property returning a Styler object containing methods for
     |      building a styled HTML representation fo the DataFrame.
     |      
     |      See Also
     |      --------
     |      pandas.formats.style.Styler
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  plot = <class 'pandas.tools.plotting.FramePlotMethods'>
     |      DataFrame plotting accessor and method
     |      
     |      Examples
     |      --------
     |      >>> df.plot.line()
     |      >>> df.plot.scatter('x', 'y')
     |      >>> df.plot.hexbin()
     |      
     |      These plotting methods can also be accessed by calling the accessor as a
     |      method with the ``kind`` argument:
     |      ``df.plot(kind='line')`` is equivalent to ``df.plot.line()``
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from pandas.core.generic.NDFrame:
     |  
     |  __abs__(self)
     |  
     |  __array__(self, dtype=None)
     |  
     |  __array_wrap__(self, result, context=None)
     |  
     |  __bool__ = __nonzero__(self)
     |  
     |  __contains__(self, key)
     |      True if the key is in the info axis
     |  
     |  __delitem__(self, key)
     |      Delete item
     |  
     |  __finalize__(self, other, method=None, **kwargs)
     |      Propagate metadata from other to self.
     |      
     |      Parameters
     |      ----------
     |      other : the object from which to get the attributes that we are going
     |          to propagate
     |      method : optional, a passed method name ; possibly to take different
     |          types of propagation actions based on this
     |  
     |  __getattr__(self, name)
     |      After regular attribute access, try looking up the name
     |      This allows simpler access to columns for interactive use.
     |  
     |  __getstate__(self)
     |  
     |  __hash__(self)
     |      Return hash(self).
     |  
     |  __invert__(self)
     |  
     |  __iter__(self)
     |      Iterate over infor axis
     |  
     |  __neg__(self)
     |  
     |  __nonzero__(self)
     |  
     |  __round__(self, decimals=0)
     |  
     |  __setattr__(self, name, value)
     |      After regular attribute access, try setting the name
     |      This allows simpler access to columns for interactive use.
     |  
     |  __setstate__(self, state)
     |  
     |  abs(self)
     |      Return an object with absolute value taken--only applicable to objects
     |      that are all numeric.
     |      
     |      Returns
     |      -------
     |      abs: type of caller
     |  
     |  add_prefix(self, prefix)
     |      Concatenate prefix string with panel items names.
     |      
     |      Parameters
     |      ----------
     |      prefix : string
     |      
     |      Returns
     |      -------
     |      with_prefix : type of caller
     |  
     |  add_suffix(self, suffix)
     |      Concatenate suffix string with panel items names.
     |      
     |      Parameters
     |      ----------
     |      suffix : string
     |      
     |      Returns
     |      -------
     |      with_suffix : type of caller
     |  
     |  as_blocks(self, copy=True)
     |      Convert the frame to a dict of dtype -> Constructor Types that each has
     |      a homogeneous dtype.
     |      
     |      NOTE: the dtypes of the blocks WILL BE PRESERVED HERE (unlike in
     |            as_matrix)
     |      
     |      Parameters
     |      ----------
     |      copy : boolean, default True
     |      
     |             .. versionadded: 0.16.1
     |      
     |      Returns
     |      -------
     |      values : a dict of dtype -> Constructor Types
     |  
     |  as_matrix(self, columns=None)
     |      Convert the frame to its Numpy-array representation.
     |      
     |      Parameters
     |      ----------
     |      columns: list, optional, default:None
     |          If None, return all columns, otherwise, returns specified columns.
     |      
     |      Returns
     |      -------
     |      values : ndarray
     |          If the caller is heterogeneous and contains booleans or objects,
     |          the result will be of dtype=object. See Notes.
     |      
     |      
     |      Notes
     |      -----
     |      Return is NOT a Numpy-matrix, rather, a Numpy-array.
     |      
     |      The dtype will be a lower-common-denominator dtype (implicit
     |      upcasting); that is to say if the dtypes (even of numeric types)
     |      are mixed, the one that accommodates all will be chosen. Use this
     |      with care if you are not dealing with the blocks.
     |      
     |      e.g. If the dtypes are float16 and float32, dtype will be upcast to
     |      float32.  If dtypes are int32 and uint8, dtype will be upcase to
     |      int32. By numpy.find_common_type convention, mixing int64 and uint64
     |      will result in a flot64 dtype.
     |      
     |      This method is provided for backwards compatibility. Generally,
     |      it is recommended to use '.values'.
     |      
     |      See Also
     |      --------
     |      pandas.DataFrame.values
     |  
     |  asfreq(self, freq, method=None, how=None, normalize=False)
     |      Convert TimeSeries to specified frequency.
     |      
     |      Optionally provide filling method to pad/backfill missing values.
     |      
     |      Parameters
     |      ----------
     |      freq : DateOffset object, or string
     |      method : {'backfill'/'bfill', 'pad'/'ffill'}, default None
     |          Method to use for filling holes in reindexed Series (note this
     |          does not fill NaNs that already were present):
     |      
     |          * 'pad' / 'ffill': propagate last valid observation forward to next
     |            valid
     |          * 'backfill' / 'bfill': use NEXT valid observation to fill
     |      how : {'start', 'end'}, default end
     |          For PeriodIndex only, see PeriodIndex.asfreq
     |      normalize : bool, default False
     |          Whether to reset output index to midnight
     |      
     |      Returns
     |      -------
     |      converted : type of caller
     |      
     |      Notes
     |      -----
     |      To learn more about the frequency strings, please see `this link
     |      <http://pandas.pydata.org/pandas-docs/stable/timeseries.html#offset-aliases>`__.
     |  
     |  asof(self, where, subset=None)
     |      The last row without any NaN is taken (or the last row without
     |      NaN considering only the subset of columns in the case of a DataFrame)
     |      
     |      .. versionadded:: 0.19.0 For DataFrame
     |      
     |      If there is no good value, NaN is returned.
     |      
     |      Parameters
     |      ----------
     |      where : date or array of dates
     |      subset : string or list of strings, default None
     |         if not None use these columns for NaN propagation
     |      
     |      Notes
     |      -----
     |      Dates are assumed to be sorted
     |      Raises if this is not the case
     |      
     |      Returns
     |      -------
     |      where is scalar
     |      
     |        - value or NaN if input is Series
     |        - Series if input is DataFrame
     |      
     |      where is Index: same shape object as input
     |      
     |      See Also
     |      --------
     |      merge_asof
     |  
     |  astype(self, dtype, copy=True, raise_on_error=True, **kwargs)
     |      Cast object to input numpy.dtype
     |      Return a copy when copy = True (be really careful with this!)
     |      
     |      Parameters
     |      ----------
     |      dtype : data type, or dict of column name -> data type
     |          Use a numpy.dtype or Python type to cast entire pandas object to
     |          the same type. Alternatively, use {col: dtype, ...}, where col is a
     |          column label and dtype is a numpy.dtype or Python type to cast one
     |          or more of the DataFrame's columns to column-specific types.
     |      raise_on_error : raise on invalid input
     |      kwargs : keyword arguments to pass on to the constructor
     |      
     |      Returns
     |      -------
     |      casted : type of caller
     |  
     |  at_time(self, time, asof=False)
     |      Select values at particular time of day (e.g. 9:30AM).
     |      
     |      Parameters
     |      ----------
     |      time : datetime.time or string
     |      
     |      Returns
     |      -------
     |      values_at_time : type of caller
     |  
     |  between_time(self, start_time, end_time, include_start=True, include_end=True)
     |      Select values between particular times of the day (e.g., 9:00-9:30 AM).
     |      
     |      Parameters
     |      ----------
     |      start_time : datetime.time or string
     |      end_time : datetime.time or string
     |      include_start : boolean, default True
     |      include_end : boolean, default True
     |      
     |      Returns
     |      -------
     |      values_between_time : type of caller
     |  
     |  bfill(self, axis=None, inplace=False, limit=None, downcast=None)
     |      Synonym for NDFrame.fillna(method='bfill')
     |  
     |  bool(self)
     |      Return the bool of a single element PandasObject.
     |      
     |      This must be a boolean scalar value, either True or False.  Raise a
     |      ValueError if the PandasObject does not have exactly 1 element, or that
     |      element is not boolean
     |  
     |  clip(self, lower=None, upper=None, axis=None, *args, **kwargs)
     |      Trim values at input threshold(s).
     |      
     |      Parameters
     |      ----------
     |      lower : float or array_like, default None
     |      upper : float or array_like, default None
     |      axis : int or string axis name, optional
     |          Align object with lower and upper along the given axis.
     |      
     |      Returns
     |      -------
     |      clipped : Series
     |      
     |      Examples
     |      --------
     |      >>> df
     |        0         1
     |      0  0.335232 -1.256177
     |      1 -1.367855  0.746646
     |      2  0.027753 -1.176076
     |      3  0.230930 -0.679613
     |      4  1.261967  0.570967
     |      >>> df.clip(-1.0, 0.5)
     |                0         1
     |      0  0.335232 -1.000000
     |      1 -1.000000  0.500000
     |      2  0.027753 -1.000000
     |      3  0.230930 -0.679613
     |      4  0.500000  0.500000
     |      >>> t
     |      0   -0.3
     |      1   -0.2
     |      2   -0.1
     |      3    0.0
     |      4    0.1
     |      dtype: float64
     |      >>> df.clip(t, t + 1, axis=0)
     |                0         1
     |      0  0.335232 -0.300000
     |      1 -0.200000  0.746646
     |      2  0.027753 -0.100000
     |      3  0.230930  0.000000
     |      4  1.100000  0.570967
     |  
     |  clip_lower(self, threshold, axis=None)
     |      Return copy of the input with values below given value(s) truncated.
     |      
     |      Parameters
     |      ----------
     |      threshold : float or array_like
     |      axis : int or string axis name, optional
     |          Align object with threshold along the given axis.
     |      
     |      See Also
     |      --------
     |      clip
     |      
     |      Returns
     |      -------
     |      clipped : same type as input
     |  
     |  clip_upper(self, threshold, axis=None)
     |      Return copy of input with values above given value(s) truncated.
     |      
     |      Parameters
     |      ----------
     |      threshold : float or array_like
     |      axis : int or string axis name, optional
     |          Align object with threshold along the given axis.
     |      
     |      See Also
     |      --------
     |      clip
     |      
     |      Returns
     |      -------
     |      clipped : same type as input
     |  
     |  consolidate(self, inplace=False)
     |      Compute NDFrame with "consolidated" internals (data of each dtype
     |      grouped together in a single ndarray). Mainly an internal API function,
     |      but available here to the savvy user
     |      
     |      Parameters
     |      ----------
     |      inplace : boolean, default False
     |          If False return new object, otherwise modify existing object
     |      
     |      Returns
     |      -------
     |      consolidated : type of caller
     |  
     |  convert_objects(self, convert_dates=True, convert_numeric=False, convert_timedeltas=True, copy=True)
     |      Deprecated.
     |      
     |      Attempt to infer better dtype for object columns
     |      
     |      Parameters
     |      ----------
     |      convert_dates : boolean, default True
     |          If True, convert to date where possible. If 'coerce', force
     |          conversion, with unconvertible values becoming NaT.
     |      convert_numeric : boolean, default False
     |          If True, attempt to coerce to numbers (including strings), with
     |          unconvertible values becoming NaN.
     |      convert_timedeltas : boolean, default True
     |          If True, convert to timedelta where possible. If 'coerce', force
     |          conversion, with unconvertible values becoming NaT.
     |      copy : boolean, default True
     |          If True, return a copy even if no copy is necessary (e.g. no
     |          conversion was done). Note: This is meant for internal use, and
     |          should not be confused with inplace.
     |      
     |      See Also
     |      --------
     |      pandas.to_datetime : Convert argument to datetime.
     |      pandas.to_timedelta : Convert argument to timedelta.
     |      pandas.to_numeric : Return a fixed frequency timedelta index,
     |          with day as the default.
     |      
     |      Returns
     |      -------
     |      converted : same as input object
     |  
     |  copy(self, deep=True)
     |      Make a copy of this objects data.
     |      
     |      Parameters
     |      ----------
     |      deep : boolean or string, default True
     |          Make a deep copy, including a copy of the data and the indices.
     |          With ``deep=False`` neither the indices or the data are copied.
     |      
     |          Note that when ``deep=True`` data is copied, actual python objects
     |          will not be copied recursively, only the reference to the object.
     |          This is in contrast to ``copy.deepcopy`` in the Standard Library,
     |          which recursively copies object data.
     |      
     |      Returns
     |      -------
     |      copy : type of caller
     |  
     |  describe(self, percentiles=None, include=None, exclude=None)
     |      Generate various summary statistics, excluding NaN values.
     |      
     |      Parameters
     |      ----------
     |      percentiles : array-like, optional
     |          The percentiles to include in the output. Should all
     |          be in the interval [0, 1]. By default `percentiles` is
     |          [.25, .5, .75], returning the 25th, 50th, and 75th percentiles.
     |      include, exclude : list-like, 'all', or None (default)
     |          Specify the form of the returned result. Either:
     |      
     |          - None to both (default). The result will include only
     |            numeric-typed columns or, if none are, only categorical columns.
     |          - A list of dtypes or strings to be included/excluded.
     |            To select all numeric types use numpy numpy.number. To select
     |            categorical objects use type object. See also the select_dtypes
     |            documentation. eg. df.describe(include=['O'])
     |          - If include is the string 'all', the output column-set will
     |            match the input one.
     |      
     |      Returns
     |      -------
     |      summary: NDFrame of summary statistics
     |      
     |      Notes
     |      -----
     |      The output DataFrame index depends on the requested dtypes:
     |      
     |      For numeric dtypes, it will include: count, mean, std, min,
     |      max, and lower, 50, and upper percentiles.
     |      
     |      For object dtypes (e.g. timestamps or strings), the index
     |      will include the count, unique, most common, and frequency of the
     |      most common. Timestamps also include the first and last items.
     |      
     |      For mixed dtypes, the index will be the union of the corresponding
     |      output types. Non-applicable entries will be filled with NaN.
     |      Note that mixed-dtype outputs can only be returned from mixed-dtype
     |      inputs and appropriate use of the include/exclude arguments.
     |      
     |      If multiple values have the highest count, then the
     |      `count` and `most common` pair will be arbitrarily chosen from
     |      among those with the highest count.
     |      
     |      The include, exclude arguments are ignored for Series.
     |      
     |      See Also
     |      --------
     |      DataFrame.select_dtypes
     |  
     |  drop(self, labels, axis=0, level=None, inplace=False, errors='raise')
     |      Return new object with labels in requested axis removed.
     |      
     |      Parameters
     |      ----------
     |      labels : single label or list-like
     |      axis : int or axis name
     |      level : int or level name, default None
     |          For MultiIndex
     |      inplace : bool, default False
     |          If True, do operation inplace and return None.
     |      errors : {'ignore', 'raise'}, default 'raise'
     |          If 'ignore', suppress error and existing labels are dropped.
     |      
     |          .. versionadded:: 0.16.1
     |      
     |      Returns
     |      -------
     |      dropped : type of caller
     |  
     |  equals(self, other)
     |      Determines if two NDFrame objects contain the same elements. NaNs in
     |      the same location are considered equal.
     |  
     |  ffill(self, axis=None, inplace=False, limit=None, downcast=None)
     |      Synonym for NDFrame.fillna(method='ffill')
     |  
     |  filter(self, items=None, like=None, regex=None, axis=None)
     |      Subset rows or columns of dataframe according to labels in
     |      the specified index.
     |      
     |      Note that this routine does not filter a dataframe on its
     |      contents. The filter is applied to the labels of the index.
     |      
     |      Parameters
     |      ----------
     |      items : list-like
     |          List of info axis to restrict to (must not all be present)
     |      like : string
     |          Keep info axis where "arg in col == True"
     |      regex : string (regular expression)
     |          Keep info axis with re.search(regex, col) == True
     |      axis : int or string axis name
     |          The axis to filter on.  By default this is the info axis,
     |          'index' for Series, 'columns' for DataFrame
     |      
     |      Returns
     |      -------
     |      same type as input object
     |      
     |      Examples
     |      --------
     |      >>> df
     |      one  two  three
     |      mouse     1    2      3
     |      rabbit    4    5      6
     |      
     |      >>> # select columns by name
     |      >>> df.filter(items=['one', 'three'])
     |      one  three
     |      mouse     1      3
     |      rabbit    4      6
     |      
     |      >>> # select columns by regular expression
     |      >>> df.filter(regex='e$', axis=1)
     |      one  three
     |      mouse     1      3
     |      rabbit    4      6
     |      
     |      >>> # select rows containing 'bbi'
     |      >>> df.filter(like='bbi', axis=0)
     |      one  two  three
     |      rabbit    4    5      6
     |      
     |      See Also
     |      --------
     |      pandas.DataFrame.select
     |      
     |      Notes
     |      -----
     |      The ``items``, ``like``, and ``regex`` parameters are
     |      enforced to be mutually exclusive.
     |      
     |      ``axis`` defaults to the info axis that is used when indexing
     |      with ``[]``.
     |  
     |  first(self, offset)
     |      Convenience method for subsetting initial periods of time series data
     |      based on a date offset.
     |      
     |      Parameters
     |      ----------
     |      offset : string, DateOffset, dateutil.relativedelta
     |      
     |      Examples
     |      --------
     |      ts.first('10D') -> First 10 days
     |      
     |      Returns
     |      -------
     |      subset : type of caller
     |  
     |  get(self, key, default=None)
     |      Get item from object for given key (DataFrame column, Panel slice,
     |      etc.). Returns default value if not found.
     |      
     |      Parameters
     |      ----------
     |      key : object
     |      
     |      Returns
     |      -------
     |      value : type of items contained in object
     |  
     |  get_dtype_counts(self)
     |      Return the counts of dtypes in this object.
     |  
     |  get_ftype_counts(self)
     |      Return the counts of ftypes in this object.
     |  
     |  get_values(self)
     |      same as values (but handles sparseness conversions)
     |  
     |  groupby(self, by=None, axis=0, level=None, as_index=True, sort=True, group_keys=True, squeeze=False, **kwargs)
     |      Group series using mapper (dict or key function, apply given function
     |      to group, return result as series) or by a series of columns.
     |      
     |      Parameters
     |      ----------
     |      by : mapping function / list of functions, dict, Series, or tuple /
     |          list of column names.
     |          Called on each element of the object index to determine the groups.
     |          If a dict or Series is passed, the Series or dict VALUES will be
     |          used to determine the groups
     |      axis : int, default 0
     |      level : int, level name, or sequence of such, default None
     |          If the axis is a MultiIndex (hierarchical), group by a particular
     |          level or levels
     |      as_index : boolean, default True
     |          For aggregated output, return object with group labels as the
     |          index. Only relevant for DataFrame input. as_index=False is
     |          effectively "SQL-style" grouped output
     |      sort : boolean, default True
     |          Sort group keys. Get better performance by turning this off.
     |          Note this does not influence the order of observations within each
     |          group.  groupby preserves the order of rows within each group.
     |      group_keys : boolean, default True
     |          When calling apply, add group keys to index to identify pieces
     |      squeeze : boolean, default False
     |          reduce the dimensionality of the return type if possible,
     |          otherwise return a consistent type
     |      
     |      Examples
     |      --------
     |      DataFrame results
     |      
     |      >>> data.groupby(func, axis=0).mean()
     |      >>> data.groupby(['col1', 'col2'])['col3'].mean()
     |      
     |      DataFrame with hierarchical index
     |      
     |      >>> data.groupby(['col1', 'col2']).mean()
     |      
     |      Returns
     |      -------
     |      GroupBy object
     |  
     |  head(self, n=5)
     |      Returns first n rows
     |  
     |  interpolate(self, method='linear', axis=0, limit=None, inplace=False, limit_direction='forward', downcast=None, **kwargs)
     |      Interpolate values according to different methods.
     |      
     |      Please note that only ``method='linear'`` is supported for
     |      DataFrames/Series with a MultiIndex.
     |      
     |      Parameters
     |      ----------
     |      method : {'linear', 'time', 'index', 'values', 'nearest', 'zero',
     |                'slinear', 'quadratic', 'cubic', 'barycentric', 'krogh',
     |                'polynomial', 'spline', 'piecewise_polynomial',
     |                'from_derivatives', 'pchip', 'akima'}
     |      
     |          * 'linear': ignore the index and treat the values as equally
     |            spaced. This is the only method supported on MultiIndexes.
     |            default
     |          * 'time': interpolation works on daily and higher resolution
     |            data to interpolate given length of interval
     |          * 'index', 'values': use the actual numerical values of the index
     |          * 'nearest', 'zero', 'slinear', 'quadratic', 'cubic',
     |            'barycentric', 'polynomial' is passed to
     |            ``scipy.interpolate.interp1d``. Both 'polynomial' and 'spline'
     |            require that you also specify an `order` (int),
     |            e.g. df.interpolate(method='polynomial', order=4).
     |            These use the actual numerical values of the index.
     |          * 'krogh', 'piecewise_polynomial', 'spline', 'pchip' and 'akima' are all
     |            wrappers around the scipy interpolation methods of similar
     |            names. These use the actual numerical values of the index. See
     |            the scipy documentation for more on their behavior
     |            `here <http://docs.scipy.org/doc/scipy/reference/interpolate.html#univariate-interpolation>`__  # noqa
     |            `and here <http://docs.scipy.org/doc/scipy/reference/tutorial/interpolate.html>`__  # noqa
     |          * 'from_derivatives' refers to BPoly.from_derivatives which
     |            replaces 'piecewise_polynomial' interpolation method in scipy 0.18
     |      
     |          .. versionadded:: 0.18.1
     |      
     |             Added support for the 'akima' method
     |             Added interpolate method 'from_derivatives' which replaces
     |             'piecewise_polynomial' in scipy 0.18; backwards-compatible with
     |             scipy < 0.18
     |      
     |      axis : {0, 1}, default 0
     |          * 0: fill column-by-column
     |          * 1: fill row-by-row
     |      limit : int, default None.
     |          Maximum number of consecutive NaNs to fill.
     |      limit_direction : {'forward', 'backward', 'both'}, defaults to 'forward'
     |          If limit is specified, consecutive NaNs will be filled in this
     |          direction.
     |      
     |          .. versionadded:: 0.17.0
     |      
     |      inplace : bool, default False
     |          Update the NDFrame in place if possible.
     |      downcast : optional, 'infer' or None, defaults to None
     |          Downcast dtypes if possible.
     |      kwargs : keyword arguments to pass on to the interpolating function.
     |      
     |      Returns
     |      -------
     |      Series or DataFrame of same shape interpolated at the NaNs
     |      
     |      See Also
     |      --------
     |      reindex, replace, fillna
     |      
     |      Examples
     |      --------
     |      
     |      Filling in NaNs
     |      
     |      >>> s = pd.Series([0, 1, np.nan, 3])
     |      >>> s.interpolate()
     |      0    0
     |      1    1
     |      2    2
     |      3    3
     |      dtype: float64
     |  
     |  isnull(self)
     |      Return a boolean same-sized object indicating if the values are null.
     |      
     |      See Also
     |      --------
     |      notnull : boolean inverse of isnull
     |  
     |  iterkv(self, *args, **kwargs)
     |      iteritems alias used to get around 2to3. Deprecated
     |  
     |  keys(self)
     |      Get the 'info axis' (see Indexing for more)
     |      
     |      This is index for Series, columns for DataFrame and major_axis for
     |      Panel.
     |  
     |  last(self, offset)
     |      Convenience method for subsetting final periods of time series data
     |      based on a date offset.
     |      
     |      Parameters
     |      ----------
     |      offset : string, DateOffset, dateutil.relativedelta
     |      
     |      Examples
     |      --------
     |      ts.last('5M') -> Last 5 months
     |      
     |      Returns
     |      -------
     |      subset : type of caller
     |  
     |  mask(self, cond, other=nan, inplace=False, axis=None, level=None, try_cast=False, raise_on_error=True)
     |      Return an object of same shape as self and whose corresponding
     |      entries are from self where cond is False and otherwise are from
     |      other.
     |      
     |      Parameters
     |      ----------
     |      cond : boolean NDFrame, array or callable
     |          If cond is callable, it is computed on the NDFrame and
     |          should return boolean NDFrame or array.
     |          The callable must not change input NDFrame
     |          (though pandas doesn't check it).
     |      
     |          .. versionadded:: 0.18.1
     |      
     |          A callable can be used as cond.
     |      
     |      other : scalar, NDFrame, or callable
     |          If other is callable, it is computed on the NDFrame and
     |          should return scalar or NDFrame.
     |          The callable must not change input NDFrame
     |          (though pandas doesn't check it).
     |      
     |          .. versionadded:: 0.18.1
     |      
     |          A callable can be used as other.
     |      
     |      inplace : boolean, default False
     |          Whether to perform the operation in place on the data
     |      axis : alignment axis if needed, default None
     |      level : alignment level if needed, default None
     |      try_cast : boolean, default False
     |          try to cast the result back to the input type (if possible),
     |      raise_on_error : boolean, default True
     |          Whether to raise on invalid data types (e.g. trying to where on
     |          strings)
     |      
     |      Returns
     |      -------
     |      wh : same type as caller
     |      
     |      Notes
     |      -----
     |      The mask method is an application of the if-then idiom. For each
     |      element in the calling DataFrame, if ``cond`` is ``False`` the
     |      element is used; otherwise the corresponding element from the DataFrame
     |      ``other`` is used.
     |      
     |      The signature for :func:`DataFrame.where` differs from
     |      :func:`numpy.where`. Roughly ``df1.where(m, df2)`` is equivalent to
     |      ``np.where(m, df1, df2)``.
     |      
     |      For further details and examples see the ``mask`` documentation in
     |      :ref:`indexing <indexing.where_mask>`.
     |      
     |      Examples
     |      --------
     |      >>> s = pd.Series(range(5))
     |      >>> s.where(s > 0)
     |      0    NaN
     |      1    1.0
     |      2    2.0
     |      3    3.0
     |      4    4.0
     |      
     |      >>> df = pd.DataFrame(np.arange(10).reshape(-1, 2), columns=['A', 'B'])
     |      >>> m = df % 3 == 0
     |      >>> df.where(m, -df)
     |         A  B
     |      0  0 -1
     |      1 -2  3
     |      2 -4 -5
     |      3  6 -7
     |      4 -8  9
     |      >>> df.where(m, -df) == np.where(m, df, -df)
     |            A     B
     |      0  True  True
     |      1  True  True
     |      2  True  True
     |      3  True  True
     |      4  True  True
     |      >>> df.where(m, -df) == df.mask(~m, -df)
     |            A     B
     |      0  True  True
     |      1  True  True
     |      2  True  True
     |      3  True  True
     |      4  True  True
     |      
     |      See Also
     |      --------
     |      :func:`DataFrame.where`
     |  
     |  notnull(self)
     |      Return a boolean same-sized object indicating if the values are
     |      not null.
     |      
     |      See Also
     |      --------
     |      isnull : boolean inverse of notnull
     |  
     |  pct_change(self, periods=1, fill_method='pad', limit=None, freq=None, **kwargs)
     |      Percent change over given number of periods.
     |      
     |      Parameters
     |      ----------
     |      periods : int, default 1
     |          Periods to shift for forming percent change
     |      fill_method : str, default 'pad'
     |          How to handle NAs before computing percent changes
     |      limit : int, default None
     |          The number of consecutive NAs to fill before stopping
     |      freq : DateOffset, timedelta, or offset alias string, optional
     |          Increment to use from time series API (e.g. 'M' or BDay())
     |      
     |      Returns
     |      -------
     |      chg : NDFrame
     |      
     |      Notes
     |      -----
     |      
     |      By default, the percentage change is calculated along the stat
     |      axis: 0, or ``Index``, for ``DataFrame`` and 1, or ``minor`` for
     |      ``Panel``. You can change this with the ``axis`` keyword argument.
     |  
     |  pipe(self, func, *args, **kwargs)
     |      Apply func(self, \*args, \*\*kwargs)
     |      
     |      .. versionadded:: 0.16.2
     |      
     |      Parameters
     |      ----------
     |      func : function
     |          function to apply to the NDFrame.
     |          ``args``, and ``kwargs`` are passed into ``func``.
     |          Alternatively a ``(callable, data_keyword)`` tuple where
     |          ``data_keyword`` is a string indicating the keyword of
     |          ``callable`` that expects the NDFrame.
     |      args : positional arguments passed into ``func``.
     |      kwargs : a dictionary of keyword arguments passed into ``func``.
     |      
     |      Returns
     |      -------
     |      object : the return type of ``func``.
     |      
     |      Notes
     |      -----
     |      
     |      Use ``.pipe`` when chaining together functions that expect
     |      on Series or DataFrames. Instead of writing
     |      
     |      >>> f(g(h(df), arg1=a), arg2=b, arg3=c)
     |      
     |      You can write
     |      
     |      >>> (df.pipe(h)
     |      ...    .pipe(g, arg1=a)
     |      ...    .pipe(f, arg2=b, arg3=c)
     |      ... )
     |      
     |      If you have a function that takes the data as (say) the second
     |      argument, pass a tuple indicating which keyword expects the
     |      data. For example, suppose ``f`` takes its data as ``arg2``:
     |      
     |      >>> (df.pipe(h)
     |      ...    .pipe(g, arg1=a)
     |      ...    .pipe((f, 'arg2'), arg1=a, arg3=c)
     |      ...  )
     |      
     |      See Also
     |      --------
     |      pandas.DataFrame.apply
     |      pandas.DataFrame.applymap
     |      pandas.Series.map
     |  
     |  pop(self, item)
     |      Return item and drop from frame. Raise KeyError if not found.
     |  
     |  rank(self, axis=0, method='average', numeric_only=None, na_option='keep', ascending=True, pct=False)
     |      Compute numerical data ranks (1 through n) along axis. Equal values are
     |      assigned a rank that is the average of the ranks of those values
     |      
     |      Parameters
     |      ----------
     |      axis: {0 or 'index', 1 or 'columns'}, default 0
     |          index to direct ranking
     |      method : {'average', 'min', 'max', 'first', 'dense'}
     |          * average: average rank of group
     |          * min: lowest rank in group
     |          * max: highest rank in group
     |          * first: ranks assigned in order they appear in the array
     |          * dense: like 'min', but rank always increases by 1 between groups
     |      numeric_only : boolean, default None
     |          Include only float, int, boolean data. Valid only for DataFrame or
     |          Panel objects
     |      na_option : {'keep', 'top', 'bottom'}
     |          * keep: leave NA values where they are
     |          * top: smallest rank if ascending
     |          * bottom: smallest rank if descending
     |      ascending : boolean, default True
     |          False for ranks by high (1) to low (N)
     |      pct : boolean, default False
     |          Computes percentage rank of data
     |      
     |      Returns
     |      -------
     |      ranks : same type as caller
     |  
     |  reindex_like(self, other, method=None, copy=True, limit=None, tolerance=None)
     |      Return an object with matching indices to myself.
     |      
     |      Parameters
     |      ----------
     |      other : Object
     |      method : string or None
     |      copy : boolean, default True
     |      limit : int, default None
     |          Maximum number of consecutive labels to fill for inexact matches.
     |      tolerance : optional
     |          Maximum distance between labels of the other object and this
     |          object for inexact matches.
     |      
     |          .. versionadded:: 0.17.0
     |      
     |      Notes
     |      -----
     |      Like calling s.reindex(index=other.index, columns=other.columns,
     |                             method=...)
     |      
     |      Returns
     |      -------
     |      reindexed : same as input
     |  
     |  rename_axis(self, mapper, axis=0, copy=True, inplace=False)
     |      Alter index and / or columns using input function or functions.
     |      A scaler or list-like for ``mapper`` will alter the ``Index.name``
     |      or ``MultiIndex.names`` attribute.
     |      A function or dict for ``mapper`` will alter the labels.
     |      Function / dict values must be unique (1-to-1). Labels not contained in
     |      a dict / Series will be left as-is.
     |      
     |      Parameters
     |      ----------
     |      mapper : scalar, list-like, dict-like or function, optional
     |      axis : int or string, default 0
     |      copy : boolean, default True
     |          Also copy underlying data
     |      inplace : boolean, default False
     |      
     |      Returns
     |      -------
     |      renamed : type of caller
     |      
     |      See Also
     |      --------
     |      pandas.NDFrame.rename
     |      pandas.Index.rename
     |      
     |      Examples
     |      --------
     |      >>> df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
     |      >>> df.rename_axis("foo")  # scalar, alters df.index.name
     |           A  B
     |      foo
     |      0    1  4
     |      1    2  5
     |      2    3  6
     |      >>> df.rename_axis(lambda x: 2 * x)  # function: alters labels
     |         A  B
     |      0  1  4
     |      2  2  5
     |      4  3  6
     |      >>> df.rename_axis({"A": "ehh", "C": "see"}, axis="columns")  # mapping
     |         ehh  B
     |      0    1  4
     |      1    2  5
     |      2    3  6
     |  
     |  replace(self, to_replace=None, value=None, inplace=False, limit=None, regex=False, method='pad', axis=None)
     |      Replace values given in 'to_replace' with 'value'.
     |      
     |      Parameters
     |      ----------
     |      to_replace : str, regex, list, dict, Series, numeric, or None
     |      
     |          * str or regex:
     |      
     |              - str: string exactly matching `to_replace` will be replaced
     |                with `value`
     |              - regex: regexs matching `to_replace` will be replaced with
     |                `value`
     |      
     |          * list of str, regex, or numeric:
     |      
     |              - First, if `to_replace` and `value` are both lists, they
     |                **must** be the same length.
     |              - Second, if ``regex=True`` then all of the strings in **both**
     |                lists will be interpreted as regexs otherwise they will match
     |                directly. This doesn't matter much for `value` since there
     |                are only a few possible substitution regexes you can use.
     |              - str and regex rules apply as above.
     |      
     |          * dict:
     |      
     |              - Nested dictionaries, e.g., {'a': {'b': nan}}, are read as
     |                follows: look in column 'a' for the value 'b' and replace it
     |                with nan. You can nest regular expressions as well. Note that
     |                column names (the top-level dictionary keys in a nested
     |                dictionary) **cannot** be regular expressions.
     |              - Keys map to column names and values map to substitution
     |                values. You can treat this as a special case of passing two
     |                lists except that you are specifying the column to search in.
     |      
     |          * None:
     |      
     |              - This means that the ``regex`` argument must be a string,
     |                compiled regular expression, or list, dict, ndarray or Series
     |                of such elements. If `value` is also ``None`` then this
     |                **must** be a nested dictionary or ``Series``.
     |      
     |          See the examples section for examples of each of these.
     |      value : scalar, dict, list, str, regex, default None
     |          Value to use to fill holes (e.g. 0), alternately a dict of values
     |          specifying which value to use for each column (columns not in the
     |          dict will not be filled). Regular expressions, strings and lists or
     |          dicts of such objects are also allowed.
     |      inplace : boolean, default False
     |          If True, in place. Note: this will modify any
     |          other views on this object (e.g. a column form a DataFrame).
     |          Returns the caller if this is True.
     |      limit : int, default None
     |          Maximum size gap to forward or backward fill
     |      regex : bool or same types as `to_replace`, default False
     |          Whether to interpret `to_replace` and/or `value` as regular
     |          expressions. If this is ``True`` then `to_replace` *must* be a
     |          string. Otherwise, `to_replace` must be ``None`` because this
     |          parameter will be interpreted as a regular expression or a list,
     |          dict, or array of regular expressions.
     |      method : string, optional, {'pad', 'ffill', 'bfill'}
     |          The method to use when for replacement, when ``to_replace`` is a
     |          ``list``.
     |      
     |      See Also
     |      --------
     |      NDFrame.reindex
     |      NDFrame.asfreq
     |      NDFrame.fillna
     |      
     |      Returns
     |      -------
     |      filled : NDFrame
     |      
     |      Raises
     |      ------
     |      AssertionError
     |          * If `regex` is not a ``bool`` and `to_replace` is not ``None``.
     |      TypeError
     |          * If `to_replace` is a ``dict`` and `value` is not a ``list``,
     |            ``dict``, ``ndarray``, or ``Series``
     |          * If `to_replace` is ``None`` and `regex` is not compilable into a
     |            regular expression or is a list, dict, ndarray, or Series.
     |      ValueError
     |          * If `to_replace` and `value` are ``list`` s or ``ndarray`` s, but
     |            they are not the same length.
     |      
     |      Notes
     |      -----
     |      * Regex substitution is performed under the hood with ``re.sub``. The
     |        rules for substitution for ``re.sub`` are the same.
     |      * Regular expressions will only substitute on strings, meaning you
     |        cannot provide, for example, a regular expression matching floating
     |        point numbers and expect the columns in your frame that have a
     |        numeric dtype to be matched. However, if those floating point numbers
     |        *are* strings, then you can do this.
     |      * This method has *a lot* of options. You are encouraged to experiment
     |        and play with this method to gain intuition about how it works.
     |  
     |  resample(self, rule, how=None, axis=0, fill_method=None, closed=None, label=None, convention='start', kind=None, loffset=None, limit=None, base=0, on=None, level=None)
     |      Convenience method for frequency conversion and resampling of time
     |      series.  Object must have a datetime-like index (DatetimeIndex,
     |      PeriodIndex, or TimedeltaIndex), or pass datetime-like values
     |      to the on or level keyword.
     |      
     |      Parameters
     |      ----------
     |      rule : string
     |          the offset string or object representing target conversion
     |      axis : int, optional, default 0
     |      closed : {'right', 'left'}
     |          Which side of bin interval is closed
     |      label : {'right', 'left'}
     |          Which bin edge label to label bucket with
     |      convention : {'start', 'end', 's', 'e'}
     |      loffset : timedelta
     |          Adjust the resampled time labels
     |      base : int, default 0
     |          For frequencies that evenly subdivide 1 day, the "origin" of the
     |          aggregated intervals. For example, for '5min' frequency, base could
     |          range from 0 through 4. Defaults to 0
     |      on : string, optional
     |          For a DataFrame, column to use instead of index for resampling.
     |          Column must be datetime-like.
     |      
     |          .. versionadded:: 0.19.0
     |      
     |      level : string or int, optional
     |          For a MultiIndex, level (name or number) to use for
     |          resampling.  Level must be datetime-like.
     |      
     |          .. versionadded:: 0.19.0
     |      
     |      To learn more about the offset strings, please see `this link
     |      <http://pandas.pydata.org/pandas-docs/stable/timeseries.html#offset-aliases>`__.
     |      
     |      Examples
     |      --------
     |      
     |      Start by creating a series with 9 one minute timestamps.
     |      
     |      >>> index = pd.date_range('1/1/2000', periods=9, freq='T')
     |      >>> series = pd.Series(range(9), index=index)
     |      >>> series
     |      2000-01-01 00:00:00    0
     |      2000-01-01 00:01:00    1
     |      2000-01-01 00:02:00    2
     |      2000-01-01 00:03:00    3
     |      2000-01-01 00:04:00    4
     |      2000-01-01 00:05:00    5
     |      2000-01-01 00:06:00    6
     |      2000-01-01 00:07:00    7
     |      2000-01-01 00:08:00    8
     |      Freq: T, dtype: int64
     |      
     |      Downsample the series into 3 minute bins and sum the values
     |      of the timestamps falling into a bin.
     |      
     |      >>> series.resample('3T').sum()
     |      2000-01-01 00:00:00     3
     |      2000-01-01 00:03:00    12
     |      2000-01-01 00:06:00    21
     |      Freq: 3T, dtype: int64
     |      
     |      Downsample the series into 3 minute bins as above, but label each
     |      bin using the right edge instead of the left. Please note that the
     |      value in the bucket used as the label is not included in the bucket,
     |      which it labels. For example, in the original series the
     |      bucket ``2000-01-01 00:03:00`` contains the value 3, but the summed
     |      value in the resampled bucket with the label``2000-01-01 00:03:00``
     |      does not include 3 (if it did, the summed value would be 6, not 3).
     |      To include this value close the right side of the bin interval as
     |      illustrated in the example below this one.
     |      
     |      >>> series.resample('3T', label='right').sum()
     |      2000-01-01 00:03:00     3
     |      2000-01-01 00:06:00    12
     |      2000-01-01 00:09:00    21
     |      Freq: 3T, dtype: int64
     |      
     |      Downsample the series into 3 minute bins as above, but close the right
     |      side of the bin interval.
     |      
     |      >>> series.resample('3T', label='right', closed='right').sum()
     |      2000-01-01 00:00:00     0
     |      2000-01-01 00:03:00     6
     |      2000-01-01 00:06:00    15
     |      2000-01-01 00:09:00    15
     |      Freq: 3T, dtype: int64
     |      
     |      Upsample the series into 30 second bins.
     |      
     |      >>> series.resample('30S').asfreq()[0:5] #select first 5 rows
     |      2000-01-01 00:00:00     0
     |      2000-01-01 00:00:30   NaN
     |      2000-01-01 00:01:00     1
     |      2000-01-01 00:01:30   NaN
     |      2000-01-01 00:02:00     2
     |      Freq: 30S, dtype: float64
     |      
     |      Upsample the series into 30 second bins and fill the ``NaN``
     |      values using the ``pad`` method.
     |      
     |      >>> series.resample('30S').pad()[0:5]
     |      2000-01-01 00:00:00    0
     |      2000-01-01 00:00:30    0
     |      2000-01-01 00:01:00    1
     |      2000-01-01 00:01:30    1
     |      2000-01-01 00:02:00    2
     |      Freq: 30S, dtype: int64
     |      
     |      Upsample the series into 30 second bins and fill the
     |      ``NaN`` values using the ``bfill`` method.
     |      
     |      >>> series.resample('30S').bfill()[0:5]
     |      2000-01-01 00:00:00    0
     |      2000-01-01 00:00:30    1
     |      2000-01-01 00:01:00    1
     |      2000-01-01 00:01:30    2
     |      2000-01-01 00:02:00    2
     |      Freq: 30S, dtype: int64
     |      
     |      Pass a custom function via ``apply``
     |      
     |      >>> def custom_resampler(array_like):
     |      ...     return np.sum(array_like)+5
     |      
     |      >>> series.resample('3T').apply(custom_resampler)
     |      2000-01-01 00:00:00     8
     |      2000-01-01 00:03:00    17
     |      2000-01-01 00:06:00    26
     |      Freq: 3T, dtype: int64
     |  
     |  sample(self, n=None, frac=None, replace=False, weights=None, random_state=None, axis=None)
     |      Returns a random sample of items from an axis of object.
     |      
     |      .. versionadded:: 0.16.1
     |      
     |      Parameters
     |      ----------
     |      n : int, optional
     |          Number of items from axis to return. Cannot be used with `frac`.
     |          Default = 1 if `frac` = None.
     |      frac : float, optional
     |          Fraction of axis items to return. Cannot be used with `n`.
     |      replace : boolean, optional
     |          Sample with or without replacement. Default = False.
     |      weights : str or ndarray-like, optional
     |          Default 'None' results in equal probability weighting.
     |          If passed a Series, will align with target object on index. Index
     |          values in weights not found in sampled object will be ignored and
     |          index values in sampled object not in weights will be assigned
     |          weights of zero.
     |          If called on a DataFrame, will accept the name of a column
     |          when axis = 0.
     |          Unless weights are a Series, weights must be same length as axis
     |          being sampled.
     |          If weights do not sum to 1, they will be normalized to sum to 1.
     |          Missing values in the weights column will be treated as zero.
     |          inf and -inf values not allowed.
     |      random_state : int or numpy.random.RandomState, optional
     |          Seed for the random number generator (if int), or numpy RandomState
     |          object.
     |      axis : int or string, optional
     |          Axis to sample. Accepts axis number or name. Default is stat axis
     |          for given data type (0 for Series and DataFrames, 1 for Panels).
     |      
     |      Returns
     |      -------
     |      A new object of same type as caller.
     |      
     |      Examples
     |      --------
     |      
     |      Generate an example ``Series`` and ``DataFrame``:
     |      
     |      >>> s = pd.Series(np.random.randn(50))
     |      >>> s.head()
     |      0   -0.038497
     |      1    1.820773
     |      2   -0.972766
     |      3   -1.598270
     |      4   -1.095526
     |      dtype: float64
     |      >>> df = pd.DataFrame(np.random.randn(50, 4), columns=list('ABCD'))
     |      >>> df.head()
     |                A         B         C         D
     |      0  0.016443 -2.318952 -0.566372 -1.028078
     |      1 -1.051921  0.438836  0.658280 -0.175797
     |      2 -1.243569 -0.364626 -0.215065  0.057736
     |      3  1.768216  0.404512 -0.385604 -1.457834
     |      4  1.072446 -1.137172  0.314194 -0.046661
     |      
     |      Next extract a random sample from both of these objects...
     |      
     |      3 random elements from the ``Series``:
     |      
     |      >>> s.sample(n=3)
     |      27   -0.994689
     |      55   -1.049016
     |      67   -0.224565
     |      dtype: float64
     |      
     |      And a random 10% of the ``DataFrame`` with replacement:
     |      
     |      >>> df.sample(frac=0.1, replace=True)
     |                 A         B         C         D
     |      35  1.981780  0.142106  1.817165 -0.290805
     |      49 -1.336199 -0.448634 -0.789640  0.217116
     |      40  0.823173 -0.078816  1.009536  1.015108
     |      15  1.421154 -0.055301 -1.922594 -0.019696
     |      6  -0.148339  0.832938  1.787600 -1.383767
     |  
     |  select(self, crit, axis=0)
     |      Return data corresponding to axis labels matching criteria
     |      
     |      Parameters
     |      ----------
     |      crit : function
     |          To be called on each index (label). Should return True or False
     |      axis : int
     |      
     |      Returns
     |      -------
     |      selection : type of caller
     |  
     |  set_axis(self, axis, labels)
     |      public verson of axis assignment
     |  
     |  slice_shift(self, periods=1, axis=0)
     |      Equivalent to `shift` without copying data. The shifted data will
     |      not include the dropped periods and the shifted axis will be smaller
     |      than the original.
     |      
     |      Parameters
     |      ----------
     |      periods : int
     |          Number of periods to move, can be positive or negative
     |      
     |      Notes
     |      -----
     |      While the `slice_shift` is faster than `shift`, you may pay for it
     |      later during alignment.
     |      
     |      Returns
     |      -------
     |      shifted : same type as caller
     |  
     |  squeeze(self, **kwargs)
     |      Squeeze length 1 dimensions.
     |  
     |  swapaxes(self, axis1, axis2, copy=True)
     |      Interchange axes and swap values axes appropriately
     |      
     |      Returns
     |      -------
     |      y : same as input
     |  
     |  tail(self, n=5)
     |      Returns last n rows
     |  
     |  take(self, indices, axis=0, convert=True, is_copy=True, **kwargs)
     |      Analogous to ndarray.take
     |      
     |      Parameters
     |      ----------
     |      indices : list / array of ints
     |      axis : int, default 0
     |      convert : translate neg to pos indices (default)
     |      is_copy : mark the returned frame as a copy
     |      
     |      Returns
     |      -------
     |      taken : type of caller
     |  
     |  to_clipboard(self, excel=None, sep=None, **kwargs)
     |      Attempt to write text representation of object to the system clipboard
     |      This can be pasted into Excel, for example.
     |      
     |      Parameters
     |      ----------
     |      excel : boolean, defaults to True
     |              if True, use the provided separator, writing in a csv
     |              format for allowing easy pasting into excel.
     |              if False, write a string representation of the object
     |              to the clipboard
     |      sep : optional, defaults to tab
     |      other keywords are passed to to_csv
     |      
     |      Notes
     |      -----
     |      Requirements for your platform
     |        - Linux: xclip, or xsel (with gtk or PyQt4 modules)
     |        - Windows: none
     |        - OS X: none
     |  
     |  to_dense(self)
     |      Return dense representation of NDFrame (as opposed to sparse)
     |  
     |  to_hdf(self, path_or_buf, key, **kwargs)
     |      Write the contained data to an HDF5 file using HDFStore.
     |      
     |      Parameters
     |      ----------
     |      path_or_buf : the path (string) or HDFStore object
     |      key : string
     |          indentifier for the group in the store
     |      mode : optional, {'a', 'w', 'r+'}, default 'a'
     |      
     |        ``'w'``
     |            Write; a new file is created (an existing file with the same
     |            name would be deleted).
     |        ``'a'``
     |            Append; an existing file is opened for reading and writing,
     |            and if the file does not exist it is created.
     |        ``'r+'``
     |            It is similar to ``'a'``, but the file must already exist.
     |      format : 'fixed(f)|table(t)', default is 'fixed'
     |          fixed(f) : Fixed format
     |                     Fast writing/reading. Not-appendable, nor searchable
     |          table(t) : Table format
     |                     Write as a PyTables Table structure which may perform
     |                     worse but allow more flexible operations like searching
     |                     / selecting subsets of the data
     |      append : boolean, default False
     |          For Table formats, append the input data to the existing
     |      data_columns :  list of columns, or True, default None
     |          List of columns to create as indexed data columns for on-disk
     |          queries, or True to use all columns. By default only the axes
     |          of the object are indexed. See `here
     |          <http://pandas.pydata.org/pandas-docs/stable/io.html#query-via-data-columns>`__.
     |      
     |          Applicable only to format='table'.
     |      complevel : int, 1-9, default 0
     |          If a complib is specified compression will be applied
     |          where possible
     |      complib : {'zlib', 'bzip2', 'lzo', 'blosc', None}, default None
     |          If complevel is > 0 apply compression to objects written
     |          in the store wherever possible
     |      fletcher32 : bool, default False
     |          If applying compression use the fletcher32 checksum
     |      dropna : boolean, default False.
     |          If true, ALL nan rows will not be written to store.
     |  
     |  to_json(self, path_or_buf=None, orient=None, date_format='epoch', double_precision=10, force_ascii=True, date_unit='ms', default_handler=None, lines=False)
     |      Convert the object to a JSON string.
     |      
     |      Note NaN's and None will be converted to null and datetime objects
     |      will be converted to UNIX timestamps.
     |      
     |      Parameters
     |      ----------
     |      path_or_buf : the path or buffer to write the result string
     |          if this is None, return a StringIO of the converted string
     |      orient : string
     |      
     |          * Series
     |      
     |            - default is 'index'
     |            - allowed values are: {'split','records','index'}
     |      
     |          * DataFrame
     |      
     |            - default is 'columns'
     |            - allowed values are:
     |              {'split','records','index','columns','values'}
     |      
     |          * The format of the JSON string
     |      
     |            - split : dict like
     |              {index -> [index], columns -> [columns], data -> [values]}
     |            - records : list like
     |              [{column -> value}, ... , {column -> value}]
     |            - index : dict like {index -> {column -> value}}
     |            - columns : dict like {column -> {index -> value}}
     |            - values : just the values array
     |      
     |      date_format : {'epoch', 'iso'}
     |          Type of date conversion. `epoch` = epoch milliseconds,
     |          `iso`` = ISO8601, default is epoch.
     |      double_precision : The number of decimal places to use when encoding
     |          floating point values, default 10.
     |      force_ascii : force encoded string to be ASCII, default True.
     |      date_unit : string, default 'ms' (milliseconds)
     |          The time unit to encode to, governs timestamp and ISO8601
     |          precision.  One of 's', 'ms', 'us', 'ns' for second, millisecond,
     |          microsecond, and nanosecond respectively.
     |      default_handler : callable, default None
     |          Handler to call if object cannot otherwise be converted to a
     |          suitable format for JSON. Should receive a single argument which is
     |          the object to convert and return a serialisable object.
     |      lines : boolean, defalut False
     |          If 'orient' is 'records' write out line delimited json format. Will
     |          throw ValueError if incorrect 'orient' since others are not list
     |          like.
     |      
     |          .. versionadded:: 0.19.0
     |      
     |      
     |      Returns
     |      -------
     |      same type as input object with filtered info axis
     |  
     |  to_msgpack(self, path_or_buf=None, encoding='utf-8', **kwargs)
     |      msgpack (serialize) object to input file path
     |      
     |      THIS IS AN EXPERIMENTAL LIBRARY and the storage format
     |      may not be stable until a future release.
     |      
     |      Parameters
     |      ----------
     |      path : string File path, buffer-like, or None
     |          if None, return generated string
     |      append : boolean whether to append to an existing msgpack
     |          (default is False)
     |      compress : type of compressor (zlib or blosc), default to None (no
     |          compression)
     |  
     |  to_pickle(self, path)
     |      Pickle (serialize) object to input file path.
     |      
     |      Parameters
     |      ----------
     |      path : string
     |          File path
     |  
     |  to_sql(self, name, con, flavor=None, schema=None, if_exists='fail', index=True, index_label=None, chunksize=None, dtype=None)
     |      Write records stored in a DataFrame to a SQL database.
     |      
     |      Parameters
     |      ----------
     |      name : string
     |          Name of SQL table
     |      con : SQLAlchemy engine or DBAPI2 connection (legacy mode)
     |          Using SQLAlchemy makes it possible to use any DB supported by that
     |          library. If a DBAPI2 object, only sqlite3 is supported.
     |      flavor : 'sqlite', default None
     |          DEPRECATED: this parameter will be removed in a future version,
     |          as 'sqlite' is the only supported option if SQLAlchemy is not
     |          installed.
     |      schema : string, default None
     |          Specify the schema (if database flavor supports this). If None, use
     |          default schema.
     |      if_exists : {'fail', 'replace', 'append'}, default 'fail'
     |          - fail: If table exists, do nothing.
     |          - replace: If table exists, drop it, recreate it, and insert data.
     |          - append: If table exists, insert data. Create if does not exist.
     |      index : boolean, default True
     |          Write DataFrame index as a column.
     |      index_label : string or sequence, default None
     |          Column label for index column(s). If None is given (default) and
     |          `index` is True, then the index names are used.
     |          A sequence should be given if the DataFrame uses MultiIndex.
     |      chunksize : int, default None
     |          If not None, then rows will be written in batches of this size at a
     |          time.  If None, all rows will be written at once.
     |      dtype : dict of column name to SQL type, default None
     |          Optional specifying the datatype for columns. The SQL type should
     |          be a SQLAlchemy type, or a string for sqlite3 fallback connection.
     |  
     |  to_xarray(self)
     |      Return an xarray object from the pandas object.
     |      
     |      Returns
     |      -------
     |      a DataArray for a Series
     |      a Dataset for a DataFrame
     |      a DataArray for higher dims
     |      
     |      Examples
     |      --------
     |      >>> df = pd.DataFrame({'A' : [1, 1, 2],
     |                             'B' : ['foo', 'bar', 'foo'],
     |                             'C' : np.arange(4.,7)})
     |      >>> df
     |         A    B    C
     |      0  1  foo  4.0
     |      1  1  bar  5.0
     |      2  2  foo  6.0
     |      
     |      >>> df.to_xarray()
     |      <xarray.Dataset>
     |      Dimensions:  (index: 3)
     |      Coordinates:
     |        * index    (index) int64 0 1 2
     |      Data variables:
     |          A        (index) int64 1 1 2
     |          B        (index) object 'foo' 'bar' 'foo'
     |          C        (index) float64 4.0 5.0 6.0
     |      
     |      >>> df = pd.DataFrame({'A' : [1, 1, 2],
     |                             'B' : ['foo', 'bar', 'foo'],
     |                             'C' : np.arange(4.,7)}
     |                           ).set_index(['B','A'])
     |      >>> df
     |               C
     |      B   A
     |      foo 1  4.0
     |      bar 1  5.0
     |      foo 2  6.0
     |      
     |      >>> df.to_xarray()
     |      <xarray.Dataset>
     |      Dimensions:  (A: 2, B: 2)
     |      Coordinates:
     |        * B        (B) object 'bar' 'foo'
     |        * A        (A) int64 1 2
     |      Data variables:
     |          C        (B, A) float64 5.0 nan 4.0 6.0
     |      
     |      >>> p = pd.Panel(np.arange(24).reshape(4,3,2),
     |                       items=list('ABCD'),
     |                       major_axis=pd.date_range('20130101', periods=3),
     |                       minor_axis=['first', 'second'])
     |      >>> p
     |      <class 'pandas.core.panel.Panel'>
     |      Dimensions: 4 (items) x 3 (major_axis) x 2 (minor_axis)
     |      Items axis: A to D
     |      Major_axis axis: 2013-01-01 00:00:00 to 2013-01-03 00:00:00
     |      Minor_axis axis: first to second
     |      
     |      >>> p.to_xarray()
     |      <xarray.DataArray (items: 4, major_axis: 3, minor_axis: 2)>
     |      array([[[ 0,  1],
     |              [ 2,  3],
     |              [ 4,  5]],
     |             [[ 6,  7],
     |              [ 8,  9],
     |              [10, 11]],
     |             [[12, 13],
     |              [14, 15],
     |              [16, 17]],
     |             [[18, 19],
     |              [20, 21],
     |              [22, 23]]])
     |      Coordinates:
     |        * items       (items) object 'A' 'B' 'C' 'D'
     |        * major_axis  (major_axis) datetime64[ns] 2013-01-01 2013-01-02 2013-01-03  # noqa
     |        * minor_axis  (minor_axis) object 'first' 'second'
     |      
     |      Notes
     |      -----
     |      See the `xarray docs <http://xarray.pydata.org/en/stable/>`__
     |  
     |  truncate(self, before=None, after=None, axis=None, copy=True)
     |      Truncates a sorted NDFrame before and/or after some particular
     |      index value. If the axis contains only datetime values, before/after
     |      parameters are converted to datetime values.
     |      
     |      Parameters
     |      ----------
     |      before : date
     |          Truncate before index value
     |      after : date
     |          Truncate after index value
     |      axis : the truncation axis, defaults to the stat axis
     |      copy : boolean, default is True,
     |          return a copy of the truncated section
     |      
     |      Returns
     |      -------
     |      truncated : type of caller
     |  
     |  tshift(self, periods=1, freq=None, axis=0)
     |      Shift the time index, using the index's frequency if available.
     |      
     |      Parameters
     |      ----------
     |      periods : int
     |          Number of periods to move, can be positive or negative
     |      freq : DateOffset, timedelta, or time rule string, default None
     |          Increment to use from the tseries module or time rule (e.g. 'EOM')
     |      axis : int or basestring
     |          Corresponds to the axis that contains the Index
     |      
     |      Notes
     |      -----
     |      If freq is not specified then tries to use the freq or inferred_freq
     |      attributes of the index. If neither of those attributes exist, a
     |      ValueError is thrown
     |      
     |      Returns
     |      -------
     |      shifted : NDFrame
     |  
     |  tz_convert(self, tz, axis=0, level=None, copy=True)
     |      Convert tz-aware axis to target time zone.
     |      
     |      Parameters
     |      ----------
     |      tz : string or pytz.timezone object
     |      axis : the axis to convert
     |      level : int, str, default None
     |          If axis ia a MultiIndex, convert a specific level. Otherwise
     |          must be None
     |      copy : boolean, default True
     |          Also make a copy of the underlying data
     |      
     |      Returns
     |      -------
     |      
     |      Raises
     |      ------
     |      TypeError
     |          If the axis is tz-naive.
     |  
     |  tz_localize(self, tz, axis=0, level=None, copy=True, ambiguous='raise')
     |      Localize tz-naive TimeSeries to target time zone.
     |      
     |      Parameters
     |      ----------
     |      tz : string or pytz.timezone object
     |      axis : the axis to localize
     |      level : int, str, default None
     |          If axis ia a MultiIndex, localize a specific level. Otherwise
     |          must be None
     |      copy : boolean, default True
     |          Also make a copy of the underlying data
     |      ambiguous : 'infer', bool-ndarray, 'NaT', default 'raise'
     |          - 'infer' will attempt to infer fall dst-transition hours based on
     |            order
     |          - bool-ndarray where True signifies a DST time, False designates
     |            a non-DST time (note that this flag is only applicable for
     |            ambiguous times)
     |          - 'NaT' will return NaT where there are ambiguous times
     |          - 'raise' will raise an AmbiguousTimeError if there are ambiguous
     |            times
     |      infer_dst : boolean, default False (DEPRECATED)
     |          Attempt to infer fall dst-transition hours based on order
     |      
     |      Returns
     |      -------
     |      
     |      Raises
     |      ------
     |      TypeError
     |          If the TimeSeries is tz-aware and tz is not None.
     |  
     |  where(self, cond, other=nan, inplace=False, axis=None, level=None, try_cast=False, raise_on_error=True)
     |      Return an object of same shape as self and whose corresponding
     |      entries are from self where cond is True and otherwise are from
     |      other.
     |      
     |      Parameters
     |      ----------
     |      cond : boolean NDFrame, array or callable
     |          If cond is callable, it is computed on the NDFrame and
     |          should return boolean NDFrame or array.
     |          The callable must not change input NDFrame
     |          (though pandas doesn't check it).
     |      
     |          .. versionadded:: 0.18.1
     |      
     |          A callable can be used as cond.
     |      
     |      other : scalar, NDFrame, or callable
     |          If other is callable, it is computed on the NDFrame and
     |          should return scalar or NDFrame.
     |          The callable must not change input NDFrame
     |          (though pandas doesn't check it).
     |      
     |          .. versionadded:: 0.18.1
     |      
     |          A callable can be used as other.
     |      
     |      inplace : boolean, default False
     |          Whether to perform the operation in place on the data
     |      axis : alignment axis if needed, default None
     |      level : alignment level if needed, default None
     |      try_cast : boolean, default False
     |          try to cast the result back to the input type (if possible),
     |      raise_on_error : boolean, default True
     |          Whether to raise on invalid data types (e.g. trying to where on
     |          strings)
     |      
     |      Returns
     |      -------
     |      wh : same type as caller
     |      
     |      Notes
     |      -----
     |      The where method is an application of the if-then idiom. For each
     |      element in the calling DataFrame, if ``cond`` is ``True`` the
     |      element is used; otherwise the corresponding element from the DataFrame
     |      ``other`` is used.
     |      
     |      The signature for :func:`DataFrame.where` differs from
     |      :func:`numpy.where`. Roughly ``df1.where(m, df2)`` is equivalent to
     |      ``np.where(m, df1, df2)``.
     |      
     |      For further details and examples see the ``where`` documentation in
     |      :ref:`indexing <indexing.where_mask>`.
     |      
     |      Examples
     |      --------
     |      >>> s = pd.Series(range(5))
     |      >>> s.where(s > 0)
     |      0    NaN
     |      1    1.0
     |      2    2.0
     |      3    3.0
     |      4    4.0
     |      
     |      >>> df = pd.DataFrame(np.arange(10).reshape(-1, 2), columns=['A', 'B'])
     |      >>> m = df % 3 == 0
     |      >>> df.where(m, -df)
     |         A  B
     |      0  0 -1
     |      1 -2  3
     |      2 -4 -5
     |      3  6 -7
     |      4 -8  9
     |      >>> df.where(m, -df) == np.where(m, df, -df)
     |            A     B
     |      0  True  True
     |      1  True  True
     |      2  True  True
     |      3  True  True
     |      4  True  True
     |      >>> df.where(m, -df) == df.mask(~m, -df)
     |            A     B
     |      0  True  True
     |      1  True  True
     |      2  True  True
     |      3  True  True
     |      4  True  True
     |      
     |      See Also
     |      --------
     |      :func:`DataFrame.mask`
     |  
     |  xs(self, key, axis=0, level=None, drop_level=True)
     |      Returns a cross-section (row(s) or column(s)) from the
     |      Series/DataFrame. Defaults to cross-section on the rows (axis=0).
     |      
     |      Parameters
     |      ----------
     |      key : object
     |          Some label contained in the index, or partially in a MultiIndex
     |      axis : int, default 0
     |          Axis to retrieve cross-section on
     |      level : object, defaults to first n levels (n=1 or len(key))
     |          In case of a key partially contained in a MultiIndex, indicate
     |          which levels are used. Levels can be referred by label or position.
     |      drop_level : boolean, default True
     |          If False, returns object with same levels as self.
     |      
     |      Examples
     |      --------
     |      >>> df
     |         A  B  C
     |      a  4  5  2
     |      b  4  0  9
     |      c  9  7  3
     |      >>> df.xs('a')
     |      A    4
     |      B    5
     |      C    2
     |      Name: a
     |      >>> df.xs('C', axis=1)
     |      a    2
     |      b    9
     |      c    3
     |      Name: C
     |      
     |      >>> df
     |                          A  B  C  D
     |      first second third
     |      bar   one    1      4  1  8  9
     |            two    1      7  5  5  0
     |      baz   one    1      6  6  8  0
     |            three  2      5  3  5  3
     |      >>> df.xs(('baz', 'three'))
     |             A  B  C  D
     |      third
     |      2      5  3  5  3
     |      >>> df.xs('one', level=1)
     |                   A  B  C  D
     |      first third
     |      bar   1      4  1  8  9
     |      baz   1      6  6  8  0
     |      >>> df.xs(('baz', 2), level=[0, 'third'])
     |              A  B  C  D
     |      second
     |      three   5  3  5  3
     |      
     |      Returns
     |      -------
     |      xs : Series or DataFrame
     |      
     |      Notes
     |      -----
     |      xs is only for getting, not setting values.
     |      
     |      MultiIndex Slicers is a generic way to get/set values on any level or
     |      levels.  It is a superset of xs functionality, see
     |      :ref:`MultiIndex Slicers <advanced.mi_slicers>`
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from pandas.core.generic.NDFrame:
     |  
     |  at
     |      Fast label-based scalar accessor
     |      
     |      Similarly to ``loc``, ``at`` provides **label** based scalar lookups.
     |      You can also set using these indexers.
     |  
     |  blocks
     |      Internal property, property synonym for as_blocks()
     |  
     |  dtypes
     |      Return the dtypes in this object.
     |  
     |  empty
     |      True if NDFrame is entirely empty [no items], meaning any of the
     |      axes are of length 0.
     |      
     |      Notes
     |      -----
     |      If NDFrame contains only NaNs, it is still not considered empty. See
     |      the example below.
     |      
     |      Examples
     |      --------
     |      An example of an actual empty DataFrame. Notice the index is empty:
     |      
     |      >>> df_empty = pd.DataFrame({'A' : []})
     |      >>> df_empty
     |      Empty DataFrame
     |      Columns: [A]
     |      Index: []
     |      >>> df_empty.empty
     |      True
     |      
     |      If we only have NaNs in our DataFrame, it is not considered empty! We
     |      will need to drop the NaNs to make the DataFrame empty:
     |      
     |      >>> df = pd.DataFrame({'A' : [np.nan]})
     |      >>> df
     |          A
     |      0 NaN
     |      >>> df.empty
     |      False
     |      >>> df.dropna().empty
     |      True
     |      
     |      See also
     |      --------
     |      pandas.Series.dropna
     |      pandas.DataFrame.dropna
     |  
     |  ftypes
     |      Return the ftypes (indication of sparse/dense and dtype)
     |      in this object.
     |  
     |  iat
     |      Fast integer location scalar accessor.
     |      
     |      Similarly to ``iloc``, ``iat`` provides **integer** based lookups.
     |      You can also set using these indexers.
     |  
     |  iloc
     |      Purely integer-location based indexing for selection by position.
     |      
     |      ``.iloc[]`` is primarily integer position based (from ``0`` to
     |      ``length-1`` of the axis), but may also be used with a boolean
     |      array.
     |      
     |      Allowed inputs are:
     |      
     |      - An integer, e.g. ``5``.
     |      - A list or array of integers, e.g. ``[4, 3, 0]``.
     |      - A slice object with ints, e.g. ``1:7``.
     |      - A boolean array.
     |      - A ``callable`` function with one argument (the calling Series, DataFrame
     |        or Panel) and that returns valid output for indexing (one of the above)
     |      
     |      ``.iloc`` will raise ``IndexError`` if a requested indexer is
     |      out-of-bounds, except *slice* indexers which allow out-of-bounds
     |      indexing (this conforms with python/numpy *slice* semantics).
     |      
     |      See more at :ref:`Selection by Position <indexing.integer>`
     |  
     |  ix
     |      A primarily label-location based indexer, with integer position
     |      fallback.
     |      
     |      ``.ix[]`` supports mixed integer and label based access. It is
     |      primarily label based, but will fall back to integer positional
     |      access unless the corresponding axis is of integer type.
     |      
     |      ``.ix`` is the most general indexer and will support any of the
     |      inputs in ``.loc`` and ``.iloc``. ``.ix`` also supports floating
     |      point label schemes. ``.ix`` is exceptionally useful when dealing
     |      with mixed positional and label based hierachical indexes.
     |      
     |      However, when an axis is integer based, ONLY label based access
     |      and not positional access is supported. Thus, in such cases, it's
     |      usually better to be explicit and use ``.iloc`` or ``.loc``.
     |      
     |      See more at :ref:`Advanced Indexing <advanced>`.
     |  
     |  loc
     |      Purely label-location based indexer for selection by label.
     |      
     |      ``.loc[]`` is primarily label based, but may also be used with a
     |      boolean array.
     |      
     |      Allowed inputs are:
     |      
     |      - A single label, e.g. ``5`` or ``'a'``, (note that ``5`` is
     |        interpreted as a *label* of the index, and **never** as an
     |        integer position along the index).
     |      - A list or array of labels, e.g. ``['a', 'b', 'c']``.
     |      - A slice object with labels, e.g. ``'a':'f'`` (note that contrary
     |        to usual python slices, **both** the start and the stop are included!).
     |      - A boolean array.
     |      - A ``callable`` function with one argument (the calling Series, DataFrame
     |        or Panel) and that returns valid output for indexing (one of the above)
     |      
     |      ``.loc`` will raise a ``KeyError`` when the items are not found.
     |      
     |      See more at :ref:`Selection by Label <indexing.label>`
     |  
     |  ndim
     |      Number of axes / array dimensions
     |  
     |  size
     |      number of elements in the NDFrame
     |  
     |  values
     |      Numpy representation of NDFrame
     |      
     |      Notes
     |      -----
     |      The dtype will be a lower-common-denominator dtype (implicit
     |      upcasting); that is to say if the dtypes (even of numeric types)
     |      are mixed, the one that accommodates all will be chosen. Use this
     |      with care if you are not dealing with the blocks.
     |      
     |      e.g. If the dtypes are float16 and float32, dtype will be upcast to
     |      float32.  If dtypes are int32 and uint8, dtype will be upcast to
     |      int32. By numpy.find_common_type convention, mixing int64 and uint64
     |      will result in a flot64 dtype.
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from pandas.core.generic.NDFrame:
     |  
     |  is_copy = None
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from pandas.core.base.PandasObject:
     |  
     |  __dir__(self)
     |      Provide method name lookup and completion
     |      Only provide 'public' methods
     |  
     |  __sizeof__(self)
     |      Generates the total memory usage for a object that returns
     |      either a value or Series of values
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from pandas.core.base.StringMixin:
     |  
     |  __bytes__(self)
     |      Return a string representation for a particular object.
     |      
     |      Invoked by bytes(obj) in py3 only.
     |      Yields a bytestring in both py2/py3.
     |  
     |  __repr__(self)
     |      Return a string representation for a particular object.
     |      
     |      Yields Bytestring in Py2, Unicode String in py3.
     |  
     |  __str__(self)
     |      Return a string representation for a particular Object
     |      
     |      Invoked by str(df) in both py2/py3.
     |      Yields Bytestring in Py2, Unicode String in py3.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from pandas.core.base.StringMixin:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    



```python
#However, I am only concerned with the mean at this point.
help(pd.DataFrame.mean)
```

    Help on function mean in module pandas.core.frame:
    
    mean(self, axis=None, skipna=None, level=None, numeric_only=None, **kwargs)
        Return the mean of the values for the requested axis
        
        Parameters
        ----------
        axis : {index (0), columns (1)}
        skipna : boolean, default True
            Exclude NA/null values. If an entire row/column is NA, the result
            will be NA
        level : int or level name, default None
            If the axis is a MultiIndex (hierarchical), count along a
            particular level, collapsing into a Series
        numeric_only : boolean, default None
            Include only float, int, boolean columns. If None, will attempt to use
            everything, then use only numeric data. Not implemented for Series.
        
        Returns
        -------
        mean : Series or DataFrame (if level specified)
    



```python
# defining a function to find average of a column
def avg_fun(column):
    return df[column].mean()
```


```python
#calling above function
avg_fun('profit_earned')
```




    70482919.14322782



The average profit of all the movies, is 70,457,104.38 (to the second decimal) i.e $70 million. 

### Research Question 4 : Which movied earned the least and most profit?


```python
import pprint
#defining the function
def calculate(column):
    #for highest earned profit
    high= df[column].idxmax()
    high_details=pd.DataFrame(df.loc[high])
    
    #for lowest earned profit
    low= df[column].idxmin()
    low_details=pd.DataFrame(df.loc[low])
    
    #collectin data in one place
    info=pd.concat([high_details, low_details], axis=1)
    
    return info

calculate('profit_earned')
```




<div>
<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>1386</th>
      <th>2244</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>id</th>
      <td>19995</td>
      <td>46528</td>
    </tr>
    <tr>
      <th>budget</th>
      <td>237000000</td>
      <td>425000000</td>
    </tr>
    <tr>
      <th>profit_earned</th>
      <td>2544505847</td>
      <td>-413912431</td>
    </tr>
    <tr>
      <th>revenue</th>
      <td>2781505847</td>
      <td>11087569</td>
    </tr>
    <tr>
      <th>original_title</th>
      <td>Avatar</td>
      <td>The Warrior's Way</td>
    </tr>
    <tr>
      <th>runtime</th>
      <td>162</td>
      <td>100</td>
    </tr>
    <tr>
      <th>genres</th>
      <td>Action|Adventure|Fantasy|Science Fiction</td>
      <td>Adventure|Fantasy|Action|Western|Thriller</td>
    </tr>
    <tr>
      <th>release_date</th>
      <td>2009-12-10 00:00:00</td>
      <td>2010-12-02 00:00:00</td>
    </tr>
    <tr>
      <th>release_year</th>
      <td>2009</td>
      <td>2010</td>
    </tr>
  </tbody>
</table>
</div>


The movie with the highest profit was 'Avatar', which had earned 2,544,505,847 ($2.5 billion). The movie with the lowest profit and incurred a loss of -41,391,2431 ($41 million) was 'The Warrior's Way'
### Using visualisations to explore profit

Because of how the human brain works, using graphs and charts by creating visualisations is a much more palatable way to identify trends and portray concepts in a quick, easy and unniversal way. 
We can create a visulisation of the a subset of target stats in one go using Plot matricies. A matrix of plots is generated. Each row and colum represents a different variable and a subplot against those variables is generated in each plot matrix cell. 


```python
g = sns.PairGrid(data = df, vars = ['budget', 'revenue', 'profit_earned', 'release_year', 'runtime']) 
g.map_diag(plt.hist) 
g.map_offdiag(plt.scatter)
```




    <seaborn.axisgrid.PairGrid at 0x7f747749af98>




![png](output_70_1.png)


Where histograms are presented, shows where the row and column variable match. From this plot matrice, the two variables where there is a positive correlation is revenue and profit earned. PairGrid only expects to depict numerica variables. 


```python
#We can also inspect the data closer, using a scatterplot.
plt.scatter(data = df, x = "revenue", y ="profit_earned")
```




    <matplotlib.collections.PathCollection at 0x7f7476df7780>




![png](output_72_1.png)


Histograms are also used to plot the distribution of numeric variables. It is the quantitative version of a bar chart. 


```python
df['profit_earned'].plot(kind='hist');
```


![png](output_74_0.png)


Based on the histogram above, profit earned is right skewed and so the mean is greater than the median value for profit earned. 


```python
#We can also inspect the data visually, using a scaterplot. 
plt.scatter(data = df, x = "budget", y ="revenue")
```




    <matplotlib.collections.PathCollection at 0x7f7476d296a0>




![png](output_76_1.png)


We can see a slight positive correlation between the variables, budget and revenue, however it is not a strong correlation and most of the movies, with an exception of a few anaomalies lie around the lower end of the axis. Indicating that the lower the budget, the lower the revenue for the film. 

### Research Question 5: What is the realtionship between genre and profit?

In this section we will look to address the question: "Which genres of movie generated the most profit?". 

To further delve into answering this question, it might be easier to create a duplicate dataframe. 


```python
#prepare a new data frame 
movie_genres = df.copy()
movie_genres.drop(['original_title','runtime', 'budget', 'revenue', 'release_date'], axis=1, inplace=True)
movie_genres.head(1)
```




<div>
<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>profit_earned</th>
      <th>genres</th>
      <th>release_year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>135397</td>
      <td>1363528810</td>
      <td>Action|Adventure|Science Fiction|Thriller</td>
      <td>2015</td>
    </tr>
  </tbody>
</table>
</div>




```python
movie_genres.head()
```




<div>
<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>profit_earned</th>
      <th>genres</th>
      <th>release_year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>135397</td>
      <td>1363528810</td>
      <td>Action|Adventure|Science Fiction|Thriller</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>1</th>
      <td>76341</td>
      <td>228436354</td>
      <td>Action|Adventure|Science Fiction|Thriller</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>2</th>
      <td>262500</td>
      <td>185238201</td>
      <td>Adventure|Science Fiction|Thriller</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>3</th>
      <td>140607</td>
      <td>1868178225</td>
      <td>Action|Adventure|Science Fiction|Fantasy</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>4</th>
      <td>168259</td>
      <td>1316249360</td>
      <td>Action|Crime|Thriller</td>
      <td>2015</td>
    </tr>
  </tbody>
</table>
</div>




```python
#drop Nan values - only targets genres at this stage
movie_genres.dropna(axis=0, how='any', inplace=True)
```

Some of the rows in the genres column hold a multiple values. To begin using the information in this column effectively, I need to:

know how many unique genres labels there are; and
split these genres out into such a way that they can be considered individually
The next set of cells will address this.


```python
# grab the id and genres column
genres = movie_genres.loc[:, ['id', 'genres']]
```


```python
genres.head()
```




<div>
<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>genres</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>135397</td>
      <td>Action|Adventure|Science Fiction|Thriller</td>
    </tr>
    <tr>
      <th>1</th>
      <td>76341</td>
      <td>Action|Adventure|Science Fiction|Thriller</td>
    </tr>
    <tr>
      <th>2</th>
      <td>262500</td>
      <td>Adventure|Science Fiction|Thriller</td>
    </tr>
    <tr>
      <th>3</th>
      <td>140607</td>
      <td>Action|Adventure|Science Fiction|Fantasy</td>
    </tr>
    <tr>
      <th>4</th>
      <td>168259</td>
      <td>Action|Crime|Thriller</td>
    </tr>
  </tbody>
</table>
</div>




```python
# split the genres cells by the pipe and add to a list
genre_list = genres['genres'].str.split('|').tolist()
genre_list[:5]
```




    [['Action', 'Adventure', 'Science Fiction', 'Thriller'],
     ['Action', 'Adventure', 'Science Fiction', 'Thriller'],
     ['Adventure', 'Science Fiction', 'Thriller'],
     ['Action', 'Adventure', 'Science Fiction', 'Fantasy'],
     ['Action', 'Crime', 'Thriller']]



In the following code, this list must be transfromed into a usesable format and data frame. 
It will be usefull in this case to create a 'nested list' as an element of the previous genres list.  


```python
for i in range (len(genre_list)):
    if not isinstance(genre_list[i],list):
        genre_list[i] = [genre_list [i]]
```

The code above has a loop through each nested list within genre_list. This is because of syntax errors that could only seemingly be resolved by using a loo[/ 

The following cell will create a new dataframe using genre_list and the id column as the index. This will result in multiple colums with an individual genre value per id. Therefore .stack() will pivot the data.


```python
stacked_genres = pd.DataFrame(genre_list, index=genres['id']).stack()
```


```python
print(stacked_genres.head())
```

    id       
    135397  0             Action
            1          Adventure
            2    Science Fiction
            3           Thriller
    76341   0             Action
    dtype: object



```python
stacked_genres = stacked_genres.reset_index()
```


```python
print(stacked_genres.head())
```

           id  level_1                0
    0  135397        0           Action
    1  135397        1        Adventure
    2  135397        2  Science Fiction
    3  135397        3         Thriller
    4   76341        0           Action



```python
#we need to remove the extra colums here such as level_o and level_1.
stacked_genres = stacked_genres.loc[:,['id',0]]
```


```python
print(stacked_genres.head())
```

           id                0
    0  135397           Action
    1  135397        Adventure
    2  135397  Science Fiction
    3  135397         Thriller
    4   76341           Action



```python
#rename the genres column 
stacked_genres.columns = ['id','genre']
```


```python
print(stacked_genres.head())
```

           id            genre
    0  135397           Action
    1  135397        Adventure
    2  135397  Science Fiction
    3  135397         Thriller
    4   76341           Action



```python
#merge stacked_grenre and movie_genres and drop unecessary columns
merged_df = pd.merge(movie_genres, stacked_genres, on='id', how = 'left')
merged_df.drop(['genres', 'id',], axis=1, inplace=True)
```


```python
merged_df.head()
```




<div>
<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>profit_earned</th>
      <th>release_year</th>
      <th>genre</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1363528810</td>
      <td>2015</td>
      <td>Action</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1363528810</td>
      <td>2015</td>
      <td>Adventure</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1363528810</td>
      <td>2015</td>
      <td>Science Fiction</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1363528810</td>
      <td>2015</td>
      <td>Thriller</td>
    </tr>
    <tr>
      <th>4</th>
      <td>228436354</td>
      <td>2015</td>
      <td>Action</td>
    </tr>
  </tbody>
</table>
</div>



In our new merdged dataframes we can see that the genres have been broken down according to their profit earned and year of movie release. 
Additionally it would be helpful to get a visual idea of how frequently each genre occurs in our data frame. 


```python
merged_df['genre'].value_counts().plot(kind='bar', figsize=(10, 4));
```


![png](output_103_0.png)


We can see from the bar chart above the different genres and frequncy of their occurance. It would be helpful to organise the genres by release year and calculate the mean profit earned by each group. This wil make it easier to veiw the relationship between annual average profit per genre across each of the years. 
