---
title: 'Cognitive Unit Tests (work in progress)'
date: 2022-02-01
permalink: /posts/2022/02/cognitive-unit-tests/
author_profile: false
tags:
  - essays
  - cognition
---

This essay introduces the concept of "cognitive unit tests".

## Rumination and the prefrontal cortex

The pre-frontal cortex is the newest part of our brain, in evolutionary terms.
It can be considered our greatest tool and separates us from other species.
The pre-frontal cortex allows us to rationalize, to plan and schedule, and to do complex computations.
It is a very tired discussion in cognitive science whether the brain is a computer or not [1].
Every few years or so this debate flares up again, and then dies again without any satisfactory progress.
However, I would argue that if any part of the brain resembles a computer it would be the pre-frontal cortex.

But these powerful capabilities bring risks with them.
David Foster Wallace called the mind (which in this context mainly refers to the pre-frontal cortex) "an excellent servant, but a terrible master".
This notion has penetrated popular culture: a few years ago I saw a banner at a music festival in Germany that said "Fuck the Pre-Frontal Cortex".
Planning can bring excessive worrying, and the relatively unique human trait of being able to get stressed or anxious about *imagined* events [2].
Those who do not master this tool can become slaves to it.
Enter the unit test.

## What are unit tests?

Unit tests are a concept that originates from software development.
The idea is to write small tests for particular pieces of the entire computer programme.
For example, let's say we have some complex script that compiles and computes fields in a large data table.
A simple unit test could check whether all expected data columns are present in the table, before passing it on to the next step in the programme.
Unit tests are often written about the steps to be executed as well (i.e. functions).
Let's say we have a function that we know has to return a positive number.
A unit test can then check for positive function outcomes for a range of example inputs.
This approach is especially useful when many developers are working together on a large code base.
If someone makes an update to one part of the system, unit tests can make sure that the behavior of other functions across the system remains as expected.
In modern software development, unit tests are often run every time a code change has been made.
Such a workflow is often referred to as Continuous Integration or Continuous Development (CI or CD).
If we make a change in this particular function, and suddenly it spits out a few negative numbers, a developer can directly see that this respective change may have been wrongly implemented.
Developers typically will only merge changes into production systems when all unit tests pass.

Cognition and reasoning in humans often emerges from a collection of such smaller patterns as well.
Defining and testing for common patterns may alert us about flaws in the execution of our thoughts.
I am not talking about the content of thoughts here, such as holding a wrong fact in memory.
Rather, it is about the way in which we go about reaching the desired outcome and thus how confident we can be about such an outcome.
Everyone knows that we shouldn't believe everything we __hear__ or __read__, but it is harder for many to realize we also shouldn't believe everything we __think__.

## Useful unit tests

So what might such cognitive unit tests look like?
I have compiled a list of ones that can be helpful and which I believe are the most common causes of "programme errors".
Similarly to unit tests in software development, there are no golden standard tests to perform.
Each individual will be more receptive to certain pitfalls, and will have unique tests they will need to define for themselves.
The below unit tests are questions you can ask yourself about a certain belief or idea.
They will help you understand if they are balanced and true.
For each unit test I have included an example situation to apply it in.

1. Am I looping over this idea? Am I progressing? Am I going through the same sequential steps of thoughts and insights, without any new idea? How many times have I gone through the same loop?
  - There is evidence that certain thought patterns strengthening neurophysiological "grooves", reinforcing the same loop
	- One definition of insanity is to try the same thing, hoping for a different outcome (this quote is often attributed to Einstein, but there is no evidence he actually said or wrote it).

1. Where am I on the Dunning-Kruger effect curve? It is common for people to overestimate their knowledge of a certain topic. Sub-questions here might include:
	- What do people who have a lot more experience talk about this idea?
	- What have I done to test my idea?

