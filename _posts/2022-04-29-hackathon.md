---
title: 'Climate Data Challenge Hackathon'
date: 2022-04-29
permalink: /posts/2022/04/hackathon/
tags:
  - hackathon
---

Providing Historical Context To An Event In Real Time (AON)
======

There were four seperate problems presented at the climate data challenge hackthon. The problem I choose to work on was presented by AON - Providing Historical Context To An Event In Real Time. Based on my previous experience of real time computations this problem piqued my interest and did not disappoint. We were grouped into teams and I got the chance to work alongside some extremely talented individuals: Linda Speight (Oxford), Faye Wyatt (Met Office), Timothy Lam (University of Exeter) and Jakob Deutloff (University of Exeter).

Challenge Outline
======

There is a need within the insurance industry to garner an understanding of the severity of an upcoming event in real time. This severity estimate can then be utilised to estimate a predicted loss. 

Storm Ciara which impacted the UK on Feb 9th 2020 was chosen as a test case example. The Met Office's MOGREPs ensemble forecast for this event served as the input data leading up to the event. 12 ensemble members with a 54 hour lead time formed the forecast. In order to associate the forecasted rainfall with historical return periods, a maximum of the summed precipitation amount over 24 hour periods was obtained for each grid cell. The return periods for each cell was then predicted by referencing this maximum precipitation against the precipitation thresholds for 5,10,25,50 and 100 year return periods. The return period thresholds were sourced from the ERA5 reanalaysis dataset.  

Outputs
======

A dynamic coding notebook which on-the-fly calculated all the above operations was produced. The operations are as follows:

1. Read in the seperate ensemble forecast
2. For each grid point find the maximum summed precipitation amount over 24 hour periods for the 54 hour lead time forecast
3. Loop through each grid point and assign the correct return period for that cell. The precipitation amount is compared to the 5,10,25,50 and 100 year return period precipitation thresholds.
4. Plot the resulting return period for each cell. 

The different ensemble members can then be interrogated by simply moving a slider. The dynamic coding notebook relies upon the performance of Julia and in particular the dynamic nature of Pluto notebooks. The source code can be accessed [here](https://github.com/JakobDeutloff/ReturnPeriods/tree/main/visualisation).
