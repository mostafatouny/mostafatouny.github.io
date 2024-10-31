---
title: "Lab 01"
math: true
date: "2023-11-03"
---

$\newcommand{\nfrac}[2]{\frac{\displaystyle{#1}}{\displaystyle{#2}}}$

## Exercises {#exercises .unnumbered}

### 1.1.4 {#section .unnumbered}

*Hints*
-   You are given a square number $n$. Given some integer $k$, How can we verify it is the root?
-   Follow the exhaustive search strategy, to find the root of $n$.
-   You are given a real number $r$. Given some integer $k$, How can we verify it is the floor of $r$?
-   Follow the exhaustive search strategy, to find the floor of $n$.
-   Combine all previous hints to find a unique definition of $\lfloor \sqrt{n} \rfloor$.
-   Follow the exhaustive search strategy, to solve the main problem.

*Solution*
```
      for i in n-1 .. 0
        if (i)^2 <= n
          return i
```

### 1.1.8 {#section-1 .unnumbered}

*Hints*
-   Try this case on concrete examples like $m = 2$ and $n = 3$.
-   Why $m \mod n = m$ when $m < n$?
-   Recall the definition of mod. What are the possible ranges of $x \mod n$ for any integer $x$?

*Solution*

It shall swap them as $r = m \mod n = m$ when $m < n$.

Only once. Given $m > n$, Necessarily $n > m \mod n$.

## 1.2.5 {#section-2 .unnumbered}

*Hints*
-   Convert a concrete decimal number to binary. Observe how the right most digit from the binary representation is obtained.
-   Given a binary representation, What is the number we divide on it,
    so that the quotient eliminate the right most digit?
-   Follow the *Decrease and Conquer* strategy, with the above two hints, to solve the problem.

*Solution*
```
    DecToBin(n):
      # input: integer n
      # output: binary representation as a list

      # binary representation
      l = [ ]

      while n != 0:
        # kth digit from right to left
        b.appendLeft( n % 2 )

        # remove the rightmost digit
        # division output is an integer
        n = n/2
```

### 1.2.9 {#section-3 .unnumbered}

*Hint*
-   Are there duplicated computations?
-   Are there pairs tested twice?
-   Observe $| a - b | = | b - a |$.
-   If we checked all elements with $A[i]$, Do we need to test $A[j]$ with $A[i]$?

*Solution*
```
MinDistance( A ):
      # input: array of size n
      # output: minimum distance between two distinct elements

      dmin = infinity
      for i in 0 .. n-1:
        for j in i+1 .. n-1:
          dis = | A[i] - A[j] |
          if dis < dmin:
            dmin = dis
```


## 1.3.1 {#section-4 .unnumbered}

*Hints*

-   if $A[i] == A[j]$ which index shall be counted? What can we conclude about $S$?

*Solution*

**a**. Tedious to typeset.

**b**. No. Observe counting only happens when strictly $i < j$. If $A[i] == A[j]$ then the code counts $A[i]$ not $A[j]$. Therefore $A[i]$

shall succeed $A[j]$. In fact equal cells are reversed in the sorted array.

**c**. No. It does not modify array $A$ but output is a different array $S$.


## 1.4.2 {#section-6 .unnumbered}

*Hint*

-   For ascendingly ordered array $A$, Is it possible for the target value $t$ to exist in $A[i..n-1]$ given the fact $t > A[i]$?
-   Use the above hint to prune the search space.
-   Which index of the array you think shall prune the greatest search space.

*Solution*

For target value $t$:

**a**. Access some element $x$ in the array. If $t \neq x$, We can ignore searching in the right/left side of $x$.

**b**. While linear scanning, Terminate the algorithm earlier once some $A[i] > t$.

## 1.4.10 {#section-7 .unnumbered}

*Hints*
-   Is it possible for two strings to be anagrams in case they different
    lengths?
-   Is it possible for two strings to be anagrams if one of them has a
    character not present in the other?
-   You can convert a character to its corresponding ascii number. Use
    that for a cheaper data strucutre.
-   the ascii number corresponds to an index.

*Solution*

Two strings are *anagrams* if and only if they have the same count of
characters.

```
      AreStringsAnagrams(A, B):
        # input two strings
        # output True if anagrams and False otherwise
        
        # if lengths are not the same, then not anagrams
        if length(A) != length(B):
          return False

        # initialize characters counts to zeros for both strings
        A_chCount = B_chCount = [ 0 ] * 26

        # Count characters in both strings
        for ch in A:
          A_chCount[ int(ch) ] = A_chCount[ int(ch) ] + 1

        for ch in B:
          B_chCount[ int(ch) ] = B_chCount[ int(ch) ] + 1

        # Anagrams if and only if characters count is exactly the same
        return A_chCount == B_chCount
```
