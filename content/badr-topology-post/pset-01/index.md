---
title: Homework 01
math: true
date: "2025-05-26"
---

## Exercises

### 1

For every $x \in A$, we know there exists an open $U_x$ such that $x \in U_x \subset A$. Observe $A = \cup_{x \in A} U_x$ is expressed as unions of open sets. By *axiom 2*, $A$ is open. $\blacksquare$

### 3

**Lemma.** $\mathcal{T}_c$ is a topology.

As $X - \phi = X$ and $X - X = \phi$, we get $\phi, X \in \mathcal{T}$.

For a collection of open sets $U = \bigcup\limits_{x \in I} U_x$:

-   Case. $U_{x} = \phi$ for all $x \in I$. Then clearly $U = \phi$ is open.

-   Case. $U_{x_0} \neq \phi$ for some $x_0 \in I$. Then $X - U = X - \bigcup\limits_{x \in I} = \bigcap\limits_{x \in I} (X - U_x) \subset X - U_{x_0}$. It follows $X - U$ is countable as it is a subset of a countable set.

For open $U_0$ and $U_1$, if either is empty then $U_0 \cap U_1 = \phi$ is open. If both $X - U_0$ and $X - U_1$ are countable then so is $(X - U_0) \cup (X - U_1) = X - (U_0 \cap U_1)$.

**Lemma.** $\mathcal{T}_\infty$ is not a topology in general.

We show that by a counter-example. Let $X = \mathcal{R}$, $U_0 = R - \{ 0, 2, 4, \dots \}$, and $U_1 = R - \{ 0, 1, 3, \dots \}$. Clearly $R - U_0$ and $R - U_1$ are both infinite but $R - (U_0 \cup U_1) = R - (R - \{0\}) = \{0\}$ is non-empty finite, and hence not open.

### 4

**a.**

$\bigcap \mathcal{T}_\alpha$ is a topology by lifting every property common along all $T_\alpha$ to $\bigcap \mathcal{T}_\alpha$.

$\bigcup \mathcal{T}_\alpha$ is not a topology in general. Consider $X = \{ a, b \}$, $\mathcal{T}_a = \{ \phi, \{a\}, X \}$, and $\mathcal{T}_b = \{ \phi, \{b\}, X \}$. Observe $\mathcal{T}_a \cup \mathcal{T}_b = \{ \phi, \{a\}, \{b\}, X \}$ but
$\{a\} \cup \{b\} = \{ a, b \} \not\in \mathcal{T}_a \cup \mathcal{T}_b$.

**b.**

**Lemma.** Unique smallest.

Let $F$ be the family of all topologies containing $\{ \mathcal{T}_\alpha \}$. $F$ is non-empty as the discrete topology $\mathcal{T}_{\text{disc}}$ is finer than any topology on $X$. By *(a)*, $\bigcap F$ is a topology. By minimality in set theory, it is smallest and unique.

**Lemma.** Unique greatest.

Observe $\mathcal{T} = \bigcap_\alpha \mathcal{T}_\alpha$ is a topology by *(a)*. It is largest as any open set $U$ common in all topologies will be in $\mathcal{T}$. For any largest such topology $\mathcal{T}'$, by definition $\mathcal{T}' \subset \bigcap_\alpha \mathcal{T}_\alpha$ and $|\mathcal{T}'| \geq \mathcal{T}$, implying $\mathcal{T}' = \mathcal{T}$.

**c.**

Smallest is $\{ \phi, X, \{a\}, \{a,b\}, \{b,c\}, \{b\} \}$, and largest is $\{ \phi, X, \{a\} \}$.

### 6

**Lemma.** $\mathcal{R}_l$ is not finer than $\mathcal{R}_k$.

Consider $0 \in B = (-1, 1) - K$ for $\mathcal{T}''$ in $\mathcal{R}_k$. In $\mathcal{R}_l$, for any $[y,x)$ where $y \leq 0 < x$, there is a small enough $1/n$, concluding $[y,x) \not\subseteq B$.

**Lemma.** $\mathcal{R}_k$ is not finer than $\mathcal{R}_l$.

Consider $0 \in [0, 1)$ in $\mathcal{R}_l$. For any $(x',y')$ containing $0$, it follows $x' < 0 < y'$, and hence $(x',y') \not\subseteq [0,1)$.

### 7

$\mathcal{T}_1$ contains $\mathcal{T}_4$.

$\mathcal{T}_2$ contains $\mathcal{T}_1$.

$\mathcal{T}_5$ contains $\mathcal{T}_1$, $\mathcal{T}_2$, and $\mathcal{T}_4$.

### 8

**a.**

Since $\mathcal{Q} \subseteq \mathcal{R}$, it follows $\mathcal{B} \subseteq \mathcal{T}$. Take arbitrary open $(a,b)$ with $x$ contained in it. By density of rationals, there are $q,p \in \mathcal{Q}$ such that $a < q < x < p < b$. Hence
$x \in (q,p) \subseteq (a,b)$.

**b.**

Since a basis generates a unique topology, if $\mathcal{T} = \mathcal{T}'$ then $\mathcal{T}$ and $\mathcal{T}'$ have common bases (plural of basis). It suffices to show $\mathcal{C}$ is not a basis of the *lower limit topology*.

We show the generated topology $\mathcal{T}$ by $\mathcal{C}$ is missing an element in $\mathcal{R}_l$. Take irrational $a_0 \in [a_0, b_0) \in \mathcal{R}_l$. For any basis element $B = [q,p) \in \mathcal{C}$, either $q > a_0$ or $q < a_0$. For the former, $a_0 \not\in B$. For the latter $B \not\subseteq [a_0, b_0)$. Hence $[a_0, b_0) \not\in \mathcal{T}$.
