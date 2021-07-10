---
title: "Deal or No Deal: decision-making under uncertainty"
date: 2021-07-10
permalink: /posts/2021/7/deal-or-no-deal-decision-making-under-uncertainty/
tags:
---

Imagine you are in one of these situations:

- You are going to pass $N$ gas stations on your way to return a rental car,
  and you want to minimize theprice you will pay for gas before returning the
car. (But you must fill up the car before returning it!)
- You are at a speed dating event, where you will meet $N$ people, and you'd
  like to "lock in" your preferred match by proposing to immediately leave the
  event with that person after you meet them. (This assumes that you much rather
  go on any date, even with the last person you meet, than to leave alone.)
- You need to buy a gift for someone, and you have limited time to shop. You
  know you’ll get to see about $N$ options before you have to pick one and go
  home.

How do you figure out which option to pick? If you're like me, your instinct is
to look at some fraction of options --maybe a quarter, or a half-- and then
pick the best one after that first exploration.

While this is a reasonable *type* of strategy, it's usually the wrong one. In fact,
you usually need to look at many fewer options before you have enough information
to make a good choice.

To see why, let's look at the game show _Deal or No Deal_. The show's format is
a bit convoluted. There are a number of briefcases, each with a certain amount
of money inside. The contestant picks a case at the beginning of the show and
holds it, unopened. They then open other cases, getting successive offers for a
prize. They must take an offer, or pass on it forever. If they reject all
offers, they go home with the amount of money that was in the original case
they picked.

Here's a slightly simplifed version of the game: there are $N$ cases, each with
some reward. The contestant opens each case, one at a time, and can either go
home with that case or reject it forever. If they reject all cases, they must
take home the reward from the last case. You might recognize this game as
analogous to the situations I posed at the start!

What is the optimal strategy for this game? It seems pretty clear we should
open some number of cases to get a sense of what the range of rewards looks
like and then choose a case that looks good. There is a tension between explore
and exploit: if you explore with too few cases, you'll take a sub-par case
because you don't know better, but if you explore with too many cases, you're
end up rejecting a case you should have taken.

If we clarify the problem a little more, we can work out the optimal
explore/exploit balance mathematically. Say there are $N$ cases, and you will
open $M<N$, then take the first case larger than all the $M$ you initially
explored. (If you reach the last case, you must take it.) What is the optimal
$M$?

It turns out, the optimal $M$ is much smaller than I expected. It's tempting to
think we should use some constant fraction, maybe a quarter or a half of all
cases, for exploration. In fact, the optimal $M$ is $\sqrt{N}-1$. For 3 to 6
cases, you should only open 1 before picking the best one you've seen. For 7 to
11 cases, you should open 2. For 12 to 20 cases, you should open 3. For 100
cases, you should open only 9.

Can you imagine hearing that you have 20 options, and saying to yourself, "When
I've seen 3, that will be enough to have a fair sense of the distribution of
rewards"? I certainly couldn't, but that is in fact the right thing to say to
yourself!

And the result of this strategy is surprisingly good: the expected value for
the rank of the result is $N - \sqrt{N}$. So if you have 100 cases, you can
expect to get a case in the 90th percentile or better. (The distribution of
results is actually right-skewed, so you can generally expect a result better
than the expected value.)

Now, there are two big caveats. The first is that this game might not actually
be the one you're playing. In the game described here, it is always better to
take *some* case than to take no case. In real life, we usually have some
alternative that might be better than a middling case. If, say, you were
looking for a business venture to invest in, then you always have the
alternative of just holding on to your money, or putting it in another
investment, rather than being forced to take one of the $N$ ventures offered to
you.

The second caveat is that this strategy gets better with larger $N$, that is,
with more cases. Stated another way, when $N$ is low, the difference between
choices of $M$ is smaller. For example, for $N=20$, the optimal $M$ is 3,
giving an expected value of 16.8 (i.e., you might expect one of the 3 best
cases), and choosing instead $M=10$ only lowers the expected value to 14.8
(i.e., you will still likely get one of the top 5 cases). That being said, if
the game described is an accurate characterization of your situation, it is
still irrational to explore with the number of cases that might seem more
natural.
