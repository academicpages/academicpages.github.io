---
title: "Analysing movie data"
excerpt: "Analyzing data associated with information from 10,000 movies collected from the Movie Database (TMDb). The first data science project completed with python. <br/><img src='/images/2020-08-19-moviedata-images/movie.jpg' with='500' height='300'/>"
collection: portfolio
---



# Project: TMDb Movie Data Analysis

## Table of Contents
<ul>
<li><a href="#intro">Introduction</a></li>
<li><a href="#wranging">Data Wrangling</a></li>
<li><a href="#eda">Exploratory Data Analysis</a></li>
<li><a href="#conclusions">Conclusions</a></li>
</ul>

<a id="intro"></a>
##Introduction

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



<a id="wrangling"></a>
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

<a id="eda"></a>
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

the help function outputs a decsription of each method. 


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




![png](/images/2020-08-19-moviedata-images/output_68_1.png)


Where histograms are presented, shows where the row and column variable match. From this plot matrice, the two variables where there is a positive correlation is revenue and profit earned. PairGrid only expects to depict numerica variables. 


```python
#We can also inspect the data closer, using a scatterplot.
plt.scatter(data = df, x = "revenue", y ="profit_earned")
```




    <matplotlib.collections.PathCollection at 0x7f7476df7780>




![png](/images/2020-08-19-moviedata-images/output_70_1.png)


Histograms are also used to plot the distribution of numeric variables. It is the quantitative version of a bar chart. 


```python
df['profit_earned'].plot(kind='hist');
```


![png](/images/2020-08-19-moviedata-images/output_72_0.png)


Based on the histogram above, profit earned is right skewed and so the mean is greater than the median value for profit earned. 


```python
#We can also inspect the data visually, using a scaterplot. 
plt.scatter(data = df, x = "budget", y ="revenue")
```




    <matplotlib.collections.PathCollection at 0x7f7476d296a0>




![png](/images/2020-08-19-moviedata-images/output_74_1.png)


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


![png](/images/2020-08-19-moviedata-images/output_101_0.png)


We can see from the bar chart above the different genres and frequncy of their occurance. It would be helpful to organise the genres by release year and calculate the mean profit earned by each group. This wil make it easier to veiw the relationship between annual average profit per genre across each of the years. 


```python

```


```python
def group_years(genre_name):
    #filter for the genres and makes a copy of the df so pandas doesn't return and error message
    genre = merged_df[merged_df['genre'] == genre_name].copy()
    #Genre column is no longer necessary, so we can drop it.
    genre.drop(['genre'], axis=1, inplace=True)
    #Group by release_year and calulate the mean for profit
    mean_profit = genre.groupby(['release_year']).mean().reset_index()
    #rename the profit column to include the genre name. 
    mean_profit.rename(columns={'profit_earned':'profit_earned_' + genre_name.lower()}, inplace=True)
    return mean_profit
```


```python
#The def function takes a string that idendtifies the target colum in merged_df. grups the data by release_year and calculates the average profit.
#It then returns a dataframe with two columsL release_year and average profit of the input genre. 
```


```python
#fun the function against all the genre columns and store against a variable 
drama_profit = group_years ('Drama')
comedy_profit = group_years ('Comedy')
thriller_profit = group_years ('Thriller')
action_profit = group_years ('Action')
adventure_profit = group_years ('Adventure')
romance_profit= group_years ('Romance')
crime_profit = group_years ('Crime')
scifi_profit = group_years ('Science Fiction')
horror_profit = group_years ('Horror')
family_profit = group_years ('Family')
fantasy_profit = group_years ('Fantasy')
mystery_profit = group_years ('Mystery')
animation_profit = group_years ('Animation')
music_profit = group_years ('Music')
history_profit = group_years ('History')
war_profit = group_years ('War')
western_profit = group_years ('Western')
documentary_profit = group_years ('Documentary')
foreign_profit = group_years ('Foreign')
tv_profit = group_years ('TV Movie')
```

