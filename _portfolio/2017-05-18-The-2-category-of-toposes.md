---
layout: post
title: The 2-category of toposes
author: Sina Hazratpour
category: research
tags: 
use_math: true
comments: true
---

{{ page.title }}
================


{% include macros %}

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




