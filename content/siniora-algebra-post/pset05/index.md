---
title: Chapter 05
math: true
date: "2023-11-18"
---


## Problems {#problems .unnumbered}

### 1 {#section .unnumbered}

**a**
$$
\alpha^{-1} =
\begin{bmatrix}
    1 & 2 & 3 & 4 & 5 & 6 \\\\
    2 & 1 & 3 & 5 & 4 & 6
\end{bmatrix}
$$

**b**
$$
\beta \alpha = 
\begin{bmatrix}
    1 & 2 & 3 & 4 & 5 & 6 \\\\
    1 & 6 & 2 & 3 & 4 & 5
\end{bmatrix}
$$

**c** 
$$
\alpha \beta = 
\begin{bmatrix}
    1 & 2 & 3 & 4 & 5 & 6 \\\\
    6 & 2 & 1 & 5 & 3 & 4
\end{bmatrix}
$$

### 3(b) {#b .unnumbered}

**b.** $(1 2 4)(3 5)(6)$

### 6(a) {#a .unnumbered}

**a.** disjoint cycles form: $(1 2)(3 5 6)$. Order is $6$.

### 8(c,d) {#cd .unnumbered}

**c.** $(1 7)(1 6)(1 5)(1 3)$.

**d.** $(2 4)(2 3)(1 5)$.

### 10 {#section-1 .unnumbered}

We want to find some permutation
$$
\begin{bmatrix}
    1 & 2 & 3 & 4 & 5 & 6 \\\\
      &   &   &   &   &  
\end{bmatrix}
$$

where:
- Order is $15$, i.e $lcm$ of disjoint cycles lengths is $15$, and
- Even, i.e Has an even number of 2-cycles.

Observe $15 = 3 \cdot 5$ which suggests two disjoint cycles of lengths $3$ and $5$. A standard candidate is $(1 2 3)(4 5 6 7 8)$. Its 2-cycles form: $(4 8)(4 7)(4 6)(4 5)(1 3)(1 2)$, A total of even 6 cycles.

The permutation in matrix form is:
$$
\begin{bmatrix}
    1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 \\\\
    2 & 3 & 1 & 5 & 6 & 7 & 8 & 4
\end{bmatrix}
$$


### 17 {#section-2 .unnumbered}

Using *theorem 3.3* (page 64), It suffices to show the set of even permutations are closed under permutation composition. By definition, Given even permutations $\alpha = (a b)(c d) \dots (e f)$ and $\beta = (g h)(i j) \dots (k l)$, The composition $\alpha \beta = (a b) \dots (k l)$ consists of even number of 2-cycles, As even + even = even.


### 23 {#section-3 .unnumbered}

Let $H$ be a subgroup of $S_n$. Assume not every member is even. We show $H$ must have an equal number of even and odd members.

We follow the same proof approach of *theorem 5.7* (page 104). We know there is an odd member $\alpha$. For every odd $\beta$, $\alpha \beta$ is even, So there as many evens as there are odds. For every even $\beta$, $\alpha \beta$ is odd, So there are as many odds as there are evens. Therefore, the number of even and odd members are equal.


### 25 {#section-4 .unnumbered}

The identity permutation is even. Not closed as the composition of two
odd members is even.


### 43 {#section-5 .unnumbered}

For $n \geq 3$, It is easy to see $(1 2) \in S_n$ and $(2 3) \in S_n$. However

$$
(2 3)(1 2) = 
\begin{bmatrix}
    1 & 2 & 3 & 4 & 5 & \dots \\\\
    3 & 1 & 2 & 4 & 5 & \dots
\end{bmatrix}
\neq
\begin{bmatrix}
    1 & 2 & 3 & 4 & 5 & \dots \\\\
    2 & 3 & 1 & 4 & 5 & \dots
\end{bmatrix}
= (1 2)(2 3)
$$