To plot the lines it is easier to move all of the stored variables to a new daaframe. 


```python
genre_merge = pd.merge(drama_profit, comedy_profit, on = 'release_year', how = 'left')
genre_merge = pd.merge(genre_merge, thriller_profit, on='release_year', how='left')
genre_merge = pd.merge(genre_merge, action_profit, on='release_year', how='left')
genre_merge = pd.merge(genre_merge, romance_profit, on='release_year', how='left')
genre_merge = pd.merge(genre_merge, horror_profit, on='release_year', how='left')
genre_merge = pd.merge(genre_merge, adventure_profit, on='release_year', how='left')
genre_merge = pd.merge(genre_merge, crime_profit, on='release_year', how='left')
genre_merge = pd.merge(genre_merge, family_profit, on='release_year', how='left')
genre_merge = pd.merge(genre_merge, scifi_profit, on='release_year', how='left')
genre_merge = pd.merge(genre_merge, fantasy_profit, on='release_year', how='left')
genre_merge = pd.merge(genre_merge, mystery_profit, on='release_year', how='left')
genre_merge = pd.merge(genre_merge, animation_profit, on='release_year', how='left')
genre_merge = pd.merge(genre_merge, documentary_profit, on='release_year', how='left')
genre_merge = pd.merge(genre_merge, music_profit, on='release_year', how='left')
genre_merge = pd.merge(genre_merge, history_profit, on='release_year', how='left')
genre_merge = pd.merge(genre_merge, war_profit, on='release_year', how='left')
genre_merge = pd.merge(genre_merge, foreign_profit, on='release_year', how='left')
genre_merge = pd.merge(genre_merge, tv_profit, on='release_year', how='left')
genre_merge = pd.merge(genre_merge, western_profit, on='release_year', how='left')
# check the first result to see that we have all the expected columns
genre_merge.head(1)
```




<div>
<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>release_year</th>
      <th>profit_earned_drama</th>
      <th>profit_earned_comedy</th>
      <th>profit_earned_thriller</th>
      <th>profit_earned_action</th>
      <th>profit_earned_romance</th>
      <th>profit_earned_horror</th>
      <th>profit_earned_adventure</th>
      <th>profit_earned_crime</th>
      <th>profit_earned_family</th>
      <th>...</th>
      <th>profit_earned_fantasy</th>
      <th>profit_earned_mystery</th>
      <th>profit_earned_animation</th>
      <th>profit_earned_documentary</th>
      <th>profit_earned_music</th>
      <th>profit_earned_history</th>
      <th>profit_earned_war</th>
      <th>profit_earned_foreign</th>
      <th>profit_earned_tv movie</th>
      <th>profit_earned_western</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1960</td>
      <td>33731017</td>
      <td>13050000.0</td>
      <td>31193052.0</td>
      <td>25452500.0</td>
      <td>13050000.0</td>
      <td>31193052.0</td>
      <td>2905000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>48000000.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2905000.0</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 21 columns</p>
</div>




```python
#As it is hard to view the column headers, it will be useful to print a list for easier viewing 
```


```python
list(genre_merge.columns.values)
```




    ['release_year',
     'profit_earned_drama',
     'profit_earned_comedy',
     'profit_earned_thriller',
     'profit_earned_action',
     'profit_earned_romance',
     'profit_earned_horror',
     'profit_earned_adventure',
     'profit_earned_crime',
     'profit_earned_family',
     'profit_earned_science fiction',
     'profit_earned_fantasy',
     'profit_earned_mystery',
     'profit_earned_animation',
     'profit_earned_documentary',
     'profit_earned_music',
     'profit_earned_history',
     'profit_earned_war',
     'profit_earned_foreign',
     'profit_earned_tv movie',
     'profit_earned_western']



To gain more insight and analysis, it will be helpful to plot the data visually. There are 20 different columns, however it will be difficult to properly plot and analyse all 20 on a line graph. I will split these into groups of 5 which will generate 4 different plots. 


