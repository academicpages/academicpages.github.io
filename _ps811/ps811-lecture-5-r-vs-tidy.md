---
title: "Lecture 5: base R vs. tidyverse"
collection: ps811
type: "Graduate course"
venue: "Department of Political Science at the University of Wisconsin-Madison"
permalink: /ps811/ps811-lecture-5-r-vs-tidy
date: 2020-08-27
---

In this lesson, you will learn the differences between base R and Tidyverse, how you can achieve the same results using either language, and the advantages and disadvantages of both.

While my predecessors are tidyverse zealots, I am not. When it comes to learning R, I don't feel the need to force anyone into learning it one way or the other. People may disagree with this philosophy! Ultimately, I feel comfortable whenever you encounter R. And, the fact is, many people use both base R and tidyverse so it is best to know both. In PS 812, for example, you will be using primarily base R functions. So forcing you to learn only Tidyverse at this point feels impractical and incompatible with your broader learning goals.

Throughout this course, I will try to specify when I am using base R and when I am using Tidyverse. There are some functions that I find much easier (and more intuitive) in base R, and others that I prefer written in tidyverse. But just know this: if there's a way to write it in tidyverse, there's a way to write in base R, and vice versa.

## But first, what's Tidyverse?

[Tidyverse](https://www.tidyverse.org/) is a R package designed to clean and manipulate data. Compared to base R, Tidyverse can clean and manipulate data much faster with code that is more compact and practical. 

However, there are commands that are faster to write and easier to remember in base R, even if it doesn't process faster than its Tidyverse equivalent. You will figure out which commands those turn out to be.

In general, processing time is dependent on the amount of data you have, so if you only have a few thousand observations, it might not make much of a difference, but it will probably make a difference if you have tens or hundreds of thousands of observations.

# R basics

Some of these exercises were inspired by [Mike DeCrescenzo's R basics materials](https://github.com/mikedecr/PS811-computing/blob/master/code/01_basics.R).

1. Go to RStudio.

2. Go to File > Open Project in New Session. Find your `ps811-exercises` folder.

2. Go to File > New File > R Script.

3. A new Untitled1 R Script tab will open. Go to File > Save As. Name it `lecture5-practice.R`.

*Use R as a calculator*

4. Use R to add/subtract/multiply/divide. You don't *need* the spaces between each command, but it is easier to read if you do.

    ```
    2 + 3
    3 - 1
    12 * 12
    50 / 2
    ```
    Outputs should be 5, 2, 144, and 25, respectively.

5. R searches the next line if the inital line is incomplete.

    ```
    50 /
    2
    ```
    Output should be 25.
    
6. Use R to conduct order of operations.

    ```
    5^(10/5)
    ```
    Output should be 25.
    
7. You may also use commands for Euler's constant and the natural log in R.

    ```
    exp(1)
    log(1)
    ```

8. R recognizes pi and cosines.

    ```
    pi
    cos(pi)
    ```

If you ever want to figure out how to calculate something in R, just Google it or check out this short [Quick-R Operators](https://www.statmethods.net/management/operators.html) list for commonly used arithmetic and logical operators.

*Creating objects*

9. You want to put `8 + 1` into an object called `nine`.

    ```
    nine <- 8 + 1
    ```
10. See what happens when you type the name of the object, `six`. You get an output of `9`.

11. You can also do math with the object. Type in `sqrt(nine)`. You get an output of `3`.

12. Everything can be an object. You can store text in some other text.

    ```
    hello <- "hi"
    hello
    ```
    Output should be hi.
    
13. If you would like to put something else in the object, you can simply overwrite it.

    ```
    hello <- "hi, nice to meet you, what is your name"
    hello
    the_answer <- 8 + 1
    then_answer
    nine <- 50 + 4
    four # the answer does not have to be four
    ```
    Output should be "hi, nice to meet you, what is your name," 4, and 5, respectively.
    
*Creating vectors*

14. Vectors can be a bunch of different values.

    ```
    vector_example <- c(5, 6, 7, 8, 9, 10, 100)
    ```
15. You can multiple the vector with an equation, such as `2x`.

    ```
    results <- 2 * vector_example
    results
    ```
    Output should be 10, 12, 14, 16, 18, 20, 200.

16. You can multiply vectors.

    ```
    vector_example * results
    ```
    Output should be 50, 72, 98, 128, 162, 200, 20000.
    
17. You can do a matrix multiplication using `%*%`.

    ```
    vector_example %*% results
    ```
    
18. You can plug in the vectorrs into various functions.

    ```
    mean(vector_example)
    median(vector_example)
    mode(vector_example)
    sd(vector_example) # standard deviation
    sum(vector_example)
    ```
    Ouptut should be 20.71429, 8, "numeric" (there is no mode), 25.0034, 145, respectively.
    
# Loading data into R

1. When you first start with R, most tutorials will suggest that you use `setwd()` to call in your directory. And sure, that's fine. But since this course emphasize sreplication, what if someone opens your .Rproj in hopes of replicating your work and get an error when they try to run `setwd("/Users/marcyshieh/marcyshieh.github.io/_ps811")`? They are not you, they do not work on your computer, so they need to go through the extra step of changing that line.

    The person trying to replicate your project can probably type `getwd()` and replace whatever you have in `setwd()` with the resulting URL, but you want to make their lives (and your life!) easier.

2. Consider the `here` package. The `here` package allows anyone to replicate your work without being in your exact workspace and directory.

3. Paste the following code into your .R file. Highlight all the lines and click "Run" on RStudio OR command+return on MacOS or ctrl+enter on Windows.

    ```
    # install the here package
    install.packages("here")

    # load the here library
    library("here")
    # this is an equivalent to setwd()

    # check out where "here" is
    here()
    # this is an equivalent to getwd()
    
    # as you have probably guessed by now, the "#"" denotes comments and R leaves them alone when you run chunks of code
    ```
4. Download the `movie_metadata.csv` dataset. This [dataset is from Kaggle](https://www.kaggle.com/roshansharma/movies-meta-data) and contains metadata about movies from [IMDb](https://imdb.com). 

5. Move the `movie_metadata.csv` from the download location to your ps811-exercises directory.

6. Go to your .R file. Load the CSV file into your R environment.

    ```
    movie_metadata <- read.csv(here("movie_metadata.csv"))
    ```
    You are calling here() inside the read.csv() command because you are using the here() package. 
    
# Comparing base R vs. tidyverse

Much of the lesson here is indebted to [Hugo Taraves](https://tavareshugo.github.io/data_carpentry_extras/base-r_tidyverse_equivalents/base-r_tidyverse_equivalents.html), who wrote a nifty guide to syntax equivalents of base R vs. Tidyverse.

*Prerequisites* You need to install the `dplyr` and `tidyr` packagess, and load them. Use the `install.packages()` and `library()` functions to do this. You need these packages to use tidyverse functions.

    Always load your packages on the top of the .R file.

Take a look at the variables in the dataset using `names(movie_metadata)`.

We are going to first go through everything in base R, then repeat everything in Tidyverse. Hopefully this gives you a sense of how base R and Tidyverse work.

## base R

This is how these commands work in base R.

1. Extract the first 100 rows.

    ```
    movie_metadata_100 <- movie_metadata[1:100, ]
    ```
    
    - Rows are equivalent to observations.
    - Columns are equivalent to variables.

2. Look at the existing variables in dataset.

    ```
    # you can identify the variables by name
    movie_metadata_100[, c("director_name", "movie_title")] 
    
    # or you can identify the variables by their column index/number
    movie_metadata_100[, c(2, 12)]
    ```

3. Create a new variable in the dataset.

    ```
    # you want to get the sum of facebook likes for the first 3 actors listed in the movie
    movie_metadata_100$main_actors_fb_popularity <-
    movie_metadata_100$actor_1_facebook_likes +
    movie_metadata_100$actor_2_facebook_likes +
    movie_metadata_100$actor_3_facebook_likes
    ```

4. Filter rows in dataset.

    ```
    # you want to extract the observations where there is a IMDB score of 5+ and 2 number of faces in the poster
    subset(movie_metadata_100, imdb_score > 5 &
    facenumber_in_poster==2)
    ```

5. Arrange rows.

    ```
    # descending order of movie title followed by
    ascending order of budget
    iris[order(rev(movie_metadata_100$movie_title),
    movie_metadata_100$budget) , ]
    ```

6. Summarize observations.

    ```
    # Create a dataframe with mean and standard deviation information
    data.frame(budget.mean = mean(movie_metadata_100$budget),
    budget.sd = sd(movie_metadata_100$budget),
    gross.mean = mean(movie_metadata_100$gross),
    gross.sd = sd(movie_metadata_100$gross))
    ```

7. Group observations.

    * Summarize rows within groups

     ```
     # Using aggregate
     aggregate(formula = cbind(budget, gross) ~ country + genres, 
          data = movie_metadata_100$gross, 
          FUN = function(x){
            c(mean = mean(x), sd = sd(x))
          })
     ```

    * Create new columns based on calculations done within groups.
    
    ```
    # centering the budget and subtracting the mean within the country
    movie_metadata_100$budget_centered <- ave(movie_metadata_100$budget,
    movie_metadata_100$country, FUN = function(x) x - mean(x))
    ```
    
    * Filter based on conditions
    
    ```
    # Navigate the data frame via groups.
    max_budget <- by(movie_metadata_100, 
                    INDICES = movie_metadata_100$country, 
                    FUN = function(x){
                      x[x$budget == max(x$budget), ] 
                    })

    # Turn the results into a data frame
    do.call(rbind, max_budget)
    ```

## Tidyverse

You know how to do it in base R, so now you can see how it works in Tidyverse!

1. Extract the first 100 rows.

    ```
    movie_metadata_100tidy <- movie_metadata %>% top_n(100)
    ```
    As you have probably noticed, Tidyverse uses `%>%`, which are called "pipes." In essence, you are calling your dataset, and piping functions into it.

2. Look at existing variables in dataset.

    ```
    # you can identify the variables by name
    select(movie_metadata_100tidy, director_name, movie_title)
    
    # or you can identify the variables by their column index/number
    select(movie_metadata_100tidy, 2, 12)
    ```
    If you want to turn this selection into an object, just put `movie_metadata_100tidy_select<-` (or whatever would make sense for you) in front of the command.

3. Create a new variable in the dataset.

    ```
    # you want to get the sum of facebook likes for the first 3 actors listed in the movie
    
    movie_metadata_100tidy <- mutate(movie_metadata_100tidy,
    main_actors_fb_popularity = actor_1_facebook_likes +
    actor_2_facebook_likes + actor_3_facebook_likes)
    
    # you should have created a brand new variable!
    View(movie_metadata_100tidy)
    ```
    
    Notice that you don't have to refer to the data set every time you call a variable. That's one of the advantages of Tidyverse!

4. Filter rows in dataset.

    ```
    # you want to extract the observations where there is a IMDB score of 5+ and 2 number of faces in the poster
    filter(movie_metadata_100tidy, imdb_score > 5 & facenumber_in_poster==2)
    ```
    You may also turn this filtered dataset into an object if you would like!

5. Arrange rows.

    ```
    # descending order of movie title followed by
    ascending order of budget
    arrange(movie_metadata_100tidy, desc(movie_title), budget) 
    ```

6. Summarize observations.

    ```
    # Create a dataframe with mean and standard deviation information
    summarise(movie_metadata_100tidy,
              budget.mean = mean(budget),
              budget.sd = sd(budget),
              gross.mean = mean(gross),
              gross.sd = sd(gross)
    ```

7. Group observations.

    * Summarize rows within groups

     ```
     movie_metadata_100tidy %>% 
          group_by(country, genres) %>% 
          summarise(budget.mean = mean(budget),
            budget.sd = sd(budget),
            gross.mean = mean(gross),
            gross.sd = sd(gross)) %>% 
            ungroup()
            
      # ungroup() removes any grouping changes you make from analyses beyond this section
     ```

    * Create new columns based on calculations done within groups.
    
    ```
    # centering the budget and subtracting the mean within the country
    
    movie_metadata_100tidy %>% 
    group_by(country) %>% 
    mutate(budget.centered = budget - mean(budget)) %>% 
    ungroup() # remove any groupings from downstream analysis
    ```
    
    * Filter based on conditions
    
    ```
    movie_metadata_100tidy %>% 
    group_by(country) %>% 
    filter(budget == max(budget))
    ```
    