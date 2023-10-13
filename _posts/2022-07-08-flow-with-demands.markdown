---
title:  "A somewhat-not-short blog on flow with demands"
date:   2022-07-08 10:00:00 -0700
tags:
  - competitive programming
---

I started trying to learn about flows with demands about 3-4 years ago while in high school from [this cp-algorithm post](https://cp-algorithms.com/graph/flow_with_demands.html), but for some reason the construction presented in that blog was pretty alien and unintuitive for me, so I never really understood how it worked. As I entered college and took my algorithm class though, I was introduced to this extremely nice construction that stuck with me from that day, and it even helped me earn my first publication.

*Quick warning*: The blog will include a lot of linear program formulation of the flow problem, but I assure you that the formulation is very easy to understand :)

### The problem

You are probably familiar with the flow problem: Given a graph $$G = (V, E)$$, in which two special vertices called the source $$s$$ and the sink $$t$$ are given. Each edge $$(u, v)$$ in the graph is also given a **capacity** $$c(u, v)$$. Then, a *flow* from $$s$$ to $$t$$ is defined as a way to assign $$f(u, v)$$ to all edges $$(u, v)$$ such that:

$$
\begin{align*}
 0 \le f(u, v) &\le c(u, v) & (\forall (u, v) \in E) \\
 \sum_{(u_1, v) \in E} f(u_1, v) &= \sum_{(v, u_2) \in E} f(v, u_2) & (\forall v \in V \setminus \{s, t\}) \\
\end{align*}
$$

where the second condition is commonly referred to as *conservation of flows*: the sum of the flows entering a node $$v$$ must equal the sum of the flows exiting that same node. The *value* of a flow is just the sum of flows exiting the source $$s$$ (or entering the sink $$t$$), and the maximum flow problem asks us to maximize this value.

The *flow with demands* (or *flow with edge lower bounds*) problem simply generalizes the lower bound condition on the flow of each edge: We are now given a non-negative lower bound $$l(u, v)$$ on each edge, and now we need to find a flow that satisfies $$l(u, v) \le f(u, v) \le c(u, v)$$ for all edges.

### An extension of the flow problem: the circulation problem

I don't know if it's only me, but I find the definition of the flow problem rather ugly. What's with leaving out $$s$$ and $$t$$ in the conservation of flows constraints??

It turns out that not leaving out $$s$$ and $$t$$ leads to a different type of problem called *the circulation problem*. It turns out that we can solve a lot of flow problems by simply adding the edge $$(t, s)$$ with capacity $$c(t, s) = \infty$$ and solve the equivalent circulation problem on the modified graph; it is pretty easy to see that each flow on $$G$$ is equivalent to a circulation on the modified graph. There is also another property we can spot here: the value of the flow is actually $$f(t, s)$$!

### Circulation with node demands

Let's go even crazier with the generalization. So far the conservation of flows constraint has been pretty intuitive: flow going in = flow going out. Let's add node demands and supplies: if a node has a demand, it takes in more flow than it spits out; conversely, a node with a supply can spits out more flow than it intakes. More formally, if we let each node's demand be $$d(u)$$ (where supply is denoted as negative demand), the problem asks us to find $$f(u, v)$$ such that:

$$
\begin{align*}
 0 \le f(u, v) &\le c(u, v) & (\forall (u, v) \in E) \\
 \sum_{(u_1, v) \in E} f(u_1, v) - \sum_{(v, u_2) \in E} f(v, u_2) &= d(v) & (\forall v \in V) \\
\end{align*}
$$

To solve this problem, let's create a new graph $$G' = (V', E')$$. First, we add the same nodes and edges from $$G$$ to $$G'$$, then we create a new source $$s'$$ and a new sink $$t'$$. Finally, for each node $$u$$ with a demand, add an edge $$(u, t')$$ with capacity $$c(u, t') = d(u)$$; similarly, for each node $$u$$ with a supply, add an edge $$(s, u')$$ with capacity $$c(s, u') = -d(u)$$. Intuitively, each of these edges is there to balance out the demand/supply so that the conservation of flows on every node is preserved. Finally, we simply run the max flow algorithm on this new graph; if all edges from $$s'$$ and to $$t'$$ are saturated, this means all supplies and demands are satisfied, which means the resulting max flow can be mapped to a feasible circulation.

### Solving flow with edge lower bounds

Now, we finally tackle our original problem. From the original flow with edge lower bounds problem, we add an edge from $$t$$ to $$s$$ with capacity $$c(t, s) = \infty$$ and lower bound $$l(t, s) = 0$$ to obtain a circulation with edge lower bounds problem.

Let's analyze the local structure of each node: it has some incoming edges and outcoming edges, each with its own lower bound $$l(u, v)$$ and capacity $$c(u, v)$$. Instead of thinking of $$l(u, v)$$'s as lower bounds, let's think of them as the "forced" flow that must go through each edge, and the actual "capacity" is actually just $$c(u, v) - l(u, v)$$. Additionally, since $$l(u, v)$$'s are "forced", the conservation of flows on the node may not be true, but we already have the tool to solve this: we just say that the demand of node $$v$$ as the amount of flow $$v$$ must "intake" to satisfy the conservation of flows, i.e. $$d(v) = \sum_{(u_1, v) \in E} l(u_1, v) - \sum_{(v, u_2) \in E} l(v, u_2)$$.

To recap:
- From a flow with edge lower bounds problem, add edge $$(t, s)$$ with $$c(t, s) = \infty$$ and $$l(t, s) = 0$$ to obtain a circulation with edge lower bounds problem.
- From a circulation with edge lower bounds problem, for each edge $$(u, v)$$, let its new capacity $$c'(u, v)$$ be $$c(u, v) - l(u, v)$$; additionally, for each node $$v$$, let its demand be $$d(v) = \sum_{(u_1, v) \in E} l(u_1, v) - \sum_{(v, u_2) \in E} l(v, u_2)$$. We then obtain a circulation with node demands problem.
- Create two new sources $$s'$$ and $$t'$$, and connect each node to either $$s'$$ or $$t'$$ with the capacity being $$\|d(u)\|$$. We can now solve the ciruclation with node demands problem by running max flow on this new graph.

### Some generalizations

Let's tackle some more generalizations. The construction so far only allows us to find the existence of any flow with the correct lower bounds. What if we want to find, say, the max flow (or min flow) among all feasible answers?

Notice our previous observation: the flow $$f(t, s)$$ on the back edge from sink to source is the value of our flow. We have been blindly assigning this edge's lower bound and capacity to be $$0$$ and $$\infty$$, but we can indeed change these values to reflect our goal. For example, if we want to find the min flow among all feasible answers, we can binary search the capacity of this back edge; similarly, if we want to find the max flow among all feasible answers, we can binary search the lower bound of this back edge.

Finally, it is indeed possible to solve the min-cost circulation with node demands problem with our construction, and it turns out that there are also [solvers](https://developers.google.com/optimization/flow/mincostflow) to do this quickly (I am not pretending to understand the algorithm behind this solver, but I do know that it comes from [this book](https://www.amazon.com/Network-Flows-Theory-Algorithms-Applications/dp/013617549X) and it has a time complexity of $$O(n^2 \cdot m \cdot \log(n \max c))$$.
