---
title: "A Topos Without Points"
author: Sina Hazratpour
excerpt: "An example of topos (from logic) that does not have any points. "
category: research notes
tags: topos, points, sup-topology, atoms
permalink: /scribbling/19-04-2015-a-topos-without-points
collection: portfolio
type: "scribbling"
date: 19-06-2016
use_math: true
location: "London, Canada"
---


{% include macro %}


Let $B$ be complete [Boolean algebra](https://ncatlab.org/nlab/show/Boolean+algebra). Here, completeness is categorical completeness which means $B$ has all limits (i.e. meets). Note that any complete poset is necessarily cocomplete. Consider [locale](https://ncatlab.org/nlab/show/locale) $L_B$ whose corresponding frame $O(L_B)$ is $B$. We now construct a [site](https://ncatlab.org/nlab/show/site) on $B$ by introducing a basis for a [Grothendieck topology](https://ncatlab.org/nlab/show/Grothendieck+topology) . 

Note that for any $a$ in $B$ a sieve on $a$ is just a downward closed subset $S$ of $\darr (a) = \{ b \in B | b \leq a \}$.  



Toposes, geometric morphisms, and natural transforamtions form a 2-category denoted by $\mathfrak{Top}$. Note that for each pair of toposes $D$ and $E$, $\mathbf{Geom}(D,E)$ is a large though locally small category. 

------------------------------------------------------------------




#### Example.  
Suppose $X$ is a (non-$T_1$) topological space  We define the following (non-trivial) _partial_ order on points of $X$. 
 \begin{equation} 
 x \leq x'  \ \ \text{iff every neighbourhood of} \ \ x  \ \ \text{contains} \ \ x'
 \end{equation}
 
We can extend this order to all maps between topological spaces. Suppose $f,g: X \rightrightarrows Y$ are (continuous) maps. Define



\begin{equation}\label{def-order on maps}
 f \leq g  \ \  \text{iff} \ \ f(x) \leq g(x) \ \ \text{for every} \ \  x \in X 
\end{equation} 



A ramification of above defintion, which is straightforward to see, is that $f \leq g$ if and only if $f^{-1} (V) \subseteq g^{-1}(V)$ for evey open set $V$ of $Y$.  Notice that $f$ and $g$ give us $f_{\ast},g_{\ast}: Sh(X) \rightrightarrows Sh(Y)$ which are _pushfoward_ geometric morphisms along $f$ and $g$ respectively. 

Thus, if $f \leq g$, then  for any sheaf $P$ on $X$, and any open $V$ of $Y$, we get the restriction 
$$g_{\ast}(P)(V)=P(g^{-1}(V)) \rightarrow P(f^{-1}(V))= f_{\ast}(P)(V)$$.
This yields a natural transforamtion $f \Rightarrow g$ in $\geom(Sh(X),Sh(Y))$. 

----------------------------------------------------------------------------------


#### Remark.
From the construction above we obtain a functor $$ \mathbf{Top}(X,Y) \rightarrow \mathbf{Geom}(Sh(X),Sh(Y))$$. 


As a consequence, it is generally too much to expect diagrams in Top to commute on the nose", i.e up to
equality { commuting is usually only up to isomorphism. In broad terms, this is because
in a category equality between ob jects is less important that isomorphism


$\x$ 

---------------------------------------------------------------------------------
