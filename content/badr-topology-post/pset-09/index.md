---
title: Homework 09
math: true
date: "2025-05-26"
---

## Section 23

### 1

Assume $X$ is connected with respects to $\Tau'$. Clearly, if there is a separation in $\Tau$, so would it exist in $\Tau'$. Thereby $X$ is connected with respects to $\Tau$.

On the other hand, $X$ is connected in $\Tau = \{ \phi, X \}$, but for other topologies $\Tau'$, it may not be connected.

### 4

We use the fact $X$ is connected iff the only open subsets are $\phi$ and $X$.

Let $U$ be both open and closed. Then either $X-U$ finite or $U = \phi$ (1). Moreover, $X-U$ is open. Then either $X - (X - U) = U$ is finite or $U = X$ (2).

Assume towards contradiction $U$ is neither $\phi$ nor $X$. Then by (1) and (2), we get both $X-U$ and $U$ are finite, implying $X$ is finite. Contradiction.

### 5

If we took subspace $B = \phi$, which is not a one-point set, then it is trivially connected.

We show for any subspace $B$ where $|B| \geq 2$, it is not connected. Take $b_1 \in B$, and set $C = \{ b_1 \}$ and $D = B - C$. Clearly both are non-empty open sets in $B$ as a subspace, hence constitute a separation.

The converse holds if $X$ is finite. For fixed $x \in X$, we have open $U_y$ containing $x$ but not $y$ for every $y \in X - \{x\}$. Finite intersection $\bigcap_y U_y = \{ x \}$ is open. Since all singletons are open, $X$ has the discrete topology, by taking arbitrary unions.

I guess the converse does not hold in general.

### 8

Not connected. We extend example 6 in Munkres but for the uniform topology. Recall in any metric, including the uniform metric, $\epsilon$-balls for $\epsilon < 1$ are open. Take $A$ to be the set of bounded sequences and $B$ the set of unbounded sequences. They are disjoint. For any $x \in A$, we have an open ball $B(x,1) \subset A$. Similarly for any $x \in B$.

## Section 24

### 3

### 8

### 11
