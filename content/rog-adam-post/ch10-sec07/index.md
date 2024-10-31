---
title: Ch.10, Sec.7
math: true
date: "2024-01-31"
---

$\newcommand{\nfrac}[2]{\frac{\displaystyle{#1}}{\displaystyle{#2}}}$

## Exercises

### Ex. 7.03

denote $a_n = \nfrac{f^n(0)}{n!}$.

Observe
\begin{align*}
    f^0(x) &= \nfrac{1}{1-2x} &f^0(0) = 1 \\\\
    f'(x) &= 1 \cdot 2 \cdot (1-2x)^{-2} &f'(0) = 1 \cdot 2 \\\\
    f''(x) &= 1 \cdot 2 \cdot 2^2 \cdot (1 - 2x)^{-3} &f''(0) = 1 \cdot 2 \cdot 2^2 \\\\
\end{align*}
Generally $f^n(x) = n! \cdot 2^n (1 - 2x)^{-(n+1)}$ and $f^n(0) = n! \cdot 2^n$. It follows:
\begin{align*}
    \nfrac{1}{1-2x} &= 1 + 2^1 x^1 + 2^2 x^2 + \dots \\\\
    r &= 2x \\\\
    \nfrac{1}{1-2x} &= (2x)^0 + (2x)^1 + (2x)^2 + \dots + (2x)^n \\\\
    &= 1 + 2^1 x + 2^2 x^2 + \dots + 2^n x^n
\end{align*}
Hence it is valid for
\begin{align*}
    |r| < 1 \\\\
    |2x| < 1 \\\\
    |x| < \nfrac{1}{2}
\end{align*}
