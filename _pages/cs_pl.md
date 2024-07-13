---

title: "Computer Science (mainly Programming Languages)"
permalink: /cs_pl/
author_profile: true

---


<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-4MFKZNB73K"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-4MFKZNB73K');
</script>

Under Construction!!!
======
I am preparing an article on continuation.


Derivatives of Regular Expression
======
Regular expressions can be converted to deterministic finite automata (DFA) using well-known methods such as Thompson's construction. However, this involves intermediate steps through non-deterministic finite automata (NFA), which can be cumbersome. In this article, we explore the concept of the derivatives of regular expressions and how to construct equivalent automata using this derivatives. For more detailed information, refer to Chapter 4.4 of *Elements of Automata Theory* by Jacques Sakarovitch. A basic understanding of regular expressions, finite automata, and group theory is assumed.


* Definition
The derivative of a regular expression e with respect to a character a is defined as follows:

$∂_a$ &#8709; = &#8709;\\
$∂_a$  a = ε\\
$∂_a$  ε = &#8709;\\
$∂_a$  b = &#8709;\\
$∂_a$ (e1 e2) = ($∂_a$ e1) e2 + ν(e1)$∂_a$ e2 (← This is remarkably different from the typical differentiation of functions.)\\
$∂_a$ (e1 + e2) = $∂_a$ e1 + $∂_a$ e2\\ 
$∂_a$ e\\UTF{2217} = ($∂_a$ e)e\\UTF{2217}\\

Here, a,b ∈ Σ and a ≠ b

The auxiliary function for the given regular expression ν(e) is defined as follows:

\varepsilon & \text{if } \varepsilon \in L(e) \\
\emptyset & \text{otherwise}
\end{cases} \]

The derivative with respect to strings is extended as follows:\\
$∂_a$ e = e,\\
$∂_w_a$ e = $∂_a$ ($∂_w$ e)

Example
For e = xyza(b + c)* and w = "xyz", we have:
$∂_wa$ e = (b +c)*

* Language Described by $∂_w$ e

Regular expressions are closed under string derivatives (Theorem 4.1 in [Brzozowski, 1964]). Thus, we can define the language described by regular expression $∂_w$ e. The language denoted by ∂_w e corresponds to the left quotient of L(e) by the string "w".

L($∂_w$ e) = w^(−1) L(e)
	      = {w′ | ww′ ∈ L(e)} 

* Constructing Automata Using Derivatives of Regular Expressions
  * Definition (Equivalence of Regular Expressions)
    * We write e1 ≡ e2 if L(e1) = L(e2). The relation ≡ divides expressions e into equivalence classes denoted by [e].
    * Example
      * For instance, L((0+1)*) = L((0*1*)*) = {0, 1}*, hence (0+1)* ≡ (0*1*)*.
    * Here, the set Q = {[$∂_w$ e0]| w ∈ Σ*} becomes finite. We can construct a DFA A_e0 that accepts L(e0) by using these equivalence classes [$∂_w$ e0] as states. (This construction corresponds to reading character a from state e by differentiating e with a.)
A_e0 = (Q, Σ, δ, [e0], F)
where: 
δ([e], a) = [$∂_w$ e0]，F = {[e] | [e] ∈ Q, ε∈ L(e)}
    * Weaker Equivalence Relation
      * Using a weaker relation \UTF{2248} defined below instead of ≡, we can ensure that the equivalence classes remains finite, allowing for the construction of a DFA.  
 e1 +e2 \UTF{2248} e2 +e1, (e1 +e2) + e3 \UTF{2248} e1 +(e2 + e3), (e1 e2) e3 \UTF{2248} e1(e2 e3), (e\UTF{2217})\UTF{2217} \UTF{2248} e\UTF{2217}, e+e\UTF{2248}e, e \UTF{2205} \UTF{2248} \UTF{2205} e \UTF{2248} \UTF{2205}, e ε \UTF{2248} ε e \UTF{2248} e, \UTF{2205} + e \UTF{2248} e, ε\UTF{2217} \UTF{2248} ε, \UTF{2205}\UTF{2217} \UTF{2248} ε


* Example
To construct a DFA from the regular expression e = (0 + 1)\UTF{2217}00(0 + 1)\UTF{2217}: 

Firstly, to determine the set of states for the DFA, compute all [$∂_a$ e0] using the equivalence \UTF{2248} mentioned above, where  a ={0, 1} and e0 = {e, e1 e2, e3}, resultion in 2 * 4 patterns.
Define: 
e1 = e + 0(0 + 1)\UTF{2217}, e2 = e1 +(0+1)\UTF{2217}, e3 = e+(0+1)\UTF{2217} 

For exmple: 
$∂_0$e \UTF{2248} e+0(0+1)\UTF{2217} = e1,\\ 
$∂_1$e \UTF{2248} e,\\
$∂_0$e1 \UTF{2248}e+0(0+1)\UTF{2217} +(0+1)\UTF{2217} =e2,\\
$∂_1$e1 \UTF{2248} e\\
...

Since ε∈ L(e2) and ε∈ L(e3), F = {e2, e3}. Thus, with Q = {e, e1, e2, e3}, we can construct the DFA A_e = (Q, {0,1}, δ, e, F) using the above transitions. (States [e2] and [e3] are collapsed into a single state due to their language equivalence under ≡.

Here is the transition diagram of the DFA.


* Research on Derivatives of Regular Expressions
  * 


* Appendix 1: The Definition of Regular Language using Finite Monoids and Homomorphisms
This definition will be particularly useful for defining regular tree languages using finite algebras.


* Appendix 2: History of Regular Expressions
Key papers by McCulloch and Pitts, Kleene, and Thompson.



* References
    * Janusz A. Brzozowski. 1964. Derivatives of Regular Expressions. J. ACM 11, 4 (Oct. 1964), 481\UTF{2013}494.
    * John E. Hopcroft, Rajeev Motwani, and Jeffrey D. Ullman. *Introduction to automata theory, languages, and computation*, 2nd edition, (March 2001).
    *  Sakarovitch J. *Elements of Automata Theory*. Thomas R, trans. Cambridge University Press; 2009.
    * *Encyclopedia of Theoretical Computer Science*, 2022






