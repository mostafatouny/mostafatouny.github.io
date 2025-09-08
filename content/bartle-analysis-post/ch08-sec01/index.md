---
title: "Chapter 08 - Section 01"
math: true
date: "2024-01-10"
---

## Exercises {#exercises .unnumbered}

### Ex. 11 {#ex.-11 .unnumbered}

For $f_n(x) = \frac{\displaystyle{x}}{\displaystyle{x+n}}$, and $f = 0$, Clearly 

$||f_n - f ||_{[0,a]} = ||f_n||_{[0,a]} = \frac{\displaystyle{a}}{\displaystyle{a+n}}$. But $\lim_{n \rightarrow \infty} \frac{\displaystyle{a}}{\displaystyle{a+n}} = 0$. Hence by *lemma 8.1.8* (page 244), The uniform convergence on $[0,a]$ follows.

We follow *Lemma 8.1.5* (page 244). Consider subsequences $n_k = x_k = k$. Then $f_{n_k}(x_k) = \frac{\displaystyle{k + k}}{\displaystyle{k}} = \frac{\displaystyle{1}}{\displaystyle{2}}$. Therefore $|f_{n_k}(x_k) - f(x_k)| = |f_{n_k}(x_k)| = \frac{\displaystyle{1}}{\displaystyle{2}} = \epsilon_0$.

### Ex. 18 {#ex.-18 .unnumbered}

We use *lemma 8.1.8* (page 244). Note $f_n(x) = xe^{-nx}$ and $f = 0$. Then $||f_n - f||_{[0,\infty)} = ||f_n||_{[0,\infty)} = 1/n$.

To see why, Observe $f_n'(x) = (e^{-nx})(1-nx)$, and setting $f_n'(x) = 0$ yields local max/min at $x = 0$ and $x = 1/n$. That justifies the supremum we aforementioned.

But $\lim_{n \rightarrow \infty} 1/n = 0$, Concluding uniform convergence.

### Ex. 21 {#ex.-21 .unnumbered}

Observe $| (f_n(x) + g_n(x) ) - ( f(x) + g(x) ) | \leq |f_n(x) - f(x)| + |g_n(x) - g(x)| < \epsilon/2 + \epsilon/2 = \epsilon$, Following by the triangle inequality.
