---
title: Homework 1
math: true
date: "2026-06-16"
---

$\newcommand{\nfrac}[2]{\frac{\displaystyle{#1}}{\displaystyle{#2}}}$

# Notes, Theorem 15.2.1

## iv

Take arbitrary $a' \in \varphi(A)$ and $s' \in S$. Then we have
$\varphi(s) = s'$ and $\varphi(a) = a'$ where $as, sa \in A$. It follows
$a's' = \varphi(a) \varphi(s) = \varphi(as) \in \varphi(A)$. Similarly,
$s'a' \in \varphi(A)$.

## viii

*Fact.* $\varphi(0) = 0$.

Observe $\varphi(0) = \varphi(0 + 0) = \varphi(0) + \varphi(0)$,
implying by additive cancellation $0 = \varphi(0)$.

*Theorem.* Main problem.

$(\rightarrow)$ We know $\varphi(0) = 0$ for any homomorphism. For any
$r \in Ker \; \varphi$, by definition $\varphi(r) = 0$, implying by
injectivity $r = 0$.

$(\leftarrow)$ Take $\varphi(r) = \varphi(r')$. Then $$\begin{aligned}
  \varphi(r) - \varphi(r') &= 0 \\
  \varphi(r - r') &= 0
\end{aligned}$$ Implying $r - r' = 0$, i.e $r = r'$.

## ix

Clearly $\varphi^{-1}$ is a bijection. It remains to show operations are
preserved.

For arbitrary $a', b' \in S$, we know there are $a, b \in R$, such that
$\varphi(a) = a'$ and $\varphi(b) = b'$. It follows for the operation
$*$, interpreted as either addition $+$ or multiplication $\cdot$:
$$\begin{aligned}
  &                     & \varphi^{-1}(a' * b') &= \varphi^{-1}(a') * \varphi^{-1}(b') \\
  & \longleftrightarrow & \varphi^{-1}(\varphi(a) * \varphi(b)) &= (\varphi^{-1} \circ \varphi)(a) * (\varphi^{-1} \circ \varphi)(b) \\
  & \longleftrightarrow & \varphi^{-1}(\varphi(a * b)) &= a * b \\
  & \longleftrightarrow & a * b &= a * b
\end{aligned}$$


# Gallian (9th ed), Chapter 15

## 6

Call the map $\varphi$. Observe $$\begin{aligned}
  \varphi(3 \cdot 3) &= \phi(1) = 3 \cdot 1 = 3 \\
  \varphi(3) \cdot \varphi(3) &= (3 \cdot 3) \cdot (3 \cdot 3) = 9 \cdot 9 = 9
\end{aligned}$$

## 8

Denote $\varphi(1) = a$. Clearly, $$\begin{aligned}
  \varphi(x) &= \varphi(\underbrace{1 + \dots + 1}_{x \text{ times}}) = \underbrace{\varphi(1) + \dots + \varphi(1)}_{x \text{ times}} = x \cdot \varphi(1) = ax \\
  a^2 &= \varphi(1) \cdot \varphi(1) = \varphi(1 \cdot 1) = \varphi(1) = a
\end{aligned}$$

## 10 (a)

Let $\varphi$ be an arbitrary homomorphism. $$\begin{aligned}
  \varphi(4) = \varphi(2) + \varphi(2) &= \varphi(2) \cdot \varphi(2) \\
  3x + 3x &= 3x \cdot 3x
\end{aligned}$$ By injectivity $x \neq 0$.

Claim. no such integer $x$ satisfies that. Observe $$\begin{aligned}
  3x + 3x &= 3x \cdot 3x \\
  x + x &= 3x^2 \\
  2x &= 3x^2 \\
  2 &= 3x
\end{aligned}$$

## 17 (compare with thm 15.2.1 (vii) of the notes)

Yes. We show a more general statement, that the following $\varphi$ is a
ring homomorphism:

$$\varphi : \mathbb{Z}_n \longrightarrow \mathbb{Z}_{kn}, \qquad \varphi(x) = kx,
\quad \text{where } k = mn + 1.$$

**Lemma.** Addition is preserved, i.e
$\varphi(a + b) = \varphi(a) + \varphi(b)$.

Let $$a + b = nq + r, \qquad r \in \{0,1,\dots,n-1\},$$ then
$$k(a + b) = knq + kr, \qquad kr \in \{0,\dots,kn-k\}.$$ Note
$kr = \varphi(a + b)$. Observe also
$$(k\cdot a) + (k\cdot b) = knq + kr, \qquad ka, kb \in \{0,\dots,kn-k\}.$$
Note $kr = \varphi(a) + \varphi(b)$.

**Lemma.** Multiplication is preserved, i.e
$\varphi(a \cdot b) = \varphi(a)\cdot\varphi(b)$.

Let $$a \cdot b = nq + r, \qquad r \in \{0,1,\dots,n-1\},$$ then
$$\begin{aligned}
  k (a \cdot b) &= knq + kr & &\text{where } kr \in \{0,\dots,kn-k\}
\end{aligned}$$ Note $kr = \varphi(a \cdot b).$ $$\begin{aligned}
  (k\cdot a)(k\cdot b) &= (k\cdot k\cdot n)q + (k\cdot k)r & &\text{where } ka,kb \in \{0,\dots,kn-k\}, \\
  &= (k\cdot k\cdot n)q + kmnr + kr & &\text{since } k = mn + 1, \\
  &= kn(kq + mr) + kr.
\end{aligned}$$ Note $kr = \varphi(a)\cdot\varphi(b).$

**Corollary.** $\varphi : \mathbb{Z}_5 \longrightarrow \mathbb{Z}_{30}$
is a ring homomorphism.

## 21

**Theorem.** All homomorphisms from $\mathbb{Z}_6$ to $\mathbb{Z}_6$.

For any homomorphism $\varphi$, observe
$\varphi(x) = x\varphi(1) = x \cdot_{Z_6} \varphi(1)$, since
$x \in Z_6$.

So $\varphi(1)$ decides $\varphi$. Thereby, all homomorphisms correspond
to $\varphi(1) = 0, 1, \dots, 5$.

**Theorem.** All homomorphisms from $\mathbb{Z}_{20}$ to
$\mathbb{Z}_{30}$.

Any $x \in \mathbb{Z}_{20}$ is also in $\mathbb{Z}_{30}$. So similarly,
all homomorphisms correspond to $\varphi(1) = 0, 1, \dots, 29$.

## 34

**Note.** Up against the stated question we show $\varphi$ is a ring
homomorphism, regardless of the divisibility condition --- I am looking
for your feedback ya Ibrahim.

**Lemma.** Addition $$\begin{aligned}
  &\phi(a + b) = \phi(a) + \phi(b) \\
  \Longleftrightarrow &(a + b) \bmod n = \bigl[(a \bmod n) + (b \bmod n)\bigr] \bmod n
\end{aligned}$$ Observe $$\begin{aligned}
  a + b &= nq + r,\quad 0 \le r < n \\
  a &= nq_0 + r_0 \\
  b &= nq_1 + r_1 \\
  a + b &= n(q_0 + q_1) + (r_0 + r_1)
\end{aligned}$$

Take $r_0 + r_1 = nq' + r'$. Then
$$a + b = n(q_0 + q_1 + q') + r',\quad 0 \le r' < n$$ by uniqueness
$r = r'$.

**Lemma.** Multiplication $$\begin{aligned}
  &\phi(a \cdot b) = \phi(a) \cdot \phi(b) \\
  \Longleftrightarrow &(a \cdot b) \bmod n = \bigl[(a \bmod n)\cdot(b \bmod n)\bigr] \bmod n
\end{aligned}$$ Observe $$\begin{aligned}
  a \cdot b &= nq + r,\quad 0 \le r < n \\
  a &= nq_0 + r_0 \\
  b &= nq_1 + r_1 \\
  a \cdot b &= (nq_0 + r_0)(nq_1 + r_1) \\
  &= n^2 q_0 q_1 + nq_0 r_1 + nq_1 r_0 + r_0 r_1
\end{aligned}$$ Take $r_0 r_1 = nq' + r'$, $0 \le r' < n$. $$a \cdot b
= n\bigl(nq_0 q_1 + q_0 r_1 + q_1 r_0 + q'\bigr) + r'$$ By Euclid,
$r = r'$.
