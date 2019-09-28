---
date: '2017-06-12'
slug: credit-card-math
title: 'Credit card math: Chase Sapphire Reserve or Citi Double Cash?'
---

[mathjax]

I was talking with a friend about how to choose between credit cards, and I realized that the math is sufficiently complicated that it would be nice to write about it here.

I assume that you are a person with good credit who pays your entire credit card bill every month. For people in this category, credit cards are a scheme for just making money, but you need to be smart about it.

Some cards come with a joining bonus. The Chase Sapphire Reserve made a splash for having something like 50,000 bonus points if you spend a certain amount within a certain period. (In general, a "point" is worth $0.01 in cash, travel, or whatever.) This means using the card can get you $500 in free money. After you get the bonus, should you keep the card? In other words, ignoring the bonus, is the card worth it?

This comes down to a few factors:




  * How many points do you collect? I call this the _collection multiplier_. For example, the Reserve gets 3 points per $1 spent on travel and dining and 1 point for every other $1 spent, so the multiplier is 3 for one part of your spending and 1 for the rest.


  * How much cash do you get for your points? I call this the _redemption multiplier_. For example, the reserve says you can get "up to" 50% extra redemption on travel. As I mentioned above, the base rate if $0.01 per point, so the 50% extra redemption means $0.015 per point.


  * What's the annual fee? For the Chase Reverse, this is about $400, but they give you a $300 bonus if you spend money on travel, so I'll say it's $100.



The number of points \(P\) that you get depends on the total \(T\) amount you spend in a year, the collection multiplier \(c_i\) that you get for purchases in category \(i\), and the fraction \(f_i\) of your total \(T\) that you spend in each category. For example, for the Chase Reserve, you get \(c = 3\) for the fraction \(f\) that you spend on travel and restaurants and \(c = 1\) for the remaining \(1 - f\), so \(P = T \left[ 3f + (1 - f)\right] = T (1 + 2f)\). More generally, you would write \(P = T \sum_i c_i f_i\).

The amount of cash \(C\) that you get depends on the number of points \(P\) and the redemption multipliers. Most of the cards I look at give you a base rate redemption of $0.01 per point and some higher rate for redemption on travel. I'll assume that I spend enough of my budget on travel that I can redeem all the rewards at the higher rate. For example, with the Chase Reserve, you get a number of points that's somewhere between 1% and 3% of \(T\). Because I spend more than 3% of my budget on travel, I can redeem all those points at the higher rate. So in general you would need to write the cash reward \(C\) as some weighted sum of the redemption categories, but I'll just assume you get everything redeemed at the highest rate \(r\) so that \(C = rP\). For the Chase Reserve, \(r = 0.015\).

As an aside, I'll note that the Reserve lets you transfer your points to airline miles rather than cash. Comparing cash and miles requires assigning a cash value to miles. For me, miles feel almost worthless: I've only been able to buy a flight with miles every few years. In general, the [value of miles](http://onemileatatime.boardingarea.com/value-miles-points/) seems to be less than $0.02 per mile. So you might argue that the Chase Reverse redemption multiplier is closer to \(r = 2 \times 0.015 = 0.03\).

Putting this all together, the total cash that you get from a card is \(C\) minus the annual fee \(F\). For the Chase Reserve, this could be as high as \(rP - F = r (1 + 2f) T - 100\). If you don't spend any money of the card, then \(T = 0\), and you just end up paying the annual fee \(-100\). If you spend a lot of money, then \(T\) is so large that the points overwhelm the fee.

The break-even point, when \(rP - F = 0\), depends on \(r\), \(f\) and \(T\). Let's say you spend a generous quarter of your money on travel and restaurants (i.e., \(f = 0.25\)). Assuming the very generous \(r = 0.03\), then the break-even point is $2,222. (If you spend more than this, the card is better than no card at all.) Conservatively, if you get take cash rewards and don't redeem on travel, then \(r = 0.01\), and the break-even point if $6,667. This is a pretty manageable number for a graduate student/postdoc making smaller-than-median salary.

However, it's unfair to compare one card to no card at all. The real question is whether this card is better than a different, competing card. I'll compare the Chase Reserve against the Citi Double Cash. The way they advertise the Double Cash is confusing, but essentially you get 1 point per dollar (\(c = 1\)) and $0.02 per point (\(r = 0.02\)) with no annual fee (\(F = 0\)), so the total cash you get is \(0.02 T\).

How does this compare to the Chase Reserve? For small \(T\), the Chase Reserve costs money (the annual fee), and the Double Cash costs nothing. For large \(T\), the Reserve's annual fee is negligible and the Reserve's higher collection/redemption multiplier beats the Double Cash. Where is that break-point \(T\)? Let's keep \(f = 0.25\). For the generous \(r = 0.03\), then the break-even point is the reasonable $4,000. For a more conservative \(r = 0.015\), then the break-even point is $40,000, which is only a little lower than the NIH postdoc salary.

The break-point is more sensitive to the redemption rate \(r\) than the fraction \(f\) you spend on travel/restaurants. For the generous \(r = 0.03\) and a conservative \(f = 0.05\), the break-even point is $7,700. So whereas halving \(r\) from \(0.03\) to \(0.015\) increased the break-point by a factor of 10, dividing \(f\) by 5 (from 25% to 5%) only doubled the break-point.

What's the bottom line? If you get good value out of your airline miles, then the Chase Reserve is a good deal. If you redeem travel through the card, then you're doing better than having no card at all, but you'll need to spend a lot of money to do better than the Double Cash. If you just use the card to get cash rewards, then the Double Cash is better.