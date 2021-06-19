---
title: 'Who owns a car in New York City?'
date: 2021-06-20
permalink: /posts/2021/06/cars-in-nyc/
tags:
  - New York City
  - Transit
  - Cars
---

With vehicle traffic on New York roads [back to pre-pandemic levels](https://www.nytimes.com/2021/05/29/nyregion/city-traffic-pre-covid.html) and upon seeing unsubstantiated [claims](https://twitter.com/ShanaS_Warren/status/1394095700959453187) swirling about who uses cars, I decided to find data about car ownership in New York City.

The most granular and latest available data is from [American Community Survey (ACS) 2014-2019](https://api.census.gov/data/2019/acs/acs5/profile.html). The highest granularity of data released by the Census Bureau is by [Census tracts](https://www.census.gov/programs-surveys/geography/about/glossary.html#par_textimage_13), which are small, typically unchanging geographical regions that contain between 1200 and 8000 people. While individual-level data would have been preferable, data from Census tracts are still [indicative of individual-level outcomes](https://opportunityinsights.org/neighborhoods/).

The majority of New Yorkers do not own a car
------

Across the five boroughs, 55% of households do not own a car and only 22% of people commute to work by driving alone in a car while 66% commute by public transit or walking. The plots below show this data broken down by borough along with the corresponding city-wide statistic.

The large majority share of those commuting by transit or walking is not a statistical artifact -- it is the norm in every borough except Staten Island. This might not surprise anyone who has lived in New York City, but it is useful to see the data.

To get a granular view of the data, I visualize car ownership, and other tract-level statistics, on a map of New York City overlayed with subway lines: 

<iframe src="https://car-ownership-nyc.herokuapp.com/nyc_mapping" title="Car ownership in NYC" width="950" height="775" style="border: none;"></iframe>

From the above map, it is evident that the residents of East Bronx, South Brooklyn, Eastern Queens, Most of Staten Island, and Upper East Side
have an *above-average share* of car ownership, compared to the city or their borough. While some of these neighborhoods are transit deserts, others most certainly are not (hello, Upper East Side). This leads to the next question:

What factors explain car ownership?
======
Perhaps unsurprisingly, the percentage of workers driving to work is the single best predictor of car ownership explaining 77% of the variance. Do people own a car because they need it for work? Or do they commute by car to work because they own one? It’s likely the former but even in neighborhoods with 60% car ownership, only 32% of workers on average drive to work.

The percentage of workers commuting by walking or public transit is negatively correlated with car ownership and explains the same amount of variance as the percentage of workers driving to work. While this does not prove causation, increased access to public transit in a neighborhood is linked with a reduced need for cars.

No other single variable is as good at predicting car ownership: median household income barely explains any of the variance in car ownership (R^2 = 0.06; positively correlated), average household size is a modest predictor (R^2 = 0.19; positively correlated), and poverty rate is a slightly better predictor (R^2 = 0.23; negatively correlated).

Did the pandemic change everything?
======


What does all of this imply?
======

