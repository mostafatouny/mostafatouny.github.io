---
title: Chapter 13
math: true
date: "2023-12-18"
---

## Problems {#problems .unnumbered}

### 3 {#section .unnumbered}

Let $R$ be a commutative ring with the cancellation property. Assume for contradiction $a$ is a zero-divisor. Then $a \neq 0$ and there's $b \neq 0$ such that $ab = 0$. By *theorem 12.1* (page 229) It follows:
$$
\begin{aligned}
    ab - ab &= 0 \\
    a(b-b) &= 0 \\
           &= 0 \cdot 0 \\
           &= 0 \cdot (b-b) \\
    a      &= 0
\end{aligned}
$$
Contradiction.

#### 4 {#section-1 .unnumbered}

Zero-divisors are $2, 4, 6, 8, 10, 12, 14, 15, 16, 18, 5, 15$. To see why assume $ab \mod 20 \equiv 0 \mod 20$. Then $ab - 0 = ab = 20k$ for some $k$. $a$ must contain a common factor with $20$, as otherwise $b \geq 20$. So zero-divisors are multiples of a factor of $20$.

Unities are $1, 3, 7, 9, 11, 13, 17, 19$. No proof is found.

Zero-divisors and unities partition $\mathbb{Z}_{20}$.

### 9 {#section-2 .unnumbered}

We call $a \in Z \oplus Z \oplus Z$ *strictZero* if some component of $a$ is $0$ like $(x, y, 0)$ but $a \neq (0,0,0)$.

Clearly $a$ is a zero-divisor if and only if $a$ is a *strictZero*.

For $a,b,c \in Z \oplus Z \oplus Z$, if $ab, ac, bc$ are zero-divisors then they are *strictZeros*. If $abc$ is not a zero-divisor then it is not a *strictZero*, in other words either $abc = (0,0,0)$, or $abc = (x, y, z)$ where $x,y,z \neq 0$. The latter case cannot happen as $ab$ is a a *strictZero* so some component must be zero in $abc$. Therefore $abc = (0,0,0)$.

Since $Z$ has no zero-divisor, it follows each component is zero in one of $a,b,c$. In other words, The $a,b,c$ we are characterizing, are *strictZeros*, such that no component is non-zero in the three of them.

### 18 {#section-3 .unnumbered}

Let $R$ be an integral domain and $a^2 = a$. Then
$$
\begin{aligned}
    a^2 - a &= 0 \\
    a(a-1) &= 0
\end{aligned}
$$
Since there are no zero-divisors, either $a = 0$ or $a - 1 = 0$.


#### 32 {#section-4 .unnumbered}

We know $R$ is a group. By usual properties of addition and multiplication, It is a commutative ring.

$6$ is unity as
$$
\begin{aligned}
    6 \cdot 0 = 0 \\
    6 \cdot 2 = 2 \\
    6 \cdot 4 = 4 \\
    6 \cdot 6 = 6 \\
    6 \cdot 8 = 8
\end{aligned}
$$

Each non-zero element has a unit as
$$
\begin{aligned}
    2 \cdot 8 = 6 \\
    4 \cdot 4 = 6 \\
    6 \cdot 6 = 6 \\
    8 \cdot 2 = 6
\end{aligned}
$$

#### 57 {#section-5 .unnumbered}

Observe by distributivity of rings $x^2 -5x + 6 = (x-3)(x-2)$.

#### a {#a .unnumbered}

By the *corollary* (page 239) $\mathbb{Z}_7$ is a field, and hence has no zero-divisors. It follows either $x-3 = 0$ or $x-2 = 0$ so $x = 3$ or $x = 2$. Exactly two solutions.

#### b {#b .unnumbered}

By computation $2$ and $3$ are the solutions.

Note nothing certifies $\mathbb{Z}_8$ is an integral domain.
