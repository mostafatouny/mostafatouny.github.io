---
title: "Problem Set 07"
math: true
date: "2023-05-14"
---

## Problem. 1 {#problem.-1 .unnumbered}

## Problem. 2 {#problem.-2 .unnumbered}

## Problem. 3 {#problem.-3 .unnumbered}

By hypothesis, For any reals $x$ and $t$, We are given
$| f(t) - f(x) | \leq (t-x)^2$. Clearly:
$$
\begin{aligned}
    \frac{\displaystyle{|f(t) - f(x)|}}{\displaystyle{|t-x|}} \leq&                  \frac{\displaystyle{(t-x)^2}}{\displaystyle{|t-x|}} \\
    \left | \frac{\displaystyle{f(t) - f(x)}}{\displaystyle{t-x}} \right | \leq& |t- x|
\end{aligned}
$$
But $\lim_{t \rightarrow x} |t-x| = 0$ which concludes
$\lim_{t \rightarrow x} \left | \frac{\displaystyle{f(t)-f(x)}}{\displaystyle{t-x}}  \right | \leq 0$.
Since the absolute value is always equal or greater than 0, We get also
$\lim_{t \rightarrow   x} \left | \frac{\displaystyle{f(t)-f(x)}}{\displaystyle{t-   x}} \right | \geq 0$.
Therefore $f'(x) = 0$ for any real $x$.
