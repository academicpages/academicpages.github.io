---
title: purrr for analysis in R
author: ~
date: '2018-12-11'
slug: purrr-for-analysis-in-r
categories: []
tags: []
---

In my postdoc work, I was running a lot of models on data. I found R really useful to doing the models, but I often struggled to write nice code around running many models. Until I discovered [purrr](https://purrr.tidyverse.org/).

As an example, say I wanted to do some analysis on the "iris" data set, which "gives the measurements in centimeters of the variables sepal length and width and petal length and width, respectively, for 50 flowers from each of 3 species of iris", *Iris setosa*, *I. versicolor*, and *I. virginica*.

```{r}
iris %>%
  head(3) %>%
  knitr::kable(caption = 'First records in the iris data')
```

Let's consider the relationship between sepal length and width in the three species.

```{r}
iris %>%
  ggplot(aes(x = Sepal.Length, y = Sepal.Width, color = Species)) +
  stat_smooth(method = 'lm') +
  geom_point()
```

In base R it is relatively straightforward to extract the slope $m$ and intercept $b$ for a least-squares best fit to each species by specifying a model that includes interactions between species $s$ and slope:
$$
y_i \sim m_{s_i} x_i + b_{s_i}
$$

```{r}
lm(Sepal.Width ~ Species * Sepal.Length, data = iris) %>%
  summary()
```

In that regression, R treated *I. setosa* as the "base" species, so `(Intercept)` and `Sepal.Length` are the intercept and slope for *I. setosa*. The intercept for *I. versicolor* is the `(Intercept)` term plus the `Speciesversicolor` term, and the slope is the `Sepal.Length` term plus the `Speciesversicolor:Sepal.Length` term.

This is a bit of a mess if I just wanted to know what the slopes and intercepts were for each species. If I wanted three separate models, there's a few ways to do it.

I'll start with the ugly, naive way, which is to make three different data frame and three different models:

```{r}
# these two lines would be repeated for I. versicolor and I. virginica
setosa_data = iris[iris$Species == 'setosa', ]
setosa_model = lm(Sepal.Width ~ Sepal.Length, data = setosa_data)

# the slope for I. setosa
coef(setosa_model)['Sepal.Length']
```

This approach, although it works for the iris data, doesn't scale well, since it requires a lot of manual typing of the species names. The second approach is to use some the base R functions `split`, which will break the data into a list of three separate data sets, and `lapply`, which will run a function on each member of that list:

```{r}
species_datasets = split(iris, iris$Species)
species_models = lapply(species_datasets, function(data) {
  lm(Sepal.Width ~ Sepal.Length, data = data)
})

# get the slope from the first model, which is for I. setosa
coef(species_models[[1]])['Sepal.Length']
```

This approach is still awkward because the data and the models are in separate objects. You need to manually keep track of them, make sure they are in the same order, etc. It would be a lot nicer if the data, the models, and whatever else you wanted to pull out from either of those were in one structure.

It turns out that data frame the columns in data frames can be lists, so we can make a vector in the data frame a list of objects:

```{r}
data_frame(
  species = levels(iris$Species),
  model = species_models
)
```

(The "S3" in `S3: lm` means that the linear model object is an S3 object. R has multiple object-oriented programming systems, and S3 is one of them. It's not that important.)

This is where `purrr` comes in. First, there is a function `nest`. Like `split`, it breaks a dataset down into smaller parts. Unlike `split`, it keeps them in a nice dataframe. It's called "nest" because one of the columns in the data frame is a list of the smaller data frames.

```{r}
# For this and future examples, it will be convenient to have the iris
# data as a tibble, rather than data.frame. It prints out nicer.
iris %<>% as_tibble

# "minus" means put all columns except Species into the nested dataframes
tidyr::nest(iris, -Species)
```

Next, there is a family of functions `map`. Just like map functions in other languages and the `Map` and `lapply` functions in base R, it takes a function and a vector of inputs, or multiple inputs, and returns the outputs.

```{r}
iris %>%
  tidyr::nest(-Species) %>%
  mutate(
    # this works
    model1 = lapply(data, function(x) lm(Sepal.Width ~ Sepal.Length, data = x)),
    # "map" also works
    model2 = map(data, function(x) lm(Sepal.Width ~ Sepal.Length, data = x)),
    # "map" also allows a shorthand for anonymous functions
    model3 = map(data, ~ lm(Sepal.Width ~ Sepal.Length, data = .))
  )
```

The really nice bit about `map` is that is has close cousins like `map_dbl` which specify that the output should be a vector of numbers, rather than a list of numbers. Here's what I mean:

```{r}
iris %>%
  tidyr::nest(-Species) %>%
  mutate(
    model = map(data, ~ lm(Sepal.Width ~ Sepal.Length, data = .)),
    slope1 = map(model, ~ coef(.)['Sepal.Length']),
    slope2 = map_dbl(model, ~ coef(.)['Sepal.Length'])
  )
```

Note that the `map` for `slope` in the above gave a list of single numbers, while `map_dbl` gave a vector that "lays" more nicely in the data frame.

Now it's nice and easy to compare the models in the context of a data frame:

```{r}
iris %>%
  tidyr::nest(-Species) %>%
  mutate(
    model = map(data, ~ lm(Sepal.Width ~ Sepal.Length, data = .)),
    slope = map_dbl(model, ~ coef(.)['Sepal.Length']),
    slope_confint = map(model, ~ confint(.)['Sepal.Length', ]),
    slope_cil = map_dbl(slope_confint, first),
    slope_ciu = map_dbl(slope_confint, last)
  ) %>%
  ggplot(aes(x = Species, y = slope, ymin = slope_cil, ymax = slope_ciu)) +
  geom_point() +
  geom_errorbar()
```

Note that this final result only computed each model once, only computed the confindence intervals once, and managed to make the output figure without once creating an intermediate object!
