---
title: "Chapter 04 - Section 02"
math: true
date: "2024-01-30"
---

$\newcommand{\nfrac}[2]{\frac{\displaystyle{#1}}{\displaystyle{#2}}}$

## Exercises {#exercises .unnumbered}

### 9 {#section .unnumbered}

We follow the standard recipe.
$$
\begin{align*}
    r^2 &= 3r + 10 \\\\
    r^2 - 3r - 10 &= 0 \\\\
    (r + 2)(r - 5) &= 0 \\\\
\end{align*}
$$
$r = -2$ or $r = 5$. The general solution form is $\alpha_1(-2)^n + \alpha_2(5)^n$. From the base cases:
$$
\begin{align*}
    F(0) &= 4 \\\\
    &= \alpha_1 + \alpha_2 \\\\
    F(1) &= 13 \\\\
    &= -2 \alpha_1 + 5 \alpha_2 \\\\
\end{align*}
$$
Which by substitution implies $\alpha_1 = 1$ and $\alpha_2 = 3$. Therefore $F(n) = (-2)^n + 3 (5)^n$.
