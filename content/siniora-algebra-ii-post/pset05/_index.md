---
title: Homework 5
math: true
date: "2026-06-16"
---

# Gallian (9th ed), Chapter 20

## 5

Take $\mathbb{C}$ an extension of $\mathbb{Q}$. Interpret the polynomial
over it.

The roots of $x^2 + x + 1$ over $\mathbb{C}$, using the quadratic
formula, are $$x = \frac{-1 \pm \sqrt{-3}}{2}$$ Similarly, the roots of
$x^2 - x + 1$ over $\mathbb{C}$ are $$x = \frac{1 \pm \sqrt{-3}}{2}$$ It
follows a splitting field is
$\mathbb{Q}(\frac{-1 \pm \sqrt{-3}}{2},\frac{1 \pm \sqrt{-3}}{2}) = \mathbb{Q}(\frac{1 \pm \sqrt{-3}}{2})$,
eliminating algebraic dependency over $\mathbb{C}$.

By the interpretation of vector spaces:
$$\mathbb{Q} \left ( \frac{1 \pm \sqrt{-3}}{2} \right ) = \left \{a + b \left ( \frac{1 + \sqrt{-3}}{2} \right ) + c \left ( \frac{1 - \sqrt{-3}}{2} \right ) + d \left ( \frac{1 + \sqrt{-3}}{2} \right ) \left ( \frac{1 - \sqrt{-3}}{2} \right ) \mid a,b,c,d \in \mathbb{Q} \right \}$$

## 12

Take $p(x) = x^3 - \pi^3$. Then $p(\pi) = \pi^3 - \pi^3 = 0$. Hence the
extension is algebraic. In order to conclude the basis is
$\{1, \pi, \pi^2\}$, we show $p$ is a minimal degree polynomial with
root $\pi$.

Assume towards a contradiction $p'(\pi) = a\pi + b = 0$ for some $p'$.
It follows $\pi = -b/a$, implying $\pi \in \mathbb{Q}(\pi^3)$. Hence
$\pi = P_0(\pi^3)/Q_0(\pi^3)$ for some $P_0, Q_0 \in \mathbb{Q}[x]$.
Observe: $$Q_0(\pi^3) \pi = P_0(\pi^3)$$ Interpret that expression as
polynomials over the single variable $\pi$. Clearly the degree of the
L.H.S cannot match the degree of the R.H.S. Contradiction.

Assume towards a contradiction $p'(\pi) = a\pi^2 + b\pi + c = 0$ for
some $p'$. Since by definition $a,b,c \in \mathbb{Q}(\pi^3)$:
$$p'(\pi) = \frac{P_0(\pi^3)}{Q_0(\pi^3)} \pi^2 + \frac{P_1(\pi^3)}{Q_1(\pi^3)} \pi + \frac{P_2(\pi^3)}{Q_2(\pi^3)} = 0$$
where $P_0, Q_0, P_1, Q_1, P_2, Q_2 \in \mathbb{Q}[x]$. By multiplying
both sides by $Q_0(\pi^3) Q_1(\pi^3) Q_2(\pi^3)$: $$\begin{aligned}
  Q_1(\pi^3) Q_2(\pi^3) P_0(\pi^3) \pi^2 + Q_0(\pi^3) Q_2(\pi^3) P_1(\pi^3) \pi + Q_0(\pi^3) Q_1(\pi^3) P_2(\pi^3) = 0 \\
  Q_0(\pi^3) Q_1(\pi^3) P_2(\pi^3) = -Q_1(\pi^3) Q_2(\pi^3) P_0(\pi^3) \pi^2 - Q_0(\pi^3) Q_2(\pi^3) P_1(\pi^3) \pi
\end{aligned}$$ Interpret that expression as polynomials over the single
variable $\pi$. Clearly the degree of the L.H.S cannot match the degree
of the R.H.S. Contradiction.

## 14

**Fact.** For an isomorphism
$\phi: \mathbb{Q}[x] \rightarrow \mathbb{Q}[x]$:

-   \(1\) $\forall z \in \mathbb{Z}, \phi(1/z) = 1/z$.

-   \(2\) $\forall k \in \mathbb{Q}, \phi(k) = k$.

-   \(3\)
    $\forall k \in \mathbb{Q}, \forall p \in \mathbb{Q}[x], \phi(kp) = k \phi(p)$.

For (1), it suffices to show $\phi(1/n) \cdot n = 1$. Observe
$$\phi(1/n) \cdot n = \phi(1/n) \cdot \phi(n) = \phi(n/n) = \phi(1) = 1$$

