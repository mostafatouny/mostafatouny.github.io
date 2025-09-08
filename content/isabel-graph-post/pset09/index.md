---
title: Homework 09
math: true
date: "2024-06-01"
---

## Exercises {#exercises .unnumbered}

### 1 {#section .unnumbered}

Any $C_n$ with vertices $\\{ v_1, v_2, \dots, v_n \\}$ is *3-colorable* by $k = \\{ 1, 2, 3, 1, 2, 3, 1, \dots \\}$.

Any $C_n$, where $n$ is even, is *2-colorable* by $k = \\{ 1, 2, 1, 2, 1, \dots \\}$. Observe $k(v_i) = 1$ if $i$ is odd and $k(v_i) = 2$ if $i$ is even. Particularly $k(v_1) \neq k(v_n)$.

### 2 {#section-1 .unnumbered}

**Fact 1.** Colouring a graph is equivalent to partitioning it into independent subsets.

**Fact 2.** Since a colouring exists of any graph, It follows there exist independent subsets $P_i$ of $V(G)$ such that $\bigcup P_i = V(G)$, and $P_i \cap P_j = \phi$ for $i \neq j$.

**Fact 3.** $|P_i| \leq \alpha(G)$.

**(a).**

Given a graph, Colour it with $\chi(G)$ colours. By *Fact 1* there exists equivalent independent subsets $P_1, P_2, \dots, P_{\chi(G)}$. By *Fact 3* $$|G| = \sum_{i=1}^{\chi(G)} |P_i| \leq \sum_{i=1}^{\chi(G)} \alpha(G) = \chi(G) \cdot \alpha(G) \quad \blacksquare$$

**(b).**

Given a graph $G$ of order $n$, label its vertices by $v_1, v_2, \dots, v_{\alpha(G)}, v_{\alpha(G)+1}, \dots, v_n$.

We know the greedy algorithm constructs a valid colouring for $G$. So the number of colours will be at least $\chi{G}$.

By independency, $v_1, v_2, \dots, v_{\alpha(G)}$ counts one colour. It follows $v_{\alpha(G) + 1}, \dots, v_n$ contains at least $\chi_{G} - 1$ vertices to fulfill remaining colours. Therefore
$$
|G| = n \geq \alpha(G) + \chi(G) - 1
$$

### 3 {#section-2 .unnumbered}

**Fact 4.** For a possibly disconnected graph $G$, $\Delta(G) = \max \\{ \Delta(G_i) \mid G_i \text{ is a component in } G \\}$, and $\chi(G) = \max \\{ \chi(G_i) \mid G_i \text{ is a component in } G \\}$.

The condition is that the graph $G$ contains a component $G_i = C_n$ or $G_i = K_n$ whereby $\Delta(G_i) = \Delta(G)$.

**Sufficient.**

*Case 1.* If the graph contains a component $K_n$ where $\Delta(K_n) = \Delta(G)$, Then $\chi(G) = \chi(K_n)$. To see why, Assume for the sake of contradiction $\chi(G_i) > \chi(K_n)$ for some component $G_i$, Then
$$
\chi(G_i) > \chi(K_n) = \Delta(K_n) + 1 = \Delta(G) + 1 \geq \Delta(G_i) + 1
$$

*Case 2.* If the graph contains a component $C_n$ for odd $n$ where $2 = \Delta(C_n) = \Delta(G)$ then also $3 = \chi(C_n) = \chi(G)$. To see why, Symmetrically to *Case 1*, Assuming $\chi(G_i) > \chi(C_n)$ for any component $G_i$ yields $\chi(G_i) > \Delta(G_i) + 1$.

Now for both *Case 1* and *Case 2*, By *Brooke* we know the bound is sharp for component $K_n$ and $C_n$. That implies it is sharp for the whole graph also. For example $\chi(K_n) = \Delta(K_n) + 1$ implies $\chi(G) = \Delta(G) + 1$.

**Necessary.**

We show the contrapositive. Assume for any component $G_i$, If $\Delta(G_i) = \Delta(G)$ then neither $G_i = K_n$ nor $G_i = C_n$. By *Brooke*
$$
\chi(G_i) < \Delta(G_i) + 1 = \Delta(G) + 1 \quad (1)
$$
For components $G_j$ where $\Delta(G_j) < \Delta(G)$, We get
$$
\chi(G_j) \leq \Delta(G_j) + 1 < \Delta(G) + 1 \quad (2) \\
$$
From $(1)$ and $(2)$, It follows $\chi(G) < \Delta(G) + 1$, i.e the bound is not sharp. $\blacksquare$

### 4 {#section-3 .unnumbered}

We reduce the problem to graph colouring as follows:

-   Vertices of the graph are the committees.
-   Two distinct committees $C_i$ and $C_j$ are connected if and only if some member is in both of them.
-   Number of meetings is the number of colours.

The resulting graph is

<img src=./committee.jpg width=600>

So 3 meetings are needed.
