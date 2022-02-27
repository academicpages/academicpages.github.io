---
title: 'Google R Style Guide'
date: 2018-02-26
permalink: /posts/2018/02/google-r-style-guide/
tags:
  - tutorial
  - code style
  - google
---

This post introduces R style guide from [google community](https://google.github.io/styleguide/Rguide.xml). It is very useful for beginners to learn how to code in an appropriate way that can share with other scholars. The basic goal of this post is to introduce the commonly used coding styles.

## R Style Rules

* File Names: end in .R
* Identifiers: variable.name (or variableName), FunctionName, kConstantName
* Line Length: maximum 80 characters
* Indentation: two spaces, no tabs
* Spacing
* Curly Braces: first on same line, last on own line
* else: Surround else with braces
* Assignment: use <-, not =
* Semicolons: don't use them
* General Layout and Ordering
* Commenting Guidelines: all comments begin with # followed by a space; inline comments need two spaces before the #

### Organization
Google R style guide empashizes a very useful general Layout and Ordering:
> If everyone uses the same general ordering, we'll be able to read and understand each other's scripts faster and more easily.
* Copyright statement comment
* Author comment
* File description comment, including purpose of program, inputs, and outputs
* source() and library() statements
* Function definitions
* Executed statements, if applicable (e.g., print, plot)



### Indentifier Conventions
Google R style guide suggests that
> Don't use underscores ( _ ) or hyphens ( - ) in identifiers. Identifiers should be named according to the following conventions. The preferred form for variable names is all lower case letters and words separated with dots (variable.name), but variableName is also accepted; function names have initial capital letters and no dots (FunctionName); constants are named like functions but with an initial k.

### Funcion Documentation
Google R style guide recommends that
> Functions should contain a comments section immediately below the function definition line. These comments should consist of a one-sentence description of the function; a list of the function's arguments, denoted by Args:, with a description of each (including the data type); and a description of the return value, denoted by Returns:. The comments should be descriptive enough that a caller can use the function without reading any of the function's code.

Here is an example:
```
CalculateSampleCovariance <- function(x, y, verbose = TRUE) {
  # Computes the sample covariance between two vectors.
  #
  # Args:
  #   x: One of two vectors whose sample covariance is to be calculated.
  #   y: The other vector. x and y must have the same length, greater than one,
  #      with no missing values.
  #   verbose: If TRUE, prints sample covariance; if not, not. Default is TRUE.
  #
  # Returns:
  #   The sample covariance between x and y.
  n <- length(x)
  # Error handling
  if (n <= 1 || n != length(y)) {
    stop("Arguments x and y have different lengths: ",
         length(x), " and ", length(y), ".")
  }
  if (TRUE %in% is.na(x) || TRUE %in% is.na(y)) {
    stop(" Arguments x and y must not have missing values.")
  }
  covariance <- var(x, y)
  if (verbose)
    cat("Covariance = ", round(covariance, 4), ".\n", sep = "")
  return(covariance)
}
```

### Re-format Your code
If you are not a good code writer, there is a easy way that you can reformat your codes using the FORMATR package developed by [Yihui Xie](https://yihui.name/formatr/).
>The formatR package was designed to reformat R code to improve readability; the main workhorse is the function tidy_source(). Features include:
* long lines of code and comments are reorganized into appropriately shorter ones
* spaces and indent are added where necessary
* comments are preserved in most cases
* the number of spaces to indent the code (i.e. tab width) can be specified (default is 4)
* an else statement in a separate line without the leading } will be moved one line back
* = as an assignment operator can be replaced with <-
* the left brace { can be moved to a new line