For (2), let $k = a/b$ for integers $a,b \in \mathbb{Z}$. Then
$$\phi(k) = \phi(a/b) = \phi(1/b) \phi(a) = (1/b) a = a/b$$

For (3), it follows by definition since $\phi$ is a homomorphism,
interpreting $k$ as a constant polynomial in $\mathbb{Q}[x]$. Then we
use (3) to get $\phi(k)\phi(p) = k \phi(p)$.

**Fact.** An isomorphism $\phi: \mathbb{Q}[x] \rightarrow \mathbb{Q}[x]$
is decided by $\phi(x)$.

It follows immediately by applying the shown linearity. For example,
$ax^2 + bx + c \mapsto a[\phi(x)]^2 + b \phi(x) + c$.

**Lemma.** The only isomorphism
$\phi: \mathbb{Q}[x] \mapsto \mathbb{Q}[x]$ is the identity.

If $\phi(x) = c$ then $\phi$ won't be surjective.

If $\phi(x) = a_mx^{k_m} + \cdot + a_0x^{k_0}$ with degree at least $2$,
then $\phi$ won't be surjective. We know $\phi$ maps a constant to a
constant. If $\phi$ is applied to a non-constant polynomial, it yields a
polynomial of degree at least $2$. Thereby, polynomials of degree $1$
are missed.

Therefore, $\phi(x) = kx$. For some polynomials, by definition we know:
$$\begin{aligned}
  \phi(a_0x \cdot a_1x) &= \phi(a_0x) \cdot \phi(a_1x) \\
  k a_0a_1x^2 &= ka_0x \cdot ka_1x \\
  &= k^2a_0a_1x^2
\end{aligned}$$ It concludes $k = k^2$ which is true only if $k = 0$ or
$k = 1$. The former maps all polynomials to constants violating the
surjectivity of $\phi$.

Therefore, $\phi(x) = x$, i.e the only isomorphism is the identity.

**Theorem.** Main Problem.

Observe $p(x) = x^3 - 5$ satisfies $p(5^{1/3}) = 0$. By Eisenstein's
criteria with prime $5$, the polynomial $p$ is irreducible over
$\mathbb{Q}$. By vector space interpretation:
$$\mathbb{Q}(5^{1/3}) = \{ a + b 5^{1/3} + c 5^{2/3} \mid a,b,c \in \mathbb{Q} \}$$
Considering the interpretation of polynomials over the variable
$5^{1/3}$, the only isomorphism
$\phi: \mathbb{Q}(5^{1/3}) \rightarrow \mathbb{Q}(5^{1/3})$ is the
identity.

## 20

**Partially Solved.**

It suffices to find a polynomial $p(x) \in \mathbb{Q}[x]$ which has
$\sqrt{1 + \sqrt{5}}$ as a root.

Take $p(x) = (x^2 - 1)^2 - 5 = x^4 - 2x^2 - 4$. Trivially, polynomial
$p$ has $\sqrt{1 + \sqrt{5}}$ as a root. Thereby, there exists an
irreducible minimal degree polynomial which has $\sqrt{1 + \sqrt{5}}$ as
a root.

If $p$ is a minimal degree polynomial, then we are done. Maybe $p$ is
reducible over $\mathbb{Q}$ and hence can be factored.

## 38

**Fact.** $(\mathbb{Z}/3\mathbb{Z})(i) = \mathbb{Z}_3(i)$ is a field.

Factorize $p(x) = x^4 - x^2 - 2 = (x^2 + 1)(x^2 - 2)$. It suffices to
construct an extension where each factor has a root.

Observe $x^2 + 1$ is irreducible and has a root over $\mathbb{Z}_3(i)$.

However, $x^2 - 2$ has no roots over $\mathbb{Z}_3(i)$. Consider
$\mathbb{Z}_3(i)/\langle x^2 - 2 \rangle$. Clearly $x^2 - 2$ is
irreducible and has a root over it. The root is
$x + \langle x^2 - 2 \rangle$; Call it $\sqrt{2}$. It follows
$$\mathbb{Z}(i, \sqrt{2}) = \mathbb{Z}(i)(\sqrt{2}) = \{ a + bi + c\sqrt{2} + di\sqrt{2} \mid a,b,c,d \in \mathbb{Z} \}$$
is a splitting field of $x^4 - x^2 - 2$ over $\mathbb{Z}_3$.
