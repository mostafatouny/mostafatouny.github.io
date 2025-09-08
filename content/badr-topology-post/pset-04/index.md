---
title: Homework 04
math: true
date: "2025-05-26"
---

## Exercises

### 2

Yes. Take arbitrary open $U \ni f(x)$. By continuity $f^{-1}(U)$ is open. Moreover $x \in f^{-1}(U)$. By hypothesis $f^{-1}(U) \cap A \neq \phi$. It follows $\phi \neq f \left ( f^{-1}(U) \cap A \right ) \subseteq f(f^{-1}(U)) \cap f(A) = U \cap f(A)$.

### 3

#### (a)

$(\leftarrow)$ For open $U \subseteq X$, by hypothesis $i^{-1}(U) = U$ is also open in $X'$.

$(\rightarrow)$ Take $U \in \Tau$. By definition $U \subseteq X$. By hypothesis $i^{-1}(U) = U$ is open in $X'$, i.e $U \in \Tau'$.

#### (b)

By $(a)$, $i$ continuous $\longleftrightarrow \Tau' \supseteq \Tau$.

Consider the continuous $i^{-1}:X \rightarrow X'$ map. By $(a)$, $i^{-1}$ continuous $\longleftrightarrow \Tau' \subseteq \Tau$.

The intended conclusion follows.

### 5

Construct $f: (a,b) \rightarrow (0,1)$ where $f(x) \mapsto \dfrac{x-a}{b-a}$. It is injective as $\dfrac{x-a}{b-a} = \dfrac{x'-a}{b-a}$ implies $x = x'$, and surjective as for $y \in (0,1)$ we can take $x$ such that $b > x = y(b-a)+a > a$ implying $f(x) = y$. Hence $f$ is bijective.

Observe for $(c,d) \subseteq (0,1)$ we have $f^{-1}(c,d) = (c(b-a)+a, d(b-a)+a)$. For an arbitrary open $U \subseteq (0,1)$, we know $U = \bigcup_n (a_n, b_n)$. Thereby $f^{-1}(U_n (a_n, b_n)) = \bigcup_n f^{-1}(a_n, b_n)$ a union of open sets, which in turn is open.

To show $[a,b]$ is homeomorphic with $[0,1]$, consider the function $f: [a,b] \rightarrow [0,1]$ where $f(x) \mapsto \dfrac{x-a}{b-a}$. Then for $y \in [0,1]$ we can take $x$ such that $b \geq x = y(b-a) + a \geq a$. The remaining parts of the proof are analogous.

### 9

#### (a)

Observe given a well-defined $f: X \rightarrow Y$, if some $x \in A \cap B$ then $f|A(x) = f|B(x)$. Hence, the *Pasting Lemma* is applicable.

It follows if $f|(A_1 \cup \dots \cup A_{N-1})$ is continuous and $f|A_N$ is continuous, then so is $f|(A_1 \cup \dots \cup A_N)$. By ordinary induction the intended result follows on any finite collection $\{ A_\alpha \}$.

#### (b)

**Lemma.** Let $Y$ be a subspace of $X$. if $U$ is closed in $X$ and $U \subseteq Y$, then $U$ is closed in $Y$.

We know $X - U$ is open in $X$. Then $Y \cap (X - U)$ is open in $Y$. It follows $$\begin{aligned}
    Y \cap (X - U) &= (Y \cap X) \cap (Y - U) \\
    &= Y \cap (Y - U) \\
    &= Y - U
\end{aligned}$$
Thus $Y - (Y - U) = U$ is closed in $Y$.

**Theorem.** main problem.

Consider the function $f: (0,1) \rightarrow \mathbb{R}$ where $x \mapsto 2x$. It is not continuous as $[0,1]$ is closed in $\mathbb{R}$ but $f^{-1}([0,1]) = (0,1/2]$ is not closed in $(0,1)$.

Take $A_n = \left [ \dfrac{1}{n}, 1 - \dfrac{1}{n} \right ]$ and observe $\bigcup_n^\infty A_n = (0, 1)$.

Let $B$ be an arbitrary closed set in $\mathbb{R}$. Then $\{ y/2 \mid y \in B \}$ is closed in $\mathbb{R}$. To see why, take $z$ a limit point of it. Then $2z$ would be a limit point of $B$ and it follows $2z \in B$, concluding $2z/2 = z$ is contained in the set.

Thereby $f^{-1}|A_n(B) = \{ y/2 \mid y \in B \} \cap A_n$ is closed in $\mathbb{R}$. Since $A_n$ is a subspace of $\mathbb{R}$ and $f^{-1}|A_n(B) \subseteq A_n$, by our lemma, we conclude $f^{-1}|A_n(B)$ is closed in $A_n$ also.

### 10

Let $U \times V$ be an arbitrary open set of $B \times D$. By definition $U$ and $V$ are respectively open in $B$ and $D$. By hypothesis the following are open sets
$$\begin{aligned}
    f^{-1}(U) &= \{ a \in A \mid f(a) \in U \} \\
    g^{-1}(V) &= \{ c \in C \mid g(c) \in V \}
\end{aligned}$$
Moreover, by definition
$$\begin{aligned}
    (f \times g)^{-1} (U \times V) &= \{ (a,c) \in A \times C \mid f(a) \in U \wedge f(c) \in V \} \\
    &= f^{-1}(U) \times g^{-1}(V)
\end{aligned}$$
Which is open by definition of product topology.

### 13

Let $g_1: \bar{A} \rightarrow Y$ and $g_2: \bar{A} \rightarrow Y$ be two extensions of $f$. Then $g_1(x) = g_2(x) \; \forall x \in A \; (1)$. Take $x \in \bar{A}$ and assume towards contradiction $g_1(x) \neq g_2(x)$.

Note $\forall \, U \ni x$ open, $U \cap A \neq \phi \; (2)$.

Since $Y$ is Hausdorff, there are open sets $V_1 \ni g_1(x)$ and $V_2 \ni g_2(x)$ where $V_1 \cap V_2 = \phi$ $(3)$.

By continuity of $g_1$ and $g_2$ along *thm 18.1*, there are open $U_1 \ni x$ and $U_2 \ni x$ such that $g_1(U_1) \subseteq V_1$ and $g_2(U_2) \subseteq V_2$ $(4)$.

Take open $U = U_1 \cap U_2$ and note $U \ni x$, implying by $(2)$ $\exists x_0 \in U \cap A$. By $(1)$, $g_1(x_0) = g_2(x_0)$. By $(4)$, a contradiction of $(3)$ is reached $\blacksquare$
