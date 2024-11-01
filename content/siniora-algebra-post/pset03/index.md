---
title: Chapter 03
math: true
date: "2023-11-16"
---

## Problems {#problems .unnumbered}

### 2 {#section .unnumbered}

$(Q, +)$. $\{ \frac{\displaystyle{x}}{\displaystyle{2}} \mid x \in \mathcal{Z} \}$.

$(Q^*, *)$. $\{ 2^x \mid x \in \mathcal{Z}^+ \} \cup \{ \frac{\displaystyle{1}}{\displaystyle{2^x}} \mid x \in \mathcal{Z}^+ \} \cup \{ 1 \}$.

### 4 {#section-1 .unnumbered}

Consider $|x| = n$. Then $x^n = 1$ and no positive $r < n$ where $x^r = 1$. It follows.
$$
\begin{aligned}
    (x^n)^{-1} &= (1)^{-1} \\
    (x \cdot x \cdot \dots \cdot x)^{-1} &= 1 \\
    x^{-1} \cdot \dots \cdot x^{-1} &= \\
    (x^{-1})^n &=
\end{aligned}
$$
Analogously if $(x^{-1})^r = 1$ then $x^r = 1$. That cannot happen for $r < n$.

### 6(b) {#b .unnumbered}

Identity is $e = 0$.

$|3| = 4$. $|8| = 3$. $|11| = 12$.

### 7 {#section-2 .unnumbered}

**Fact.** For any element $x$ in any group, $x^{n+m} = x^n x^m$.

**Fact.** For any element $x$ in any group, $(x^{k})^m = x^{km}$.
$$
\begin{aligned}
    (a^4 c^{-2} b^4)^{-1} &= (b^4)^{-1} (c^{-2})^{-1} (a^4)^{-1} \\
                          &= (b^4)^{-1} (c^2 ) (a^4)^{-1} \\
                          &= (b^7 b^{-3})^{-1} (c^2) (a^6 a^{-2})^{-1} \\
                          &= (b^{-3})^{-1} (c^2) (a^{-2})^{-1} \\
                          &= b^3 c^2 a^2
\end{aligned}
$$

### 10 {#section-3 .unnumbered}

We naively construct all possible subgroups, pruning possible branches by their properties.

Any subgroup must have the identity element. $\{R_0\}$. (+1)

${R_0, X}$ is a subgroup for any reflection $X = H,V,D,D'$. (+4)

Considering a subgroup with ${R_0, X_0, X_1}$ for distinct reflections $X_0, X_1$ it must be the case we get rotation $R_s$ for $s \neq 0$. So we cannot have a subgroup restricted on reflections other than the aforementioned case.

$\{ R_0, R_{180} \}$. (+1)

For any subgroup with $R_{90}$ or $R_{270}$, since it is closed it must contain also $\{ R_0, R_{90}, R_{180}, R_{270} \}$. (+1)

For any subgroup containing $\{ R_0, R_{180}, H \}$ it must contain also $\{ R_0, R_{180}, H, V \}$. For any subgroup containing $\{ R_0, R_{180}, V \}$ it must contain also $\{ R_0, R_{180}, V, H \}$.
(+1)

For any subgroup containing $\{ R_0, R_{180}, D \}$ it must contain also $\{ R_0,    R_{180}, D, D' \}$. For any subgroup containing $\{ R_0, R_{180}, D' \}$ it must contain also $\{ R_0, R_{180}, D, D' \}$. (+1)

For any subgroup containing $R_s$ for $s \neq 180$ and any reflection $X = H, V, D, D'$, since it is closed, it must contain also $\{ R_0, R_{90}, R_{180}, R_{270}, H, V, D, D'\}$. (+1)

So far we counted 10 subgroups.

### 19 {#section-4 .unnumbered}

We show the contrapositive. Assume $a^m = a^n$ for $m > n$. Then $a^m a^{-n} = a^n a^{-n}$ implying $a^{m-n} = e$, but $m - n > 0$ so $a$ is of a finite order.

### 30 {#section-5 .unnumbered}

The question presumes the uniqueness of $H$. We won't prove it.

$H = \{ 2 (9 k_1 + 15 k_2 + 20 k_3) \mid k_1,k_2,k_3 \in \mathcal{Z} \}$.

Taking $k_1 = k_2 = k_3 = 0$ yields the identity $e = 0$. For $x \in H$ corresponding to $k_i$, Take $-(k_i)$ to obtain the inverse. Closed property is clear from the definition. Associativity follows from $G$. Odd numbers are excluded conforming to the fact $H$ is a proper subgroup.

### 34 {#section-6 .unnumbered}

Since $e \in H$ and $e \in K$ by definition, We have $e \in H$.

if $x,y,z \in H \cap K$, then $x,y,z \in H$ and associativity follows.

if $x \in H \cap K$, then $-x \in H$ and $-x \in K$, and any element has an inverse.

if $x,y \in H \cap K$, then $x + y \in H$ and $x + y \in K$ by properties of a group.

A trivial argument by induction shows the intersection of any number of subgroups.
