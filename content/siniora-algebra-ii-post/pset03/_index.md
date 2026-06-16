---
title: Homework 3
math: true
date: "2026-06-16"
---

# Sheet A

## 1

**1**

($\leftarrow$). Assume $x = 0$. Then
$N(0) = N(0 + 0 \sqrt{d}) = |0^2 - d 0^2| = |0 - 0| = 0$.

($\rightarrow$). Observe for any $x^2 \neq 0$,
$x^2 = (p_0)^2 (p_1)^2 \dots (p_k)^2$ for distinct primes $p_i$.

Assume $N(x) = 0$. Then $|a^2 - db^2| = 0$, implying $a^2 - db^2 = 0$
and in turn $a^2 = db^2$.

Towards a contradiction, assume $a^2 \neq 0$. Since $d \neq 1$ by def,
and $b^2$ is a product of prime squares, $d$ must be divisible by a
prime square. Contradiction.

**2**

Let $x = a_0 + b_0 \sqrt{d}$ and $y = a_1 + b_1 \sqrt{d}$.
$$\begin{aligned}
  N(x) \cdot N(y) &= |(a_0)^2 - d (b_0)^2| \cdot |(a_1)^2 = d (b_1)^2| \\
  &= |((a_0)^2 - d (b_0)^2) \cdot ((a_1)^2 - d (b_1)^2)| \\
  &= |(a_0 a_1)^2 - d(a_0 b_1)^2 - d(a_1 b_0)^2 + (b_0 b_1)^2 d^2|
\end{aligned}$$ $$\begin{aligned}
  N(xy) &= N((a_0 + b_0 \sqrt{d}) (a_1 + b_1 \sqrt{d})) \\
  &= N((a_0 a_1 + b_0 b_1 d) + (a_0 b_1 + a_1 b_0) \sqrt{d}) \\
  &= |(a_0 a_1 + b_0 b_1 d)^2 - d (a_0 b_1 + a_1 b_0)^2| \\
  &= | [(a_0 a_1)^2 - 2(a_0 a_1) (b_0 b_1 d)^2] - d [(a_0 b_1)^2 + 2(a_0 b_1)(a_1 b_0) + (a_1 b_0)^2] | \\
  &= |(a_0 a_1)^2 - 2(a_0 a_1) (b_0 b_1 d) + (b_0 b_1 d)^2 - d (a_0 b_1)^2 - d 2(a_0 b_1) (a_1 b_0) - d (a_1 b_0)^2| \\
  &= |(a_0 a_1)^2 - d (a_0 b_1)^2 - d (a_1 b_0)^2 + (b_0 b_1 d)^2|
\end{aligned}$$

**3**

Let $x = a + b \sqrt{d}$.

($\rightarrow$). Assume $N(x) = 1$. Then $|a^2 - db^2| = 1$.

Case. $a^2 - db^2 = 1$. Take $x^{-1} = a - bd\sqrt{d}$. Observe
$(a + b \sqrt{d})(a - b \sqrt{d}) = a^2 - db^2 = 1$.

Case. $a^2 - db^2 = -1$. Then $-(a^2 - db^2) = 1$. Take
$x^{-1} = (-a + b \sqrt{d})$. Observe
$(a + b \sqrt{d})(-a + b \sqrt{d}) = -(a^2) + db^2 = -(a^2 - db^2) = 1$.

($\leftarrow$). Assume $x$ is a unit. Then $x^{-1}$ exists. In other
words, $$\begin{aligned}
  (a' + b' \sqrt{d}) (a + b \sqrt{d}) = 1
  (a'a + b'bd) + (a'b + b'a) \sqrt{d} = 1 + 0 \sqrt{d}
\end{aligned}$$ Thus, $aa' + bb'd = 1$ (7), implying $gcd(a, b) = 1$ (1)
and $gcd(a', b') = 1$ (2). Also, $a'b + ab' = 0$, implying $a'b = -ab'$
(3).

From (1) and (3), $a | a'$ (4). From (2) and (3), $a; | (-a)$ (5).

From (4) and (5), either $a' = a$ or $a' = -a$ (6).

From (6) and (3), either $b' = -b$ or $b' = b$. (8)

