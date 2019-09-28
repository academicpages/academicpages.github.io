---
date: '2017-04-28'
slug: berksons-paradox-making-psychics-seem-real
title: "Berkson's paradox: Making psychics seem real"
---

Today I discovered this really lovely little thing called [Berkson's
paradox](https://en.wikipedia.org/wiki/Berkson%27s_paradox). It's one of those
paradoxes that isn't actually a paradox, it just seems initially crazy. (It
turns out that there's a
[name](https://en.wikipedia.org/wiki/Paradox#Quine.27s_classification) for that
kind of paradox!)

Say you're flipping a coin. Sometimes it comes up heads, sometimes tails. I
claim to be psychic, and I make predictions about what your coin flip is going
to be. You, being statistically minded, decide to keep track of how well I'm
doing: very many times, you flip a coin, hide the result from me, I guess
whether it's heads or tails, and then you record the true answer and my guess.

To show that I'm not psychic, you could show that the probability that I call
"heads" does not depend on whether you actually flipped heads or tails.
Formally, the probability that I call "heads" is *independent* of whether you
flip heads. Let $H_c$ be the event where the coin falls heads, and
let $H_p$ be the event where the psychic (me) calls heads. Then
your claim is that $P(H_p | H_c) = P(H_p)$, that is, that the
probability that I call "heads" is the same whether the coin is actually heads
or not.

Note that if the first quantity were greater, then I'm more likely to call
heads when the coin lands heads, that is, I'm actually capable of some
divination. (If the second quantity were greater, then I'm actually capable of
divination, I'm just doing it backwards, more often calling "heads" when it's
tail. I would say this means that your negative energy is causing my mental
image of the coin to "flip" from heads to tails and vice versa. I would still
be predicting something!)

Having been confronted with your null result, which showed that my
predictions have no bearing on the real state of the coin, I claim that the
negative energy of the tails was mucking up my predictions, and I ask you to
exclude cases where I correctly guessed tails. In other words, I ask you to
only consider cases where the coin was heads and/or I called heads.
Mathematically, I'm asking you to compare $P(H_p | H_c \text{ and } H_c \cup
H_p)$ against $P(H_p | H_c \cup H_p)$.

If you looked at the numbers from our very large trial, you would find that
the second quantity is larger: it looks like I'm doing (reversed) divination!
Mathematically, this shakes out fairly easily: because $H_c$ implies $H_p \cup
H_c$, the first quantity in this second comparison is just $P(H_p | H_c)$,
which we previously showed was just $P(H_p)$. It's now clear that the second
quantity will be larger: the probability that I call heads *given* that I
called heads and/or you flipped heads is greater than the probability that I
call heads *in general*. So this is a "paradox" only insofar as my request to
exclude the tails-tails causes seemed right to your (incorrect) intuition.

This may sound silly and arcane because I told a story about psychics, but
consider this much more real idea: say you're curious if white people are more
likely to be promoted in your company. You interview white people who got
promoted, non-white people who got promoted, and non-white people who didn't
get promoted. Then you look for an association between being white and getting
promoted.

Now imagine that race had no effect on getting promoted. (Clearly, this is
still an unreal example, but wait for the punchline.) Then let non-whiteness be
like the psychic's calling "heads" and being promoted be like the coin actually
falling heads. You interviewed only people who got promoted and/or are
non-white, which is like including the tails-tails cases. Thus, Berkson's
paradox shows that you will measure a negative relationship between being
non-white and being promoted. In other words, by excluding white people who
didn't get promoted, you will falsely conclude that being white does make you
more likely to be promoted. Weird, right?

Here's another example: you have two friends who rank movies on a 1 to 10
scale. You only want to watch the best movies, so you decide to consider only
those movies where the sum of their two scores is 14. If their recommendations
were independent, then they might comment on 100 movies and create a perfect
grid: one movie where *A* voted 1 and *B* voted 1, another movie
where *A* voted 1 and *B* voted 2, and so on. Selecting only those movies with
a combined score of at least 14 selects for the upper-right quadrant, among
which their scores are negatively correlated: you get the erroneous sense
that *A* and *B* have non-overlapping tastes, when if fact they are completely
independent.

```{r berksons-movies, echo=FALSE}
library(dplyr)
library(ggplot2)
library(tidyr)

crossing(x=1:10, y=1:10) %>%
  mutate(good = x+y >= 14) %>%
  (function (df) {
    ggplot(df, aes(x, y, color=good, group=good)) +
    geom_smooth(data=filter(df, good), method='lm', se=F, color='black') +
    geom_point() +
    scale_x_continuous(breaks=c(1, 5, 10)) +
    scale_y_continuous(breaks=c(1, 5, 10)) +
    xlab("A's rating") + ylab("B's rating") +
    guides(color=guide_legend(title='Movie is good?')) +
    theme_classic()
  })
```
