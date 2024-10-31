---
title: Chapter 06
math: true
date: "2023-12-01"
---

## Problems {#problems .unnumbered}

### 1 {#section .unnumbered}

$\phi(n) = 2n$. If $2a = 2b$ then $a = b$. For each $2k$ we have $\phi(k) = 2k$. Observe $\phi(ab) = 2(a+b) = 2a + 2b = \phi(a)\phi(b)$, Following by usual properties of integers.

### 2 {#section-1 .unnumbered}

We Follow the same proof approach of *Example 15* (page 130). Let $\phi \in Aut(Z)$ be arbitrary. Then by the usual properties of integers and isomorphisms, $\phi(k) = \phi(1 + 1 + \dots + 1) = \phi(1) + \dots + \phi(1) = k \cdot \phi(1)$. But by definition $\phi(1) = c$ for some integer $c$. Therefore $\phi(k) = kc$. In other words, $Aut(Z) = \{ \phi \mid \exists c, \; \forall k \; \phi(k) = kc \}$

### 4 {#section-2 .unnumbered}

Caylay table of $U(8)$:
|   |  1  |  3  |  5 | 7 |
|---|----|----|----|---|
| 1 | 1 | 3 | 5 | 7 | 
| 3 | 3 | 1 | 7 | 5 |
| 5 | 5 | 7 | 1 | 3 |
| 7 | 7 | 5 | 3 | 1 |

Caylay table of $U(10)$:
|   | 1 | 3 | 7 | 9 |
|---|----|----|----|---|
| 1 | 1  | 3 | 7  | 9 |
| 3 | 3  | 9 | 1 | 7 |
| 7 | 7  | 1 | 9 | 3 |
| 9 | 9  | 7 | 3 | 1 |

Recall from *theorem 6.2* (page 126), Any $\phi$ maps the identity to the identity of the other group.

In $U(8)$ we have $3 \cdot 3 = 1$. Then $\phi(3 \cdot 3) = \phi(3) \cdot \phi(3) = \phi(1) = 1$. The only non-identity element in $U(10)$ satisfying that is $9$. Hence $\phi(3) = 9$.

Similarly $5 \cdot 5 = 1$. Then we must have some $a \in U(10)$ such that $a \cdot a = 1$ where $a \notin \{ 1, 9 \}$. Contradiction.

### 8 {#section-3 .unnumbered}

*Injective.* Given $\log_{10} a = \log_{10} b$, we get $10^{\log_{10} a} = 10^{\log_{10} b}$, and $a = b$.

*Surjective.* Given $x \in \mathcal{R}$, take $a = 10^x \in \mathcal{R}^+$. Then $\log_{10} a = \log_{10} 10^x = x$.

*Group Operation.* Observe $\phi(ab) = \log_{10} ab = \log_{10} a + \log_{10} b = \phi(a) + \phi(b)$.

### 11 {#section-4 .unnumbered}

Observe $\phi(a^3 b^{-2}) = \phi(a^3) + \phi(b^{-2}) = [\phi(a)]^3 + [\phi(b)]^{-2} = (\overline{a})^3 + (\overline{b})^{-2}$. We used *theorem 6.2* (2).

### 12 {#section-5 .unnumbered}

$(\rightarrow)$. For any $a,b \in G$, We have:
\begin{aligned}
    \alpha(a^{-1}b^{-1})  &= \alpha(a^{-1}) \alpha(b^{-1}) \\\\
     (a^{-1} b^{-1})^{-1} &= \\\\
                      ba  &= ab
\end{aligned}

$(\leftarrow)$. Symmetrically, If we have $b^{-1} a^{-1} = a^{-1} b^{-1}$, Then $\alpha(ab) = \alpha(a) \alpha(b)$. Bijection is clear by properties of inverses.

### 14 {#section-6 .unnumbered}

By *theorem 6.5* (page 131), $Aut(Z_3) \approx U(3)$ and $Aut(Z_4) \approx U(4)$, so $Aut(Z_3) \approx Aut(Z_4)$ by the *transitivity* of isomorphism. But $Z_3 \not\approx Z_4$ as the two groups have different orders, so no bijection exists.

### 21 {#section-7 .unnumbered}

Clearly groups $H$ and $K$ are isomorphic to $S_4$. By transitivity $H \approx K$.

### 22 {#section-8 .unnumbered}

For every $c = 2, 3, 4 \dots$, Consider the subset $H_c = \{ ck \mid k \in \mathcal{Z} \}$. It is a subgroup, As it has the identity $c(0)$, inverses $c(-k)$, and closed $ck_1 + ck_2 = c(k_1 + k_2)$.

It remains to show those subgroups are distinct. For any $c_1$ and $c_2$ where $c_1 < c_2$ we have $c_1(1) \in H_{c_1}$ but $c_1(1) \not\in H_{c_2}$. Therefore $H_{c_1} \neq H_{c_2}$.

### 24 {#section-9 .unnumbered}

We use *theorem 3.2* (page 63). If $\phi(a) = a$ then $\phi(a^{-1}) = (\phi(a))^{-1} = a^{-1}$. Also, If $\phi(a) = a$ and $\phi(b) = b$ then $\phi(ab) = \phi(a) \phi(b) = ab$.

### 34 {#section-10 .unnumbered}

Let $K$ be a subgroup of $G$. We use *theorem 3.2* (page 63).

**Inverse.** For any $\phi(k) \in \phi(K)$, $(\phi(k))^{-1} = \phi(k^{-1})$. But $k^{-1} \in K$, So $\phi(k^{-1}) \in \phi(K)$.

**Closed.** For $\phi(k_1), \phi(k_2) \in \phi(K)$, We have $\phi(k_1) \phi(k_2) = \phi(k_1 k_2)$. But $k_1 k_2 \in K$, So $\phi(k_1 k_2) \in \phi(K)$.
