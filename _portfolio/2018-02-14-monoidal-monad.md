---
title: "Notes On Monoidal Monad"
author: Sina Hazratpour
permalink: /scribbling/2018-02-14-monoidal-monads
collection: portfolio
type: "scribbling"
date: 2018-02-14
excerpt: "Notes from my Lab Lunch talk on February 13, 2018"
use_math: true
location: "Birmingham, UK"
---

{% include macro %}

`Abstract:`
In the talk, I introduce well-known and by now classical notion of monoidal monads. They are oplax monads on a monoidal category such that the monoidal structures are compatible with monad structures. These compatibility conditions are stated by several coherence axioms. These conditions can be wrapped in the following equivalent definition: A monoidal monad is a monad in the 2-category of monoidal categories, oplax monoidal functors, and monoidal transformations.  

I will then show that oplax monoidal structures of the monad, making it an oplax monoidal monad, is in one-to-one correspondence with monoidal structures of the Eilenberg–Moore category of algebras of that monad such that the forgetful functor from the category of algebras to the base category is strict monoidal. In other words, we get a lifting of the tensor structures of base category to tensor structures of the category of algebras over its objects. I give two important examples of such situation: first, power set monad on monoidal category of sets where tensor product is just cartesian product and unit is the terminal set. The algebras are complete join semi-lattices (aka sup-lattices) and tensoring of algebras is the tensoring of sup-lattices (which is how coproduct of frames is constructed.) The unit of tensor product is the free sup-lattice on one generator, i.e. the lattice containing two elements $\bot$ and $\top$ where $\bot \leq \top$.
The second example is symmetric algebra monoidal monad on the monoidal category of $k$-vector spaces over some field $k$. The algebras of this monad are commutative unital $k$-algebras.  
Also, for any commutative monoid $M$, the delooping category $\bb{B} M$ is a monoidal category in which both tensoring and composition are given by multiplication in $M$. Any monoidal monad on $\bb{B} M$ is necessarily the identity monad.

`Notes:`
Notes from the talk <a href="/files/CT/monoidal-monad.pdf" target="_blank"> <i class="fa fa-file-pdf-o" aria-hidden="true"></i> </a>




`Further Reading:`
* Kock, A. (1968) 'Monads on symmetric monoidal closed categories', Arch. Math (1970) 21: 1. https://doi.org/10.1007/BF01220868

* Moerdijk, I (2002). '[Monads on tensor categories](https://www.sciencedirect.com/science/article/pii/S0022404901000962?via%3Dihub)', Journal of Pure and Applied Algebra, Volume 168, Issues 2–3, 23 March 2002, Pages 189-208

* Simon Willerton (2008), 'A diagrammatic approach to Hopf monads', [arXiv:0807.0658](https://arxiv.org/abs/0807.0658)

* Lack, S. & Street, R. (2002) 'The formal theory of monads II', Journal of Pure and Applied Algebra
Volume 175, Issues 1–3, Pages 243-265 