From (6), (7), (8), either $a^2 - db^2 = 1$ or $a^2 - db^2 = -1$. In
both cases, $|a^2 - db^2| = 1$.

**4**

We show the contrapositive: $x$ reducible implies $N(x)$ is composite.

Assume $(a + b \sqrt{d}) = (a_0 + b_0 \sqrt{d}) (a_1 + b_1 \sqrt{d})$, a
product of non-units. $$\begin{aligned}
  N(a + b \sqrt{d}) &= N( (a_0 + b_0 \sqrt{d}) (a_1 + b_1 \sqrt{d}) ) \\
  &= N(a_0 + b_0 \sqrt{d}) \cdot N(a_1 + b \sqrt{d})
\end{aligned}$$ By problem 1-2, both factors are greater than $1$. Hence
$N(x)$ is composite.

**5**

$(\leftarrow)$. reducible $\rightarrow$ composite.

Let $x \in D$ be a reducible element of a UFD.

Then $x = x_0 \cdot x_1 \cdot \dots \cdot x_k$ where all $x_i$ are
irreducible by hypothesis of UFD. Also $x = y_0 y_1$ where $y_0$ and
$y_1$ are non-units.

Take $b = y_0$ and $c = y_1$. Note $x \nmid y_0$ as some irreducibles of
$y_1$ do not divide $b$. Similarly $x \nmid y_1$.

$(\rightarrow)$. irreducible $\rightarrow$ prime.

We show $x | bc \wedge x \nmid b \rightarrow x | c$. Assume the
hypothesis.

Set $xz = bc$. By uniqueness and since $x \nmid b$, we know $x$ isn't
associate to any irreducible divisor of $b$. Thereby $x$ is associate to
some irreducible $c_0$ of $c$.

Note $x = uc_0$ and $u^{-1}x = c_0$. Replace $c_0$ in the expansion of
$c$ by $u^{-1}x$. It follows $x | c$.

**6**

## 2

**3**

Let $g \in gcd(a,b)$. Then $gw_0 = a$ and $gw_1 = b$ for some $w_0$ and
$w_1$.

$(\rightarrow)$. Take $r_0a + s_0b$ in $\langle a, b \rangle$. It is
equal to
$r_0(gw_0) + s_0(gw_0) = g(r_0w_0 + s_0w_0) \in \langle g \rangle$.

$(\leftarrow)$. Observe $\langle g \rangle = \langle g' \rangle$
whenever $g \sim g'$.

Since we are in PID, we have $\langle a, b \rangle = \langle c \rangle$
for some $c$. Observe $0a + 1b = s_0c$ implying $c | b$. Observe
$1a + 0b = s_1c$ implying $c | a$. Let $d$ be arbitrary such that
$d | a \wedge d | b$. Then $dw_0 = a$ and $dw_1 = b$. Hence
$d(w_0 + w_1) = a + b = s_2c$. However, we know $c = m_0a + m_1b$ for
some $m_0$ and $m_1$. Hence
$c = m_0(dw_0) + m_1(dw_1) = d(m_0w_0 + m_1w_1)$, concluding $d | c$.
Thus $c$ is a gcd.

By uniqueness, $\langle a, b \rangle = \langle g \rangle$ for all
$g \in gcd(a,b)$.

**5**

**5(1).** Assume $p \nmid a$. Clearly $a | p$ and $1 | a$. Assume
$d | p$ and $d | a$. Then $dw_0 = p$ and $dw_1 = a$.

The goal is to show $d | 1$. Since $p$ is irreducible,

Case. $d$ is a unit. then $d \cdot d^{-1} = 1$.

Case. $w_0$ is a unit. Then $dw_0(w_0)^{-1} = p(w_0)^{-1} = d$. Hence
$p(w_0)^{-1}(w_1) = a = p ((w_0)^{-1}(w_1))$. So $p | a$. Contradiction.

**5(2).**

**5(3).** Let $p$ be irreducible. then by def, $p \neq 0$. assume
$p | ab$. if $p | a$, we are done. if $p \nmid a$, then $1 \in gcd(p,a)$
by (1). by (2), $p | b$.
