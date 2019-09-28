---
date: '2017-08-23'
slug: simpsons-paradox
title: Simpson's paradox
---

Imagine I told you that the acceptance rate for women at a prestigious university was lower than for men. Sounds simple. Now imagine that, restricting our attention to each individual department in the university, the acceptance rate for women is higher than for men. How can this be? The answer, in this case, is that women apply to departments that have lower acceptance rates.

This is an example of Simpson's paradox: the trend within each group (e.g., women having higher acceptance rates within each department) is the opposite of the trend overall (e.g., women having lower acceptance rates overall). There's a nice visual explanation for this phenomenon. Imagine you're interested in the relationship between the *y* and *x* variables. Within the two colored groups, increasing *x* goes with increasing *y*, but across all data points, the trend is reversed.

```{r, echo=FALSE}
library(dplyr)
library(ggplot2)

data_frame(x=1:10, y=c(6:10, 1:5), group=c(rep('A', 5), rep('B', 5))) %>%
  ggplot(aes(x, y, color=group)) +
  geom_smooth(aes(color=NULL), method='lm', se=F, color='gray', fullrange=T) +
  geom_smooth(method='lm', se=F) +
  geom_point(shape=1, size=5) +
  guides(color=F) +
  theme_classic() +
  xlim(0, 12)
```

[Wikipedia](https://en.wikipedia.org/wiki/Simpson%27s_paradox) has a pretty good explanation (I lifted these examples from there). The usual conclusion I've gotten from hearing about Simpson's paradox is that you need to know the important, extra division in the data to come to the right answer. For example, you need to know to separate the application data by department to see that the data aren't showing a gender bias in admissions.

Simpson's [original paper](http://www.jstor.org/stable/2984065) also has a great example that shows how the opposite can be true, when it's not clear whether you should use the aggregated or unaggregated data to come to your conclusion. He suggests that we imagine that there is some investigator who "wished to examine whether in a pack of cards the proportion of court cards (King, Queen, Knave) was associated with colour". Imagine you didn't know what was in a deck of cards: do you expect more royals among the black cards than among the red?

He suggests that we further imagine that "the pack which he examined was one with which Baby had been playing, and some of the cards were dirty." (Who this capital-B Baby is is not described.) The investigator, being pretty ignorant about cards, records the royal-ness (i.e., face card or not), color, and dirtiness of each card.

The investigator finds these results:

<table>
<tr>
<th></th>
<th colspan="2">Dirty</th>
<th colspan="2">Clean</th>
</tr>
<tr>
<th></th>
<th>Royal</th>
<th>Plain</th>
<th>Royal</th>
<th>Plain</th>
<tr>
<td><emph>Red</emph></td>
<td>4</td><td>8</td><td>2</td><td>12</td>
</tr>
<tr>
<td><emph>Black</emph></td>
<td>3</td><td>5</td><td>3</td><td>15</td>
</tr>
</table>

Interestingly, black cards are more likely to be royal among the dirty cards ($3/5 = 60\%$ for black vs. $4/8 = 50\%$ for red) and among the clean cards ($3/15 = 20\%$ vs. $2/12 = 17\%$). However, if you collapse the dirty and clean cards, you find that there are 6 royal cards and 20 plain cards for both black and red. This "provides what we would call the sensible answer, namely, that there is no such association".

Simpson then suggests that we change the labels to imagine that the investigator had actually done a medical experiment:

<table>
<tr>
<th></th>
<th colspan="2">Male</th>
<th colspan="2">Female</th>
</tr>
<tr>
<th></th>
<th>Control</th>
<th>Treatment</th>
<th>Control</th>
<th>Treatment</th>
<tr>
<td><emph>Recovered</emph></td>
<td>4</td><td>8</td><td>2</td><td>12</td>
</tr>
<tr>
<td><emph>Did not recover</emph></td>
<td>3</td><td>5</td><td>3</td><td>15</td>
</tr>
</table>

Now it's less clear what the "sensible" answer is. Men who got the treatment were more likely to recover than men who did not, and women who got the treatment than women who did not, but, overall, the _people_ who got the treatment were just as likely to recover as those who did not.

Simpson concludes that "[t]he treatment can hardly be rejected as valueless to the race when it is beneficial when applied to males and to females." In other words, we find it reasonable to expect that men might have a different recovery rate from women when untreated, and men might have a different recovery rate from women when treated, and that the relationship between those rates within each sex could be different.

The tricky question is to figure out when this kind of division is sensible. It was sensible to divide up participants in medical experiment by sex, but it wasn't sensible to divide up a census of playing cards by their smudginess.
