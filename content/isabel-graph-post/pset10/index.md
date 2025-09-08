---
title: Homework 10
math: true
date: "2024-06-01"
---

## Exercises {#exercises .unnumbered}

### 1 {#section .unnumbered}

We prove by strong induction the statement: For any $m \geq 0$, If $G$ is a graph with $m$ edges and $n$ vertices, Then
-   $P_G(k) = a_0 + a_1 k^1 + \dots + a_n k^n$, For some polynomial representation.
-   $a_0 = 0$
-   $a_n = 1$

Base case. $m = 0$. Then $G = E_n$, the empty graph with $n$ vertices. By combinatorics we know $P_G(k) = k^n = 0 + (1) k^n$.

Induction hypothesis. Assume the statement holds for any graph with at most $m$ edges for $m \geq 0$.

Induction step. For a graph $G$ with $m+1$ edges and $n$ vertices, Note $G$ has some edge $e$ and the graphs $G-e$ and $G/e$ have at most $m$ edges. By *Birkhoff* and the *induction hypothesis*,
\begin{aligned}
    P_G(k) &= P_{G-e}(k) - P_{G/e}(k) \\\\
    &= (0 + a_1 k^1 + \dots + (1) k^n) - (0 + a_1' k^1 + \dots + (1) k^{n-1}) \\\\
    &= 0 + (a_1 - a_1') k^1 + \dots + (a_{n-1} - 1) k^{n-1} + (1) k^n \quad \blacksquare
\end{aligned}

### 2 {#section-1 .unnumbered}

**(i).** For a maximum matching $M$, if adding an additional edge results in a valid matching, then $M$ won't be maximum. Hence it is maximal.

**(ii).** For a perfect matching $M$ let $k = |M|$. If there were a matching with more than $k$ edges, then that matching shall cover more than $2k$ vertices. That implies the graph contains more than $2k$ vertices, and as a result $M$ does not cover all graph's vertices, so not perfect.

**(iii).** Consider the set $AM = \\{ M \mid M \text{ is a matching of } G \\}$. Since a matching $M$ is a subgraph, and there are finitely many subgraphs, it follows $AM$ is finite. Moreover it has a maximum edge size matching.

**(iv).** Call the perfect matching $M_0$ and let $k_0 = |M_0|$. By definition it covers all vertices of the graph, and in turn $G$ has exactly $2k_0$ vertices, Concluding $|G|$ is even.

It suffices to prove, If an arbitrary matching $M$ is not perfect, Then it is not maximum. By definition $M$ covers less than $2k_0$ vertices. Then $M$ has less than $k_0$ edges, So $|M| < |M_0|$. Since $M_0$ is a valid matching, It follows $M$ is not maximum. $\blacksquare$

### 3 {#section-2 .unnumbered}

**(1).** This is exactly the definition of matching $X$ into $Y$.

**(2).** We reduce it to *Hall's Marriage*. Let $X = \\{ S_i \mid i \in I \\}$ and $Y = \bigcup_{i \in I} S_i$. Now the problem of *system of distinct representatives* is equivalent to matching hall of $X$ into $Y$. In other words, Matching childs injectively to gifts is equivalent to matching $S_i$ to representatives. By *Hall's Marriage Theorem*, This is possible if and only if $|X| \leq |N(X)|$. However, $|X| = |I|$ and $N(X) = Y$. Therefore *system of distinct representatives* is possible *iff* $|I| \leq |\bigcup_{i \in I} S_i|$.
