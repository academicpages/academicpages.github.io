---
title: "Markov Decision Processes"
collection: teaching
type: "Undergraduate course"
permalink: /math/markov_decision_processes
---


CHECKING IF THIS UPDATES...

Markov chains can be used to represent a discrete time stochastic transition process between states.  The probability of transition from one state to another only depends on the current state, not on previous states.  This is actually a less restrictive assumption than one might assume since one can incorporate previous history by augmenting the state space (although there would be however a pretty substantial increase in the size of the problem.)


Suppose we have an initial probability distribution over the states $\rho_0 \in \mathbb{R}^{|\mathcal{S}|}$.  A Markov chain can be represented by a column stochastic matrix $M \in [0,1]^{|\mathcal{S}|\times|\mathcal{S}|}$.  The state distribution at time $t$, $\rho_t$ can be computed by the recursive equation
$$ \rho_{t+1} = M \rho_t $$
Column stochastic means that each column of $M$ sum to $1$, $\mathbf{1}^TM = \mathbf{1}^T$ and represents probability mass conservation.  Clearly, $\mathbf{1}^T$ is a left eigenvector of $M$.   The Jordan decomposition of $M$ has the form

\\[
M = RDL  =
\begin{bmatrix} | & | & | \\\\ \bar\rho & Z  & A \\\\ | & | & | \end{bmatrix}
\begin{bmatrix} I &  &  0 \\\\  & z  &  \\\\ 0 &  & a \end{bmatrix}
\begin{bmatrix} - & \mathbf{1}^T & - \\\\ - & Z'  & - \\\\ -& A' & - \end{bmatrix}
\\]

where the columns of $R$ and rows of $L$ are right and left eigenvectors respectively.  We will explain $\bar\rho, Z,A, Z',A'$ further on.  For now note that the first left eigenvector(s) $\mathbf{1}^T$ is a row (or rows) of ones.  


Figure 1 illustrates mass evolution of a Markov chain.  Figure 2 illustrates a Markov transition matrix where show the columns of $M$ within a symplex.    Figures 3 and 4 illustrates the forward evolution of the Markov chain.  Note from Figure 3 that $\rho_{t+1}$ is always a convex combination of the columns of $M$ (since $\rho_t$ lives on the simplex).  In this case, the state distribution eventually converges to some final distribution, $\bar{\rho}$.  

[FIGURE 1] [ FIGURE 2]
[FIGURE 3] [FIGURE 4]

This final distribution is called the steady state distribution and satisfies $\bar{\rho} = M\bar{\rho}$, i.e. $\bar{\rho}$ or in other words $\bar{\rho}$ is an eigenvector of $M$ with eigenvalue $1$.   Note from Figure 3, one can see also that if all the columns of $M$ are in the interior of the symplex ($M > 0$, elementwise), then the update equation is a contraction map on the simplex and as a result (due to Brouwer's fixed point theorem), the stationary distribution is the unique fixed point of the update map.  This is known as the Perron-Frobenius theorem.  If some entries of $M$ equal 0, then $M$ may have multiple steady state distributions (the Markov chain has more than one irreducible subset) or not converge at all (the Markov chain is periodic).  

An irreducible subset of the state space is a set of states that are all fully path connected, i.e. there is a path from every state to every other within the set with positive probability.   A Markov chain with two irreducible subsets is illustrated in Figure 5 and 6 as well as the 2-dimensional continuum of steady state distributions.  Note that this continuum of steady state distributions is the convex hull of the unique steady state distribution of each irreducible subset of the Markov chain.  

[FIGURE 5] [FIGURE 6]

If the Markov chain has more than one steady state distribution, we will abuse notation and use $\bar{\rho}$ to represent a matrix whose columns span the space of steady state distributions.  The columns of $\bar{\rho}$ are the right eigenvectors corresponding to the left eigenvectors of $\mathbf{1}^T$.  

If the Markov chain is periodic, it may not converge to a steady state distribution but rather "converge" to a set of oscillating distributions.  We will represent the discrete Fourier basis vectors that span this set of oscillating distributions by the columns of a matrix $Z$.  Two examples of this situation are illustrated in Figures 7,8 and 9,10.  Note that the first Markov chain is a pure cycle and thus any initial distribution will just oscillate and not converge.  In this case, the Jordan decomposition will have the form

\\[
M = RDL  =
\begin{bmatrix} | & |  \\\\ \mathbf{1} & Z  \\\\ | & |  \end{bmatrix}
\begin{bmatrix} 1 &  0 \\\\  & z  \end{bmatrix}
\begin{bmatrix} - & \mathbf{1}^T & - \\\\ - & Z'  & - \end{bmatrix}
\\]

In other words $M$ is just a circulant matrix who eigenvalue decomposition represents a Fourier basis decomposition.  

The second Markov chain has multiple cycles but the cycles have a common period of 3 only allowing certain harmonic modes of oscillation.  The eigenvalue decomposition is then

\\[
M = RDL  =
\begin{bmatrix} | & | & | \\\\ \bar\rho & Z  & A \\\\ | & | & | \end{bmatrix}
\begin{bmatrix} I &  &  0 \\\\  & z  &  \\\\ 0 &  & a \end{bmatrix}
\begin{bmatrix} - & \mathbf{1}^T & - \\\\ - & Z'  & - \\\\ -& A' & - \end{bmatrix}
\\]
with $Z = $.  
