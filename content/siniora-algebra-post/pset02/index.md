---
title: Chapter 02
math: true
date: "2023-11-16"
---

$\newcommand{\nfrac}[2]{\frac{\displaystyle{#1}}{\displaystyle{#2}}}$

## Problems {#problems .unnumbered}

### 1 {#section .unnumbered}

**(b).** No. 3/2 is not an integer.

**(d).** Yes. $cA$ is a totally valid matrix for any scalar $c$ or matrix $A$.

### 2 {#section-1 .unnumbered}

**(a).** Yes.

**(b).** No.
$\frac{\displaystyle{1/2}}{\displaystyle{3}} = \frac{\displaystyle{1}}{\displaystyle{2}} \frac{\displaystyle{1}}{\displaystyle{3}} \neq \frac{\displaystyle{3}}{\displaystyle{2}} = \frac{\displaystyle{1}}{\displaystyle{2/3}}$.

**(e).** No. $(2^2)^3 = 2^6 \neq 2^8 = 2^{(2^3)}$

### 3 {#section-2 .unnumbered}

**(c).** No. $3(x^2) \neq 3^2 x^2 = (3x)^2$.

**(d).** No. Known from linear algebra.

### 5 {#section-3 .unnumbered}

**(a).** $20 - 13 = 7$.

**(b).** The problem is reduced to finding $x$ and $y$ such that $13x = 14y + 1$. In other familiar notation from chapter 1, $13x - 14y = 1$. Clearly $13(-1) + (-14)(-1) = 1$ so $13(-1 + 14) + (-14)(-1 + 13) = 1$. Thus the inverse of $13$ is $13$.

### 7 {#section-4 .unnumbered}

Not closed. $1 + 3 = 4$.

No inverse. $3 + x \neq 1$ for any odd integer $x$.

### 14 {#section-5 .unnumbered}

$(ab)^3 = ababab$.

$(ab^{-2}c)^{-2} = (ab^{-2}c)^{-1} (ab^{-2}c)^{-1} = c^{-1}b^{-3}a^{-1}c^{-1}b^{-3}a^{-1}$

### 16 {#section-6 .unnumbered}

**Fact.** $x^n$ is an odd integer for any odd $x$.

**Fact.** The summation of two even integers is even.

We take a different perspective of the problem by the set $\{ (5 \cdot 1), (5 \cdot 3), (5 \cdot 5), (5 \cdot 7) \}$ modulo $5 \cdot 8$. Upon multiplying any two elements we get the form $5 \cdot 5 \cdot x \cdot y$ where $x,y \in \{ 1, 3, 5, 7 \}$. Think of the output of multiplication as the factor of $5$ deciding the element.

Observe the element is decided by $5 \cdot x \cdot y \mod 8$. For example if we knew $5 \cdot 5 \cdot 5 \cdot 1 = (5)(8 + 8 + 8 + 1)$ then we can easily deduce the output of $\mod 5 \cdot 8$ operation is $(5)(1)$.

The numbers $1$, $3$, $5$, and $7$ are all odds. So whatever $x$ or $y$ chosen, $5 \cdot x \cdot y$ will be odd. It follows $\textit{odd} \mod 8 = \textit{odd} \in \{1, 3, 5, 7\}$. To see why note $8k + \textit{odd} = \textit{odd}$.

**Lemma.** The given set is closed under the given operation.

**Lemma.** The identity is $5 \cdot 5 = 25$.

Observe $5 \cdot 5 \cdot x \mod 8 = 24x + x \mod 8 = x \mod 8$ since $24x \mod 8 = 0$.

**Lemma.** THe inverse of $5x$ is $5x$ by computation on the given elements.

**Lemma.** Associativity is known from integers and modulus properties.

### 18 {#section-7 .unnumbered}

$(R_0)^2 = (R_{180})^2 = H^2 = V^2 = D^2 = (D')^2 = R_0$.

$(R_{90})^2 = (R_{270})^2 = R_{180}$.

So $K = \{ R_0, R_{180} \}$, and $L = \{ R_0, R_{180}, H, V, D, D' \}$.

### 33 {#section-8 .unnumbered}

Observe the group follows the same pattern as $\mathcal{Z}_4$.

|   | e | a | b | c | d |
|---|---|--|---|---|--- |
| e | e | a | b | c | d | 
| a | a | b | c | d | e |
| b | b | c | d | e | a |
| c | c | d | e | a | b |
| d | d | e | a | b | c |

**inverses.** Since $ad = e$, $d = a^{-1}$. Since $bc = e$, $c = b^{-1}$.

**ab = c.** $ab = (cc)b = c(cb) = ce = c$.

**db = a.** $db = d(aa) = (da)a = ea = a$.

**cd = b.** $cd = c(bb) = (cb)b = eb = b$.

**dc = b.** $dc = (bb)c = b(bc) = be = b$.

**ac = d.** $d = bb = (aa)(dc) = a(ad)c = ac$.

**bd = a.** $bd = (dc)(bb) = d(cb)b = db = a$.

**dd = c.** $dd = (ac)(bb) = a(cb)b = ab = c$

### 34 {#section-9 .unnumbered}

$(\leftarrow)$. Given $ab = ba$
\begin{aligned}
    (ab)^2 &= (ab)(ab) \\\\
           &= a(ba)b, \text{Associativity} \\\\
           &= a(ab)b \\\\
           &= (aa)(bb), \text{Associativity} \\\\
           &= a^2b^2
\end{aligned}

$(\rightarrow)$. Given $(ab)^2 = a^2b^2$
\begin{aligned}
        (ab)^2 &= (ab)(ab) \\\\
               &= a(ba)b \\\\
               &= aabb \\\\
            ba &= ab, \text{Cancellation}
\end{aligned}

$(\leftarrow)$. Given $ab = ba$
\begin{aligned}
    (ab)^2 &= (ab)^{-1} (ab)^{-1} \\\\
           &= b^{-1} a^{-1} b^{-1} a^{-1} \\\\
           &= b^{-1} (ba)^{-1} a^{-1} \\\\
           &= b^{-1} (ab)^{-1} a^{-1} \\\\
           &= b^{-1} b^{-1} a^{-1} a^{-1} \\\\
           &= (b)^{-2} (a)^{-2}
\end{aligned}

$(\rightarrow)$. Given $(ab)^{-2} = b^{-2} a^{-2}$
\begin{aligned}
    (ab)^{-1} (ab)^{-1} &= b^{-1} a^{-1} b^{-1} a^{-1} \\\\
                        &= b^{-1} b^{-1} a^{-1} a^{-1} \\\\
          a^{-1} b^{-1} &= b^{-1} a^{-1}, \text{Cancellation} \\\\
             (ba)^{-1}  &= (ab)^{-1}
\end{aligned}

Now observe by the definition of inverse, if $x = y^{-1}$ then $y = x^{-1}$. Therefore $ab = [ (ab)^{-1} ]^{-1}$ and $ba = [ (ba)^{-1} ]^{-1}$, and $ab = ba$.

### 47 {#section-10 .unnumbered}

Clearly $aabb = a^2b^2 = ee = e$, and $abab = (ab)^2 = e$. It follows $aabb = abab$, and by *cancellation* $ab = ba$.
