---
title: "Chapter 03 - Section 02"
math: true
date: "2024-01-21"
---

## Exercises {#exercises .unnumbered}

### B {#b .unnumbered}

#### Ex. 2 {#ex.-2 .unnumbered}

$(\rightarrow)$ Trivial.

$(\leftarrow)$ Consider
$$
v_i = \begin{bmatrix}
        0 \\\\
        \vdots \\\\
        1 \\\\
        \vdots \\\\
        0
    \end{bmatrix}
$$
Where only ith position is $1$. Then
\begin{align*}
    (Av_i)[Col \\ i] &= (Bv_i)[Col \\ i] \quad \text{By hypothesis} \\\\
                     &= A[Col \\ i] \quad \text{Multiplication by 1}
\end{align*}
Then it follows $A[Col \\ i] = B[Col \\ i]$ for all $i$.
