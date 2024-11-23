---
title: Chapter 12
math: true
date: "2023-12-18"
---

## Problems {#problems .unnumbered}

### 2 {#section .unnumbered}

It is $6$. For any $i \in \\{ 0,2,4,6,8 \\}$, $6i \mod 10 = i$.

### 3 {#section-1 .unnumbered}

It suffices to find a ring with a subgroup which in turn is not closed under multiplication. Particularly the ring of rationals $\mathbb{Q}$ and its subset $S = \{ \dfrac{x}{2} \mid x \in \mathbb{Z} \} = \{ x\ \dfrac{r}{2} \mid x \in \mathbb{Z}, y = 0,1 \}$. It is a subgroup as $\dfrac{x_0}{2} + \dfrac{x_1}{2} = \dfrac{x_0 + x_1}{2}$ where $x_0 + x_1 \in \mathbb{Z}$, and for $\dfrac{x_0}{2}$ there is $\dfrac{-x_0}{2}$ such that $\dfrac{x_0}{2} + \dfrac{-x_0}{2} = 0$. Observe $\dfrac{1}{2} \cdot \dfrac{1}{2} = \dfrac{1}{4} \notin S$, So $S$ is not closed under multiplication.

P.S.
-   Any subgroup under addition of a ring, satisfies the ring's definition, except for being closed under multiplication.
-   Any set $S$ closed under usual addition of integers, is also closed under usual multiplication of integers, Since $ab = \underbrace{a + a + \dots + a}_{b \text{ times}} \in S$.

### 5 {#section-2 .unnumbered}

**Unity's uniqueness.** Let $1$ and $1'$ be two unities. Then by definition $11' = 1'1 = 1'$, and $1'1 = 11' = 1$. So $1 = 1'$.

**Multiplicative inverse uniqueness.** Fix $a_0$. Let $b_0$ and $b_1$ be two multiplicative inverses of $a_0$. Then $b_0a_0 = a_0b_0 = 1$, and $b_1a_0 = a_0b_1 = 1$. So
$$
\begin{aligned}
    a_0b_0 &= a_0b_1 \\
    b_0(a_0b_0) &= b_0(a_0b_1) \\
    (b_0a_0)b_0 &= (b_0a_0)b_1 \\
    b_0 &= b_1
\end{aligned}
$$

### 6 {#section-3 .unnumbered}

**a.** For $Z_6$, $3^2 = 3$ but $3 \neq 0$ and $3 \neq 1$.

**b.** For $Z_4$, $3 \cdot 3 = 0$ but $3 \neq 0$.

**c.** For $Z_4$, $2 \cdot 1 = 2 = 2 \cdot 3$ and $2 \neq 0$ but $1 \neq 3$.

### 12 {#section-4 .unnumbered}

$(\rightarrow)$. By definition for some $k$,
$$
\begin{aligned}
    bk &= c \\
    bk \cdot 1 &= \\
    bk \cdot aa^{-1} &= \\
    ab \cdot ka^{-1} &=
\end{aligned}
$$

$(\leftarrow)$. By definition for some $k$,
$$
\begin{aligned}
    ab \cdot k &= c \\
    a \cdot bk &=
\end{aligned}
$$

### 39 {#section-5 .unnumbered}

Consider arbitrary $ar_0a, ar_1a \in S$. Then
$$
\begin{aligned}
    ar_0a \cdot ar_1a \\
    &= ar_0a^2r_1a \\
    &= ar_0r_1a \in S
\end{aligned}
$$
As $r_0r_1 \in R$. Also,
$$
\begin{aligned}
    ar_0a - ar_1a \\
    &= a [r_0a - r_1a] \\
    &= a \left [ (r_0 - r_1) a \right ] \\
    &= a(r_0 - r_1)a \in S
\end{aligned}
$$
As $r_0 - r_1 \in R$.

Since $1 \in R$, $a1a \in S$ but $a1a = a^2 = 1$.

### 40 {#section-6 .unnumbered}

(1), (2), (3), (5), (6) of a ring's definition in page 227 are satisfied by the usual properties of matrix algebra and integers.

Note the additive identity is the matrix
$$
\begin{bmatrix}
0 & 0+0 \\
0+0 & 0
\end{bmatrix}
$$

We show (4). For any matrix $M \in R$, where
$$
M = \begin{bmatrix} a & a+b \\ a+b & b \end{bmatrix}
$$
The matrix $-M$ defined as
$$ -M =  \begin{bmatrix} -a & -a+(-b) \\ -a+(-b) & -b \end{bmatrix}
$$
is in $M_2(Z)$, as $-a \in Z$ whenever $a \in Z$. Clearly $M - M$ is the additive identity.

### 46 {#section-7 .unnumbered}

$2 \in 2Z$ and $3 \in 3Z$ but $2+3 = 5 \not\in 2Z \cup 3Z$, so $2Z \cup 3Z$ is not closed under addition.
