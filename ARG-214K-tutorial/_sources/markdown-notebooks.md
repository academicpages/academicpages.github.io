---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Data loading
In this chapter, we will see how we can load the data in the three formats that have been published (MySQL, TSV and HDF).

## Working with MySQL 
Follow [this link](https://dev.mysql.com/doc/mysql-getting-started/en/) to see how to install MySQL and setup a database.

### Configuring MySQL settings
Here, one can either either configure a [my.cnf file](https://dev.mysql.com/doc/refman/8.0/en/option-files.html), or store the settings manually in a `config.json` file as given below:

```
{
    "host": "localhost", 
    "password": "password!", 
    "user": "username", 
    "port": "port", 
    "database": "db_name", 
    "datadir": "dataFolder"
}
```

### Loading MySQL dumps into the database
For each of the dump files (.sql), load them with the command `mysql db_name < dump-file.sql`. `db_name` is the name of database to contain the tables, and the `dump-file.sql` is the file **containing** the table structure and data.
****
We have written a short bash script loader.sh for this, where we give the path to the directory containing dump files (`-d $dataDir`) and the name of the MySQL database (`-n $database`):
:::{code-block} bash
> loader.sh -d $dataDir -n $database
:::

````{dropdown} Script: loader.sh
```{code-block} bash
#!/bin/sh
instructions() {
    echo "Load MySQL dump file(s) into a MySQL database." >&2
    echo "Usage: $0 [-d DIRECTORY] [-n DATABASE] " >&2
    echo " -d Directory with dump files." >&2
    echo " -n Name of database to load tables into." >&2
}

while getopts d:n:h option
do
case "${option}" in
d) dumpdir=${OPTARG};;
n) dbname=${OPTARG};;
h) instructions; exit 0;;
\?)
    echo "Option '-$OPTARG' is not a valid option." >&2
    instructions
    exit 1
    ;;
:)
    echo "Option '-$OPTARG' needs an argument." >&2
    instructions
    exit 1
    ;;
esac
done


# find files
find $dumpdir -type f -name "*.sql" | while read dumpfile; do
    mysql $dbname < $dumpfile
    echo "Loaded $dumpfile into MysQL database $dbname." 
done
```
````

### Reading MySQL data

`````{tabbed} Python
There are different ways for retrieving data lying in a MySQL database. Here, we show two approaches: one with Pandas and one with a custom function.

````{dropdown} Pandas
It is possibly to use the [`pandas.read_sql`](https://pandas.pydata.org/docs/reference/api/pandas.read_sql.html) function to query the database, although this also requires [mysql-connector-python](https://dev.mysql.com/doc/connector-python/en/connector-python-installation-binary.html) to be installed.
```{code-block} bash
python -m pip install mysql-connector-python
```


```{code-block} python
import mysql.connector as connection
import pandas as pd

mydb = connection.connect(host=host, port=port, database=database, user=user, passwd=passwd, use_pure=True)
query = "select * from metadata"
df = pd.read_sql(query, mydb)
mydb.close()

df.head()
```

````

````{dropdown} Custom function
This is a custom function that interacts with the mysql client installed in your terminal, where you can add the configuration settings in the `args=` argument in the function.
```{code-block} python
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

cli_args = f"--database={database} --host={host} --port={port} --user={user} --password={passwd}"
df = query_db("select * from metadata", args=cli_args)
df.head()
```
````
`````

`````{tabbed} R
We can use the [RMySQL](https://cran.r-project.org/web/packages/RMySQL/) package to connect to the MySQL database.

```{code-block} R
install.packages("RMySQL")
library(RMySQL)
mydb = dbConnect(MySQL(), user=user, password=passwd, host=host, port=as.integer(port), dbname=database)
rs = dbSendQuery(mydb, "select * from metadata")
data = fetch(rs, n=5)
data
```
`````

## Working with TSV files
It is fairly straightforward to work with the .tsv files.

### Loading TSV files
`````{tabbed} Python
For example, with Pandas:
```{code-block}
import os
import pandas as pd
tsvFile = os.path.join(dataDir, 'metadata.tsv')
df = pd.read_csv(tsvFile, sep='\t')
df.head()
```
`````

`````{tabbed} R
To read the .tsv files in R one can use either base functions or for example [readr](https://readr.tidyverse.org/).
````{dropdown} Base R
```{code-block} R 
data <- read.csv(file.path(dataDir, 'metadata.tsv'), sep='\t')
```
````

````{dropdown} readr
```{code-block} R
install.packages("readr")
data <- readr::read_tsv(file.path(dataDir, 'metadata.tsv'))
```
````
`````

## Working HDF files
HDF5 is a data software ibrary that is built for fast I/O processing and storage.

### Loading HDF files
### Loading TSV files
`````{tabbed} Python
The Pandas library contains the function [`pandas.read_hdf`](https://pandas.pydata.org/docs/reference/api/pandas.read_hdf.html).

```{code-block}
import os
import pandas as pd
h5File = os.path.join(dataDir, 'metadata.h5')
df = pd.read_hdf(h5File)
df.head()
```
`````

`````{tabbed} R
There are no straight forward ways in R to load the HDF5 file types, although there are several libraries that claim to do it, like [hdf5r](https://hhoeflin.github.io/hdf5r/) and [rhdf5](https://www.bioconductor.org/packages/devel/bioc/vignettes/rhdf5/inst/doc/rhdf5.html).
Let me know if you can get it to work!
`````
