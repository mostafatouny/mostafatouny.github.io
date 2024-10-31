---
title: "Lab 02"
math: true
date: "2023-11-03"
---

$\newcommand{\nfrac}[2]{\frac{\displaystyle{#1}}{\displaystyle{#2}}}$

## Exercises {#exercises .unnumbered}

### 2.1.1 {#section .unnumbered}

**(a)**

```
    def sumOfArrayNumbers(A[0 .. n-1])
      sum = 0
      for i in 0..n-1
        sum = sum + A[i]
      return sum
```

n; Summation; no.

**(b)**
```
    def factorial(n)
      res = 1
      for i in n..1
        res = res * i
      return res
```

1; Multiplication; yes.

**(c)**

Algorithm is in page 61.

```
    def maxElementInArray(A[0..n-1])
      max = A[0]
      for i in 1..n-1
        if A[i] > max
          max = A[i]
      return max
```

n; Comparison; no.

**(d)**

```
    def gcd(m,n)
      while n != 0
        r = m mod n
        m = n
        n = r
      return m
```

2; mod operation; yes.

**(e)** Homework.

**(f)** Homework.

### 2.1.3 {#section-1 .unnumbered}

Yes.

*Classical Search*

-   Worst-case is $\mathcal{O}(n)$.
-   Average-case is $1 \cdot \frac{\displaystyle{1}}{\displaystyle{n}} + \dots + n \cdot \frac{\displaystyle{1}}{\displaystyle{n}} = \frac{\displaystyle{1}}{\displaystyle{n}} (1 + \dots + n) = \frac{\displaystyle{1}}{\displaystyle{n}} \frac{\displaystyle{n(n+1)}}{\displaystyle{2}} = \frac{\displaystyle{n+1}}{\displaystyle{2}} = \mathcal{O}(n)$.
-   Best-case is $\mathcal{O}(1)$.

*Varied Search*

Worst-case, Average-case, and Best-case, are all $\Omega(n)$. For any determinstic algorithm not reading all the $n$ cells, We can construct a counter-example input.

P.S. Big-Oh is used to upper-bound complexity, showing an algorithm is efficient. So it can't be used here while we are showing the inefficiency.

### 2.2.5 {#section-2 .unnumbered}

$5 \lg(n+100)^{10}, \ln^2 n, n^{1/3}, 0.001n^4 + 3n^2 + 1, 3^n, 2^{2n}, (n-2)!$

### 2.2.12 {#section-3 .unnumbered}

**Homework**

### 2.3.4 {#section-4 .unnumbered}

**(a)** $s(n)_{i=1}^n = \sum_{i=1}^n i*i$, The sum of squares up to $n$.

**(b)** Multiplication.

**(c)** $\sum_{i=1}^n 1 = n(1) = n$.

**(d)** $\mathcal{O}(n)$.

**(e)** **Homework**.

### 2.3.6 {#section-5 .unnumbered}

**(a)** **Homework**.

**(b)** Comparison.

**(c)**
$\sum_{i=0}^{n-2} \sum_{j=i+1}^{n-1} 1 = \sum_{i=0}^{n-2} (n-1) - (i+1) + 1 = \sum_{i=0}^{n-2} n-i-1 = (n+1) + n + \dots + (n - (n-2) - 1) = \frac{\displaystyle{n(n+1)}}{\displaystyle{2}}$

**(d)** $\mathcal{O}(n^2)$

**(e)** **Homework**.

### 2.4.3 {#section-6 .unnumbered}

**(a)**

\begin{aligned}
    S(n) &= S(n-1) + 2 \\
         &= S(n-2) + 4 \\
         &\dots \\
         &= S(n-(n-1)) + 2(n-1) \\
         &= 0 + 2n - 2
\end{aligned}

Hence $\mathcal{O}(n)$.

**(b)** **Homework**.

## 2.4.9 {#section-7 .unnumbered}

**(a)** **Homework**.

**(b)**

\begin{aligned}
    S(n) &= S(n-1) + 1 \\
         &= S(n-2) + 2 \\
         &\dots \\
         &= S(n-(n-1)) + n-1 \\
         &= 1 + n - 1
\end{aligned}

Hence $\mathcal{O}(n)$

## 2.5.10 {#section-8 .unnumbered}

**Homework**

## 2.5.12 {#section-9 .unnumbered}

**Homework**

## 2.6.1 {#section-10 .unnumbered}

No count of the comparison basic operation $A[j] > v$ in case it is $False$.

Fix by adding `if j >= 0 then count = count+1` after the end of while.

## 2.6.10 {#section-11 .unnumbered}

**Homework**