```python
#plot 1: drama, comedy, thriller, action, Romance
fig, ax = plt.subplots(figsize=(16, 8))
plt.title('Average profit of films by genre (Plot 1)')
plt.ylabel('Average Annual Profit')
plt.xlabel('Release Year')
plt.xticks(np.arange(1960, 2016, 2))
ax.plot('release_year', 'profit_earned_drama', data=genre_merge, label="Drama")
ax.plot('release_year', 'profit_earned_comedy', data=genre_merge, label="Comedy")
ax.plot('release_year', 'profit_earned_thriller', data=genre_merge, label="Thriller")
ax.plot('release_year', 'profit_earned_action', data=genre_merge, label="Action")
ax.plot('release_year', 'profit_earned_romance', data=genre_merge, label = "Romance")
ax.legend(loc='upper left');
```


![png](/images/2020-08-19-moviedata-images/output_112_0.png)


### Plot 1
There are a few inferances that can be made from the first plot. The units of movie profit is given to 1e8, which is 10 means 10^8 (10 power 8), thus  100,000,000 ($100 million). 
The graph depicts that Drama and comedy follow the same overal trend with a slight increase in profit. 
However, Thriller, Action and Romance have various sprikes in profit through the different release years. 
Most notably during the following years:
* Thriller: 1972 - 1976
* Action: 1976-1978, 1980-1982, 2000- onwards (climbed steadily)
* Romance: 1988-1992, 1993-1995, 1996-1999

It would be interesting to invetigate which movies were released at these time points and correlate with the spikes in profit. 


```python
#plot 2: Horror, adventure, crime, family, scifi
fig, ax = plt.subplots(figsize=(16, 8))
plt.title('Average profit of films by genre (Plot 2)')
plt.ylabel('Average Annual Profit')
plt.xlabel('Release Year')
plt.xticks(np.arange(1960, 2016, 2))
ax.plot('release_year', 'profit_earned_horror', data=genre_merge, label="Horror")
ax.plot('release_year', 'profit_earned_adventure', data=genre_merge, label="Adventure")
ax.plot('release_year', 'profit_earned_crime', data=genre_merge, label="Crime")
ax.plot('release_year', 'profit_earned_family', data=genre_merge, label="Family")
ax.plot('release_year', 'profit_earned_science fiction', data=genre_merge, label = "Science Fiction")
ax.legend(loc='upper left');
```


![png](/images/2020-08-19-moviedata-images/output_114_0.png)


## Plot 2

The graph illustrates that Adventure, Family and scifi films all rose steady through the time period  of 1960 t0 2014. Crime and Horror remained fairly level from 1982 to 2012 in the range of 50million to 100million dollars. However there was a sharp spike for Horror, prior to this in 1974 with a profit of roughly 430million dollars. 


```python
#plot 3: Fantasy, mystery, animation, documentary, music
fig, ax = plt.subplots(figsize=(16, 8))
plt.title('Average profit of films by genre (Plot 3)')
plt.ylabel('Average Annual Profit')
plt.xlabel('Release Year')
plt.xticks(np.arange(1960, 2016, 2))
ax.plot('release_year', 'profit_earned_fantasy', data=genre_merge, label="Fantasy")
ax.plot('release_year', 'profit_earned_mystery', data=genre_merge, label="Mystery")
ax.plot('release_year', 'profit_earned_animation', data=genre_merge, label="Animation")
ax.plot('release_year', 'profit_earned_documentary', data=genre_merge, label="Documentary") 
ax.plot('release_year', 'profit_earned_music', data=genre_merge, label = "Music")
ax.legend(loc='upper left');
```


![png](/images/2020-08-19-moviedata-images/output_116_0.png)


### Plot 3
The second plot above indictates a similar upward trend depicting an increase in profit for both Fantasy and Animation. Animation, also has a large peak with a profit of 


### Research Question 6: What was the average run time?


