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

  This past year I developed a college basketball model that performed pretty well. [Ken Pom](https://www.kenpom.com) a basketball forecasting expert, has a model with an average error of roughly 8.2 points, and in fact says that "I don’t think you can come up with a prediction method that will have an error of less than eight points." My model was able to come close to his limit at 8.49 for the second half of the season. This is more accurate than ESPN's model, BPI, which I set as a goal to beat. Ultimately, I don't want to share too much about my college basketball model, because, my hope is that it becomes good enough for me to gain exposure in the sports analytics field. However, I believe it's strengths lie in its opponent adjustments (roughly strength of schedule) which, from my back-testing, out perform Ken Pom's AdjEM. Through this, I believe with some architecture improvemets, I can close in on Ken Pom's number.   
  Now taking a look at college football, it's a completeley different beast, and one that is much more difficult to predict than college basketball. The reason for this, is the increased randomness for the decreased sample size and data you have for college football. There are four main features that make college football much more difficult to predict. The first is rather obvious, there are simply less games, almost three times left, so there just isn't as much data. Secondly, I find college basketball to be a much more data rich environment, for example the [four factors](https://www.kenpom.com/blog/four-factors/) can explain a lot of the variability in college basketball scores, college football lacks as succesful a proxy. Third, what I like to call the superstar effect. Having 5 players versus 11 players is a substansial difference in the amount of impact an individual player can have. Finally, and the most influential, is the lack of possesions, and the inconsistency of those possesions within college football. College basketball has about 70 possessions a game, and there are pretty good metrics for measuring the pace at which a game will play at. College football on the other hand has about 13 possesions per game. This means that a team going from scoring on 40% of possesions to 45% of posessions, can be much more significant in deciding the outcome of the game in football compared to basketabll. That small of a percent change, can often be described as just the random noise that comes with trying to forecast sporting events.  
  That all being said, here are my models predictions for this season. I will say, my model has some substansial differences compared to a lot of college football experts, however I'm excited to see how it does.
|SEC              ||    |
|-----------------|------|----------|
|EAST             |Record|Conference|  
|Tennessee        |11-1  |7-1       |
|Georgia          |11-1  |7-1       |
|South Carolina   |8-4   |5-3       |
|Kentucky         |6-6   |3-5       |
|Florida          |4-8   |2-6       |
|Missouri           |4-8   |1-7       |
|Vanderbilt       |3-9   |0-8       |
|WEST             |      |          |
|Alabama          |11-1  |7-1       |
|LSU              |10-2  |6-2       |
|Mississippi      |9-3   |6-2       |
|Texas  A&M       |8-4   |4-4       |
|Auburn           |6-6   |3-5       |
|Arkansas         |6-6   |3-5       |
|Mississippi State|5-7   |2-6       |

|Big 10      |||
|------------|------|------|
|EAST        |Record      |Conference      |
|Ohio State  |12-0  |9-0   |
|Penn State  |10-2  |7-2   |
|Michigan    |10-2  |7-2   |
|Maryland    |8-4   |5-4   |
|Michigan State |6-6   |4-5   |
|Indiana     |6-6   |3-6   |
|Rutgers     |3-9   |1-8   |
|WEST        |      |      |
|Illinois    |9-3   |6-3   |
|Wisconsin   |8-4   |6-3   |
|Purdue      |8-4   |5-4   |
|Iowa        |7-5   |4-5   |
|Minnesota   |5-7   |3-6   |
|Northwestern|3-9   |1-8   |
|Nebraska    |3-9   |1-8   |

|PAC-12         ||    |
|---------------|------|----------|
|               |Record|Conference|
|USC            |11-1  |8-1       |
|Utah           |11-1  |8-1       |
|Oregon State   |10-2  |7-2       |
|Washington     |8-4   |5-4       |
|Oregon         |8-4   |5-4       |
|Washington State|8-4   |5-4       |
|UCLA           |7-5   |5-4       |
|California     |8-4   |5-4       |
|Arizona State  |4-8   |2-7       |
|Colorado       |4-8   |2-7       |
|Stanford       |3-9   |1-8       |
|Arizona        |3-9   |1-8       |

|Big 12         ||    |
|---------------|------|----------|
|               |Record|Conference|
|K State        |10-2  |7-2       |
|Texas          |9-3   |7-2       |
|Oklahoma       |9-3   |6-3       |
|Oklahoma St   |9-3   |6-3       |
|TCU            |8-4   |5-4       |
|BYU            |8-4   |5-4       |
|Texas Tech     |7-5   |5-4       |
|UCF            |8-4   |5-4       |
|Baylor         |6-6   |4-5       |
|Kansas         |6-6   |4-5       |
|Iowa State     |6-6   |4-5       |
|West Virginia  |3-9   |2-7       |
|Cincinatti     |4-8   |2-7       |
|Houston        |4-8   |1-8       |

|ACC            ||    |
|---------------|------|----------|
|               |Record|Conference|
|Florida St     |10-2  |7-1       |
|North Carolina |10-2  |6-2       |
|Clemson        |9-3   |6-2       |
|Pitt           |9-3   |6-2       |
|NC State       |9-3   |5-3       |
|Miami          |8-4   |5-3       |
|Louisville     |7-5   |5-3       |
|Wake Forest    |6-6   |4-4       |
|Duke           |6-6   |3-5       |
|Syracuse       |7-5   |4-4       |
|Boston College |5-7   |2-6       |
|Georgia Tech   |4-8   |2-6       |
|Virginia Tech  |4-8   |1-7       |
|Virginia       |2-10  |0-8       |

Ultimately this lead to my model predicting the conference championship games as follows. 

|Conference|Winner    |Loser   |
|----------|----------|--------|
|SEC       |Tennesee  |Alabama |
|BIG 10    |Ohio State|Illinois|
|Pac 12    |Utah      |USC     |
|Big 12    |Texas     |K State |
|ACC       |FSU       |UNC     |

I believe this would result in a college football playoff of Ohio State, Tennesee, Utah, and Georgia, in that order. Overall, this model was just for fun, and I have nowhere near the amount of confidence in this model as I do in my college basketball model, but it was fun to play around with (and cook the books for Cal, if you didn't notice :)). 
