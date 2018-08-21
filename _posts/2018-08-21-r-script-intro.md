---
title: 'How to Write R Code in a Efficient Way'
date: 2018-08-21
permalink: /posts/2018/02/r-script-intro.md/
tags:
  - tutorial
  - R package
  - R script
---

This post briefly introduces my personal preference writing R code with Rstudio. This is not to say this is the best way, but I think it fits me at least.

I would suggest you to use part of it that fits your preference. If you use Rstudio to organize your codes, it would be better to create your R project, which is more convinient for the replication purpose.

Here are some codes I often copy and paste from one project to another project at the begining of the script.
```
# script to clean dissertation campaign finance data
# author: yongjun zhang
# email: yongjunzhang@email.arizona.edu

# rm(list=ls()) ****I do not suggest to use this.
# load pacman packages
if(require(pacman)){
  cat("Package exists...\n")
  library(pacman)
}else{
  cat("Package not installed; Installing...\n")
  install.packages("pacman")
  library(pacman)
}
# define necessary packages
packages<-c("tidyverse","ggplot2","ggsci","gdata"","ggpubr","ggthemes","haven","here")
p_load(packages,character.only = T)

here()

file=list.files(path=here("03 data","campaignmoney"),full.names = T)

data<-read_csv(file,col_names = T)%>%
  mutate_at(vars(.),funs(tolower))
```