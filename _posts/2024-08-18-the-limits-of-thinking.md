---
title: 'The Limits of Thinking'
date: 2024-08-18
permalink: /posts/2024/08/the-limits-of-thinking/
author_profile: false
tags:
  - essays
  - cognition
---

This essay discusses the mental concept of thinking in limits.
Its utility is demonstrated in a situation where humans have poor intuition.

## Physicists and Their Limits

During my undergrad studying physics, we were taught a common trick to deal with real-world complex scenarios.
Physicists have to deal with finding elegant equations and tractable models in a world that is noisy.
In order for them to model a system realistically, they need to make simplifications, assumptions, and approximations.
For example, when considering the movement of a car down a hill, it is common to consider the car as a solid block and to neglect surface friction.
By doing so, they can focus on the fundamental principles governing a system without getting bogged down by every minor detail.
This approach can be viewed as analyzing the situation in a specific **limit**, where certain parameters are taken to extremes—such as the limit of very low friction, very large numbers, or very small perturbations.
These "limits" help physicists gain insights into the behavior of systems under **idealized** conditions, which can often be extended to more complex, real-world situations.

## People Have Bad Intuition Regarding Statistics

People often struggle with statistics because our brains are wired to rely on intuition and gut feelings, which can lead to faulty reasoning when faced with probability and uncertainty.
Our cognitive processes have evolved to handle immediate, concrete situations rather than abstract, probabilistic thinking.
We are naturally inclined to make decisions based on patterns we perceive in everyday life, often using mental shortcuts, known as **heuristics**, to simplify complex information.
While these shortcuts can be useful in some situations, they often lead to errors in judgment when dealing with statistics.

One reason for this is the **representativeness heuristic**, where we tend to judge the likelihood of an event based on how similar it is to our existing stereotypes or expectations, rather than on actual statistical probabilities.
For instance, when asked to consider whether a quiet, bookish person is more likely to be a librarian or a farmer, many people instinctively choose librarian because that fits the stereotype, even though there are far more farmers than librarians, making it statistically more likely that this person is a farmer.

Another cognitive bias that affects our understanding of statistics is **confirmation bias**, where we tend to seek out and give more weight to information that confirms our preconceptions, while disregarding evidence that contradicts them.
This bias can make it difficult to accurately assess probabilities because we might focus on data that supports what we already believe rather than considering all the evidence objectively.

The **availability heuristic** is also at play, where we judge the probability of events based on how easily examples come to mind.
For example, people might overestimate the likelihood of plane crashes because such events are widely reported and memorable, even though statistically, air travel is much safer than driving.

Lastly, there’s the **illusion of control**, where people overestimate their ability to influence outcomes that are actually determined by chance.
This can lead to misunderstandings about probability, such as gamblers believing they can “control” a roll of the dice by using a particular technique, even though each roll is independent and random.

## A Concrete Example

Let's demonstrate the benefit of thinking in limits by applying it to a famous brain teaser that's based on an old game show scenario: the Monty Hall problem.

