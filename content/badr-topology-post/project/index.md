---
title: Topological Combinatorics through Kneser Graph
math: true
date: "2025-05-27"
---

## Preliminaries

### Graph Theory

**Definition.** A coloring is proper if no adjacent vertices are assigned the same color.

**Definition.** The chromatic number $\chi(G)$ is the smallest number of colours to colour a graph.


### Complex Analysis

**Definition.** A curve $\gamma$ in open $U \subseteq \mathbb{C}$ is $$\gamma: [a,b] \rightarrow U$$

**Notation.** The curve $\gamma$ could be expressed as a parameteric function $f(e^{2 \pi i t})$ for $0 \leq t \leq 1$.

**Definition.** The continuity of a complex-valued function is defined in an analogous manner to real-valued functions.

**Definition.** For continuous $F:[a,b] \rightarrow \mathbb{C}$, the integral of $[a,b]$ is $$\int_a^b F(t) \; dt = \int_a^b u(t) \; dt + i \int_a^b v(t) \; dt$$

**Definition.** The winding number with respect to point $\alpha$ over closed path $\gamma$ is $$W(\gamma,\alpha) = \frac{1}{2 \pi i} \int_\gamma \frac{1}{z - \alpha} \; dz$$

**Definition.** The degree of a function $deg(f)$ is the wind number $W(f(e^{2 \pi it}))$.

### Other

**Fact.** Vectors of d-dim sphere are exactly the vectors of the (d+1)-dim Euclidean space whose norm is $1$.

**Fact.** The equator of a d-dim sphere is a subspace of the d-dim Euclidean space.

**Definition.** The distance between a point $x$ and a closed set $C_i$ is $dist(x,C_i) = \inf_{y \in C_i} ||y-x||$, i.e the distance between $x$ and the closest point of $C_i$.

**Fact.** If point $p$ is in closed set $C_i$, then $dist(p, C_i) = 0$, and if not then $dist(p, C_i) > 0$.

**Definition.** Two points of a sphere are antipodal if they are diametrically opposite, i.e expressed as $p$ and $-p$.

**Definition.** The open hemisphere of pole $x$ is $H(x) = \{ y \in \mathbb{S}^d \mid \langle x,y \rangle > 0 \}$.


## Topological Methods

**Lemma 1.** Given $f: S^1 \rightarrow S^1$, and $f(-z) = -f(z) \; \forall z \in S^1$, then $deg(f)$ is odd.

*Proof.* Recall by definition $deg(f) = wind(f(e^{2 \pi it}))$. Set $g:[0,1] \rightarrow S^1$ by $g(t) = f(e^{2 \pi it})$.

If $z = e^{2\pi it}$ then $-z = e^{\pi i} = e^{\pi i}z = e^{\pi i} e^{2 \pi it} = e^{\pi i + 2 \pi it} = e^{2 \pi i (t + 1/2)}$.

If $0 \leq t \leq \frac{1}{2}$ then $\frac{1}{2} \leq t+\frac{1}{2} \leq 1$. We have $g(t+\frac{1}{2}) = f(e^{2 \pi i (t + 1/2)}) = f(-z) = -f(z) = -f(e^{2\pi it}) = -g(t)$.

For a partition of $[0,1]$ into $[0,\frac{1}{2}] \cup [\frac{1}{2}, 1]$, partition $[0, \frac{1}{2}]$ into $\bigcup_{k=1}^n [t_{k-1}, t_k]$, where $|\theta_k| < \frac{\pi}{2}$ for $\frac{g(t_k)}{g(t_{k-1})} = e^{i \theta_k}$. Partition $[\frac{1}{2}, 1] = \bigcup_{k=1}^n [\frac{1}{2} + t_{k-1}, \frac{1}{2} + t_k]$.

It follows $\frac{g(\frac{1}{2} + t_k)}{g(\frac{1}{2} + t_{k-1})} = \frac{-g(t_k)}{-g(t_{k-1})} = e^{i \theta_k}$.

Observe an approximation of the integral of the winding number would be $$\frac{1}{2\pi} \left ( \sum_{i=1}^n f(z_i) \cdot \Delta_i \right ) = \frac{1}{2\pi} (\theta_1 + \dots + \theta_n + \theta_1 + \dots + \theta_n)$$

