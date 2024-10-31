---
title: Chapter 11
math: true
date: "2023-12-18"
---

## Problems {#problems .unnumbered}

### 2 {#section .unnumbered}

$n = 3$.

The table in page 213 shows that.

### 5 {#section-1 .unnumbered}

$45 = 3^2 \cdot 5^1$. By the *fundamental theorem of finite abelian
groups*, All possible groups are
\begin{aligned}
    Z_9 \oplus Z_5 &\approx Z_{45} \\\\
    Z_3 \oplus Z_3 \oplus Z_5 &\approx Z_3 \oplus Z_{15}
\end{aligned}

Group $(1)$ has element $3$ whose order is $|3| = 15$. Group $(2)$ has element $(0,1)$ whose order is $|(0,1)| = 15$. Therefore, Any finite abelian group of order $45$ has an element of order $15$.

By *The fundamental theorem of cyclic groups* (page 81) we know all elements orders of $Z_3$ are: $1, 3$, and all elements orders of $Z_{15}$ are: $1, 3, 5$. But by *Theorem 8.1* (page 158) all elements' orders of $Z_3 \oplus Z_{15}$ are: $1, 3, 5, 15$, by computing $lcm$ of all possible pairs of elements orders. Therefore, It is not necessarily the case any finite abelian group of order $45$ has an element of order $9$.

### 10 {#section-2 .unnumbered}

$360 = 2^3 \cdot 3^2 \cdot 5^1$.

For $2^3$, $k = 3$,
\begin{aligned}
    3 &\qquad Z_8 \\\\
    2 + 1 &\qquad Z_4 \oplus Z_2 \\\\
    1 + 1 + 1 &\qquad Z_2 \oplus Z_2 \oplus Z_2
\end{aligned}

For $3^2$, $k = 2$,
\begin{aligned}
    2 &\qquad Z_9 \\\\
    1 + 1 &\qquad Z_3 \oplus Z_3
\end{aligned}$$

For $5^1$, $k = 1$,
\begin{aligned}
    1 \qquad Z_5
\end{aligned}

It follows all groups are
\begin{aligned}
    &Z_8 \oplus Z_9 \oplus Z_5 \\\\
    &Z_8 \oplus Z_3 \oplus Z_3 \oplus Z_5 \\\\
    &Z_4 \oplus Z_2 \oplus Z_9 \oplus Z_5 \\\\
    &Z_4 \oplus Z_2 \oplus Z_3 \oplus Z_3 \oplus Z_5 \\\\
    &Z_2 \oplus Z_2 \oplus Z_2 \oplus Z_9 \oplus Z_5 \\\\
    &Z_2 \oplus Z_2 \oplus Z_2 \oplus Z_3 \oplus Z_3 \oplus Z_5
\end{aligned}

### 22 {#section-3 .unnumbered}

By *the fundamental theorem of finite abelian groups*, $G \approx Z_{p_1^{n_1}} \oplus Z_{p_2^{n_2}} \oplus \dots \oplus Z_{p_k^{n_k}}$ where $|G| = p_1^{n_1} \cdot .. \cdot p_k^{n_k}$. We claim $n_1 = n_2 = \dots = n_k = 1$.

Assume for contradiction some $n_i > 1$. Then by the theorem we can substitute $Z_{p_i^{n_i}}$ by $Z_{p_i^1} \oplus Z_{p_i^1} \oplus Z_{p_i^{n_i-2}}$. If $n_i = 2$ then just ignore the third term. It follows we have two distinct subgroups of cardinality $p_i$. In other words, two distinct subgroups of the same order of divisor $p_i$ of $|G|$. Contradiction.

Therefore $G \approx Z_{p_1^1} \oplus Z_{p_2^1} \oplus \dots \oplus Z_{p_k^1}$. But all $p_i$s are coprime, So $G \approx Z_{p_1 \cdot .. \cdot p_k}$, Concluding it is cyclic.

### 31 {#section-4 .unnumbered}

If $a = b$ then $a^2 = b^2$. So $a$ and $b$ are distinct. Moreover $(a^2)^2 = a^4 = e$ and $(b^2)^2 = b^4 = e$. So we have distinct elements $a^2$ and $b^2$ of order 2.

By the *fundamental theorem of finite abelian groups*, All possible classes are:
\begin{aligned}
    &Z_{16} \\\\
    &Z_8 \oplus Z_2 \\\\
    &Z_4 \oplus Z_4 \\\\
    &Z_4 \oplus Z_2 \oplus Z_2 \\\\
    &Z_2 \oplus Z_2 \oplus Z_2 \oplus Z_2
\end{aligned}

$(3)$ is excluded as it has only one element of order $2$, namely $8$.

$(4)$ is excluded. All orders of elements are $1,2,4,8$ and $1,2$ respectively. Elements of order $4$ in group $(4)$ can be only obtained by an element of order $4$ in $Z_8$. Otherwise the $lcm$ would be $1,2,8$. There are only two elements of order $4$ in $Z_8$, namely $2$ and $6$. So all possible elements of order $4$ in group $(4)$ are $(2,0), (6,0), (2,1), (6,1)$. But the square of any of them is $(4,0)$, Violating the given condition $a^2 \neq b^2$.

$(6)$ is excluded. All orders of elements are $1,2,4$ and $1,2$ respectively. There are only two elements in $Z_8$ of order $4$, namely $1$ and $3$. So all possible elements of order $4$ in group $(4)$ are $(1,0), (3,0), (1,1), (3,1)$. But the square of any of them is $(2,0)$, Violating the given condition of $a^2 \neq b^2$.

$(7)$ is excluded as all elements orders of $Z_2$ are $1,2$, So taking $lcm$ would always be $1,2$. So it has no element of order $4$.

Therefore the class is group $(5)$.