1. Am I making the situation more black and white than it is? We often make things more categorical than they are in reality. Extra categories are expensive (Gershman, Occam's razor). Moreover, such abstract thinking is necessary for complex thought and being able to make decisions in complex environments (Gershman, 2020). However, in certain situations this ability can make things worse. People with depressive conditions often start thinking in extremes, telling themselves they are completely worthless.

1. What is my emotional state now? Is it possible that my thoughts are generated by my emotions? Am I actually angry or just hungry? Would I think differently tomorrow?

1. Are you learning the right thing? Are you solving the right problem?

1. Am I considering all relevant information? Sometimes we focus on information that supports our current beliefs and ignore information that contradicts them. This is known as confirmation bias. Ask yourself:
    - Have I looked for evidence that contradicts my current beliefs?
    - Am I open to changing my mind based on new evidence?

1. Am I overgeneralizing? Overgeneralization is when we make broad conclusions based on limited evidence. Ask yourself:
    - Am I making a sweeping statement based on a single event or piece of evidence?
    - Can I think of exceptions to this generalization?

1. Am I personalizing the situation? Personalization is when we take responsibility for events outside our control. Ask yourself:
    - Am I blaming myself for something that is not entirely my fault?
    - Are there other factors or people involved in this situation?

1. Am I catastrophizing? Catastrophizing is when we expect the worst possible outcome to happen. Ask yourself:
    - Am I predicting a negative outcome without evidence?
    - What is the most likely outcome based on the evidence I have?

1. Am I using emotional reasoning? Emotional reasoning is when we assume that our emotions reflect the truth. Ask yourself:
    - Am I basing my conclusions on how I feel rather than on objective evidence?
    - Can I separate my emotions from the facts of the situation?

## Relevance for mental health

In this essay I created a parallel to software development, to provide us with more jargon to describe these cognitive tools.
But of course, similar approaches have been proposed in therapy and counseling literature.

In Cognitive Behavioral Therapy (CBT), similar cognitive unit tests are commonly applied as part of therapeutic interventions.
One core exercise is 'cognitive restructuring' or 'reframing' thoughts, where clients learn to identify, challenge, and modify distorted thinking patterns.
These cognitive unit tests serve multiple therapeutic functions in clinical settings.

First, they interrupt automatic negative thought patterns by introducing a metacognitive pause - a moment where patients step back and examine their thinking process rather than being swept along by it.
This pause itself has therapeutic value, as it breaks the cycle of rumination that often characterizes anxiety and depression.

Second, regular application of these tests gradually builds cognitive flexibility, a key predictor of mental health resilience.
Patients who develop the ability to question their thoughts show improvements in various outcome measures, including reduced symptom severity in mood disorders and anxiety conditions.

Third, these cognitive checks create a framework for self-directed intervention between therapy sessions.
Unlike pharmaceutical interventions alone, cognitive approaches equip patients with tools they can independently deploy when distressing thoughts arise, fostering autonomy and self-efficacy in managing their mental health.

Beyond CBT, similar approaches appear in Dialectical Behavior Therapy (DBT), where "checking the facts" serves as a core skill for emotion regulation, and in Acceptance and Commitment Therapy (ACT), where cognitive defusion techniques help patients recognize thoughts as mental events rather than objective truths requiring action.

The effectiveness of these approaches is well-documented in clinical literature, with meta-analyses demonstrating moderate to strong effect sizes for cognitive interventions across multiple conditions.
By systematizing these approaches into "cognitive unit tests," we create a framework that bridges clinical practice with everyday mental health maintenance that anyone can implement.

## Conclusion

The cognitive unit test framework offers a valuable bridge between the structured world of software development and the often chaotic landscape of human thought.
By implementing these systematic checks, individuals gain a powerful tool against rumination - that relentless, circular thinking that characterizes many mental health challenges.

What makes this approach particularly effective is its emphasis on process rather than content.
Rather than trying to suppress negative thoughts (which research shows often backfires), cognitive unit tests create a metacognitive framework that allows individuals to examine how they're thinking, not just what they're thinking.
This shift in perspective interrupts the cognitive fusion that makes rumination so difficult to escape.

The software engineering analogy provides both accessibility and precision.
Just as developers don't need to rebuild an entire codebase to fix a bug, individuals don't need complete cognitive overhauls to improve mental wellbeing.
Instead, identifying and correcting specific problematic thinking patterns can create cascading positive effects throughout one's cognitive ecosystem.

Looking forward, these principles have implications beyond individual mental health.
The systematic identification of cognitive distortions could inform computational models of human reasoning, potentially improving artificial intelligence systems by incorporating more realistic representations of human cognitive biases and correction mechanisms.
Moreover, as we continue developing increasingly sophisticated AI, understanding how to implement "cognitive unit tests" within these systems may help them avoid the equivalent of human cognitive traps while maintaining creative flexibility.

By applying these structured checks to our thinking, we transform the prefrontal cortex from a potential source of rumination to what it evolutionarily developed to be - an extraordinary problem-solving tool that expands human potential rather than constraining it.

## Further Reading

1. [The Brain-Computer Metaphor Debate Is Useless: A Matter of Semantics](https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2022.810358/full){:target="_blank"}. *Blake Richards and Timothy Lillicrap*.
1. [What Makes Us Smart: The Computational Logic of Human Cognition](https://press.princeton.edu/books/paperback/9780691205717/what-makes-us-smart?srsltid=AfmBOoqHjiBUhdWAD7l6UmadsQasHmKCURdtsuTj6BX-v1XwOh1dgzXr){:target="_blank"}. *Samuel J. Gershman*.
1. [Why Zebras Don't Get Ulcers](https://catalogofbias.org){:target="_blank"}. *Robert Sapolsky*.
