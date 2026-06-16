---
title: Homework 4
math: true
date: "2026-06-16"
---

# Sheet B

## 1

**1**

**Fact 1.** if polynomial $g(x)$ is reducible, then so is $g(k)$ for all
$k$.

**Fact 2.** For prime $p$, if $p \cdot A / B$ is an integer, and $A / B$
is not an integer, then $p \mid B$.

*Proof.* Note $p \cdot A / B = p(k + i/B)$ where $k$ is an integer and
$i < B$. It follows $p \cdot i / B$ is an integer, and hence some common
factor exists between $p$ and $B$ since $i/B$ is already reduced.

**Theorem.** Main problem.

Observe $$\begin{aligned}
  \phi_p(x+1) = \frac{(x+1)^p - 1}{x} &= \frac{ (\binom{p}{p}x^p + \binom{p}{p-1}x^{p-1} + \dots + \binom{p}{1}x + 1) - 1}{x} \\
                                      &= \binom{p}{p}x^{p-1} + \binom{p}{p-1}x^{p-2} + \dots + \binom{p}{1}
\end{aligned}$$

By *Fact 2*, $\phi_p(x+1)$ satisfies *Eisenstein*'s criterian. Hence
$\phi_p(x+1)$ is irreducible over $\mathbb{Q}$.

By *Fact 1*, $\phi_p(x)$ is irreducible over $\mathbb{Q}$.

**2**

We apply the *Mod p Irreducibility Test*.

Take $\bar{f} = x^4 + x + 1$ over $\mathbb{Z}_2$. Since neither
$\bar{f}(0)$ nor $\bar{f}(1)$ is equal to $0$, $\bar{f}$ has no linear
factors. Observe also none of $x^2$, $x^2 + 1$, or $x^2 + x$ could be a
factor, as all of them have a zero but $\bar{f}$ does not. So the only
remaining possibility is $\bar{f} = (x^2 + x + 1)(x^2 + x + 1)$ which
does not hold. Therefore, $\bar{f}$ is irreducible over $\mathbb{Z}_2$.
$\blacksquare$

## 2

**2**

Assume towards a contradiction that
$R = \cup_{n=1}^\infty \mathbb{R}[x^{1/n}]$ is a UFD.

Observe $$\begin{aligned}
  x^{5/8} + x^{7/8} + x + x^{5/4} &= (x^{1/2} + x^{3/4})(x^{1/2} + x^{1/8}) \\
                                  &= (x^{1/4} + x^{1/2})(x^{3/4} + x^{3/8})
\end{aligned}$$

By uniqueness,

-   Case 1. $x^{1/2} + x^{3/4} = u (x^{1/4} + x^{1/2})$ for some unit
    $u$.

    -   Case 1.1. $x^{1/2} = u x^{1/4}$, implying $u = x^{1/4}$ but it
        is not a unit.

    -   Case 1.2. $x^{3/4} = u x^{1/4}$, implying $u = x^{1/2}$ but
        $x^{1/2} x^{1/2} \neq x^{1/2}$.

-   Case 2. $x^{1/2} + x^{3/4} = u (x^{3/4} + x^{3/8})$ for some unit
    $u$.

    -   Case 2.1. $x^{1/2} = ux^{3/4}$, but no such $u$ exists.

    -   Case 2.2. $x^{3/4} = ux^{3/4}$, implying $u = 1$, but
        $x^{1/2} \neq (1) x^{3/8}$.

## 3

**1**

Denote $f(x) = a_0 + a_1 x^1 + \dots + a_n x^n$.

$(\rightarrow)$. We are given $gcd(a_0, \dots, a_n) = 1$. For a constant
$b$ dividing $f$, it follows $b$ is a common divisor of
$a_0, \dots, a_n$. Hence $b \mid 1$, implying it is a unit.

$(\leftarrow)$. Assume any constant $b$ dividing $f$ is a unit. Thereby,
any common divisor $b$ of $a_0, \dots, a_n$ does also divide $1$. So
there is some $b'$ such that $bb' = 1$ concluding it is a unit.

**2**

Observe $$\begin{aligned}
  f(r/s) &= a_0 + a_1 (r/s)^1 + \dots + a_n (r/s)^n = 0 \\
         &= a_0 s^n + a_1 r^1 s^{n-1} + \dots + a_{n-1} r^{n-1} s^1 + a_n r^n = 0 \\
         &= a_0 s^n + r (a_1 r^0 s^{n-1} + \dots + a_{n-1} r^{n-2} s^1 + a_n r^n) = 0 \\
         &= s (a_0 s^{n-1} + a_1 r^1 s^{n-2} + \dots + a_{n-1} r^{n-1}) + a_n r^n = 0
\end{aligned}$$ Hence $r \mid a_0 s^n$. Since $gcd(r,s) = 1$, it follows
$gcd(r,s^n) = 1$. Thus, $r \mid a_0$. Moreover, $s \mid a_n r^n$. Since
$gcd(r,s) = 1$, it follows $gcd(s,r^n) = 1$. Thus, $s \mid a_n$.

**5**

Note $\mathbb{Z}[i]$ is a UFD. By problem 3 and problem 4, it suffices
to find an irreducible $p$ in $\mathbb{Z}[i]$ which satisfies the
Eisenstein's criterian of problem 4.

Take $p = 1+i$. Observe $(1+i)(2+i) = 1+3i$; $(1+i)(2+2i) = 4i$;
$(1+i)(-3+3i) = -6$. However, In the field of quotients $F$ of
$\mathbb{Z}[i]$, $1/(1+i) = 1/2 - i \notin \mathbb{Z}[i]$. Thereby
$(1+i)$ is not a unit in $\mathbb{Z}[i]$. Moreover, $(1+i)^2 = 2i$ and
$(1+3i)/2i = 3/2 - i/2 \notin \mathbb{Z}[i]$.
