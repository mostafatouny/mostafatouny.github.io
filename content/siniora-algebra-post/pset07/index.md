---
title: Chapter 07
math: true
date: "2023-12-11"
---

## Problems {#problems .unnumbered}

### 1 {#section .unnumbered}

Those are $\\{ a \langle 3 \rangle \mid a\in \mathcal{Z} \\} = \big \\{ \\{ a \pm 0, a \pm 3, a \pm 6, \dots \\} \mid a \in \mathcal{Z} \big \\}$.

### 7 {#section-1 .unnumbered}

Observe $\langle a^4 \rangle = \{ 1, a^{4(1)}, a^{4(2)}, \dots, a^{4(14)} \}$. Then $\lvert \langle a^4 \rangle \rvert = 15$. It follows by *theorem 7.1* (page 142), The number of distinct left cosets is $30/15 = 2$.

### 9 {#section-2 .unnumbered}

Lazy to compute and typeset all left cosets.

$H$ is a subgroup. Then by *theorem 7.1* (page 142), the number of left cosets of $H$ in $S_4$ is $4!/4 = 3! = 6$.

### 10 {#section-3 .unnumbered}

Assume for contradiction $aH \cap bH = \phi$. Since we are given $aH = bK$, It follows $bK \cap bH = \phi$, Concluding $H \cap K = \phi$. Contradiction as the identity element $e \in G$ is common in both subgroups. Therefore $aH \cap bH \neq \phi$.

From *Lemma* (page 139), We get $aH = bH$. Then $bK = bH$ as we are given $aH = bK$. It follows $K = H$.

### 17 {#section-4 .unnumbered}

Let $H$ be a proper subgroup of $G$. If $\lvert H \rvert = 1$, Then $H = \{ e \} = \langle e \rangle$. it is cyclic. Now assume $\lvert H \rvert > 1$. Then by *theorem 7.1* (page 143), and without the loss of generality, $\lvert H \rvert = p$ for a prime $p$. By *corollary 3*, $H$ is cyclic.

### 19 {#section-5 .unnumbered}

$5^{16} \mod 7 = 6$ and $7^{13} \mod 11 = 2$, Using the fact $ab \mod m = (a \mod m) (b \mod m) \mod m$.

### 22 {#section-6 .unnumbered}

Let $H$ and $K$ be finite subgroups of a group $G$, Where $\lvert H \rvert$ and $\lvert K \rvert$ are coprime. Since $H \cap K$ is a subgroup of both $H$ and $K$, By *theorem 7.1* (page 142), $\lvert H \cap K \rvert = 1$. Then $H \cap K = \{e\}$, where $e$ is the identity of $G$.

### 38 {#section-7 .unnumbered}

### 39 {#section-8 .unnumbered}

We know all common divisors among $24$ and $20$ are $1,2,4$. By *theorem 7.1* (page 142), It follows $\lvert H \cap K \rvert = 1, 2,$ or $4$.

**Case.** $\lvert H \cap K \rvert = 1$. Then it is the trivial group of only the identity element.

**Case.** $\lvert H \cap K \rvert = 2$. Then it is $\{e, a\}$. Trivially abelian.

**Fact.** For any two elements $a,b$ of a group. If $ab = b$ then $a = e$, the identity element. Observe we can cancel $b$ in $ab = eb = b$.

**Case.** $\lvert H \cap K \rvert = 4$. Assume for contradiction, that $ab \neq ba$ for arbitrary distinct elements $a$ and $b$, Neither of which is the identity. Then $ab \not\in \{a, b\}$ by the *Fact*. Moreover $ab \neq e$ lest $b = a^{-1}$ and then $ab = ba$. Symmetrically these conclusions apply on $ba$. Since we excluded $3$ elements out of $4$, There is only a single element $ab$ and $ba$ can both be assigned to, i.e $ab = ba$. Contradiction.
