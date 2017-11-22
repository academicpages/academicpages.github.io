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


Let $B$ be complete [Boolean algebra](https://ncatlab.org/nlab/show/Boolean+algebra). Here, completeness is categorical completeness which means $B$ has all limits (i.e. meets). Note that any complete poset is necessarily cocomplete. Consider [locale](https://ncatlab.org/nlab/show/locale) $L_B$ whose corresponding frame $O(L_B)$ is $B$. We now construct a [site](https://ncatlab.org/nlab/show/site) on $B$ by introducing a basis for a [Grothendieck topology](https://ncatlab.org/nlab/show/Grothendieck+topology). The topology will be sup-topology $\cat{J}_{sup}$. We then consider topos of sheaves on site $(B,\cat{J}_{sup})$ and prove it does not have any points. 


## Points

A point of a Grothendiek topos $\cat{E}$ is a geometric morphismp $\Set  \rightarrow \cat{E}$; if we write $\cat{E}$ as the 
classifying topos $\Set[\thT]$ of some geometric theory $T$ then the points of $\cat{E}$ are in one-to-one correspondence with the models of $\bbT$ in $\Set$. We say a Grothendiek topos $\cat{E}$ has enough points if the inverse image of points $p: \Set → \cat{E}$ are jointly
conservative. $\cat{E} = \Set[\thT]$ has enough points precisely when $\thT$ has enough models. 


### A topos with no points  

The way we proceed to show that $\Sh((B,\cat{J}_{sup}))$ does not have any points is through a process called localic reflection. That is we can assign to any topos, its localic reflection $L(\cat{E})$, the locale which has the partially ordered set $Sub_{\cat{E}}(1)$ as frame of opens. If the topos $\cat{E} = \Sh (L)$ is localic, then we do not lose any information in the process of localic reflection; that is to say $Sub_{\cat{E}}(1) \simeq L $ 
