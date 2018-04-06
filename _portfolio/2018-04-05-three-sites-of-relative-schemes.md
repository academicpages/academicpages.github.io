---
title: "Three Sites Of Relative Schemes"
author: Sina Hazratpour
excerpt: "Warning: in construction! We introduce three Grothendieck topologies on the category of based schemes; the Zariski, the étale and the fpqc topology"
category: research notes
tags: 
   - schemes
   - the Zariski topology
   - the étale topology 
   - the fpqc topology
   - flat morphisms 
permalink: /scribbling/2018-04-05-three-sites-of-relative-schemes
collection: portfolio
type: "scribbling"
date: 05-04-2018
use_math: true
location: "Vienna, Austria"
---


{% include macro %}


## Relative Schemes

Grothendeick's relative point of view philosophy in stuying schems and more generally any spatial category is that we should really be studying morphisms than objects; the emphasis of the basic theory of schemes should not be on the properties of schemes, but on the properties of morphisms. In doing this, one generalizes the notions previously defined on objects to morphisms, e.g. connectedness, local connectedness, etale, (quasi) compactness, etc. 

Suppose $(\cat{C}, \bb{J})$ is a site. and $U$ is an object of $\cat{C}$. We say a sieve $R$ _covers_ $U$ if $R \in \bb{J}(U)$. We define an inherited topology $\bb{J}_U$ in the following way: for any morphism $f \maps \colon V \to U$ in $\cat{C}/U$, and any family ${ g_i \colon V_i \to U }_i$, the family ${ h_i \colon g_i \to f }_i$ in $\cat{C}/U$ covers $f$ whenever ${h_i \colon V_i \to V}$ covers $V$.   



Jean-Pierre Serre introduced the notion of Flatness for modules in his paper Géometrie Algébrique et Géométrie Analytique in 1956. Suppose $R$ is a commutative ring. Any left $R$-module ins naturally a right $R$-module and vice versa. We denote category of $R$-modules by $Mod(R)$. An $R$-module $M$ is _flat_ whenever the functor $M \tensor_R - \maps Mod(R) \to Mod(R)$ is left exact. This means that tensoring with $M$ preserves (left) exact sequences; in particular tensoring with $M$ preserves injective morphisms of $R$-modules.   


