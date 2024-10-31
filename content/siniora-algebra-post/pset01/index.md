---
title: Chapter 01
math: true
date: "2023-11-03"
---

$\newcommand{\nfrac}[2]{\frac{\displaystyle{#1}}{\displaystyle{#2}}}$

## Problems {#problems .unnumbered}

### 2

|         | R_0     | R_120 | R_240 | D       | D'        | D'' |
|--------------|-----------|------------|------|-------|-------|----|
| R_0     | R_0     | R_120 | R_240 | D       | D'        | D''   |
| R_120 | R_120 | R_240 | R_0     | D''     | D         | D'    |
| R_240 | R_240 | R_0     | R_120 | D'      | D''       | D      |
| D       | D       | D'      | D''     | R_0     | R_120   | R_240|
| D'      | D'      | D''     | D       | R_240 | R_0       | R_120|
| D''     | D''     | R_0     | D'      | R_120 | R_240   | R_0    |


Two pictures.
![](./examples.png)

Not abelian.


### 3

**a.** $V$.

**b.** $R_{270}$.

**c.** $R_0$.

**d.** $R_0$, $R_{180}$, $H$, $V$, $D$, $D'$.

**e.** None.


### 5

We follow our intuition and generalize the cases of $D_4$ and $D_3$ with no formal   argumentation.

For both cases, Elements include rotations $\nfrac{i}{n} 360$ for $i = 1, 2, \dots,  n-1$. Counts $n$.

**Even case only.** Flips about the $ith$ diagonal (counts $n/2$), and Flips    about the $ith$ axis (counts $n/2$)

**Odd case only.** Flips about the $ith$ diagonal (counts $n$).

$D_n$ is going to have a total of $2n$ elements; This fact was mentioned in the      textbook though.


### 11

Notation. We donate _Rotation_ by _T_ and _Reflection_ by _F_.

Lemma. Through Caylay table in page 33, $TT = T$, $FF = T$, $TF = F$, and $FT = F$.  In other words $X^2 = T$, and $XY = F$ if $X \neq Y$.

Theorem. Observe we can re-structure the given composed function as $a^2b^2b^2 ac    c^2 c^2 a^2 ac = TTTacTTTac = (TTTac)^2 = T$.

Therefore, Regardless of the choices of $a, b, c$, The given function is always a    _rotation_.


### 13

$D = H R_{90} = R_{90} V$.


### 21

$X \neq H, V, D, D', R_0, R_{180}$, As otherwise $X^2 = R_0$ and then $Y = R_{90}$.  For either of the remaining two cases $X = R_{90}$ or $X = R_{270}$, Necessarily $Y  = R_{270}$.
