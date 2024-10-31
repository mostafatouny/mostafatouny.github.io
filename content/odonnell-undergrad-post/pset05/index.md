---
title: Problem Set 05
math: true
date: "2023-04-30"
---

## Ex. 0

Naively we guess any transformation $f$ of Boolean formulas preserves the property of satisfiability. Hence it would always be the case
$$
\begin{aligned}
w \not\in \textit{UNSAT} \leftrightarrow f(w) \in \textit{SAT}
\end{aligned}
$$


## Ex. 1 

Since the questions is about factor $a$ we can ignore constants. $n^r + {(n^l)}^b = n^{r+lb}$. So $a = r+lb$.


## Ex. 2

following NTM simulation by DTM, partition states into H1 and H2 subsets, and apply the same procedure on each. now the combination of delta1 and delta2 reaches all possible states of NTM.

**First.** *sipser-NTM* can be viewed as a sequence of states, Each of which, is a subset of a deterministic TM's states. A state of *binary-NTM* can be viewed as a subset of exactly two states from a deterministic TM. Since there are no restrictions on the number of elements of *sipser-NTM*'s subset, *binary-NTM* can be seen as a special case of it.

**Second.** Recall the proof idea of a deterministic TM simulating a non-deterministic TM, whereby a determinstic state encodes/resembles a non-determinstic subset of states. Following the same idea, partition $Q = Q_1 \cup Q_2$ and define $Q_1' = P(Q_1)$ and $Q_2' = P(Q_2)$. Here $P(Q_i)$ means the set of all subsets of states $Q_i$. Let $\delta_1$ and $\delta_2$ be responsible of $Q_1'$ and $Q_2'$, respectively. Observe any state of $P(Q)$ can be constructed by some $x \cup y$ where
$x \in Q_1'$ and $y \in Q_2'$. Therefore, Any configuration sequence of *sipser-TM* can be encoded/represented by some configuration sequence of *binary-TM*.


## Ex. 3

The proof is shown by constructing a *non-deterministic* *exponential-time* algorithm for solving *IMPLICIT-4COL*.

Given a circuit $C$, Construct its graph $G_C$ by enumerating all possible $2^n$ inputs of $i$ and all $2^n$ inputs of $j$, Computing $C(i,j)$, for $i \neq j$. The complexity is $2^n \times 2^n = 2^{n+1}$; Exponential.

Check whether the graph $G_C$ is 4-colorable. For each vertex of the graph, non-determinstically brute-force all the possible 4 colours. Since there are $2^n$ vertices, The complexity is *NEXP*.

Clearly the total complexity of a subroutine of *EXP* followed by a subroutine of *NEXP*, is *NEXP*.


## Ex. 4

We construct the reduction function through a polynomial algorithm. Let *C_colorable* and *C_uncolorable* be some fixed 4-colorable and 4-uncolorable graphs.

```
    L-to-3COL(w)
      check whether w is in L by the given polynomial algorithm
      if w belongs to L output C_colorable
      otherwise output C_uncolorable
```
Observe our mapping necessarily satisfies
$$
w \in L \leftrightarrow \textit{L-to-3COL(w)} \in 3COL
$$
