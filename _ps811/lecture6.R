for (i in 1:10) {
  print(i)
}

nrow(iris)
ncol(iris)

columns_loop <- numeric()

for (row in 1:nrow(iris)) {
  columns_loop[row] <- length(iris[row, ])
}

columns_loop

iris_list <- as.list(iris)

lapply(iris_list, head)

list(colors = c("red", "green", "blue"),
     food = c("pizza", "sushi", "burger"),
     drink = c("coffee", "tea", "juice"))

str(iris_list)
str(iris_list[1])
str(iris_list[[1]])

tapply(
  X = iris$Sepal.Length, 
  INDEX = list(iris$Species), 
  FUN = mean, 
  na.rm = TRUE  
)

library(tidyverse)
library(dplyr)
iris %>%
  group_by(Species) %>%
  summarize(
    mean_nom = mean(Sepal.Length, na.rm = TRUE)
  ) 

iris %>%
  mutate_if(
    .predicate = is.numeric,
    .funs = length
  )

sapply(88, function(x) x / 2)

select_if(
  iris,
  .predicate = ~ sum(is.numeric(.)) > 0
)

summarize_all(
  iris, 
  .funs = list(uniques = ~ n_distinct(.), 
               obj_type = class)
)

# df1 is a nested data frame
(df1 <- tibble(
  g = c(1, 2, 3),
  data = list(
    tibble(x = 1, y = 2),
    tibble(x = 4:5, y = 6:7),
    tibble(x = 10)
  )
))

library(purrr)

nested_models <- nested_iris %>%
  mutate(
    model = map(
      .x = data, 
      .f = ~ lm(Petal.Length ~ Petal.Width, data = .x)
    )
  ) %>%
  print()

nested_tidy <- nested_models %>%
  mutate(coefs = map(model, coefficients)) %>%
  print()

nested_tidy$coefs
