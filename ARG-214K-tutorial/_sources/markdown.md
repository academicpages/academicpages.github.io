# Data loading
In this chapter, we will see how we can load the data in the three formats that have been published (MySQL, TSV and HDF).

## Loading MySQL dumps
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

### Reading MySQL dumps into the database
For each of the dump files (.sql), load them with the command `mysql db_name < dump-file.sql`. `db_name` is the name of database to contain the tables, and the `dump-file.sql` is the file containing the table structure and data.

We have written a short bash script [`loader.sh`](loader.sh) for this, where we give the path to the directory containing dump files (`-d $dataDir`) and the name of the MySQL database (`-n $database`):
```
> ../loader.sh -d $dataDir -n $database
```

## Loading TSV files

## Loading HDF files