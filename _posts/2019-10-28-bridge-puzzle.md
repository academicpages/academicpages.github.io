---
title: "A 'bridge' math puzzle"
date: 2019-10-28
permalink: /posts/2019/10/bridge
---

I saw this puzzle in MIT's [Puzzle
Corner](https://alum.mit.edu/slice/reflections-puzzle-guy) and thought it fun.

For background, bridge is a card game played by 4 players. Players who sit
opposite one another are in a partnership, so there a 2 players in 2
partnerships.

**Problem**: 16 players, 8 men and 8 women, randomly take seats at 4 bridge
tables. Is it more likely that all the partnerships will be same-sex, or that
all partnerships will be opposite sex?

**Analysis**: There are 8 distinguishable red balls and 8 distinguishable blue
balls, placed at randomly into 8 distinguishable slot-pairs, with each slot-pair
having 2 distinguishable slots.

**Solution**: I worked this out with dynamic programming first, because I think
that's easier, and then looked at the combinatorics, to make it more beautiful.

For different-color pairings, I note that, when filling the first slot, you can
pick any of the 8 red balls, and any of the 8 blue balls, and you can put them
in red-blue or blue-red. Then, when looking at the next slot, you have $7
\times 7 \time 2$ choices. In a dynamic programming sense, let $D(r, b)$ be the
number of ways to place $r$ red and $b$ blue balls in different-color pairings:
$$
D(r, b) = \begin{cases}
2rb \times D(r-1, b-1) &\text{ if $r>0$ and $r>0$} \\
1 &\text{ if $r=b=0$}
\end{cases}
$$
It's pretty clear that $D(8,8) = (8!)^2 \times 2^8$.

From a combinatorics point of view, we can say that there are $8!$ ways to put
the red balls in the "left" slots, and $8!$ ways to put the blue balls in the
"right" slots, and then there are $2^8$ ways to permute the balls inside each
pair. This gives the same result.

For same-color pairings, I note that, when filling the first slot, you can
pick either red or blue. You have 8 choices for the first ball, and then 7 choices
for filling the other slot:
$$
S(r, b) = \begin{cases}
r(r-1) S(r-2, b) + b(b-1) S(r, b-2) &\text{ if $r>0$ and $b>0$} \\
r(r-1) S(r-2, 0) &\text{ if $r>0$ and $b=0$} \\
b(b-1) S(0, b-2) &\text{ if $r=0$ and $b>0$} \\
1 &\text{ if $r=0$ and $b=0$} \\
\end{cases}
$$
It wasn't obvious to me what this comes out to!

From a combinatorics point of view, there are $\binom{8}{4}$ ways of choosing
which slot-pairs are red, then $8!$ ways of arranging the red balls among those
red slot-pairs, and then another $8!$ for arranging the blues, giving
$\binom{8}{4} \times (8!)^2 = (8!)^3 / (4!)^2$. If you run the dynamic programming
code, it comes to the same value.

Thus, the opposite-color pairings outnumber the same-color pairings by a factor of
$2^8 \times (4!)^2 / 8! \approx 3.7$.

**Discussion**: Opposite-color arrangements only slightly outnumber same-color
arrangements. This is pretty subtle!
