---
title: 'Why There Isn't More Evidence That Pesticides Disrupt Your Hormones'
date: 2017-12-08
permalink: /posts/2017/12/pesticides-hormones/
tags:
  - organic food
  - pesticides
  - endocrine disruptors
  - hormones
---

I've really been gotten on the crunchy bandwagon this year -- buying high quality grassfed meats, organic produce, paraben-free beauty products, and swapping out plastic food storage containers for glass ones.
Up until recently, I was skeptical about the evidence that these choices really make a difference for your health.

The main reason I've been so skeptical about these kinds of products is that the scientific evidence that the amount of chemicals present in our day-to-day products directly causes worse health outcomes tends to come from poorly done statistical analyses.
Frankly, I know too much about how these things can go wrong to believe the numbers they report.
They often rely heavily on parametric modeling assumptions that are rarely satisfied.

I looked at two studies of pesticides and fertility recently.
My instinct was to rip them apart.
And yet, I couldn't help believing their qualitative results.
I want to dig into the reasons for this and to provide some thoughts on what kinds of studies and reporting would be done in an ideal world. 

The studies: pesticides and infertility
=======================================
[The first study I read was about semen quality.](https://academic.oup.com/humrep/article/30/6/1342/616110)
155 men at a fertility clinic were given dietary surveys and asked to give semen samples.
They analyzed semen quality in a number of ways and correlated that with the amount of pesticides consumed.
The authors found a nonlinear dose-response effect: more typically-pesticide-heavy foods in diet was associated with lower sperm counts and other infertility outcomes. 
That sounds like a plausible finding to me, however...

### Noisy data

They used a single 24-hour dietary recall to determine what fruits and vegetables each man ate in a day.
They assumed this was representative of their past and future diet.
The authors took several USDA pesticide measures for various fruits and vegetables and aggregated them into a single score for each food item. 
Then they dichotomized the produce into "high pesticide" and "low-to-moderate pesticide" foods.
This is pretty crude.
They checked robustness by moving the threshold be called "high pesticide" up and down, but this still assumes that the underlying pesticide consumption score is valid.

Fruits and vegetables with a total score greater than or equal to 4 (i.e. at least one of three measurements was in the third tertile) were considered to be high pesticide residue foods while fruits and vegetables with a total score <4 were considered low-to-moderate pesticide residue foods. Based on these criteria 14 fruits and vegetables were categorized as high pesticide residue produce, and 21 as low-to-moderate pesticide produce.

Their Supplementary Table 1 lists the produce categories and their scores. The highest scoring are celery, strawberries, bell peppers, and spinach while the lowest include peas, grapefruit, dried prunes, and onions. There's one strange thing in the list that sticks out to me: cooked spinach is a different entry from raw spinach. That's because they mapped "cooked spinach" in peoples' dietary surveys to "frozen spinach" in the pesticide data list. But using frozen spinach isn't the only way to cook it! I imagine there's a lot of noise in the way they map food frequency questionaires to the pesticide data.

### Not externally valid

The second thing that makes me uncomfortable is that they sampled men from a fertility clinic and not from the general population.
The results of this paper cannot be generalized to the public because the study population was at a fertility clinic where, presumably, the men giving samples are already having trouble with their fertility.
The authors don't mention this fact in the abstract.

I'm not even going to comment on the statistical models.
I guess they're less offensive because the authors aren't claiming causality, but I still worry whether the estimates mean anything.
Linear models tend to be "asymptotically consistent," meaning they estimate the right thing if you have infinite amounts of data, but with a sample size of 155 men I'm not so sure we're in the asymptotic regime.

### Another example of these issues

I'm even less inclined to believe the numbers from [this second paper on pesticide intake and pregnancy outcomes.](https://jamanetwork.com/journals/jamainternalmedicine/article-abstract/2659557?https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2659557)
This study has all the same problems as the other: they use the same kind of methods to classify fruits and vegetables as high- or low-pesticide foods, they sample women from fertility clinics, and they use generalized estimating equations to estimate the probability of live births and of clinical pregnancy for all these women undergoing assisted reproductive technologies.
These models assume that the dose-response is linear, and I'm wary of any parametric model that estimates probabilities.

But I believe it anyway.
========================

I think the trends are compelling. While the dietary survey measure is noisy, I'll concede that it probably does give some insight into how many pesticides and endocrine disruptors people are eating. The study populations are people who are undergoing infertility treatments, who presumably have compromised endocrine systems. This suggests that imbalanced hormones are susceptible to becoming even more imbalanced due to endocrine disruptors in food.

The way the results are reported, precise numbers about how humans are affected, is a big part of why these studies are offputting to me. 
[My advisor calls this "quantifauxcation"](https://www.stat.berkeley.edu/~stark/Seminars/fauxIspra15.htm#1): situations in which a number is, in effect, made up, and then is given credence merely because it is quantitative.

I find the results meaningful in a qualitative way, but not in the way that the popular media reports them. Take it at face value: people with fertility troubles seem to be negatively affected by pesticides. The findings say nothing about how an otherwise fecund person would respond. But it suggests a mechanism by which these pesticides are harmful!

Why are these studies so hard?
==============================

There are a myriad of things that make it challenging to pin down the effect of pesticides.
Some of them are due to the nature of the problem and some are just fundamental problems with science in our society.

### There are ethical and logistical challenges to studying health outcomes.

This is a problem for all kinds of health outcomes and diseases.
In a perfect world, you'd have a random sample of the population, you'd randomly assign them a certain diet with measured pesticide levels for a fixed amount of time, and you'd follow them and measure their fertility until they died.
Unfortunately, studies like this are limited to convenience samples of people, who eat whatever diet they want, and you only get to measure them a few times.
Since diet isn't randomly assigned, researchers try to control for confounding factors by using modelling approaches.
Modelling is the best they can do, but there are no guarantees that the results are right.

### Incentives to research endocrine disruptors are low.

Who wants to fund research that says that the status quo is hurting us?
There are powerful industries and lobbies with lots of money that want to keep pesticides in use.
There's no powerful organic food lobby that can compete with "Big Food".
Funding may be limited for this reason.
And when research on the harmful effects of pesticides does get funded, it's never enough money to carry out the kind of study one would like to do (a randomized control trial over a long time horizon).
Limited resources force people to use fewer subjects and lower quality measures of exposure, resulting in lower-quality research.

### The burden of proof is on consumers, not producers.

Here's the fundamental problem:
it's up to consumers to prove that these chemicals are harmful.
It seems relatively easy for companies to introduce new pesticides.
They ned to show that in lab settings, the chemicals pass certain toxicity tests.
However, these tests only tell us about short-term effects in the lab.
They don't say anything about potential long-term effects of eating low doses of pesticides over many years.
These things enter the market, and it becomes the consumers' job to show that they are harmful.
Once products are in use it is difficult to get rid of them.

### Without changing how pesticides are studied, farmers will continue to spray their crops with endocrine disrupting chemicals.

I'd like to see some changes in the way people think about studying the harm of chemical exposures.

* Simply put, do better studies. I realize this kind of effort is difficult and takes a tremendous amount of funding and effort. But the evidence from a small observational study like the ones here is not convincing. I'd like to see more patients, more external validity, and better measures of pesticide exposure. If researchers from different schools could form a consortium and pool their resources, I bet that more compelling findings would come out.
* Take into account prior knowlege when reporting statistical significance. David Colquhoun makes this suggestion in his comment on ["Five ways to fix statistics".](https://www.nature.com/articles/d41586-017-07522-z) If there has been lots of prior work showing that a chemical is harmful, then even if your study does not reach statistical significance at some pre-specified level, you may want to give more credence to a marginally significant result. 
* My suggestion *for observational data* would be to focus on the qualitative results rather than the precise numeric estimates when reporting these studies. I can believe that a positive association is real, but I lose confidence when I hear probabilities being thrown around.

And in a perfect world, regulatory agencies would respond to this kind of evidence and pull products immediately to be examined more rigorously.
It would not be such a battle to prove that these chemicals are dangerous.
Until then, we have to be vigilant and make smart choices for ourselves.
