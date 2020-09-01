---
title: "Lecture 6: Functions"
collection: ps811
type: "Graduate course"
venue: "Department of Political Science at the University of Wisconsin-Madison"
permalink: /ps811/ps811-lecture-6-functions
date: 2020-08-27
---

In this lesson, you will learn how to use R functions, such as loops, apply, lists, scoped verbs, nesting, and mapping.

These R functions are often a neglected part of contemporary R education, but they can be useful and you will encounter them in PS 812 and the machine learning course. As more R users begin to rely on packages, the need to write their own functions may seem irrelevant. However, it's good to know what *kinda* happens within the black box of a package.

Much of the material here is inspired by [Mike DeCrescenzo's Functional Programming in R](https://github.com/mikedecr/PS811-computing/blob/master/code/07_functional-programming.R) lesson.

# Loops

Say you want to repeat the same thing multiple times for `n` observations. Most specialized R packages do this for you without you having to design the loop, but we are just going over loops so you can get an idea of how they work. Loops can be kind of slow, and usually a loop in R is way faster in Python and other programming languages.

I do want to say that you do use loops in PS 812 and the machine learning class.

Here is a simple loop so you can get the basic idea of what a loop does.

```
for (i in 1:10) {
  print(i)
}
```

You should end up with an output that shows 10 vectors with one number in each vector. Each number is a number from 1 to 10. What you are doing here is:

* `for (i...)` you are calling the element `i`
* `for (i in 1:10)` vector 1:10 is contained in the element `i`
* `print(i)` you want to do an operation that uses `i`, in this case, you are just printing everything in `i`

## Using loops in a dataset

Say you want to use loops with your dataset.

We are going to do some loop examples with the datasets native to R. You can access them by typing in `data()`. We are going to use the `iris` dataset. You can take a look at the `iris` dataset by typing `View(iris)`.

The following loop tells R to count the number of columns per row. 

```
# create a container
# your results will be numeric but you want to make sure R knows that
columns_loop <- numeric()

for (row in 1:nrow(iris)) {
  columns_loop[row] <- length(iris[row, ])
  }
  
# you will find that for every row, there are 5 columns, which checks out
```
## Vectorizing the process

You can speed up this process by *vectorizing* it.

```
columns <- apply(X = iris, MARGIN = 2, FUN = length)
```

* `apply()` is a function that *applies*a function over rows or columns of a grid/array and makes it really helpful when you are working with matrices
* `X = iris` refers to the dataset
* `MARGIN = 1` refers to the number of columns in every row (`MARGIN = 2` refers to the number of rows in every column)
    * 1 = rows, 2 = columns
* `FUN = length` refers to the function that is being applied. In this case, we are applying the `length` function, which simply tells you how wide (columns) or long (rows) the dataset is.

You can learn more about the `apply` function (and many others) by typing in `?apply`.

# Applying lapply()

You can just turn a data frame into a list.

The `iris` dataset is a dataframe. You can turn it into a list.

```
iris_list <- as.list(iris)

# check out the list
iris_list

# check out the first five observations of the list
lapply(iris_list, head)
```

You can also create your own lists.

```
list(colors = c("red", "green", "blue"),
     food = c("pizza", "sushi", "burger"),
     drink = c("coffee", "tea", "juice"))
```     

# Indexing your list

```
str(iris_list)
```

`str` allows you to display the structure of R objects, including information on the type, the number of columns, the number of rows per column, the number of factors per column, etc.

```
str(iris_list[1])
```

The `[1]` allows you to specify the first column. In this case, that first column is `Sepal.Length`.

You may also double index. Each time you index, you get to a deeper level of the object, whatever it might be. Of course, the `iris` data may not be the best example, but here is a [nifty tweet](https://twitter.com/hadleywickham/status/643381054758363136?lang=en) for you to understand indexing better.

There is also `tapply()`, which allows you to apply functions to groups of data. In this case, you will be applying the mean function to each species. As such, in base R...

```
tapply(
  X = iris$Sepal.Length, 
  INDEX = list(iris$Species), 
  FUN = mean, 
  na.rm = TRUE  
)
```
You can do `tapply()` using Tidyverse in a way that is a *bit* more intuitive.

```
iris %>%
  group_by(Species) %>%
  summarize(
    mean_nom = mean(Sepal.Length, na.rm = TRUE)
  ) 
```

# Functions with dplyr and purrr packages

You want to familiarize yourself with these "scoped verbs", or "apply functions."

* `if`: apply functions to variables that fulfills certain conditions (i.e., appy this function `if` this is true)
* `at`: apply functions to specific variables (i.e., apply this function `at` this variable)
* `all`: apply functions to every variable (i.e., apply this function at `all` variables)

## Using if()

If the column contains numeric values, replace each cell with the length of the data frame.

* I am using `length` because it is a function you are already familiar.

```
iris %>%
  mutate_if(
    .predicate = is.numeric,
    .funs = length
  )
```
You can select variables that have numeric values. You can replace `is.numeric` with other R data types. Here is a [list of basic data types in R](http://www.r-tutor.com/r-introduction/basic-data-types).

```
select_if(iris, is.numeric)
```

## Using at()

The following command allows you to:

* only use the function on variables that start with "Sepal"
* divide each number in that variable by 100
* select the variables that start with "Sepal"

```
iris %>%
  mutate_at(
    .vars = vars(starts_with("Sepal")),
    .funs = function(x) x / 100
  ) %>% 
  select(starts_with("Sepal"))
```

## Defining your own functions

You can create your own functions! Below, I create a function where I divide a number by 2, or split it in half.

```
make_half <- function(x) {
  return(x / 2)
}

make_half(88)
```
Output should be 44.

### Anonymous Function

You can also create a function using `sapply` and not name it. This is called an *anonymous function*. You just use it once and move on.

```
sapply(88, function(x) x / 2)
```

### Simple lambda function

You can create a "lambda function," which also goes by the names of a "quosure-style" function or a "purrr-style" function. It is similar to an anonymous function.

```
select_if(
  iris,
  .predicate = ~ sum(is.numeric(.)) > 0
)
```
In this case, you are:

* selecting from the `iris` dataset if the variable is numeric
* variable(s) will only selected if the number of `is.numeric` variables is larger than 0

### More complex lambda function

```
iris %>%
  mutate_at(
    .vars = vars(Sepal.Length, Sepal.Width),
    .funs = ~ . / 100
  )
```
Here, you are replacing `function(z)` with `~` and call `z` with `.`.

## Applying more than one function

```
summarize_all(
  iris, 
  .funs = list(uniques = ~ n_distinct(.), 
               obj_type = class)
)
```

Here, you are looking at the `iris` dataset and applying the following two functions:

* the number of distinct numbers per variable `n_distinct(.)` in the dataset and denoting the output as `uniques`
* the data class (i.e., type) for each variable in the dataset and denoting that output as `obj_type`

# Nesting data frames

You need to install the `purrr` package and load it. `purrr` is party of the Tidyverse universe, so the following commands will be written in Tidyverse. This also means you can't use `purrr` without loading `tidyverse` first.

Nesting generates one row for each group from the non-nested columns. This is useful for models.

Probably the best way to understand nesting is through a grouping variable.

```
iris %>%
  group_by(Species) %>%
  nest() 
```

The output should show that there are 3 different groups in the Species variable. For each Species, there are 50 rows (observations) and 4 columns (variables).

Essentially, these are data frames within a data frame. Each data column is a *list*, which is called a list-column.

This is helpful when you want to estimate a model within each species.

To illustrate this, go ahead and create an object that groups your data set by Species. 

```
nested_iris <- iris %>%
  group_by(Species) %>%
  nest() %>%
  print()
```

Then, you want to know, "Does the width of the petal affect the length of the petal?" (I don't know anything about irises, so hopefully this question isn't too dumb.) To do this, you can run a regression.

```
nested_models <- nested_iris %>%
  mutate(
    model = map(
      .x = data, 
      .f = ~ lm(Petal.Length ~ Petal.Width, data = .x)
    )
  ) %>%
  print()
```  
The output should show a new column: the "model" column.

What you just did is, you grouped all the Species together, called the data, and ran the `lm` function, which is the function for an ordinary least squares regression. Then, you printed the results. 

If you want to look at each variable in the nested data frame, you can crack it open the same way you look at variables in a regular data frame.

```
nested_models$Species
nested_models$data
nested_models$model
```

If you want to extract coefficients into a new column called "coefs," you can just call the `model` function you created.

```
nested_coefs <- nested_models %>%
  mutate(coefs = map(model, coefficients)) %>%
  print()
  
nested_tidy
```
Output should show a new variable called `coefs`.

```
nested_coefs$coefs
```
output should list all the coefficients for each Species group.

When you are done, you can unnest columns.

```
coefs <- nested_coefs %>%
  unnest(coefs) %>%
  print()
```  
As you can see, the coefs column is no longer grouped together. Once they are unnested, it expands: there's a row for the intercept and the coefficient for each group.

You will be unable to unnest non-data frame objects (try `nested_coefs %>% unnest(model)`---it doesn't work!!), but, as you recall, you can pull them out by doing `nested_tidy$model`. Or, if you want to write this in a tidy way...

```
nested_coefs %>% pull(model)
```

If you want to work more with purrr, I highly recommend that you check out the [purrr cheat sheet](https://github.com/rstudio/cheatsheets/blob/master/purrr.pdf).