---
title: Homework 08
math: true
date: "2024-06-01"
---

## Exercises {#exercises .unnumbered}

**Lemma 1.**

- If a graph is a subdivision of $K_{3,3}$, then it contains $3$ vertices of $deg$ $3$.
- If a graph is a subdivision of $K_5$, then it contains $5$ vertices of $deg$ $4$.

**Corollary 2.** If a graph neither has a subgraph with $3$ vertices of
$deg$ $3$, nor a subgraph with $5$ vertices of $deg$ $4$, Then it is
planar.

### 1 {#section .unnumbered}

**(1).** $K_{r,s}$ is not planar $\leftrightarrow$ $r \geq 3$ and $s \geq 3$.

$(\leftarrow).$ Clear as $K_{r,s}$ shall contain $K_{3,3}$ as a subgraph.

$(\rightarrow).$ We show the contrapositive. Given $r < 3$ or $s < 3$, The premise of *Corollary 2* is clearly satisfied, and hence $K_{r,s}$ is planar.

**(2).** $K_{r_1, r_2, \dots, r_k}$ is not planar $\leftrightarrow$ there are consecutive $r_i \geq 3$ and $r_{i+1} \geq 3$.

Similar to *(1)*.

### 2 {#section-1 .unnumbered}

**(a).**

$(\leftarrow)$ Trivial as by definition $\bigg \\{ \\{x,y\\}, \\{y,z\\} \bigg \\}$ is a subdivision of $\bigg \\{ \\{x,z\\} \bigg \\}$, resulting in graph $G$ from $H$.

**Fact 3.** For any new vertices $a$ and $b$ resulting from subdivisions, incident to existing vertices $x$ and $z$ respectively, $a \neq b$, prohibiting $\bigg \\{ \\{x,a\\}, \\{a,z\\} \bigg \\}$.

**Fact 4.** Newly added edges from subdivisions are incident to a newly added vertex and to an existing vertex.

$(\rightarrow)$. We are given $G$ is a subdivision of $H$. Call the sequence of subdivisions $S_1, S_2, \dots, S_k$, and the corresponding graphs $G_0, G_1, \dots, G_k$, whereby $G_0 = H$ and $G_k = G$.

Necessarily some $S_i$ is on edge $\\{xz\\}$. Otherwise by *Fact 3* we won't have $\bigg \\{ \\{x,y\\}, \\{y,z\\} \bigg \\}$ in $G$. Clearly a subdivision on $\\{xz\\}$ is unique, Call it $S_m$.

By *Fact 4* a newly added edge cannot be incident to two existing vertices. It follows edge $\\{ xz \\}$ is not in any $G_j$ for $j \geq m$. In particular $G_k = G$ has no edge $\\{ xz \\}$. $\blacksquare$

**(b).**

Given a graph $G_i$, If $\\{xy\\}, \\{yz\\} \in E(G_i)$ and $\\{xz\\} \notin E(G_i)$, Construct $G_{i+1} = G_i - \\{xy\\} - \\{yz\\} + \\{xz\\}$. Now given an arbitrary graph $G$ keep applying this procedure until it can no longer be applied. Since the graph has finite edges, The process terminates. So we get $G_0, G_1, \dots, G_k$ where $G_0 = G$ and $G_{i+1}$ is a subdivision of $G_i$. Set $H = G_k$. Now $H$ is not a proper subdivision of any other graph by *(a)* $\blacksquare$

**(c).**

Given a graph $H$ is not a subdivision of any other graph, and following the same line of reasoning of *(b)*, For any $\\{xy\\}, \\{yz\\} \in E(H)$, $\\{xz\\} \in E(H)$. Assuming $H$ is connected,

Case $\Delta(G) = 0$. Then $G = K_1$.

Case $\Delta(G) = 1$. Then $G = K_2$.

Case $\Delta(G) = 2$. Then $G = K_3$, As we must have a vertex of $deg$ $2$, and by hypothesis the endpoints are connected by an edge. The existince of any additional edge shall construct a vertex with $deg$ $3$.

If $H$ is not connected, Then each of its components are either $K_1$, $K_2$, or $K_3$. $\blacksquare$

### 3 {#section-2 .unnumbered}

**(a).**

\begin{aligned}
    2m &= \sum deg \, v \\\\
    &= 24 \cdot 3 \\\\
    m &= 12 \cdot 3 = 36
\end{aligned}
\begin{aligned}
    n - m + r &= 2 \\\\
    12 - 36 + r &= 2 \\\\
    r &= 26
\end{aligned}

**(b).** Assume for contradiction $\delta(G) \geq 5$. Then
$$
m = \frac{1}{2} \sum deg \, v \geq \frac{5}{2} n
$$

By *theorem 5.15*
$$
m \leq 3 (n - 2) = 3n - 6
$$

It suffices to show $3n - 6 < \frac{5}{2} n$ to obtain a contradiction. Given $n < 12$,
\begin{aligned}
    n + 5n - 12 &< 12 + 5n - 12 \\\\
    6n - 12 &< 5n \\\\
    3n - 6 &< \frac{5}{2} n \quad \blacksquare
\end{aligned}

### 4 {#section-3 .unnumbered}

Not-planar as it contains a subdivision of $K_5$.

<img src=./non-planar.jpg width=700>
