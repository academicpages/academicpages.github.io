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

The most granular and latest available data is from [American Community Survey (ACS) 2014-2019](https://api.census.gov/data/2019/acs/acs5/profile.html). The highest granularity of data released by the Census Bureau is by [Census tracts](https://www.census.gov/programs-surveys/geography/about/glossary.html#par_textimage_13), which are small, typically unchanging geographical regions that contain between 1200 and 8000 people. While individual-level data would have been preferable, data from Census tracts are still [indicative](https://opportunityinsights.org/neighborhoods/) of individual-level outcomes.

### The majority of New Yorkers do not own a car

Across the five boroughs, 55% of households do not own a car and only 22% of people commute to work by driving alone in a car while 66% commute by public transit or walking. The plots below show this data broken down by borough along with the corresponding city-wide statistic.

The large majority share of those commuting by transit or walking is not a statistical artifact -- it is the norm in every borough except Staten Island. This might not surprise anyone who has lived in New York City, but it is useful to see the data.

<p float="left">
  <img src="/images/cars_in_nyc/car-ownership.png" width="49%" />
  <img src="/images/cars_in_nyc/transit-commute.png" width="49%" /> 
</p>

To get a granular view of the data, I visualize car ownership, and other tract-level statistics, on a map of New York City overlayed with subway lines: 

<iframe src="https://car-ownership-nyc.herokuapp.com/nyc_mapping" title="Car ownership in NYC" width="950" height="775" style="border: none;"></iframe>

From the above map, it is evident that the residents of East Bronx, South Brooklyn, Eastern Queens, Most of Staten Island, and Upper East Side
have an **above-average** share of car ownership, compared to the city or their borough. While some of these neighborhoods are transit deserts, others most certainly are not (hello, Upper East Side). This leads to the next question:

What factors explain car ownership?
======
Perhaps unsurprisingly, the percentage of workers driving to work is the single best predictor of car ownership explaining 77% of the variance (R<sup>2</sup>). Do people own a car because they need it for work? Or do they commute by car to work because they own one? It’s likely the former but even in neighborhoods with 60% car ownership, only 32% of workers on average drive to work.

The percentage of workers commuting by walking or public transit is negatively correlated with car ownership and explains the same amount of variance as the percentage of workers driving to work. While this does not prove causation, increased access to public transit in a neighborhood is linked with a reduced need for cars.

No other single variable is as good at predicting car ownership: median household income barely explains any of the variance in car ownership (R<sup>2</sup> = 0.06; positively correlated), average household size is a modest predictor (R<sup>2</sup> = 0.19; positively correlated), and poverty rate is a slightly better predictor (R<sup>2</sup> = 0.23; negatively correlated).

Did the pandemic change everything?
======

First, some historical context using data going back to 2007, the earliest year for which data exists. Between 2007 and 2019, the number of households in the city increased by 6%, and the number of workers living and commuting in the city increased by 9.5%. At the same time, the fraction of households without a car and the share of workers commuting by car both dropped by 1%. 

In New York City, as in the rest of the country, transit use (particularly the subway) [plummeted](https://new.mta.info/agency/new-york-city-transit/subway-bus-ridership-2020) during the pandemic and [more people](https://www.nytimes.com/2020/08/12/style/car-buying-new-york-coronavirus.html) might have bought cars than usual. At the same time, the pandemic also led to a [bike boom](https://www.outsideonline.com/2420131/pandemic-bike-boom-here-stay) with the number of bike trips hitting all-time highs [week after week](https://gothamist.com/news/bike-boom-shows-no-signs-slowing-citi-bike-sets-new-ridership-records). There has also been a move towards [opening up streets](https://www.bloomberg.com/news/articles/2021-04-29/what-s-next-for-the-open-streets-of-the-pandemic) for people and converting some to [parks](https://www.34avelinearpark.com/). With the pandemic now receding (famous last words), subway ridership is [on the rise](https://new.mta.info/coronavirus/ridership) and the number of bike trips shows no sign of slowing, [including on weekdays](https://nyc.streetsblog.org/2021/06/15/cycling-on-east-river-bridges-still-booming-higher-ridership-than-pre-pandemic-levels/).

Does this mean the increase in cars will be transitory? As the quote often attributed to Neils Bohr goes, “predictions are hazardous, especially about the future”. I’m not going to make a prediction but instead will emphasize that the future can be shaped by policy choices.

What does all of this imply?
======

Most New Yorkers do not own a car, much less drive to work. It might be tempting to think of the outer boroughs as all transit deserts, and ergo all its residents as owning and commuting by cars, but the reality is far from it. 

Policies such as building full-time dedicated bus lanes, protected bike lanes, implementing congestion pricing to increase transit frequency would help the vast majority of New York City residents and most certainly the least affluent. The New Yorkers living in Melrose, Borough Park, East Harlem, Flushing, and Stapleton are testament to this.
