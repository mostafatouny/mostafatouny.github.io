---
title: Chapter 14
math: true
date: "2023-12-18"
---

## Problems {#problems .unnumbered}

### 1 {#section .unnumbered}

We use *Theorem 14.1* (ideal test) (page 249).

For $r_0 a, r_1 a \in \langle a \rangle$, We have $r_0 a - r_1 a = (r_0 - r_1) a \in \langle a \rangle$ by distributivity and $r_0 - r_1 \in R$.

For $r \in R$ and $r_0 a \in \langle a \rangle$, We have $r(r_0 a) = (rr_0)a \in \langle a \rangle$ by associativity and $r r_0 \in R$. Also $(r_0 a)r = r_0(ar) = r_0(ra) = (r_0 r) a$ by associativity and commutativity and $r_0 r \in R$.

### 3 {#section-1 .unnumbered}

The proof $I$ is ideal by *Theorem 14.1* (ideal test) (page 249) is nearly identical to *Ex. 1*.

Let $J$ be an arbitrary ideal that contains $a_1,a_2, \dots, a_n$. Then by definition $r a_i \in J$. Since it's a group $r_1 a_1 + \dots + r_n a_n \in J$ for any $r_i \in R$.

### 4 {#section-2 .unnumbered}

By the *subring test* (page 230), $S = \\{ (x,x) \mid x \in Z \\}$ is a subring as $(x,x) - (y,y) = (x-y, x-y) \in S$ and $(x,x) (y,y) = (xy,xy) \in S$.

$S$ is not an ideal as $(1,1) \in S$ and $(1,2) \in \mathbb{Z} \oplus \mathbb{Z}$ but $(1,2) (1,1) = (1,2) \notin S$. In other words, $(1,1)$ did not absorb $(1,2)$.

### 5 {#section-3 .unnumbered}

We use *Theorem 12.3* (subring test) (page 230). $(a+bi) - (a'+b'i) = (a-a') + (b-b')i \in S$ as $b-b'$ is even. $(a+bi) (a'+b'i) = (aa' - bb') + (ab' + a'b)i \in S$ as $ab' + a'b$ is even.

$1 + 2i \in S$ and $1 + 1i \in Z[i]$ but $(1 + 1i)(1 + 2i) = -1 + 3i \not\in S$ as $3$ is not even. A counter-example of $S$ being an ideal.

### 11 {#section-4 .unnumbered}

#### a {#a .unnumbered}

$\langle a \rangle = \langle 1 \rangle = \mathbb{Z}$. We know $GCD(2,3) = 1$ so by *Theorem 0.2* (GCD is a linear combination) (page), there are $x, y \in \mathbb{Z}$ such that $2x + 3y = 1$. So for any integer $m$, $2(xm) + 3(ym) = m$. In other words, $\mathbb{Z} = \langle 1 \rangle \subset \langle 2 \rangle + \langle 3 \rangle$.

#### b {#b .unnumbered}

$\langle a \rangle = \langle 2 \rangle$. Trivially $\langle 6 \rangle + \langle 8 \rangle \subset \langle 2 \rangle$ as $2$ is a common divisor of $6$ and $8$. Observe $8(1) + 6(-1) = 2$. So for any multiple $2m$, We have $8(m) + 6(-m) = 2m$, concluding $\langle 2 \rangle \subset \langle 8 \rangle + \langle 6 \rangle$.

### 15 {#section-5 .unnumbered}

By definition $A \subset R$ and $r = r1 \in A$ for any $r \in R$.

### 32 {#section-6 .unnumbered}

Let $B$ be an arbitrary ideal of $\mathbb{Z} \oplus \mathbb{Z}$ such that $A \subset B \subset \mathbb{Z} \oplus \mathbb{Z}$. Assume $B$ properly contains $A$ then we show $B = \mathbb{Z} \oplus \mathbb{Z}$.

By hypothesis we have $(a,b) \in B$ but not in $A$. So $a = 3q + r$ whereby either $r = 1$ or $r = 2$. Consider each case:
- $r = 1$. Since $A \subset B$, $( 3(-q), -(b-1)) \in B$. As $B$ is a group, $(3(-q), -(b-1)) + (3q+1, b) = (1,1) \in B$.
- $r = 2$. Similarly $(3(q+1), b+1) \in B$ and $(3(q+1), b+1) - (3q+2, b) = (1, 1) \in B$.

By *Ex. 15* $B = \mathbb{Z} \oplus \mathbb{Z}$.

Had $A$ been $\\{ (4x, y) \mid x,y \in \mathbb{Z} \\}$ then the property of it being a maximal ideal fails as the ideal $\\{ (2x, y) \\}$ is strictly larger.

Generally, $\\{ (rx,y) \\}$ is a maximal ideal if and only if $r$ is a prime. If $r$ is composite then any divisor generates a larger ideal. If $r$ is prime then for any $m$ where $0 < m < r$, $gcd(r, m) = 1$. It follows by *Theorem 0.2* (GCD is a linear combination) (page 4) there is a linear combination $xr + ym = 1$.

### 37 {#section-7 .unnumbered}

If $(x,y), (a,b) \in \mathbb{Z} \oplus \mathbb{Z}$ and $(x,y)(a,b) = (xa,yb) \in I$ then by definition $yb = 0$. So either $y = 0$ or $b = 0$. In other words, either $(x,y) \in I$ or $(a,b) \in I$.

The set $\\{ (x,2y) \mid x,y \in Z \\}$ is an ideal and properly contains $I$. So $I$ is not maximal.
