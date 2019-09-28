---
date: '2017-03-28'
slug: history-stats-2
title: 'History of statistics 2: Road to the normal'
---

[mathjax]

_This is the second of three entries about the history of statistics, drawn from Stigler's amazing_ History of Statistics.

In the last entry, I talked about the origin of the combination of observations: the idea that, by combining different data points, you could reduce the uncertainty about some parameters fit from those data points. That leap was almost entirely conceptual; Mayer's method was particularly impressive from a technical point of view.

I'm calling this post "The Road to the Normal", because the development of the normal distribution was a critical juncture in the history of statistics. It didn't happen in one place or one time, and that's the fun part of the story!



#### Strain I: Error bounds on the binomial distribution



I previously said that Mayer's technique of combining observations was a conceptual leap, but it was, in a way, obvious to many people. Here's what [Jacob Berounilli](https://en.wikipedia.org/wiki/Jacob_Bernoulli) had to say:



<blockquote>Even the most stupid of men, by some instinct of nature, by himself and without any instruction (which is a remarkable thing), is convinced that the more observations have been made, the less danger there is of wandering from one's goal.</blockquote>



The tricky question was, by how much? Mayer had incorrectly assumed that uncertainty decreased linearly with the number of observations [latex]n[/latex]. (In general, we now know that uncertainty decreases like [latex]\sqrt{n}[/latex].) Jacob Bernoulli wanted to quantify this decrease. Specifically, he wanted to show that there was no lower limit to uncertainty; that with arbitrarily large numbers of experiments you could approach "moral certainty". For the case of the binomial distribution, we call this idea Bernoulli's theorem, or more commonly, the [law of large numbers](https://en.wikipedia.org/wiki/Law_of_large_numbers).

The [binomial distribution](https://en.wikipedia.org/wiki/Binomial_distribution) may seem like an odd choice, but it was an object of intense mathematical study during Bernoulli's time. The idea of flipping coins was very mathematically tractable. It was very easy to do "forward probability" and predict, given the properties of a weighted coin, how likely different outcomes were. As we'll see later, this focus on the binomial distribution (and, as it happens, certain urn models) made inverse probability (i.e., inference) pretty tricky.

Bernoulli's approach was novel: he asked, how many experiments you needed to achieve a certain error bound?



<blockquote>Bernoulli could guarantee that, with a chance exceeding [latex]1{,}000/1{,}001[/latex], [latex]n = 25{,}500[/latex] observations would produce a relative frequency of fertile cases that fell within [latex]1/50[/latex] of a true proportion [latex]30/50[/latex].</blockquote>



Here "fertile" means what we would call "successful", as in coin flips. In our modern binomial distribution terminology, he let [latex]p = 30/50 = 3/5[/latex] be the probability of success and [latex]n = 25{,}500[/latex] be the number of trials. For [latex]k[/latex] to fall within [latex]1/50[/latex] of [latex]30/50[/latex] mean it is between [latex]25{,}500 \times \frac{29}{50} = 14{,}790[/latex] and [latex]25{,}500 \times \frac{31}{50} = 15{,}810[/latex]. If [latex]f(k; n, p)[/latex] is the binomial probability distribution function, then he's asserting that

[
\sum_{14{,}790}^{15{,}810} f(k; 25\,500, 30/50) \geq \frac{1\,000}{1\,001} = 1 - \frac{1}{1\,001} \simeq 1 - 10^{-3}.
]

Bernoulli was despondent that he would need [latex]10^4[/latex] observations to get his 1 in 1,000 error bars down to [latex]1/50[/latex]. This may seem like a big margin, but proto-statisticians were interested in some pretty subtle questions. For example, folks were wondering whether there were more male births than female births. (It turns out that there are approximately 10% more male babies born than female.) To detect this kind of effect, Bernoulli's result suggested that you would need to have data from [latex]10^4[/latex] children. This may also not sound difficult to us know, but data collection was a lot more challenging in his day!

Bernoulli doesn't say it, but it seems pretty clear he considered this work a failure. As Stigler says, part of Bernoulli's failure was his insistence on such a high confidence. Now a lot of science uses 1 to 20 as a reasonable odds (the famous [latex]p = 0.05[/latex]) rather than his very stringent 1 to 1,000 odds. Bernoulli's approximation was also pretty bad. In fact, given 25,500 trials, the chance of measuring a mean within [latex]1/50[/latex] of [latex]30/50[/latex] is more like [latex]1 - 6 \times 10^{-11}[/latex].

Another mathematician, [de Moivre](https://en.wikipedia.org/wiki/Abraham_de_Moivre) followed up on Bernoulli's work. He showed that you could [approximate the binomial](https://en.wikipedia.org/wiki/De_Moivre%E2%80%93Laplace_theorem) distribution with a "binomial curve" which was, in fact, what we now call the normal curve. Using a normal curve with the same mean [latex]mu = np[/latex] and variance [latex]\sigma^2 = n p (1-p)[/latex], we can approximate that

[
\int_{14,790}^{15,810} f(x; n p, \sigma) \,\mathrm{d}x = 1 - 7 \times 10^{-11},
]

where [latex]f[/latex] is the probability density function for the normal curve. I'm pretty sure de Moivre didn't have the analytical tools to be able to make the calculation to that precision, but it goes to show how much he improved on Bernoulli's result. De Moivre even noticed that it was sensible to measure deviations from the mean in terms of what we would call standard deviations (he called it the "modulus").

Strangely, to our eyes, no one really picked up on this work, which may very well have been the first time the normal curve appeared. Stigler's explanation is that de Moivre explained a "forward" probability problem---given some number of trials, how small are the error bars?---rather than the "inverse" or inferential probability problem: say I got some results, then what are the error bars on my estimation of the true value? That conceptual leap is more related to the work of [Bayes](https://en.wikipedia.org/wiki/Thomas_Bayes) and [Simpson](https://en.wikipedia.org/wiki/Thomas_Simpson).



#### Strain II: The method of least squares



Returning to the problem of combination of observations, we'll see another strand of the prelude to the normal distribution. As discussed in the last post, one problem of combining observations was a purely mathematical one: what do you do with [latex]N[/latex] equations with [latex]M < N[/latex] unknowns? Statistically, we might say this as: how do we distribute the error among the unknowns? But mathematically, we're stuck with this problem of overdetermination.

[Legendre](https://en.wikipedia.org/wiki/Adrien-Marie_Legendre) offered a solution, which we now call the method of least squares. It goes like this: rewrite all your equations as: [latex]E = a + bx + cy + \ldots[/latex], where the [latex]a[/latex], [latex]b[/latex], [latex]c[/latex], etc. are the unknown constants to be determined, the [latex]x[/latex], [latex]y[/latex], etc. are the observed values, and [latex]E[/latex] is what we and Legendre would call the error. Then Legendre took the squares [latex]E^2[/latex], summed them up, and took the sum's derivative with respect to [latex]a[/latex], [latex]b[/latex], and so forth. Behold: this system of [latex]N[/latex] equations in [latex]M < N[/latex] unknowns is now reduced to [latex]M[/latex] equations with [latex]M[/latex] unknowns.

This method of least squares had enormous practical utility, and it was swiftly applied to problems in astronomy and geodosy. (What is that, you ask? Well, there was [a debate](https://en.wikipedia.org/wiki/History_of_geodesy#Europe) about whether the Earth was a prolate spheroid---like an egg or football---or an oblate spheroid---a sphere that got squashed at the poles and bulges at the equator. The French thought it was one way; the English thought it was another. There was national pride involved.)



#### Interlude: The problem of the best mean



Legendre noted that, aside from its mathematical elegance, the method of least squares had some other advantages. It seemed to nicely distribute the errors among the different parameters. Larger errors were penalized over smaller ones. And, importantly, if you had only one unknown, then the least-squares estimate for that unknown was equal to the simple arithmetic mean, the sum of the values divided by the number of values.

The arithmetic mean has a long history and a lot of appeal. But where does it come from? Is it a "good" mean? We certainly have [other options](https://en.wikipedia.org/wiki/Geometric_mean). Laplace (who shares his name with de Moivre on that weak law of large numbers theorem) asked, given, say 3 measurements, how do you pick the "best" single value to summarize them? Stigler says:



<blockquote>Laplace described two criteria for choosing this value. One might, he said, choose that value of [latex]x[/latex] such that it is equally probable that the true [latex]x[/latex] falls before it or after it [i.e., above or below it] [...] We call [this value] the posterior median. Alternative, one might choose that [latex]x[/latex] "that _minimizes_ the sum of the errors to be feared multiplied by their probabilities." [...] We now recognize this as a description of the value that minimized the posterior expected loss [...] Laplace then showed in perhaps the most elegant simple proof of early mathematical statistics that these two means were identical!</blockquote>



(If you're interested in the proof, you'll have to get Stigler's book, because it involves a lot of geometry.) Laplace now ran into a problem. To actually _find_ that value [latex]x[/latex], he needed to have (what we now call) an error distribution: given that the "true" value is [latex]x[/latex], what is the probability that you get a different value [latex]x + \epsilon[/latex]?

Laplace had the binomial distribution, which was discrete, and he did not have the normal distribution. So he basically made up an error distribution. He wanted it to be symmetrical about [latex]x[/latex]. (He also wanted it to go to zero at infinity and be normalized; nowadays we consider those necessary properties of a probability distribution.) He didn't like the triangular distribution (maybe becaused it seemed weird to have a sharp cutoff for possible errors). He decided, for reasons that I don't really understand, that it would be reasonable to expect that the error distribution [latex]\phi(x)[/latex] and its derivative [latex]d\phi(x)/dx[/latex] should decrease at the same rate, which leads to the [Laplace distribution](https://en.wikipedia.org/wiki/Laplace_distribution): [latex]\phi(x) \propto e^{-x/b}[/latex].

This distribution turns out to immensely difficult to work with, and Laplace found himself battling a fifteenth-degree polynomial to try to solve his problem!



#### The Gauss-Laplace synthesis



In 1809, Gauss pulled a trick. He said, assuming that the best mean _is_ the arithmetic mean, what is the error distribution that gives rise to that mean? It turns out that this is the normal distribution! And, if you have normally-distributed errors, then least squares is actually the best way to get value estimates. (This story is going to classic Gauss, doing something brilliant and then claiming you did it earlier and with more foreknowledge than you actually had.)

Many people noticed there was a missing piece in this puzzle. Why should you pick the arithmetic mean in the first place? Laplace, who had done the work with the Laplacian in 1774, published the amazing [central limit theorem](https://en.wikipedia.org/wiki/Central_limit_theorem) in 1810. This theorem says that the sum of many independent random variables tends toward---you guessed it!---a normal distribution. Laplace only read Gauss's work after publishing his theorem. Stigler says:



<blockquote>Laplace must have encountered Gauss's work soon after April 1810, and it struck him like a bolt. Of course, Laplace may have said, Gauss's derivation was nonsense [because it assumed the thing about the arithmetic mean being a good mean], but he, Laplace, already had an alternative in hand that was not --- the central limit theorem. Before seeing Gauss's book Laplace had not seen any connection between the limit theorem and linear estimation, but almost immediately afterward he could see how it all fit together. [...] If the errors [i.e., error terms] of Gauss's formulation were themselves aggregates, then the limit theorem implied they should be approximately distributed as what would be called the normal, or Gaussian, curve [latex]\phi(\Delta)[/latex]. [...] And once Gauss's choice of curve was given a rational basis, the entire development of least squares fell into place, just as Gauss had showed.</blockquote>



I'm very impressed that the normal distribution arises from all these strains: least squares, the arithmetic mean, an approximation to the binomial, and, perhaps most importantly, the central limit theorem. It's also interesting to see how hard it was to connect all these ideas to one another, and how high the barrier was for the last step. Laplace had arrived at Laplace's distribution [latex]e^{-|x|}[/latex], but it certainly did not occur to him to square it and get the normal distribution [latex]e^{-x^2}[/latex].

More fundamentally, I'm so used to thinking about distributions as models for real-life processes and querying the distributions for the kinds of values that the processes would produce. It's hard for me to imagine what it was like to _not_ have a clear idea that this kind of thinking was valid and, after that, what kind of machinery you would use to actually produce those values. Having studied Bayesian statistics, the inverse probability problem seems to follow quickly from the forward probability problem, but it's evident that that is also not an obvious transition.