```python
df.loc[:,"runtime"].mean()
```




    109.22029060716139



Although we fo not have units for run time, we can assume that it is minutes. Therefore, the average run time across all movies was 109 minutes. Since run time has smaller values than budget, revenue or profit earned, we can plot this visually. 

Visualisations are helpful in exploratory data anlysis by providing further insight. 


```python
#plotting a histogram of runtime of movies

#giving the figure size(width, height)
plt.figure(figsize=(9,5), dpi = 100)

#On x-axis 
plt.xlabel('Runtime', fontsize = 15)
#On y-axis 
plt.ylabel('Nos.of Movies in the dataframe', fontsize=15)
#Name of the graph
plt.title('Average Movie Runtime', fontsize=15)

#giving a histogram plot
plt.hist(df['runtime'], rwidth = 0.9, bins =35)
#displays the plot
plt.show()
```


![png](/images/2020-08-19-moviedata-images/output_121_0.png)


From the histogram above we can infere that the distrubution is positively/right skewed. The majority of the movies are in the time frame of 80 to 115 minutes. 1000+ movies fall into this group. 
The data can also be analysed to look for potential outliers using different types of visualisations. This includes a box plot and data point plot. 

Box plots give a general idea of  the spread and distribution of the data for the runtime of the movies.


```python
import seaborn as sns
#The First plot is box plot of the runtime of the movies 
plt.figure(figsize=(9,7), dpi = 105)

#using seaborn to generate the boxplot
sns.boxplot(df['runtime'], linewidth = 3, color = "red")
#diplaying the plot
plt.show()
```


![png](/images/2020-08-19-moviedata-images/output_123_0.png)


While the box and whiskerplot gives a good understand of the spread of that data and outliers. If we want to look at data plot points we can also use seaborn to generate such a plot. 


```python
plt.figure(figsize=(10,5), dpi=105)

#using seaborn to generate the plot
sns.swarmplot(df['runtime'],color = "orange")

#generate the plot
plt.show()
```


![png](/images/2020-08-19-moviedata-images/output_125_0.png)


We can measure the overal spread of the data by looking at the five number summary. This gives values for calculating the range and interquartile range


```python
#getting specific runtime 
df['runtime'].describe()
```




    count    3854.000000
    mean      109.220291
    std        19.922820
    min        15.000000
    25%        95.000000
    50%       106.000000
    75%       119.000000
    max       338.000000
    Name: runtime, dtype: float64



We can conclude from looking at both the data point plot and boxplot the following stastical values:
1. 25% of the movies have a runtime of 95 minutes or less, this is the lower quartile
2. The mean or average runtime of movies in this data frame is 109 minutes
3. The median value is 106 minutes (50%).
4. 75% of the movies have a runtime of 119 minutes or less, this is the upper quartile.

### What is the relationship between runtime and revenue?


```python
#We can also inspect the data visually, using a scateerplot. 
plt.scatter(data = df, x = "runtime", y ="revenue")
```

The graph starts with a higher frequency and slops down after 50 minutes run time. So we can say the graph is Right Skewed. Most movies fall in the area of 80 to 130 minutes. 

One alternative way of depicting the relationship between two categorical variables is through a heat map. Heat maps were introduced earlier as the 2-d version of a histogram; here, we're using them as the 2-d version of a bar chart. 

<a id="conclusions"></a>
## Conclusions
<!--
&gt; **Tip**: Finally, summarize your findings and the results that have been performed. Make sure that you are clear with regards to the limitations of your exploration. If you haven't done any statistical tests, do not imply any statistical conclusions. And make sure you avoid implying causation from correlation!

&gt; **Tip**: Once you are satisfied with your work, you should save a copy of the report in HTML or PDF form via the **File** &gt; **Download as** submenu. Before exporting your report, check over it to make sure that the flow of the report is complete. You should probably remove all of the "Tip" quotes like this one so that the presentation is as tidy as possible. Congratulations!
-->

```python

```


```python

```
