---
title: Homework 11
math: true
date: "2024-06-01"
---

## Exercises {#exercises .unnumbered}

### 1 {#section .unnumbered}

We know a maximum matching $M$ and a minimum covering $C$ do both exist, where $|M| = |C|$.

Observe by definition all edges $E(G)$ are exactly the edges incident to cover $C$. Clearly each edge distinctly contributes to the degrees sum. It follows $\sum_{v \in C} deg \ v \geq |E(G)|$.

Hence
$$
\Delta (G) \ |M| = \Delta (G) \ |C| = \sum_{v \in C} \Delta (G) \geq \sum_{v \in C} deg \ v \geq |E(G)|
$$

### 2 {#section-1 .unnumbered}

We reduce the problem to *theorem 7.15* and show for any $I \subset \\{1, 2, \dots, r\\}$, $|I| \leq |\bigcup_i S_i|$.

Take a subset $I = \\{ \pi_1, \pi_2, \dots, \pi_m \\} \subset \\{1, 2, \dots, r\\}$ where $0 \leq m \leq r$. If $m = 0$ then trivially $|I| = 0 = |\phi| = |\bigcup_i S_i|$. Consider $m \geq 1$. Since cardinalities of $S_{\pi_i}$ are all positive and distinct, By the *Pigeon Hole Principle*, $m$ subsets cannot be assigned cardinalities between $1$ and $m-1$. Therefore there exists a subset $S$ with $|S| \geq m$. It follows $|\bigcup_i S_{\pi_i}| \geq |S| \geq m = |I|$.

### 4 {#section-2 .unnumbered}

Claim. $R(a,b) \leq R(b,a)$

We know there is a $K_{R(b,a)}$ such that any edge 2-coloring either has a red $K_b$ or a green $K_a$ as subgraphs.

But if it has a red $K_b$, then trivially it has a green $k_b$, and if it has a green $K_a$, then trivially it has a red $K_a$.

Then there is a $K_{R(b,a)}$ such that any edge 2-coloring either has a red $K_a$ or a green $K_b$. Hence, $R(a,b) \leq R(b,a)$.

By symmetry $R(b,a) \leq R(a,b)$, Concluding $R(a,b) = R(b,a)$. $\blacksquare$

### 5 {#section-3 .unnumbered}

Claim. $R(3,3) > 5$.

The following edge colouring of $K_5$ neither has a red $K_3$ nor a green $K_3$.

<img src=./k5.jpg width=300>

Observe taking any 3 vertices, 2 of them will be adjacent by a red edge, and 2 of them will be adjacent by a green edge.

Claim. $R(3,3) \leq 6$.

Fix vertex $v_0$, and consider any edge colouring. Since $deg \ v_0 = 5$, Necessarily $3$ of which are of the same colour. WLOG assume the colour is *green*. Call those $3$ vertices $x_1, x_2, x_3$. As in the following figure we have two cases:

<img src=./k3-in-k6.jpg width=700>

Either $x_1, x_2, x_3$ form a red $K_3$, or some edge of them is green, for example edge $\\{x_1, x_3\\}$. Therefore, Either the graph contains a *red* $K_3$ or a *green* $K_3$. $\blacksquare$