Observe $g(\frac{1}{2}) = -g(0)$, and
$$\begin{aligned}
    \frac{g(t_n)}{g(t_{n-1})} \cdot \frac{g(t_{n-1})}{g(t_{n-2})} \cdot \dots \cdot \frac{g(t_2)}{g(t_1)} \cdot \frac{g(t_1)}{g(t_0)} &= \frac{t_n}{t_0} = \frac{1/2}{0} = -1 \\
    e^{i \theta_n} \cdot e^{i \theta_{n-1}} \cdot \dots \cdot e^{i \theta_2} \cdot e^{i \theta_1} &= \\
    e^{i(\theta_1 + \theta_2 + \dots + \theta_n)} &=
\end{aligned}$$
But we know $e^{i \pi} = -1$. Hence $\theta_1 + \theta_2 + \dots + \theta_n = \pi + 2 \pi N$ for some integer $N$.

It follows the wind approximation is $$\frac{1}{2 \pi}((\pi + 2 \pi N) + (\pi + 2 \pi N)) = \frac{1}{2 \pi}(2 \pi + 4 \pi N) = 1 + 2N$$ which is an odd number.

Indeed, a sequence of odd numbers converges to an odd number. Therefore, the winding number is odd.

**Lemma 2.** No map $f:S^2 \rightarrow S^1$ such that $f(-p) = -f(p) \; \forall p \in S^2$.

**Theorem.** 2-dim Borsuk-Ulam. If $f: S^2 \rightarrow \mathbb{R}^2$ is continuous, then $\exists p \in S^2$ such that $f(-p) = f(p)$.

*Proof.* Suppose towards contradiction $f(x) \neq f(-x) \; \forall x \in S^2$. Construct map $g: S^2 \rightarrow S^1$ by $$g(x) = \frac{f(x) - f(-x)}{|| f(x) - f(-x) ||_2} \in S^1 \\ $$ Observe $$\forall x \in S^2 \quad g(-x) = \frac{f(-x) - f(-(-x))}{|| f(-x) - f(-(-x)) ||_2} = \frac{f(-x) - f(x)}{|| f(-x) - f(x) ||_2} = -g(x)$$ Contradicting *lemma 2*.

**Theorem.** Borsuk-Ulam. If $f: S^n \rightarrow \mathbb{R}^n$ is continuous, then $\exists p \in S^n$ such that $f(-p) = f(p)$.

The proof is a natural generalization but requires concepts beyond a first course in topology.

**Theorem.** Lyusternik & Shnirel'man. If $S^n$ is covered by closed sets $C_1, C_2, \dots, C_n, C_{n+1}$, then there $p \in S^n$ and $C_i$ such that $p,-p \in C_i$.

*Proof.* Assume towards contradiction that if $p \in C_i$ then $-p \not\in C_i$ for all $p \in S^n$. Define functions $f_1, f_2, \dots, f_{n+1}: S^n \rightarrow \mathbb{R}$ by $f_i(x) = dist(x, C_i)$. Construct $f: S^n \rightarrow \mathbb{R}^n$ by $f(x) = (f_1(x) - f_{n+1}(x), f_2(x) - f_{n+1}(x), \dots, f_n(x) - f_{n+1})$.

By *Borsuk-Ulam* there are $p, -p \in S^n$ such that $f(p) = f(-p)$. It follows for all $1 \leq i,j \leq n+1$
$$\begin{aligned}
    f_i(p) - f_{n+1}(p) &= f_i(-p) - f_{n+1}(-p)\\
    f_j(p) - f_{n+1}(p) &= f_j(-p) - f_{n+1}(-p)
\end{aligned}$$
So $f_i(p) - f_j(p) = f_i(-p) - f_j(-p)$.

Since $p \in S^n = C_1 \cup \dots \cup C_{n+1}$, we get $p \in C_i$ for some $i$. Similarly $-p \in S^n$ so $-p \in C_j$ for some $j$. By hypothesis $i \neq j$. Clearly $f_i(p) = f_j(-p) = 0$. Then
$$\begin{aligned}
    f_i(p) - f_j(p) &= f_i(-p) - f_j(-p) \\
    -f_j(p) &= f_i(-p)
\end{aligned}$$
But $f_j(p) > 0$ since $p \not\in C_j$, and similarly $f_i(p) > 0$. So we have an equality between a negative and a positive number. Contradiction.


