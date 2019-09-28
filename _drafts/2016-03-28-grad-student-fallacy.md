---
date: '2016-03-28'
slug: grad-student-fallacy
title: The grad student's (aka "prosecutor's") fallacy
---

[mathjax]
I think the most rewarding thing about learning a little bit about Bayesian statistics is understanding the [_prosecutor's fallacy_](https://en.wikipedia.org/wiki/Prosecutor%27s_fallacy). I like to call it the _grad student's_ fallacy for fun. I'll explain why.

The prosecutor's fallacy usually takes a form like this: "If the defendant were innocent, it's very unlikely (say 1% probable) that the evidence we found would exist. Therefore, it is very unlikely that the defendant is innocent (say 1% probable). Because there is a 99% chance that the defendant is guilty, we should convict."

The fallacy is subtle: the prosecutor says (correctly) that the probability that the evidence found at the scene of the crime would exist if the defendant were innocent is low (say 1%). The prosecutor then _incorrectly_ claims that this means that, given the evidence, there is a 1% chance that the defendant is innocent.

In probability jargon, we would say that prosecutor has claimed that the probability of the parameter (being innocent) _given the data_ (the evidence) is equal to the probability of the data _given the parameter_. In equations, the "parameter" or state of nature (e.g., being innocent) is written [latex]\theta[/latex] and the "data" (e.g., the evidence) is written [latex]\mathbf{X}[/latex] so that the prosecutor equates [latex]\mathbb{P}(\theta | \mathbf{X})[/latex], i.e, the probability of being innocent given the data, and [latex]\mathbb{P}(\mathbf{X} | \theta)[/latex], i.e., the probability of the data given that the defendant is innocent.

In fact, a basic algebraic manipulation of the definition of [conditional probabilities](https://en.wikipedia.org/wiki/Conditional_probability), which is given the fancy name _[Bayes' rule](https://en.wikipedia.org/wiki/Bayes%27_rule)_, says that these two quantities are _not_ equal:

[latex]\displaystyle
\mathbb{P}(\theta | \mathbf{X}) = \frac{\mathbb{P}(\mathbf{X} | \theta) \mathbb{P}(\theta)}{\mathbb{P}(\mathbf{X})}.
[/latex]The term in the denominator is a nuisance, so this equation is often written with a proportionality sign,

[latex]\displaystyle
\mathbb{P}(\theta | \mathbf{X}) \propto \mathbb{P}(\theta) \mathbb{P}(\mathbf{X} | \theta)
[/latex]
and pronounced "_posterior_ is _prior_ times _likelihood_". The posterior probability is the probability of the state of nature (e.g., the defendant is innocent) _after_ the incorporation of new data, the prior is the probability before you saw data, and the likelihood is the probability of the data given the state of nature.

The prosecutor's fallacy states (incorrectly) that the posterior (given the data, how probable is it that the defendant is guilty?) and the likelihood (given that the defendant is guilty, how probable is the evidence?) are the same. The important different the prior, which says, "Before you saw any evidence, how probable do you think it is that the defendant is innocent?" To be a statistically proper jury member, you should walk in to the court with a prior strongly weighted toward innocence: as far as you know, this is just a random citizen nabbed off the street and dumped into the courtroom.

Most people, however, have some trust in the legal system, so they expect that, by the time a person is a defendant, there is evidence against them. Other biases, like racial or ethnic biases, factor into someone's prior.

I call this the grad student's fallacy because, in science, we often compute _p_-values, which is the probability the data observed in the experiment arose because the state of nature is something boring (a "null model"). A common example is, "Assume that my experimental treatment actually does nothing. How likely is it that the difference I observed between the control and treatment groups is due to normal fluctuations in the measurement?" This _p_-value is the Bayesian likelihood [latex]\mathbb{P}(\mathbf{X} | \theta)[/latex], which often gets confused with the posterior [latex]\mathbb{P}(\theta | \mathbf{X})[/latex]: "Because it's highly improbable that my data arose from the null model, it's high probable that my hypothesis was correct." This is exactly the prosecutor's fallacy.

Scientists, like most humans, actually _do_ use a Bayesian analysis. If I do an experiment to check if the Earth is flat, and I get a strong _p_-value, no one will believe me because their prior probabilities that the Earth is flat are basically nil. The point here is that graduate students should say, _a priori_, how likely it is that they think that the thing they are testing is true. If you're testing a wild theory, you need to have extra-wild data to support it!