---
title: 'Card trick by Fitch Cheney'
date: 2022-08-18
permalink: /posts/2022/08/cardtrick/
---

One of the most underrated card tricks of all time. (Clever mathematics included.) 
<!--more-->

_I have used [this website](https://deck.of.cards/old/) to create the pictures below._

This trick was devised by Dr. William Fitch Cheney Jr. in the late 1950’s and was printed in Wallace Lee’s _Math Miracles_, 1960. The original trick is as follows:

A participant picks up a deck of cards (no Jokers), shuffles it and then pulls out five cards at random. Alice (Magician A) picks up the cards, picks out one of them and places it face down onto the table, then arranges the remaining four cards face up on the table. The volunteer then calls Bob (Magician B) into the room, who looks at the face up cards and states the identity of the face down card!

![The cards are drawn out.](https://raw.githubusercontent.com/ArnavMetrani/arnavmetrani.github.io/blob/master/_data/Posts_Data/Card_Trick/card1.png)

![All cards are face up.](https://raw.githubusercontent.com/ArnavMetrani/arnavmetrani.github.io/blob/master/_data/Posts_Data/Card_Trick/card2.png)

![Bob is called into the room…](https://raw.githubusercontent.com/ArnavMetrani/arnavmetrani.github.io/blob/master/_data/Posts_Data/Card_Trick/card3.png)

![…and correctly predicts the Jack of Hearts.](https://raw.githubusercontent.com/ArnavMetrani/arnavmetrani.github.io/blob/master/_data/Posts_Data/Card_Trick/card4.png)

Mind blowing isn’t it! The best part of this trick is that it doesn’t involve any sneaky tricks or sleight of card. Alice could even be replaced by a computer program and the trick would work out just fine.
So you’d might want to spend some time on finding out how this trick works before looking at the solution.

## Ready?

Now, it’s necessary for some information to be exchanged between Alice and Bob, even if not directly. Stating them in the description of the trick would give it away however, and it wouldn’t be obvious to the audience at first glance. Firstly, Alice only hides the card which shares its suit with another card out of the four.[^1]
[Pigeonhole Principle](https://en.wikipedia.org/wiki/Pigeonhole_principle) applies; 5 cards and 4 suits, so two cards must share the same suit.

If you look closely, the card placed right next to the hidden card share their suit; a marker to convey information about the hidden card’s suit to Bob.[^2]
Once the suit of the hidden card has been determined, the rank of the card still needs to be conveyed to Bob. 
For this, we need to establish a system. 

**In alphabetical order: Clubs will have the highest value, then Diamonds, then Hearts and at last, Spades.**
Next, when we arrange the cards of any suit in a circle (based on their value) we notice that the shortest walk between any two cards is at most 6. For example, we can see below that we can either go from Q to 5 by traveling 6 steps clockwise, or by traveling 7 steps anti clockwise. Here, we choose to walk in anticlockwise as convention. 

![Not a perfect circle, but it does the job…](https://raw.githubusercontent.com/ArnavMetrani/arnavmetrani.github.io/blob/master/_data/Posts_Data/Card_Trick/card5.png)

We can now arrange the remaining three cards (excluding the hidden card and the marked card that is) to signify any number from 1 to 6, _which covers all of the minimum length paths._ Since none of the cards share the same value, we can designate these three cards as High (H), Middle (M) and Low (L). This seems to be the simplest way to designate value as is based on the ascending order of the value of the permutations.[^3]

$LMH = 1 , LHM = 2, MLH = 3, MHL = 4, HLM = 5, HML = 6.$

Thus, in order to indicate the rank of the card, all we have to do is choose a direction to walk in order to reach the card, and the starting point of the walk. Since we have chosen anticlockwise as the convention, we now need to choose the card to be hidden accordingly, such that it takes at most 6 steps to reach it by walking anticlockwise.

However, this would limit the choice of the hidden card. If in a random draw of 5 cards, cards with rank 2 and 7 were of the same suit, then only 7 could be hidden. This new system allows you to hide either 2 or 7.

We will have to look at another method in order to overcome this restriction. Since there are 6 different ways of arranging the rest of the three cards and there are 12 possible walks from any chosen card, combinatorics alone will not be able to help us here. 

Fortunately, the orientation of the face up cards comes in to save the day.
Any one of the four cards can be rotated clockwise or anti clockwise slightly, in order to indicate the direction in which you need to ‘walk’ / count to reach the hidden card (from the card that shares the suit).

This trick works even when you let the volunteer decide which one of the five cards should be hidden!
The card that indicates the suit can be positoned accordingly in the arrangement of the four face up cards to convey the suit of the hidden card, even if their suits do not match.
For this, let the four face up card positions (w.r.t to the face down card) be designated as (**Clubs,Diamonds,Hearts,Spades**). Now, all you have to do to indicate the suit and the rank of the hidden card is to place the card that indicates the suit at a slightly different level than the rest of the cards. Here, one of the cards will also have to be rotated slightly in order to indicate the direction of walk.
To sum up how this method would work:

1. Five cards are drawn randomly.
![](https://raw.githubusercontent.com/ArnavMetrani/arnavmetrani.github.io/blob/master/_data/Posts_Data/Card_Trick/card6.png)
2. The volunteer chooses the card to be hidden. ![](https://raw.githubusercontent.com/ArnavMetrani/arnavmetrani.github.io/blob/master/_data/Posts_Data/Card_Trick/card7.png)
3. The attendant then places the face down card as the first card from the rest.
![](https://raw.githubusercontent.com/ArnavMetrani/arnavmetrani.github.io/blob/master/_data/Posts_Data/Card_Trick/card8.png)
4. The attendant then places one of the cards at a slightly different inclination than the rest to indicate the suit. This card will also serve at the starting point of the walk.
![3rd position, as (Clubs,Diamonds,Hearts,Spades)](https://raw.githubusercontent.com/ArnavMetrani/arnavmetrani.github.io/blob/master/_data/Posts_Data/Card_Trick/card9.png)
5. Follow the numbering system to indicate the length of the walk. 
![LHM = 2 steps from the king.](https://raw.githubusercontent.com/ArnavMetrani/arnavmetrani.github.io/blob/master/_data/Posts_Data/Card_Trick/card10.png)
6. Rotate one of the cards slightly anticlockwise to indicate the direction of the walk.
7. The magician walks in, looks at the four face up cards and rightly predicts the face down card.

This modification might give away too blatantly that information is being conveyed, but this is the only method I could think of that allowed the audience to choose the card to be hidden. It is surely something you should experiment with; to find better methods.

#### This might take some time to get acquainted with, so you should try this out for yourself a couple of times with a deck of cards. 

Finally, the ingenuity that has gone into this card trick is something to marvel at, from the utilization of the Pigeonhole Principle to clever combinatorics.

_That’s the end! I hope you liked it._

Here are some resources to dive deeper into the workings of the trick:

- [Including the Joker card](https://puzzling.stackexchange.com/questions/10004/the-fitch-cheney-card-trick-extended)
- [Generalization of the trick](https://mathoverflow.net/questions/20667/generalization-of-finch-cheneys-5-card-trick)
- [Applications of the Pigeonhole principle](https://www.youtube.com/watch?v=TCZ3YwbcDaw)





[^1]: Although this is not necessary. Read on.
[^2]: To obscure this from the audience, Alice and Bob could decide beforehand to use some system for computing the positioning of the ‘marker’ card, eg. $(3n + 1) mod \ 4$ is the position of the face up card which matches suit for the nth time the trick is performed.
[^3]: Of course, you could come with your own system as well.

------
