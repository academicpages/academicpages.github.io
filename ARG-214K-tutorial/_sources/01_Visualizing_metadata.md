# Visualizing Metadata
In this chapter, a brief overview of the distribution of metadata variables and how to visualize them is given.

The code examples is based on interacting with the MySQL database, but the code for the visualizations themselves can easily be made to run as long as you have the correct dataframe loaded.

## Setup
The various settings that are sensitive are stored in a config.json file, but just change the settings to what fit your own setup.
`````{tabbed} Python
````{code-block} Python
import json
with open('../config.json', 'r') as source:
    config = json.load(source)

database=config['database'] # name of database
host=config['host'] # host address of MySQL server
port=config['port'] # port of MySQL server
user=config['user'] # user name
passwd=config['password'] # password for user 
dataDir=config['datadir'] # directory where data files are stored
````

Furthermore, let's define the query_db function again.
````{code-block} Python
import subprocess
import pandas as pd
from io import StringIO

def query_db(query, args=''):
    cmd = "mysql {} -e \"{}\"".format(args, query)
    p = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if p.returncode > 0:
        print("Failed to query database with error:")
        print(p.stderr.decode())
    
    else:
        df = pd.read_csv(StringIO(p.stdout.decode()), sep='\t')
        return df
````

`````

`````{tabbed} R
````{code-block} R
library('rjson')
config <- fromJSON(file="../config.json")

database <- config$database # name of database
host <- config$host # host address of MySQL server
port <- config$port # port of MySQL server
user <- config$user # user name
passwd <- config$password # password for user 
dataDir <- config$datadir # directory where data files are stored
````

And import other libraries for retrieving data, manipulating and plotting:
````{code-block} R
library(ggplot2)
library(RMySQL)
library(dplyr)
````

`````

## Loading metadata
The metadata are available in either the MySQL table `metadata` or in TSV format in the file `metadata.tsv` and HDF5 format `metadata.h5`. Let's load it from our MySQL database.

`````{tabbed} Python
```{code-block} Python
# Load the metadata from MySQL database
cli_args = f"--database={database} --host={host} --port={port} --user={user} --password={passwd}"
metadata = query_db("select * from metadata", args=cli_args)

metadata['collection_date'] = pd.to_datetime(metadata['collection_date'], errors='coerce')
metadata.loc[metadata['collection_date'] > '2020-01-01', 'collection_date'] = pd.NaT # cannot be later than this date

# combine host labels metagenome and metagenomes into one
metadata.loc[metadata['host'] == 'metagenomes', 'host'] = 'metagenome'
```
`````

`````{tabbed} R
```{code-block} R
mydb = dbConnect(MySQL(), user=user, password=passwd, host=host, port=as.integer(port), dbname=database)
rs = dbSendQuery(mydb, "select * from metadata")
metadata = fetch(rs, n=-1) # retrieve all with n=-1
```

Some preprocessing is required before we look at the data:
```{code-block} R
metadata$collection_date <- as.Date(metadata$collection_date)
metadata[which(metadata$collection_date > '2020-01-01'), 'collection_date'] <- NA # cannot be later than this date

# combine host laels metagenome and metagenomes into one
metadata[which(metadata$host == 'metagenomes'), 'host'] <- 'metagenome'
```
`````

## Inspecting the metadata
There are a multitude of different metadata associated with each metagenomic dataset. 

In the paper, we have looked at the distribution of samples according to the following columns: `continent`, `host`, `collection_year` (from the `collection_date`), number of trimmed reads vs mapped reads. So let's replicate these figures.

````{dropdown} Metadata columns
```{glossary}
run_accession
    Identifier for sequencing read dataset

sample_accession
    Identifier for sample

project_accession
    Identifier for project

country
    Country where sample was taken

location
    GPS coordinates for sampling location

continent
    Denotes which continent the country is in

collection_date
    Sampling date

host
    Sampling host

instrument_platform
    Sequencing platform

```
````

### Distribution of metagenomes per year
We first create the column `collection_year` from the `collection_date` column, and then we count the number of samples per year. Finally, we visualize these counts in a barplot.
`````{tabbed} Python
hwkj
`````

`````{tabbed} R
hej
`````

### Distribution of metagenomes per continent
This is a pretty similar process as for looking at the distribution of samples according to sampling year, instead we just look at the `continent` labels.

`````{tabbed} Python
hwkj
`````

`````{tabbed} R
hej
`````
### Distribution of metagenomes per host
This is a pretty similar process as for looking at the distribution of samples according to sampling year, instead we just look at the `host` labels.

NOTE: There are many host labels, so let us look at those with at least 1000 samples. 

`````{tabbed} Python
hwkj
`````

`````{tabbed} R
hej
`````
