---
title: Homework 05
math: true
date: "2024-06-01"
---

## Exercises {#exercises .unnumbered}

### 1 {#section .unnumbered}

**(a).** It follows immediately from *theorem 3.5*, which states a graph
$G$ of order $n$ is a tree iff it is connected and has exactly $n-1$
edges.

**(b).** The condition is $G$ is itself a tree. It is sufficient as $G$
is a subgraph of itself. It is necessary as if we considered an
arbitrary induced subgraph spanning tree $T$, Then by definition of
spanning, $T$ contains all the vertices of $G$. So $T = G$ and $G$ is a
tree.

### 2 {#section-1 .unnumbered}

#### (a) {#a .unnumbered}

Pick a vertex $v$ with maximal degree $k$. For each neighbour
$v_1, v_2, \dots, v_k$, We have paths:
\begin{aligned}
    (v, v_1) \\\\
    (v, v_2) \\\\
    \dots
    (v, v_k)
\end{aligned}
Since the graph is finite, By the *well-ordering* principle, There exists maximal paths $p_1, p_2, \dots, p_k$ such that $p_i$ starts with $(v, v_i)$. It follows $p_i$ ends with a leaf $l_i$.

Since the graph is a tree, The paths $p_i$ do not intersect except on $v$, lest forming a cycle. In other words, leaves $l_i$ are distinct, and hence the $k$ paths do count $k$ leaves.

#### (b) {#b .unnumbered}

We prove it by induction on the tree's order, i.e number of vertices. For the base case, We have $|T| = 2$. Then $T$'s leaves count $L(T)$ is
\begin{aligned}
    2 &= 2 + \sum_{v \in V(T^-)} ( deg(v) - 2 ) \\\\
    &= 2 + 0
\end{aligned}
Since $T^-$ is empty.

Induction hypothesis. Assume the statement is true for any $T$ such that $|T| \geq 2$.

Induction step. Consider a tree $T$ where $|T| = n+1$. Fix a leaf $l$ and its connected neighbour $f$ in $T$.

Observe $f$ cannot be a leaf, As otherwise $T$ shall be of size $2$, Contradicting our assumption. So $f$ is a non-leaf vertex.

Construct tree $T' = T - l$. Then by the induction hypothesis
\begin{aligned}
    L(T') &= 2 + \sum_{v \in T'^-} (deg(v) - 2)
\end{aligned}
Then
\begin{aligned}
    |L(T)| &= |L(T')| + 1 \\\\
    &= 2 + \sum_{v \in T'^-} (deg_{T'}(v) - 2) + 1
\end{aligned}
Observe
\begin{aligned}
    deg_T f &= deg_{T'} f + 1 \\\\
    deg_T u &= deg_{T'} u \quad \text{For any non-leaf vertex u } \neq f
\end{aligned}
It follows
\begin{aligned}
    \sum_{v \in T^- - f} (deg_T v - 2) = \sum_{v \in T'^- - f} (deg_T' v - 2)
\end{aligned}
By $(3)$ and $(5)$,
\begin{aligned}
    \sum_{v \in T^-} (deg_T(v) - 2) &= \sum_{v \in T^- - f} (deg_T(v) - 2) + (deg_T(f) - 2) \\\\
    &= \sum_{v \in T'^- - f} (deg_{T'} v - 2) + (deg_{T'}(f) - 2) + 1 \\\\
    &= \sum_{v \in T'^-} (deg_{T'} v - 2) + 1
\end{aligned}
Combining that last result with (2), We get
\begin{aligned}
    |L(T)| &= 2 + \left ( \sum_{v \in T^-} (deg_T(v) - 2) - 1 \right ) + 1 \\\\
    &= 2 + \sum_{v \in T^-} (deg_T(v) - 2) \quad \blacksquare \\\\
\end{aligned}

### 3 {#section-2 .unnumbered}

**Notation.** We denote the total weight of a graph by $w(G)$, Which is the summation of all edges weights.

We show if there are two distinct minimum spanning trees $T_0$ and $T_1$, where $w(T_0) = w(T_1) = k$, then a contradiction occurs. Namely the existince of a spanning tree $T_2$ such that $w(T_2) < k$.

Since $T_0$ and $T_1$ are distinct, They do not agree on all edges. WLOG we can select the minimal-weight edge $e_{min} = \{ v_1, v_2 \}$ in $T_0$ not in $T_1$. Since $T_1$ is connected, We know there is a path $p_1 = (v_1, \dots, v_2)$ in $T_1$. Fix an edge $e'$ from $p_1$. Construct $T_2 = T_1 - e' + e_{min}$.

The added $e_{min}$ does not construct a new cycle. If that were the case, Then $T_1$ would have had another path $p_2 = (v_1, \dots, v_2)$, Concluding $T_1$ has a cycle by combining $p_1$ and $p_2$. In conclusion $T_2$ is acyclic, i.e a spanning tree.

Recall $e_{min}$ was chosen to be the minimum weight edge. So $w(e_{min}) < w(e')$ and in turn $w(T_2) < w(T_1)$.

### 4 {#section-3 .unnumbered}

$(\rightarrow)$. Let $e$ be an arbitrary bridge. Let $T$ be an arbitrary spanning tree of $G$. Assume for contradiction $T$ does not contain $e$. By definition there are two vertices in $G$, $v_1$ and $v_2$, which are not connected in $G - e$. Since $E(T) \subset E(G)$, It follows there is no path either connecting $v_1$ and $v_2$ in $T$. Contradiction as $T$ spans $G$.

$(\leftarrow)$. Let $e$ be an edge appearing in any spanning tree of $G$.

Consider graph $G-e$, and fix $v_0$ in it. Consider the connected component $C_0$ of $G-e$ containing $v_0$. By definition $e \notin C_0$. Let $T_0$ be the tree spanning $C_0$. By hypothesis $T_0$ does not span the graph $G$. Call the vertex not covered by it $v_1$.

We claim there is no path $(v_0, \dots, v_1)$ in $G-e$ and hence concluding it is disconnected, and in turn $e$ is a bridge. Assume for contradiction we have the path $p_0 = (v_0, \dots, v_1)$ in $G-e$, Then $p_0$ is in $C_0$, and in turn $v_1$ is connected to $v_0$ in $T_0$. Contradiction.
