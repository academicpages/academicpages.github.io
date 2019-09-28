---
date: '2017-03-19'
slug: history-stats-1
title: 'History of statistics 1: The combination of observations'
---

_I intend this to be the first in a series of three posts about the history of statistics._

I'm reading Stigler's [_History of Statistics_](https://www.amazon.com/History-Statistics-Measurement-Uncertainty-before/dp/067440341X), which is fascinating and incredibly well-written, especially in light of its being the book title that I probably would have selected as the most boring in existence for most of my life. (Stigler is perhaps most widely known for his eponymous [law of eponymy](https://en.wikipedia.org/wiki/Stigler%27s_law_of_eponymy), which says that scientific discoveries are always named after someone other than their original discoverer. The law was first stated by Robert Merton.)

The history of statistics is interesting in part because of its implications for the pedagogy of statistics. I've been reading Allen Downey's [_Think Stats_](http://greenteapress.com/wp/think-stats-2e/), which has some incredibly lucid explanations of statistical concepts. For example, he introduces _p_-values via empirical simulations rather than by cumulative distribution functions. I think this "constructive", computational approach to statistics is a much better way to develop intuition for the meaning of statistical inference.

So I wondered, what were the major conceptual and technical roadblocks in the history of statistics? To what degree are these roadblocks the same ones that people today thinking about statistics run into? By looking to the history of statistics, can we learn how to identify what confuses people and help them overcome those confusions?

Stigler's story starts with [Tobias Mayer](https://en.wikipedia.org/wiki/Tobias_Mayer), an 18th century German astronomer. This may seem like a strange place to start in the history of statistics. What does statistics, which as a physics undergrad I always thought was the domain of psychologists, sociologists, and mathematicians, have to do with astronomy? It turns out that statistics has undergone a strange shuttling between disciplines: starting in astronomy, it moved to surveying and map-making, then to sociology and demography, then helped to inspire psychology, before turning around to demography again.

That's a longer story than will fit here, so let's just say that Mayer lived in a time of accelerating mathematical sophistication: Newton, Leibniz, and Pascal came before him, Euler was a contemporary, and Lagrange and Laplace were soon to follow. Despite the mathematical sophistication and the continuing studies of probability, there was almost none of what we would identify as statistical thinking. For example, the normal distribution had not been discovered, and even the idea of error distributions was not yet well-formed.

Mayer's contribution may strike us as unremarkable. Stigler writes:



<blockquote>
[Mayer's] approach was a simple and straightforward one, so simple and straightforward that a twentieth-century reader might arrive at the very mistaken opinion that the procedure was not remarkable at all.
</blockquote>



What he did was _combine observations_ and then _estimate the error_ in his results.

Mayer's contemporary fame came from his work on preparing [lunar tables](https://en.wikipedia.org/wiki/Lunar_distance_(navigation)), which could be used to compute longitude. (The [longitude problem](https://en.wikipedia.org/wiki/Longitude_rewards#The_Longitude_Problem) was later more satisfyingly solved by accurate clocks.) This story, however, is about Mayer's study of the [libration](https://en.wikipedia.org/wiki/Libration) of the moon. Stigler explains:



<blockquote>
The popular notion that the moon always present the same face to the earth is not literally true. The moon in fact is subject to "libration": The face viewed from earth varies, so that over an extended period of time about 60 percent of the moon's surface is visible from earth. [...] By the time of Mayer's work it was known that the earth's location was at a focus, not the center, of the moon's elliptical orbit. Thus the moon's rotation at a uniform speed produced a third type of libration [after the diurnal and latitudinal librations known to Galileo], one of longitude.
</blockquote>



In essence, Mayer used trigonometry to relate angles between features on the moon's surface, which could be measured with a telescope, to three arc lengths that would characterize the moon's libration. As a high school student today could tell you, if you have three unknowns, you need three equations. In other words, Mayer needed three days' of observations.

Mayer's trouble was that he had twenty-seven days' of observations. This situation presented a well-known problem to contemporary mathematicians: if you three of the equations (i.e., set of observations) to solve for the unknown variables, and then you plugged those solved variables into a different equation, the equation wouldn't equate. In other words, it was clear that at least some of the measurements had errors.

The contemporary approach would have been to select the best three observations and use those. Mayer's innovation was to combine the twenty-seven observations and figure out how to use all of them. Stigler says:



<blockquote>
The point is not that he found a particularly clever way of combining his twenty-seven equations but that he found it useful to combine the equations at all, instead of, say, being content with selecting three "good" ones and solving for the unknowns from them, as he did by way of illustration. This aspect of Mayer's approach is best appreciated by comparing Mayer's work with Euler's memoir of a year later.
</blockquote>



Stigler refers to Euler's work on resolving an apparent inconsistency in the motions of Saturn and Jupiter, which he summarizes this way:



<blockquote>
In 1750 Mayer, faced with a set of twenty-seven inconsistent equations in three unknowns, devised a sensible method of combining them and solving for the unknowns. In 1749, Euler, faced with up to seventy-five equations in up to eight unknowns, was reduced to groping for solutions. Euler worked with small sets of equations [...], and he only accepted numerical answers when different small sets of equations yielded essentially the same results. Euler's problem was similar to Mayer's, yet of the two only Mayer succeeded in finding a statistical solution to his "problem": a "combination of observations" [...]
</blockquote>



Stigler postulates that the fundamental difference in their approach was caused by a fundamental difference in their feelings about errors:



<blockquote>
Mayer [as a practical astronomer] could regard errors or variation in his observations as random [...], and he could take the step of aggregating equations without fear that the bad observations would contaminate the good ones. In fact, he approached the his problem with the conviction that a combination of observations increased the accuracy of the results [... In contrast, Euler] distrusted the combination of equations, taking the mathematician's view that errors actually increase with aggregation rather than taking the statistician's view that random errors tend to cancel one another.
</blockquote>



I should reveal what Mayer actually did. He aggregated his twenty-seven equations into three groups of nine equations each and summed those groups of equations to produce a set of three equations with three unknowns. He grouped the equations in such a way to improve the estimation of the unknowns, specifically, he tried to make the resulting three equations have as different coefficients as possible.

His second conceptual leap was, as mentioned above, to assert that aggregating results decreased the resulting error. Mayer invented the plus-minus symbol when performing his calculation (which was based on the erroneous assumption that error in measurements decreases proportionally to the number of observations rather than, as we now know, to the square root of the number of observations). He was, in a sense, the first one to put formal error bars on his results.

Personally, I find this story so remarkable because I think the Euler-style thinking is the default or easier one for people who haven't studied statistics. Why should I accept a multitude of mediocre measurements rather than finding the best measurement and just using that?

And this idea about the aggregation of errors reminds me of the climate change debate: if so many scientists have so many models---all of which predicted different outcomes for global warming, all with different error bars---it's actually a confusing idea to say that this multiplicity of different measurements makes us more confident about the probably course of climate change. Doubt about climate change is certainly influenced by [intentional obfuscation](https://en.wikipedia.org/wiki/Merchants_of_Doubt) and distrust of scientists in general, but I think it's also fair to give someone the benefit of the doubt and acknowledge that thinking statistically is not easy. Even Euler couldn't do it!