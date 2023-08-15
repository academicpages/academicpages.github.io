---
title: 'Predicting College Football vs College Basketball'
date: 8/16/2023
permalink: /posts/2023/08/college-football/
tags:
  - forecasting
  - modelling
  - college football
  - Phil Steele
---

  This past year I developed a college basketball model that performed pretty well. [Ken Pom](kenpom.com) a basketball forecasting expert, has a model with an average error of roughly 8.2 points, and in fact says that "I don’t think you can come up with a prediction method that will have an error of less than eight points." My model was able to come close to his limit at 8.49 for the second half of the season. This is more accurate than ESPN's model, BPI, which I set as a goal to beat. Ultimately, I don't want to share too much about my college basketball model, because, my hope is that it becomes good enough for me to gain exposure in the sports analytics field. However, I believe it's strengths lie in its opponent adjustments (roughly strength of schedule) which, from my back-testing, out perform Ken Pom's AdjEM. Through this, I believe with some architecture improvemets, I can close in on Ken Pom's number.   
  Now taking a look at college football, it's a completeley different beast, and one that is much more difficult to predict than college basketball. The reason for this, is the increased randomness for the decreased sample size and data you have for college football. There are four main features that make college football much more difficult to predict. The first is rather obvious, there are simply less games, almost three times left, so there just isn't as much data. Secondly, I find college basketball to be a much more data rich environment, for example the [four factors](https://kenpom.com/blog/four-factors/) can explain a lot of the variability in college basketball scores, college football lacks as succesful a proxy. Third, what I like to call the superstar effect. Having 5 players versus 11 players is a substansial difference in the amount of impact an individual player can have. Finally, and the most influential, is the lack of possesions, and the inconsistency of those possesions within college football. College basketball has about 70 possessions a game, and there are pretty good metrics for measuring the pace at which a game will play at. College football on the other hand has about 13 possesions per game. This means that a team going from scoring on 40% of possesions to 45% of posessions, can be much more significant in deciding the outcome of the game in football compared to basketabll. That small of a percent change, can often be described as just the random noise that comes with trying to forecast sporting events. 
  That all being said, here are my models predictions for this season. I will say, my model has some substansial differences compared to a lot of college football experts, however I'm excited to see how it does. 

