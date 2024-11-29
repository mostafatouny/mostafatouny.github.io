# Abstract

The interaction between discrete and continuous math gained attraction
recently.

We study the winning domination vs scoring equity of Round-Robin
tournaments, Under Erdős--Rényi Model, where vertices number tends to
infinity. Particularly, we show players scoring tend to get closer to
the mean.

We also prove on complete bipartite matches $U \times V$, No matter how
small the proportion of $U$, As vertices number tends to infinity, every
player in $V$ is more likely to lose from some player in $U$.

# Background

A curious book illustrating beautiful intersections between discrete and
continuous math is Pinsky's [Problems from the Discrete to the
Continuous](https://link.springer.com/book/10.1007/978-3-319-07965-3).

Lázló Lovász initiated the study of graph limits, especially dense
graphs through symmetric measurable functions named Graphons. See Yufei
Zhao's [Graph Theory and Additive
Combinatorics](https://ocw.mit.edu/courses/18-225-graph-theory-and-additive-combinatorics-fall-2023/).

# Definitions

**Complete Bipartite Graph.** A graph $K_{U,V}$ such that its vertices
can be divided into two disjoint sets $U$ and $V$, and edges
$E = U \times V$ of all possible pairs.

**Round-Robin Tournament.** $n$ contestants play $\dbinom{n}{2}$ matches
whereby each pair of contestants play against each other exactly once. A
match results in a winner and loser. For a player $k$, Let $score[k]$ be
the number of winnings out of the total $n-1$ matches she plays.

**Erdős--Rényi Model.** In $G(n, p)$ a random graph is constructed by
randomly connecting each pair of nodes with probability $p$. The number
of vertices $n$ is fixed.

# Methods

**Bernoulli Random Variable.** An $X$ such that $Pr[X=1] = p$ and
$Pr[X=0] = 1-p$, for some $0 \leq p \leq 1$. $$\begin{aligned}
    \text{Variance} \quad \sigma^2 &= Var[X] = np (1-p) \\
    \text{Mean} \quad \mu &= Ex[X] = np
\end{aligned}$$ source: Ross. A First Course in Probability, section
6.1, page 142.

**Chebyshev Inequality.** For any $k > 0$,
$$Pr[ |X - \mu| \geq k ] \leq \nfrac{\sigma^2}{k^2}$$ source: Ross. A
First Course in Probability, proposition 2.2, page 398.

**Limit Sandwiching.** If $g(x) \geq f(x) \geq h(x)$ then
$$\lim_{x \rightarrow c} g(x) \geq \lim_{x \rightarrow c} f(x) \geq \lim_{x \rightarrow c} h(x)$$

**Murphy's Law.** For mutually independent events
$A_1, A_2, \dots, A_n$, $T_i$ indicator random variable for $A_i$, and
$T = T_1 + \dots + T_n$, It follows $$Pr[T=0] \leq e^{ -Ex[T] }$$
source: MIT's Math for CS, thm 19.6.4, page 815.

# Remarks

**Graph-based interpretation of tournament results.** Outcomes of $n$ contestants can be interpreted as a direct graph, whereby for each pair of players $(a,b)$, exactly $(a,b) \in G(E)$ or $(b,a) \in G(E)$.


# Results

**Theorem.** In a Round-Robin tournament of $n$ players, Drawing is
possible for any $n \geq 3$ players.

The proof is constructive. Fix players $p1$, $p2$, and $p3$. Assign $p1$
loses from $p2$ and wins remaining $n-2$ players. Assign $p2$ loses from
$p3$ and wins remaining $n-2$ players. Then
$score[p1] = score[p2] = n-2$. As $p1$ and $p2$ are fully assigned, any
other player wins at most $n-3$ times.

**Theorem.** In a Round-Robin tournament of $n$ players, and with a
winning probability $p = \nfrac{1}{2}$ for all players, The probability
of \"Domination\" where a player beats all others tends to zero as
$n \rightarrow \infty$.

Let $E_i$ denote ith player wins all others. $$\begin{aligned}
    Pr[E_i] &= \left ( \nfrac{1}{2} \right )^{n-1} \\
    Pr[U_i E_i] &= \sum_{i=1}^n Pr[E_i] = n \cdot \nfrac{1}{2^{n-1}} \quad &\text{mutually exclusive events} \\
    \lim_{n \rightarrow \infty} Pr[U_i E_i] &= \lim_{n \rightarrow \infty} \nfrac{n}{2^{n-1}} = \lim_{n \rightarrow \infty} \nfrac{1}{2^{n-1} \ln 2 } = 0 \quad &\text{L'Hopital}
\end{aligned}$$

**Theorem.** In a Round-Robin tournament of $n$ players, Fix a player
$k$. Let $\mu_k$ be the mean of $score[k]$, i.e its expectation. Then
$$\lim_{r \rightarrow 0} \lim_{n \rightarrow \infty} Pr [ |score[k] - \mu_k| \geq r \cdot \mu_k ] = 0$$
Observe $$\begin{aligned}
    \text{Variance} \quad \sigma^2 &= (n-1) \left ( \frac{1}{2} \right ) \left ( 1-\frac{1}{2} \right ) = \frac{1}{4} (n-1) \\
    \text{Mean} \quad \mu &= \nfrac{n-1}{2}
\end{aligned}$$ Then for any $r > 0$ $$\begin{aligned}
    Pr[ |score[k] - \mu| \geq r \mu ] &\leq \nfrac{\nfrac{1}{4} \cdot (n-1)}{\left (r \cdot \nfrac{n-1}{2} \right )^2} \\
    &= \nfrac{1}{4} \cdot (n-1) \cdot \nfrac{1}{r^{2}} \cdot \nfrac{2}{n-1} \cdot \nfrac{2}{n-1} \\
    &= \nfrac{1}{r^2(n-1)}
\end{aligned}$$ Since
$\lim_{n \rightarrow \infty} \nfrac{1}{r^2(n-1)} = 0$, It follows by
Limit Sandwiching
$$\lim_{n \rightarrow \infty} Pr[ |score[k] - \mu| \geq r \mu] = 0$$ By
taking $r$ to be arbitrarily small, The intended result follows.

**Theorem.** We are given a complete bipartite graph of matches, with
total $n$ vertices, partitioned by $|U| = \lceil rn \rceil$, and
$|V| = \lfloor (1-r)n \rfloor$. Also $n \geq 1$, $r > 0$, and $p > 0$.
For every player $i = \lceil rn \rceil + 1, \dots, n$ of $V$, Let
$T_i = 1$ iff it won some match. Define
$T = \sum_{i = \lceil rn \rceil + 1}^n T_i$. $$$$ By Murphy
$Pr[T_i = 1] \geq 1 - e^{ - \lceil rn \rceil \cdot p }$. It follows
$$\begin{aligned}
    Ex[T]
    &= Ex[T] \\
    &= \sum_{i=\lceil rn \rceil + 1}^n Ex[T_i = 1] \\
    &= \sum_{i=\lceil rn \rceil + 1}^n Pr[T_i = 1] \quad \text{Indicator Variable} \\
    &\geq \lceil n(1-r) \rceil - \sum_{i=\lceil rn \rceil + 1}^n e^{- \lceil rn \rceil p} \\
    Ex[T/|V|] &= \frac{1}{|V|} Ex[T] \\
    &\geq \frac{1}{|V|} \lceil n(1-r) \rceil - \frac{1}{|V|} \sum_{i=\lceil rn \rceil + 1}^n e^{- \lceil rn \rceil p} \\
    &= \frac{\lceil n(1-r) \rceil}{\lceil n(1-r) \rceil} - \nfrac{1}{\lceil n(1-r) \rceil} \sum_{i=\lceil rn \rceil + 1}^n e^{- \lceil rn \rceil p} \\
    &= 1 - \nfrac{1}{\lceil n(1-r) \rceil} \sum_{i=\lceil rn \rceil + 1}^n e^{- \lceil rn \rceil p}
\end{aligned}$$ Therefore
$$\lim_{n \rightarrow \infty} 1 - \nfrac{1}{\lceil n(1-r) \rceil} \sum_{i = \lceil rn \rceil + 1}^n e^{- \lceil rn \rceil p} = 1 - 0 \cdot (0 + \dots + 0) = 1$$
Since $Pr[T_i=1] \leq 1$,
$$Ex[T/|V|] = \nfrac{1}{\lceil n(1-r) \rceil} \cdot \sum_{\lceil rn \rceil + 1}^n Pr[T_i = 1] \leq \nfrac{1}{\lceil n(1-r) \rceil} \cdot \sum_{\lceil rn \rceil + 1}^n 1 = 1$$

By Sandwiching $\lim_{n \rightarrow \infty} Ex[T/|V|] = 1$.
