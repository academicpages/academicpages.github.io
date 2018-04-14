---
title: "Relative Pseudo-Monads"
author: Sina Hazratpour
permalink: /scribbling/2017-05-06-on-relative-pseudo-monads
collection: notes
type: "scribbling"
date: 2017-05-06
excerpt: "Notes from a talk given by [Nicola Gambino](http://www1.maths.leeds.ac.uk/~pmtng/) in theory seminar "
use_math: true
location: "Birmingham, UK"
---


{% include macro %}


Nicola Gambino gave a very neat talk on his recent joint work with M. Fiore, M. Hyland, and G. Winskel. You can find their paper on arxiv here: [Relative pseudomonads, Kleisli bicategories, and substitution monoidal structures](https://arxiv.org/abs/1612.03678). 
Today, I am going to report on his talk. It will be quite brief. However, I put all of references here so you can find the original paper and much more. I also attached my notes below the summary. You should read the original paper if this summary interests you. Okay, then! Here we go. 

Nicola started by putting their work into a proper context by drawing the following table on the whiteboard<sup>1</sup>.   

|         | Traditional | Kleisli | Relative |
|:--------|:-----------:|:-------:|:--------:|
| 1-dimensional| standard notion of monad   | Kleisli triple [1]  | relative monad [2]   |
| 2-dimensional   | pseudo-monad  | no-iteration pseudo-monad [3]  | **_relative pseudo-monad_** [4] |
|====================================================================================================|




He then started by recalling definition of Kleisli triple due to Manes. After that came definition of relative pseudomonad (definition 3.1 in the paper), which is based on the notions of a relative monad and of a no-iteration pseudomonad, both of which in turn were inspired by that of Kleisli triples. He claimed that Kleisli triples are better suited to define Kleisli categories. There is some justification for this in the paper.

Now, I quote from their paper:

> For a pseudofunctor between bicategories $J: \cat{C} \rightarrow \cat{D}$ (which in our main example is the
inclusion $J : \catg → \Cat$ of the 2-category of small categories into the 2-category of locally
small categories), the core of the data for a relative pseudomonad $T$ over $J$ consists of an object
$TX \in \cat{D}$ for every $X \in \cat{C}$, a morphism $iX : JX \rightarrow TX$ for every $X \in \cat{C}$, and a morphism
$f^{\ast}: TX \rightarrow TY$ for every $f: JX \rightarrow TY$ in $\cat{D}$. This is as in a relative monad, but the equations
for a relative monad are replaced in a relative pseudomonad by families of invertible 2-cells
satisfying appropriate coherence conditions, as in a no-iteration pseudomonad. As we will see
in Theorem 4.1, these conditions imply that every relative pseudomonad $T$ over $J: \cat{C} \rightarrow \cat{D}$ has
an associated Kleisli bicategory $Kl(T)$, defined analogously to the one-dimensional case. In our
main example, the presheaf construction gives rise to a relative pseudomonad over the inclusion
$J : \catg → \Cat$ in a natural way and it is then immediate to identify its Kleisli bicategory with
the bicategory of profunctors. It should be noted here that the presheaf construction is neither
a no-iteration pseudomonad (because of size issues) nor a relative monad (because of strictness
issues). As part of our development of the theory of relative pseudomonads, we show how relative
pseudomonads generalize no-iteration pseudomonads (Proposition 3.3) and hence (by the results
in [53]) also pseudomonads.



For the rest of the story please see my notes here: 

* <i class="fa fa-file-pdf-o" aria-hidden="true"></i> [Notes from Nicola's talk](https://sinhp.github.io/files/CT/notes-from-talk-by-N.Gambino-relative-ps-monads.pdf) 

* <i class="fa fa-file-pdf-o" aria-hidden="true"></i> [Supplementary notes](https://sinhp.github.io/files/CT/Kleisli-triples.pdf) on Kleisli triples from Moggi's [Notions of computation and monads](http://fsl.cs.illinois.edu/pubs/moggi-1991-ic.pdf)
   




--------------------------------------------------------
1. One of the few negative aspects of being a student in Birmingham CS is lack of access to blackboards. It's whiteboards everywhere. Even, in the school of mathematics there are not many blackboards. I totally miss them. Some of us in theory group raised our voices to mention this to the head of school a year ago but nothing happened. Perhaps we should start carrying our own blackboards like these great folks: [the Kurdish teachers in western mountains of Iran](http://www.sbs.com.au/movies/review/kurdish-teachers-carrying-blackboards-their-backs-look-students-hills-iran). 
{: .notice}
---------------------------------------------------------



[1] E. Manes. Algebraic theories. Springer, 1976.

[2] T. Altenkirch, J. Chapman, and T. Uustalu. _Monads need not be endofunctors._ Logical Methods in Computer
Science, 11(1:3):1–40, 2015.

[3] F. Marmolejo and R. J. Wood. _Monads as extension systems – no iteration is necessary._ Theory and Applications
of Categories, 24(4):84–113, 2010.

[4] M. Fiore, M. Hyland, N. Gambino, and G. Winskel. _Relative pseudomonads, Kleisli bicategories, and substitution monoidal structures_
2017  [<i class="fa fa-external-link" aria-hidden="true"></i>](https://arxiv.org/pdf/1612.03678.pdf)
   