## Theorems

**Definition.** The Kneser graph $KG_{n,k}$ for $n \geq 2$, $k \geq 1$, has vertex set $C([n], k)$, and any two vertices $u,v \in C([n], k)$ are adjacent if and only if they are disjoint, i.e. $u \cap v = \phi$.

**Theorem.** The chromatic number of the Kneser graph $KG_{n,k}$ is $n-2k+2$.

Fix $n$ and $k$. Assume for the sake of contradiction, the chromatic number of Kneser graph $KG_{n,k}$ is less than $n-2k+2$. Then we have a proper coloring $c: C([n], k) \rightarrow \{ 1, \dots, n-2k+1 \}$ using at most $n-2k+1$ colors. Set $d = n-2k+1$ and take a set $X$ of $n$ vectors on the d-dim sphere $\mathbb{S}^d$ where any $d+1$ vectors are linearly independent.

Let $U_i = \{ x \in \mathbb{S}^d \mid \exists k\text{-set} \; S \subset X, c(S) = i, S \subset H(x) \}$ for $i=1,\dots,d$, and take complement $A = \mathbb{S}^d \setminus (U_1 \cup \dots \cup U_d)$. We claim each $U_i$ is open.

To see why, fix a point $y \in S^{d}$, and observe $U_{y} = \{ x \in S^{n-1} : \langle x, y \rangle > 0 \}$ is open as it is the preimage of the open set $(0, \infty)$ under the continuous map $f_y(x) = \langle x, y \rangle$.\ For finite k-subset $B = \{ y_1, \dots, y_k \}$, Observe $$U_B = \bigcap_{j=1}^k U_{y_j} = \left\{ x \in S^{n-1} : \langle x, y_j \rangle > 0 \ \forall j \right\}$$ is an intersection of finitely many open sets, hence *open*.

Therefore $U_i = \bigcup_{\substack{B \in \binom{[n]}{k} \\ c(B)=i}} U_B$ is a union of open sets, hence *open*. Moreover complement $A$ is closed.

Clearly $A$ alongside $U_i$ do cover $\mathbb{S}^d$. So if none of them contains a pair of antipodal points, then neither does $\mathbb{S}^d$, hence contradicting the *Lyusternik & Shnirel'man* theorem. We aim to reach that contradiction. Consider $x \in \mathbb{S}^d$.

*Case 1.* $x \in U_i$, i.e $H(x)$ contains a k-subset colored with color $i$, corresponding to a vertex colored $i$. Since $H(x)$ and $H(-x)$ are disjoint, any k-subset in $H(-x)$, is disjoint from any k-subset in $H(x)$. Thereby, corresponding vertices are adjacent. Since the coloring is proper by hypothesis, $H(-x)$ does not contain a k-subset colored with $i$, hence $-x \not\in U_i$.

*Case 2.* $\pm x \in A$. By definition of $A$, neither $H(x)$ nor $H(-x)$ contains a k-subset of $X$. Hence each of $H(x)$ and $H(-x)$ contains at most $k-1$ vectors. It follows there is at least $n-2(k-1) = n-2k+2 = d+1$ points in the equator $\{ y \in \mathbb{S}^d \mid \langle x,y \rangle = 0 \}$, contained in a subspace of dim d, concluding they are linearly dependent. Contradiction.

Finally we show a valid constructive coloring of $KG_{n,k}$ using $n-2k + 2$ colors. Color each k-set with all elements in $[2k - 1]$ with one color, and every other k-set by their largest element. Thereby we use at most $n - (2k-1) + 1 = n - 2k + 2$ colors, where all k-sets of a given color intersect.


## Resources

-   [Borsuk-Ulam Theorem by Nicolas Bourbaki](https://www.youtube.com/watch?v=gk6Unu78e-w)
-   [Kneser's Conjecture by Nicolas Bourbaki](https://www.youtube.com/watch?v=zG9Y1ksp3Qw)
-   [A Course in Topological Combinatorics, Chapter 2, by Longueville](https://link.springer.com/book/10.1007/978-1-4419-7910-0)
-   [Lecture 14. Combinatorics by Jacob Fox](http://math.mit.edu/~fox/MAT307-lecture14.pdf)
