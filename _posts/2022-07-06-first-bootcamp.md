---
title: 'Complex Bootcamp Exercises: Basics of Holomorphic Functions'
date: 2022-07-06
permalink: /posts/2022/07/bootcamp-2022-ex-1/
tags:
  - bootcamp
  - complex analysis
---

Resources
------
Ahlfors chapter 2 and section 3.2.2

Problems
======

Problem 1
------
Suppose $f$ is an entire function satisfying that $f(z) = f(z + t\xi)$ for some nonzero constant $\xi \in \mathbb{C}$ and all $t\in \mathbb{R}$. Show that $f$ is constant. 
<details>
	<summary>Hint</summary>
	Suppose that $\xi = 1$ and compute $\partial f/\partial x$. Use the Cauchy-Riemann equations to reach the desired conclusion. 
</details>

Problem 2 (Ahlfors 2.1.4.4)
------
What is the general form of a rational function $R$ satisfying $|R(z)| = 1 $ for all $ |z| = 1 $? How are the zeros and poles of $R$ related to one another?
<details>
	<summary>Hint</summary>
	We know that \(z = 1/\overline{z}\) when \(|z| = 1\) so \( \overline{R(z)} = \overline{R(1/\overline{z})}\) on \(|z| = 1\).
	Can you establish what relationship \(R(z)\) and \(\overline{R(1/\overline{z})}\) have when $|z| \ne 1$?
</details>



Problem 3 (Ahlfors 2.1.4.5)
------
What is the general form of a rational function $R$ satisfying $R(z) \in \mathbb{R}$ for all $|z| = 1$? How are the zeros and poles of $R$ related to one another?
<details>
	<summary>Hint</summary>
	As in the last problem, we can deduce a relationship between \(R\) and \(\overline{R(1/\overline{z})}\) now using the additional fact that \(\overline{R(z)} = R(z)\). 
</details>

Problem 4 (Ahlfors 2.2.4.2)
------
Write \[ \frac{2z+3}{z+1} \] as a power series in terms of $z-1$. Find the radius of convergence for this series. 
<details>
	<summary>Hint</summary>
	Algebraically manipulate the expression so you can use the geometric series formula $$ \frac{1}{1-r} = \sum_{n=0}^\infty r^n $$ where \(r\) is an expression containing $z-1$. 
</details>

Problem 5 (Ahlfors 3.2.2.2)
------
Give a precise definition of a branch of the function $\log \log(z)$. 


Problem 6 (Ahlfors 3.2.2.3)
------
Suppose $f$ is a holomorphic function satisfying $|f(z)^2 - 1| < 1$ for all $z \in \Omega$ a connected open subset of $\mathbb{C}$. Prove that either $\text{Re}(f(z)) > 0$ or $\text{Re}(f(z)) < 0$ for all $z\in \Omega$. 
<details>
	<summary>Hint</summary>
	Consider the branches of $\sqrt{z}$ that you can define on the ball of radius 1 centered at 1. 
	What can you deduce about the set of points $w$ satisfying $|w^2 - 1| < 1$?
</details>

Problem 7 (Prelim January 2014)
------
Let $f: U \to \mathbb{C}$ be a holomorphic function satisfying $f(iz) = f(z)$ for all $z \in U$. 
Define $V = \\{z: z^4 \in U\\}$ and prove that there exists a holomorphic function $g:V \to \mathbb{C}$ such that $f(z) = g(z^4)$. 
<details>
	<summary>Hint</summary>
	Intuitively this is solved if we can let $g(z) = f(\sqrt[4]{z})$, but this is ill-defined unless we work with branches of $\sqrt[4]{z}$. 
	Define two separate branch cuts of $\sqrt[4]{z}$ to find different canidates of $g(z)$ defined on different domains. Show that you can extend them to the union of their domains <br>


	Additionally, you may find that this process only defines $g:V\setminus\{0\} \to \mathbb{C}$ due to all branch cuts excluding zero. 
	Recall that such a function can be extended analytically to 0 if $\lim_{z\to 0} zg(z) = 0$ (removable singularities; Ahlfors 4.3.1.) 
</details>
