---
title: Homework 04
math: true
date: "2024-06-01"
---

## Exercises {#exercises .unnumbered}

### 1 {#section .unnumbered}

The least path we can construct between $x$ and $y$ is $(x)$ in the case
of $x = y$. So $d(x,y) \geq 0$.

if $x = y$, then $(x)$ is a valid path, concluding $d(x,y) = 0$. If
$d(x,y) = 0$ then the graph contains a path $(x) = (y)$, concluding
$x = y$.

Since the graph is undirected, It is clear $(v, v_1, \dots, v_k)$ is the
least $vv_k$ path if and only if $(v_k, v_{k-1}, \dots, v)$ is the least
$v_kv$ path. It follows $d(x,y) = d(y,x)$.

The paths $(x, \dots, y)$ and $(y, \dots, z)$ can be concatenated to
construct a new path $(x, \dots, z)$ whose length is $d(x,y) + d(y,z)$.
If we considered the minimal-length $xz$ path, Then by definition we get
$d(x,z) \leq d(x,y) + d(y,z)$. $\blacksquare$.

### 2 {#section-1 .unnumbered}

**(i)**

By definition $ecc(v) = diam(G)$. So $d(u,v) = diam(G)$. It follows
$ecc(u) = diam(G)$ as there is no longer path than the diameter.

**(ii)**

Fix $u$ and $v$. Let $u_m$ and $v_m$ be the vertices corresponding to
maximum paths for $u$ and $v$ respectively.

Assume for contradiction the difference between $d(u,u_m)$ and
$d(v,v_m)$ is greater than 1. WLOG assume $d(u,u_m)$ is the greater.
Then there is a path $(u, \dots u_m)$ whose length is greater than
$d(v,v_m)$.

**(iii)**

### 3 {#section-2 .unnumbered}

**(i)**

*Fact.* $A^k(i,j)$ is the number of $v_iv_j$ paths of length $k$.

By definition $d(v_i,v_j)$ is the least length of any path. In other
words, least $k$ where $A^k(i,j) > 0$.

**(ii)**

Consider $\min \{ k \mid S^k \text{ has some rows with no zeros} \}$.
Those rows correspond to vertices $C(G)$.

Consider $\min \{ k \mid S^k \text{ has no zeros} \}$. Rows with zeros
in $S^{k-1}$ correspond to vertices $P(G)$.

### 4 {#section-3 .unnumbered}

**(i)**

**Fact.** A connected tree of order $n$ has exactly $n-1$ edges.

Let $n_i$ denote the order of $i$th connected tree. Then by the *Fact*
$i$th tree has $n_i - 1$ edges. It follows the total number of edges of
the forest is $\sum_{i=1}^k (n_i - 1) = n - k$.

**(ii)**

If some edge is not a bridge then a cycle shall exist, contradicting the
fact a tree is acyclic.
