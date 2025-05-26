---
title: Homework 08
math: true
date: "2025-05-26"
---

## Section 26

### 1

**(a).** If $X$ is compact under $\Tau'$ then it is compact under $\Tau$.

Take open covering of $\Tau$. Then by hypothesis it is in $\Tau'$, and hence there is a finite covering subcollection.

**(b).** We show $\Tau' \supset \Tau$ implies $\Tau \subset \Tau'$.

Take arbitrary $U \in \Tau'$. Then $X-U$ is closed under $\Tau'$. By *theorem 26.2*, $X-U$ is compact under $\Tau'$. By *(a)*, $X-U$ is compact under $\Tau$. By *theorem 26.3*, $X-U$ is closed under $\Tau$, concluding $U$ is open under $\Tau$.

### 2 (b)

Not compact.

Consider open sets $U_k = \mathbb{R} - \{ 1/i \mid i \geq k \}$. Clearly for any $1/i$, there is a $k$ such that $U_k \ni 1/i$. Hence $\bigcup_k U_k$ covers $[0,1]$. However, if we took any finite sub-collection, then by considering the maximum index $k$ of them, we know $1/k$ is in $[0, 1]$ but not in the unions of that subcollection. $\blacksquare$

### 5

By *Lemma 26.4*, for each $y \in B$, we can take disjoint $U_y \ni y$ and $V_y \supset A$. Then $\bigcup_y U_y$ covers $B$ and by its compactness, we take finite sub-collection $U_1, \dots, U_m$. Set
$$\begin{aligned}
    U &= U_1 \cup \dots \cup U_m \\
    V &= V_1 \cap \dots \cap V_m \end{aligned}$$
Observe open $U \supset B$ and open $V \supset A$. Since $U_i \cap V_i = \phi$, it follows $U \cap V = \phi$.

### 8

$(\leftarrow)$ Take open neighbourhood $V$ of $f(x_0)$. Note if $V$ has no such point, then $f^{-1}(V) = \phi$ open in $X$. By definition $Y - V$ is closed. It follows $X \times (Y - V)$ is closed in $X \times Y$ and $G_f \cap X \times (Y-V)$ is closed. Applying *exercise 7*, the set $\{ x \mid f(x) \in Y-V \}$ is closed, implying the complement $\{ x \mid f(x) \in V \} = f^{-1}(V)$ is open.

$(\rightarrow)$ Unsolved.

## Section 27

### 3 (a)

Observe the following are open in $[0, 1]$ as a subspace.

-   $((-1, 2) - K) \cap [0, 1] = [0, 1] - K$.
-   $\forall a > 0, \;\; (a, 2) \cap [0, 1] = (a, 1]$.

Observe these sets constitute an open cover of $[0, 1]$ as a subspace. If we took any finite subcollection, then either we miss $0$ or we miss some $1/n$. $\blacksquare$

## Section 28

### 2

Consider the infinite set $A = \{ 1 - 1/n \mid n \in \mathbb{N}^* \}$. Consider any $x \in [0,1] - A$.

-   Case $x = 1$. Then $[1, 2) \cap [0, 1] = \{ 1 \}$ is open in $[0,1]$
    as a subspace, yet does not intersect $A$.
-   Case $0 < x < 1$. Then $1/n_1 < x < 1/n_0$ for a smallest $n_1$ and
    a biggest $n_0$. Take $[x, b)$ where $b < 1/n_0$, which is open in
    $[0, 1]$ as a subspace, yet does not intersect $A$.

Thereby, infinite set $A$ does not contain any limit point in $[0,1]$ as a subspace.

### 3

**(a).** Yes. Consider an infinite set $A$ in $f(X)$. for each $f(x) \in f(X)$, choose a single point $f^{-1}(x)$ in $X$, and construct set $A^{-1}$. Since $f$ is a function, $A^{-1}$ is infinite in $X$. Observe $f$ restricted to $A^{-1}$ is injective.

By hypothesis, there is a limit point $x$ in $A^{-1}$. We claim $f(x)$ is a limit point in $A$. For any neighbourhood $U \ni f(x)$, and since $f$ is continuous, $f^{-1}(U)$ is open in $X$. Hence some $x' \in A^{-1} \cap f^{-1}(U)$ where $x' \neq x$. It follows $f(x') \in A \cap U$ where $f(x') \neq f(x)$ by injectivity. $\blacksquare$

**(b).** Yes. Consider an infinite set $B \subseteq A$. By hypothesis, there is a limit point $x$ in $B$ with respect to $X$ as a space. We claim $x$ is a limit point in $B$ with respect to $A$ as a subspace. For open $U \ni x$ in $A$, we know $U = U' \cap A$ for open $U'$ in $X$. It follows some $x' \in U' \cap A$ where $x' \neq x$, implying $x' \in U$. $\blacksquare$

### 4

Partially Solved.

$(\leftarrow)$ We prove if $X$ is not countably compact, then it is not limit point compact.

By hypothesis, there is a countable cover $\{ U_n \}$, which has no finite sub-cover. Take $x_n \not\in U_1 \cup \dots \cup U_n$ for each $n$. If those $\{ x_n \}$ are finite then we can take some $x_m$ such that $x_m \not\in \bigcup_n U_n$, concluding $\{ x_n \}$ is infinite.

If $\{ x_n \}$ has a limit point $y$, then call open $U_k \ni y$ where $U_k \in \{ U_n \}$. Since $X$ is $T_1$ it follows $U_k$ contains infinitely many points of $\{ x_n \}$. But by definition $\forall n \geq k, x_n \not\in U_k$, implying $U_k$ contains finitely many points of $\{ x_n \}$.