![Alt text](https://upload.wikimedia.org/wikipedia/commons/3/3f/Monty_open_door.svg "Monty Hall setup")

### The Monty Hall problem

Here’s how it works: you’re a contestant facing three doors.
Behind one door is a shiny new car, and behind the other two are goats.
You pick a door, and then the host, who knows what’s behind each door, opens one of the other doors to reveal a goat.
Now, the host asks if you want to stick with your original choice or switch to the other unopened door.

It might seem like it doesn’t matter, but here’s the twist: if you switch, your chances of winning the car jump to 2/3.
Sticking with your first choice leaves you with just a 1/3 chance.
That’s because the host’s reveal actually changes the odds, making the switch the smarter move—even though it might feel a bit counterintuitive at first.
Many people have the intuition that it doesn't matter if you switch; the probability of getting the car is 1/2.
This feels intuitive because we’re used to thinking about equal chances when two options are left.

### Scaling up to Four Doors

If we scale up the Monty Hall problem to four doors, with one car and three goats, the dynamics change a bit.

Here’s the setup: you choose one of the four doors, and then the host, who knows what’s behind each door, opens *two* of the remaining three doors to reveal two goats.
Now you’re faced with the option to stick with your original choice or switch to the other unopened door.

In this scenario, your initial choice still had a 1/4 chance of being the car, while the other three doors collectively had a 3/4 chance.
After the host opens two doors to reveal goats, the entire 3/4 chance is now concentrated on that one remaining unopened door.
This means that switching to the last unopened door gives you a 3/4 chance of winning the car, while sticking with your original choice leaves you with just a 1/4 chance.
So, just like in the classic three-door version, switching is still the better strategy, and in this case, it’s even more straightforward since the odds in favor of switching are quite strong.

The intuition that the probability of getting the car is 1/2 still holds; you still have two unopened doors and one car.
This is the key insight.
Taking a single step towards the limit of infinite doors did not *fundamentally* change the nature of the brain teaser.

### Scaling up to Infinite Doors

If the nature of the problem has not changed, we can keep adding doors until we get to the limit of infinite doors.
Imagine the Monty Hall problem, but with a **million** doors instead of just three.
Out of these million doors, one hides a car, and the other 999,999 all hide goats.
You pick one door, which has a tiny 1 in a million chance of being the car.
Then, the host, who knows where the car is, dramatically opens 999,998 of the other doors, revealing goats behind every one of them.
Now you’re left with just two unopened doors: the one you originally picked and one other.
At this point, the question is whether you should stick with your original choice or switch to the last remaining door.

Initially, your choice had only a 1 in a million chance of being correct, meaning the car was almost certainly behind one of the other 999,999 doors.
After the host opens almost all of them, that 999,999 to 1 chance is now concentrated entirely on the single remaining unopened door.
This means switching gives you a near-certain 999,999 in a million chance of winning the car, while sticking with your first choice leaves you with the same slim 1 in a million odds.
In this extreme version of the Monty Hall problem, switching isn’t just a better strategy—it’s practically a guaranteed win!

Now we return to the imagined person that intuitively did not consider switching doors in the three-door scenario to make a difference.
In fact, they may still be intuitively confused about this situation.
If there are two doors left, and one of them has a car, does that not still constitute a 50/50 situation?
But now comes an important next step.
We ask them to do the million-door scenario *multiple* times.
If they follow their logic, they *should* expect to get the car half the times.
But would they intuitively think that they picked the car out of a million doors in 50% of those cases?

## Relevance for Cognition

Applying this mental framework can be useful for dealing with probabilistic reasoning in the real world.
But most people don't find themselves in such situations on a regular basis.
Here I argue that the framework of thinking in limits can be applied to daily life as well.

A common application of this principle is the ``What's the worst that can happen?'' trope.
Your friend is trying to set you up on a blind date, but you are not really in the mood.
You can explore the limits of this situation.
The downside limit are manageable: in the worst case, you just have a mediocre conversation with someone and you're on your way home.
The upside limit is much more significant: in the absolute best case you might meet the love of your life.
Thinking in limits uncovers the assymetry of the situation, and may inform your decision to meet the person or not.

Another application is in political thought.
Oftentimes politicians or voters are concerned about a concrete problem, and they are looking for a quick win.
But sometimes going for this has far reaching consequences.
A secular society might impose a small restriction on one particular religion, for whatever practical reason.
And maybe in isolation this seems like a good idea.
Or a group of activists may want the government to ban fossil fuels completely.
But what if we consider this step into its limit?
What if this could cascade into a fundamental shift in the core of society, leading to an end result that no one would be satisfied with?
Again, our intuition may kick in in the limit.
The direct, here-and-now decision could make intuitive sense, but considering the decision in its limit does not make intuitive sense.
This small mental exercise can be incredibly powerful in making more robust and principled political decisions.

### Application to Mental Health

A similar approach can help people with social anxiety.
It is tempting for many to get stuck at an intermediate level of analysis.
They might wonder if people in the metro are looking at them, or if their friends are actually not their friends and secretly despise them.
What if we have the courage to go to the limit of this situation?
Let's say all of your friends do indeed hate you.
But they also spend a lot of time with you and sometimes buy you gifts or check in on you.
That must mean they really have a manipulative plan to gain your trust, just so they can hurt you even more later.
They dedicate a lot of time of their life just to spite you.
And those people in the bus?
They would all rather spend time looking at you and judging you, rather than talk to their friends or listen to some music.
If we go to this limit, our intuition kicks back in to save us: this scenario seems incredibly unlikely.

Thinking in limits could be interpreted as 'black and white thinking', where people lose sight of nuances in the real world.
In fact, perhaps because this concept was inspired by them, mathematicians and physicists are often seen as such people.
They bring their simple and elegant models from their labs to the real world, and failing to realize that these models are oversimplified they become frustrated with the real world.
Therapists also often talk about the concept of 'catastrophizing', leading people to spiral.
Your partner did not respond to your text for a few hours, and you start to think 'what if?', and before you know if you're having a panic attack.
It's important to realize here that thinking in limits is not the end goal, and the most accurate way of seeing a situation.
It is a mental tool that allows for exploration and understanding of a situation.








## Further Reading

1. [What Makes Us Smart: The Computational Logic of Human Cognition](https://press.princeton.edu/books/paperback/9780691205717/what-makes-us-smart?srsltid=AfmBOoqHjiBUhdWAD7l6UmadsQasHmKCURdtsuTj6BX-v1XwOh1dgzXr){:target="_blank"}. *Samuel J. Gershman*.
