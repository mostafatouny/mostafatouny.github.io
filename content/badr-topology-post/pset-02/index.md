---
title: Homework 02
math: true
date: "2025-05-26"
---

# Exercises

## 1

It follows by the following observation from set theory: if $A \subseteq Y \subseteq X$, then $U \cap A = U \cap Y \cap A$ for $U \subseteq X$.

For an arbitrary $U \cap A \in \mathcal{T}_{A \subseteq Y}$ where $U \in \mathcal{T}_{Y \subseteq X}$, observe $U \cap A = U' \cap Y \cap A = U' \cap A \in \mathcal{T}_{A \subseteq X}$, where $U' \in \mathcal{T}_X$.

For an arbitrary $U' \cap A \in \mathcal{T}_{A \subseteq X}$ where $U' \in \mathcal{T}_X$, observe $U' \cap A = U' \cap Y \cap A = U \cap A \in \mathcal{T}_{A \subseteq Y}$, where $U \in \mathcal{T}_{Y \subseteq X}$.

## 2

$\mathcal{T}_Y'$ is finer than $\mathcal{T}_Y$, as for a given $Y \cap U$ with $U \in \mathcal{T}$, by hypothesis $U \in \mathcal{T}'$ as well.

In general, $\mathcal{T}_Y'$ is not strictly finer. As an example, consider the standard topology of $\mathcal{R}$ as $\mathcal{T}$ with the standard basis, and finer K-topology as $\mathcal{T}'$. If $Y = [2,3]$, then observe $K = \{ 1/n \mid n \in Z_+ \} \cap Y = \phi$. It follows $\large ( (a,b) - K \large ) \cap Y = (a,b) \cap Y$.

## 3

$A$ is open in $\mathcal{T}_\mathcal{R}$ and $\mathcal{T}_Y$ as $A = (1/2, 1) \cup (-1, -1/2)$, a union of two basis elements of $\mathcal{T}_Y$.

$B$ is not open in $\mathcal{T}_\mathcal{R}$ similarly to homework 1. It is open in $\mathcal{T}_Y$ as $[-1, 1] \cap (1/2, 2) = (1/2, 1]$ and $[-1, 1] \cap [-2,-1/2) = [-1, -1/2)$ are basis elements of $\mathcal{T}_Y$.

$C$ is not open in $\mathcal{T}_\mathcal{R}$ similarly to homework 1. It is not open in $\mathcal{T}_Y$ as for any $(a,b)$ containing $1/2$, it follows $[-1, 1] \cup (a, b)$ has a real number strictly greater than $1/2$.

$D$ is not open in both $\mathcal{T}_\mathcal{R}$ and $\mathcal{T}_Y$ similarly.

Observe $1/x \in Z_+$ iff $x = 1/n$ for $n \in Z_+$. For any $x \in E$, we can find the first $n$, such that $1/n < x < 1/(n-1)$. Therefore there is an open set $(a,b) \subseteq E$ which contains $x$. Moreover $(a,b) \subseteq [-1,1]$. It follows $E$ is open in both $\mathcal{T}_\mathcal{R}$ and $\mathcal{T}_Y$.

## 4

Follows trivially. If $U \times V \in X \times Y$, then $U$ and $V$ are open in $X$ and $Y$, respectively. Thereby, $\pi_1(U \times V) = U$ is open.

## 5

**(a).** Take arbitrary $U \times V \in X \times Y$. Then $U \in \mathcal{T}$ and $V \in \mathcal{U}$. But by hypothesis $U \in \mathcal{T}'$ and $V \in \mathcal{U}'$. In other words, $U \times V \in X' \times Y'$.

**(b).** No, as an open set may not be a subset of $Y$. A counter-example on the topological space $\mathcal{R}$ is

-   $\mathcal{T} = \mathcal{T}' = (0,1) \; \cap$ {standard topology on $\mathcal{R}$}
-   $X = X' = Y = Y' = (0,1)$
-   $\mathcal{U}' = (0,2) \; \cap$ {standard topology on $\mathcal{R}$}
-   $\mathcal{U} = (0,1) \; \cap$ {standard topology on $\mathcal{R}$}

## 6

By the density of rationals in reals, we know $\{ (a,b) \mid a<b \wedge a,b \in \mathcal{Q} \}$ is a basis of $\mathcal{R}$. By *theorem 15.1*, the result follows.

## 8

**Unsolved**
