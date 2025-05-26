---
title: Homework 07
math: true
date: "2025-05-26"
---

# Section 30

## 2

## 3

Denote the countable basis by $\mathcal{B}$.

For a non-limit point $x \in A$, by definition there is an open $U \ni x: U \cap (A - \{x\}) = \phi$. Moreover, there is a basis element $B: x \in B \subset U$.

For a non-limit point $x' \neq x$, similarly we get a $B': x' \in B' \subset U'$. It follows $B \neq B'$. So distinct non-limit points of $A$ do induce distinct basis elements of the countable $\mathcal{B}$. Thereby, countably-many points in $A$ are non-limit points of $A$, implying uncountably-many points in $A$, are limit points of $A$.

## 5a

Call the dense subset $S$. Construct $\mathcal{B} = \bigcup_{x \in S} \{ B(x, 1/n) \mid n \in \mathbb{N}^* \}$. It is countable since the countable union of countable sets is countable. We claim $\mathcal{B}$ is a basis.

Take arbitrary $x \in X$ with $B(x, \epsilon)$. We know there is $n_0$ where $\dfrac{1}{n_0} \leq \epsilon$. By density there is $s_0 \in S$ where $d(x, s_0) < \dfrac{1}{4n_0}$. Note $B ( s_0, \dfrac{1}{2n_0} )$ contains $x$. It is also contained in $B(x, \epsilon)$ since by triangular inequality, any element in it is at distance from $x$, at most $\dfrac{1}{4n_0} + \dfrac{1}{2n_0} = \dfrac{3}{4n_0} < \dfrac{1}{n_0} \leq \epsilon$.

## 12

**Second-countable**

Assume $X$ is second-countable. Let the countable basis of $X$ to be $\mathcal{B}$. Construct countable $\mathcal{B}' = \{ f(B) \mid B \in \mathcal{B} \}$. We claim $\mathcal{B}'$ is a basis.

Consider any open $U' \ni f(x)$ in $f(X)$. By hypothesis, $f^{-1}(U') \ni x$ is open in $X$. Then there is a basis element $B$ whereby $x \in B \subset f^{-1}(U')$. It follows $f(x) \in f(B) \subset U'$ where $f(B)$ is open by hypothesis.

**First-countable**

If $X$ is first-countable, then for any $f(x) \in f(X)$, we know $x \in X$ by hypothesis has a countable collection $\mathcal{B}$ where any open neighbourhood $U$ of $x$ contains some $B \in \mathcal{B}$. The set $\{ f(B) \mid B \in \mathcal{B} \}$ is a countable basis at $f(x)$. The proof is similar.

# Section 31

## 1

Take points $x \neq y$. Since a regular space is also Hausdorff, there are open $U \ni x$ and $U' \ni y$ such that $U \cap U' = \phi$. By *lemma 31.1*, there are open $V \ni x$ and $V' \ni y$ such that $\overline{V} \subset U$ and $\overline{V}' \subset U'$. It follows $\overline{V} \cap \overline{V}' = \phi$. $\blacksquare$

## 4

If $\Tau$ is Hausdorff, then trivially so is $\Tau'$.

## 5

It suffices to prove all limit points of $\{ x \mid f(x) = g(x) \}$ are contained in it. Assume towards contradiction there is a limiting point $x'$ such that $f(x') \neq g(x')$. By hypothesis there are disjoint open $V \ni f(x')$ and $V' \ni g(x')$. Consider open neighbourhood $U = f^{-1}(V) \cap g^{-1}(V')$ of $x'$ in $X$ and observe any $z \in U$ satisifes $f(z) \neq g(z)$ as otherwise $f(z) \in V \cap V'$. That $U$ violates $x'$ being a limit point. Contradiction. $\blacksquare$
