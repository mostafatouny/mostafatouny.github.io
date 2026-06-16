---
title: Homework 2
math: true
date: "2026-06-16"
---

# Gallian (9th ed), Ch 16

## 1

$$\begin{aligned}
  f(x) + g(x) &= (0 + 3)x^4 + (4 + 3)x^3 + (2 + 3)x^2 + (1 + 1)x + (3 + 4) \\
  &= 3x^4 + 7x^3 + 5x^2 + 2x + 7 \\
  &= 3x^4 + 2x^3 + 2x + 2 \\
  f(x) \cdot g(x) &= (4 \cdot 3) x^7 + (4 \cdot 3 + 2 \cdot 3) x^6 + (4 \cdot 3 + 2 \cdot 3 + 1 \cdot 3) x^5 + (4 \cdot 1 + 2 \cdot 3 + 1 \cdot 3 + 3 \cdot 3) x^4 \\
  &+ (4 \cdot 4 + 2 \cdot 1 + 1 \cdot 3 + 3 \cdot 3) x^3 + (2 \cdot 4 + 1 \cdot 1 + 3 \cdot 3) x^2 + (1 \cdot 4 + 3 \cdot 1) x + (3 \cdot 4) \\
  &= 12 x^7 + 18 x^6 + 19 x^5 + 22 x^4 + 30 x^3 + 18 x^2 + 7 x + 12
\end{aligned}$$

## 3

$$\begin{aligned}
  f(0) &= 0^2 + 3 \cdot 0 + 2 = 0 + 3 + 2 = 5 \\
  f(1) &= 1^2 + 3 \cdot 1 + 2 = 1 + 3 + 2 = 0 \\
  f(2) &= 2^2 + 3 \cdot 2 + 2 = 4 + 0 + 2 = 0 \\
  f(3) &= 3^2 + 3 \cdot 3 + 2 = 3 + 3 + 2 = 2 \\
  f(4) &= 4^2 + 3 \cdot 4 + 2 = 16 + 12 + 2 = 0 \\
  f(5) &= 5^2 + 3 \cdot 5 + 2 = 25 + 15 + 2 = 0
\end{aligned}$$

## 15

The multiplicative inverse is $-2x + 1$. Observe
$$(2x + 1)(-2x + 1) = -4x^2 + 2x - 2x + 1 = 0x^2 + 0 + 1 = 1$$

## 19

Take the commutative ring to be $\mathbb{Z}_4$. Observe
$$\begin{aligned}
  (2x + 1)(2x + 1) &= 4x^2 + 4x + 1 = 0 + 0 + 1 = 1 \\
  deg [ (2x+1)(2x+1) ] &= 0 < 2 = 1 + 1 = deg(2x+1) + deg(2x+1)
\end{aligned}$$

## 20

Recall $\langle x \rangle$ is the set of all polynomials of degree at
least one.

Let $A$ be an arbitrary ideal where
$\langle x \rangle \subseteq A \subseteq Q[x]$. Assume
$\langle x \rangle \neq A$. Then $A$ contains a non-zero polynomial of
degree zero. Call it $g_0(x) = c_0$. Let $f(x) = c$ be an arbitrary
constant polynomial. Then for $h_0(x) = c/c_0$, we get
$h_0g_0 = c/c_0 \cdot c_0 = c = f \in A$ since $A$ is an ideal. Hence
all constant polynomials are in $A$, concluding $B = Q[x]$.

## 27

$$6 \left ( x - \frac{1}{2} \right ) \left (x + \frac{1}{3} \right ) = 6x^2 - x - 1$$
