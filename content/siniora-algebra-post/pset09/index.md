---
title: Chapter 09
math: true
date: "2023-12-18"
---

## Problems {#problems .unnumbered}

### 1 {#section .unnumbered}

We use *Theorem 9.1* (page 175) to show the answer is NO. $(2 3) \in S_3$ and yet, $(2 3)H(2 3) = \{ (2 3)(1)(2 3), (2 3)(1 2)(2 3) \} = \{ (1), (1 3)\} \not\subset H$.

### 2 {#section-1 .unnumbered}

We use *Theorem 9.1* (page 174). We know from earlier chapters, $A_n$ is a subgroup of $S_n$. Then for any $x \in S_n$ and any $h \in A_n$, we get a permutation $xhx^{1}$ consisting of even 2-cycles. To see why, Observe we know $x^{-1}$ has the same number of 2-cycles as $x$. Whether $x$ consists of even or odd number of 2-cycles, The contribution of 2-cycles of both $x$ and $x^{-1}$ is even.

### 6 {#section-2 .unnumbered}

NO. It suffices to take some matrix $h \in H$ and a matrix $x \in GL(2,R)$, and show $xhx^{-1} \not\in H$. Clearly:

$$
\begin{bmatrix} 2 & 1 \\\\ 1 & 2  \end{bmatrix} \begin{bmatrix} 1 & 1 \\\\ 0 & 1 \end{bmatrix} \begin{bmatrix} 2 & 1 \\\\ 1  & 2  \end{bmatrix}^{-1} \\\\ = \begin{bmatrix} 2 & 1 \\\\ 1 & 2 \end{bmatrix} \begin{bmatrix} 1 & 1 \\\\ 0 & 1 \end{bmatrix} \begin{bmatrix} 2/3 & -1/3 \\\\ -1/3  & 2/3 \end{bmatrix} = \begin{bmatrix} 4/3 & -1 \\\\ -1/3  & 2 \end{bmatrix} \not\in H
$$

### 8 {#section-3 .unnumbered}

We immediately prove the general case of $\langle k \rangle / \langle n \rangle \cong \mathcal{Z}_{n/k}$, given $k$ divides $n$.

For arbitrary two elements of under the operation:
\begin{aligned}
    (k^a \langle n \rangle) (k^b \langle n \rangle)
        &= k^{a+b} \langle n \rangle \qquad &\text{Definition} \\\\
        &= k^{\frac{n}{k} q + r} \langle n \rangle, 0 \leq r < n/k \qquad &\text{Euclidean Division} \\\\
        &= k^{\frac{n}{k} q} k^r \langle n \rangle \\\\
        &= k^r (k^{\frac{n}{k} q} \langle n \rangle) \qquad &\text{Commutativity and Associativity of $\mathcal{Z}$} \\\\
        &= k^r (n \langle n \rangle) \\\\
        &= k^r \langle n \rangle
\end{aligned}

But in $\mathcal{Z}_{n/k}$, $ab = a + b \mod \frac{n}{k}$, which corresponds to $(k^a \langle n \rangle) (k^b \langle n \rangle) = k^{a + b \mod r} \langle n \rangle$.

### 9 {#section-4 .unnumbered}

**Fact.** Citing from the course TA, Ibrahim, left/right cosets parition
the group $G$. (msh naseek ya bob).

Since the index is given to be $2$, We know $G/H = \{ H, g_0 H \} = \{ H, Hg_0\}$.

Consider arbitrary $x \in G$. If $x \in H$ then $xH = H = Hx$ from *Lemma* (page 139). If $x \not\in H$, Then $x \in g_0H$ and $x \in Hg_0$ by our *Fact*. It follows $g_0h_0 = x = h_1g_0$ for some $h_0, h_1 \in H$, and in turn $xH = g_0H = Hg_0 = Hx$.

It follows $H$ is normal.

### 10 {#section-5 .unnumbered}

**(a).**

By *Theorem 9.1* (page 175), We construct $xhx^{-1} \not\in H$ for some $x \in A_4$ and $h \in H$.

Let $h = (1 2)(3 4)$ and $x = (1 3)(2 3)$. Then $x^{-1} = (2 3)(1 3)$, and in turn $xhx^{-1} = (1 3)(2 3)(1 2)(3 4)(2 3)(1 3)$. In other notation, 

$$
xhx^{-1} = \begin{bmatrix} 1 & 2 & 3 & 4 \\\\ 3 & 4 & 1 & 2 \end{bmatrix} \neq (1 2)(3 4)
$$

### 12 {#section-6 .unnumbered}

For arbitrary abelian group $G$ with elements $a_0$ and $a_1$, and factor group $G/H$, We have:
\begin{aligned}
  (a_0 H)(a_1 H) &= (a_0 a_1) H \qquad &\text{Definition} \\\\
                 &= (a_1 a_0) H \qquad &\text{$G$ is Abelian} \\\\
                 &= (a_1 H)(a_0 H)
\end{aligned}

### 14 {#section-7 .unnumbered}

We know the identity of $\mathcal{Z}_{24}/ \langle 8 \rangle$ is $0 + \langle 8 \rangle$. We are looking for smallest $k$ satisfying 
\begin{aligned}
    (14 + \langle 8 \rangle)^k &= 0 + \langle 8 \rangle \\\\
    14^k + \langle 8 \rangle &=
\end{aligned}
Thanks for the course TA, Ibrahim, That can be satisfied while $14^k \neq 0$.

From the *lemma* (page 139), This is true if and only if $14^k \in \langle 8 \rangle$. In other words, We want smallest positive $k$, such that $14^k = 8^m$ for some integer $m$. By computation, $k = 3$ as $14^3 = 8$.

### 22 {#section-8 .unnumbered}

Observe $(Z \oplus Z) / \langle (2,2) \rangle = \\{ (0,0)+\langle (2,2) \rangle, (0,1)+\langle (2,2) \rangle), (1,0)+\langle (2,2) \rangle, (1,1)+\langle (2,2) \rangle \\}$.

To see why consider arbitrary $(a,b) \in Z \oplus Z$ and apply Euclid's
division theorem to get $a = 2k_0 + r_0$ and $b = 2k_1 +r_1$ where
$0 \leq r_0,r_1 < 2$.

Then the order is $4$.

It is not cyclic as no single $(a,b)$ can generate all of $(0,0), (0,1), (1,0), (1,1)$.

### 37 {#section-9 .unnumbered}

Recall the notation of $|g|$ as the order of element $g$. By definition $g^{|g|} = 0$. Then $(gH)^{|g|} = g^{|g|}H = H$. By *Corollary 2* (page 77), $|gH|$ divides $|g|$.
