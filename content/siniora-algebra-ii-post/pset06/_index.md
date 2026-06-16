---
title: Homework 6
math: true
date: "2026-06-16"
---

# Gallian (9th ed), Chapter 20

## 2

Using degree of extension argument.

The irreducible polynomial over $p(x) = x^2 - 2$ over $\mathbb{Q}$
concludes $[\mathbb{Q}(\sqrt{2}) : \mathbb{Q}] = 2$. The irreducible
polynomial $p(x) = x^2 - 3$ over $\mathbb{Q}(\sqrt{2})$ concludes
$[\mathbb{Q}(\sqrt{2})(\sqrt{3}) : \mathbb{Q}(\sqrt{2})] = 2$. Hence
$[\mathbb{Q}(\sqrt{2}, \sqrt{3}): \mathbb{Q}] = 2 \cdot 2 = 4$.

The irreducible polynomial $x^4 - 10x^2 + 1$ over $\mathbb{Q}$ has
$\sqrt{2} + \sqrt{3}$ as a root, concluding
$[\mathbb{Q}(\sqrt{2} + \sqrt{3}) : \mathbb{Q}] = 4$.

Clearly
$\mathbb{Q}(\sqrt{2} + \sqrt{3}) \subseteq \mathbb{Q}(\sqrt{2}, \sqrt{3})$.
Thus $$\begin{aligned}
  [\mathbb{Q}(\sqrt{2} + \sqrt{3}) : \mathbb{Q}] &= [\mathbb{Q}(\sqrt{2} + \sqrt{3}) : \mathbb{Q}(\sqrt{2}, \sqrt{3})] \cdot [\mathbb{Q}(\sqrt{2}, \sqrt{3}) : \mathbb{Q}] \\
  4 &= [\mathbb{Q}(\sqrt{2} + \sqrt{3}) : \mathbb{Q}(\sqrt{2}, \sqrt{3})] \cdot 4
\end{aligned}$$ Thereby
$[\mathbb{Q}(\sqrt{2} + \sqrt{3}) : \mathbb{Q}(\sqrt{2}, \sqrt{3})] = 1$,
concluding
$\mathbb{Q}(\sqrt{2} + \sqrt{3}) = \mathbb{Q}(\sqrt{2}, \sqrt{3})$.

# Gallian (9th ed), Chapter 21

## 3

Observe
$[\mathbb{Q}(\sqrt{2}, \dots, \sqrt[k]{2}) : \mathbb{Q}(\sqrt{2}, \dots, \sqrt[k-1]{2})] = k$
by the polynomial $x^k - 2$. It shows the extension is algebraic; the
unique monic minimal polynomial of $\sqrt[k]{2}$, concluding the degree
is $k$.

Following Anas' advise, $\mathbb{Q}(\sqrt{2}, \sqrt[3]{2}, \dots)$ could
be interpreted as $\bigcup_k \mathbb{Q}(\sqrt{2}, \dots, \sqrt[k]{2})$.
Since every set is an algebraic extension of $\mathbb{Q}$, trivially so
is the union.

Assume for contradiction the extension is finite. Then there is an
$m$-sized basis for $\mathbb{Q}(\sqrt{2}, \sqrt[3]{2}, \dots)$ over
$\mathbb{Q}$. Clearly we can find some $k_0$ such that
$\mathbb{Q}(\sqrt{2}, \dots, \sqrt[k_0]{2})$ contains the basis
elements, and has a dimension greater than $m$ over $\mathbb{Q}$; but we
have an $m$-sized spanning set for it. Contradiction.

## 26

**Partially Solved.**

It is necessarily and sufficent to have
$1 < [F(a)(b) : F(a)] < [F(b) : F]$, since
$[F(a,b) : F] = [F(a)(b) : F(a)] \cdot [F(a) : F]$.

Observe $[\mathbb{Q}(\sqrt{2}) : \mathbb{Q}] = 2$,
$[\mathbb{Q}(\sqrt[4]{2}) : \mathbb{Q}] = 4$, but
$[\mathbb{Q}(\sqrt{2})(\sqrt[4]{2}) : \mathbb{Q}(\sqrt{2})] = 2$ by
$x^2 - \sqrt{2}$ over $\mathbb{Q}(\sqrt{2})$.

However, that violates a required condition, where
$\mathbb{Q}(\sqrt[4]{2}, \sqrt{2}) = \mathbb{Q}(\sqrt[4]{2})$ since
$\mathbb{Q}(\sqrt[4]{2}) \ni \sqrt{2}$.

## 27

## 47

We show the contrapositive. Assume $a^m$ is algebraic over $F$. Then
there is a polynomial $p$ such that $p(a^m) = 0$ over $F$. Construct
polynomial $p'$ where powers are shifted by $m$, i.e $c(x)^k$ is
replaced by $c(x)^{mk}$. Observe $c(a^m)^k = ca^{mk} = c(a)^{mk}$.
Thereby $p'(a) = p(a^m) = 0$, concluding $a$ is algebraic over $F$.
