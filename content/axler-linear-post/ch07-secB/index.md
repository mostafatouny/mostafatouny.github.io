---
title: "Ch. 07, Sec. B"
math: true
date: "2024-01-01"
---

$\newcommand{\ddfrac}[2]{\frac{\displaystyle{#1}}{\displaystyle{#2}}}$

## Exercises {#exercises .unnumbered}

### Ex. 01 {#ex.-01 .unnumbered}

False. If there is a basis consisting of eigenvectors of $T$, Then $M(T)$ is diagonal. It follows $M(T) M(T)^* = M(T)^* M(T)$, Equivalently $TT^* = T^*T$, So $T$ is self-adjoint.


### Ex. 02 {#ex.-02 .unnumbered}

Assume $F = \mathbb{R}$.

**Observation.** $p(x) = x^2 -5x + 6 = (x-2)(x-3)$. $p(T) = T^2 -5T + 6I = (T-2I)(T-3I)$

The goal is $p(T) = 0$. It suffices to show $p(T)v = 0$ for any vector $v$.

By *Real Spectral Theorem* (p. 221), There is a basis of eigenvectors of $T$ corresponding to eigenvalues $\lambda_1, .., \lambda_n$. By hypothesis we know $\lambda_i = 2$ or $\lambda_i = 3$.

Let $v$ be an arbitrary vector $v$. Then $v = a_1v_1 + \dots + a_nv_n$. Observe $p(T)(v) = p(T)(a_1v_1) + \dots + p(T)(a_nv_n) = a_1p(\lambda_1)v_1 + \dots + a_np(\lambda_n)v_n$. But $p(\lambda_i) = 0$, so $p(T)v = 0$.
