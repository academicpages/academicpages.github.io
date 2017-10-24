---
title: 'Why do people lose interest in academic careers during grad school?'
date: 2017-10-24
permalink: /posts/2017/10/academic-careers/
tags:
  - industry
  - academia
  - statistics
  - survey
---

Fewer grad students are on the job market for faculty positions -- is it because they realize that there are fewer jobs or because they are genuinely more interested in other career paths? [Roach and Sauermann studied interest in academic careers](https://doi.org/10.1371/journal.pone.0184130) in a way that has never been done before: longitudinal surveys of current graduate students. By giving people the survey twice, once in their first or second year of the PhD and then again three years later, they are able to measure **changes** in interest. Previously, people have only looked at cross-sectional data and compared two groups at different points in their PhD.

This is a super important topic of study. We need to know if there's a particular reason students are losing interest in academic careers, and whether that reason differentially impacts under-represented groups. If so, then the academic culture has to change in order to be more inclusive.

My academic sphere is a bit unconventional. I spend a lot of time around people who loosely identify as "data scientists," people who are experts in one domain but approach problems using data and computation instead of relying on theory. There's been much discussion about finding appropriate academic positions for people like us. A big problem is getting credit for our nontraditional work: how do we get recognition for things outside the scope of the usual publication process, like writing software or making our papers open and reproducible? I've talked to ecologists, linguists, sociologists, and many others who feel push back from the more established professors in their field. I myself feel the push to "do more theory" and less data work.

I think the dataset is compelling and the findings are interesting. I have some criticism of the statistical analyses below, but I don't think they're so egregious as to nullify the paper. If anything, I'd disregard the analyses and believe the summary statistics they report. If groups appear different, they probably are.

Findings
========

The survey asked students about their interest in an academic career, and specifically asked them *not* to worry about the supply of academic jobs in their field.
80% of respondents said they were interested in a faculty career in the first survey, while only 55% said they were interested in both the first and second surveys: a large fraction of the sample changed their preferences over the three years between surveys.

Among those who "remained interested" and "lost interest", their attitudes about an academic career were largely the same in the first survey but varied markedly in the second. For instance, among those who lost interest in an academic career, 87% said they were interested in the basic research in their field in the first survey, but three years later only 53% were interested. Those who remained interested in an academic career significantly increased their self-perceived ability to do research, while those who lost interest stayed the same.

The benefit of doing a survey about job preferences, as opposed to looking at actual job placement, is that you don't need to worry about the market constraints. There are only a finite number of faculty positions available each year. Using peoples' actual job placement as the outcome would make it impossible to distinguish whether demand for faculty positions was actually higher than supply or whether it was just right.

The longitudinal nature of the study is unique. I imagine that most studies survey two groups of students, students in their first year and students in their fourth year of the PhD, and compare those two indepenent groups. The problem is that if the two groups differ in their average opinion, you cannot tell whether the difference is due to the older group's experience in the PhD or whether it's due to something else. Instead, this study looks at each student's **change** in opinion. This approach gives more power to detect differences and is just more interesting.

![Alt text]
(http://journals.plos.org/plosone/article/figure/image?id=10.1371/journal.pone.0184130.g002)


Potential problems
==================

**Nonresponse bias:** The authors sent the survey to 30,000 first- and second-year doctoral students. They ended up with 854 people who responded to the first and second survey. They lost people at the following points:
- 30% of people who received the first survey responded
- Of those people, only 80% provided a permanent email address to follow up with
- Among the people who received the second survey, only 40% responded

They noted that conditional on having done the first survey, people were more likely to respond to the second survey if they were US citizens and were second year students at the time of the first survey. They say "controlling for these factors, we do not find significant differences with respect to career interests". What does that mean?

They entirely disregard nonresponse to the first survey. I could imagine that this would bias results. For instance, who is on top of responding to emails?

**Arbitrary categories for the response variable:** Defining categories is somewhat artificial. The survey instrument has five categories ranging from 1 (very disinterested or dissatisfied) to 5 (very interested or satisfied), with 3 denoting no preference. The authors dichotomized the survey responses to interested (4 or 5) or not interested (1 through 3). Would the results have changed if they changed the way they dichotomized, or if they had dealt with the survey scale directly?

**Nonparametric analyses?** They run a bunch of t tests in the section called "Nonparametric Analyses". The t test is very much a parametric test. The assumptions aren't quite satisfied, but the comparison of means is interesting and illustrative. 

**Complex regression models:** They did a complicated parametric, multi-category regression to assess the joint effect of various factors on career preference. The structure of the model is odd: it posits that the variables are linearly related to the 5-point Likert scale response and it puts the responses measured as percents on the same scale as the 5-point Likert scale questions. I have no doubt that these models are measuring correlations in the data, but I don't trust inferences about the magnitudes of coefficients.

Take-aways
==========

In my mind, the missing piece in this paper is the breakdown by gender/race/university. I'd like to know how different groups change their attitudes over the course of their PhD.  

The results seem straightforward otherwise: those who lose interest in an academic career realize they don't enjoy research as much as those who remain interested.

In my field, that realization seems to stem from the fact that there's a disconnect between the kind of research that we want to do and the kind of research that is rewarded and recognized.