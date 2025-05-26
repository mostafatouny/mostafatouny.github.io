---
title: Homework 05
math: true
date: "2025-05-26"
---

## Exercises

### 1

We satisfy the definition of a basis for a *Box Topology*.

For $\mathbf{x} = (x_\alpha) \in \prod_\alpha X_\alpha$ we have $x_\alpha \in X_\alpha$, implying the existence of a basis element $B_\alpha$ in $X_\alpha$, where $x_\alpha \in B_\alpha$. Hence $\mathbf{x} \in \prod_\alpha B_\alpha$.

Assume
$\mathbf{x} \in \prod_\alpha B_\alpha \cap \prod_\alpha B'_\alpha$. Then $x_\alpha \in B_\alpha \cap B'_\alpha$, implying the existence of $B''_\alpha$, where $x_\alpha \in B''_\alpha \subset B \cap B'$. Hence $\mathbf{x} \in \prod B''_\alpha \subset \prod B'_\alpha \cap \prod B''_\alpha$.

For a *Product Topology*, the proof is similar, except we will have finitely many $B_\alpha$. Fix $\alpha$ and observe $x_\alpha \in X_\alpha \subset X_\alpha$ where $X_\alpha$ is open.

### 2

We set the following notation:
$$\begin{aligned}
    &\mathcal{B}_{A_\alpha} & &\text{basis of } A_\alpha \\
    &\mathcal{B}_{\Pi X_\alpha} = \{ \Pi_\alpha B_\alpha \mid \text{finitely } B_\alpha \in \mathcal{B}_{X_\alpha} \text{, and remaining } B_\alpha = X_\alpha \} & &\text{basis of product topology } \Pi_\alpha X_\alpha \\
    &\mathcal{B}_{\Pi A_\alpha} = \{ \Pi_\alpha B_\alpha \mid \text{finitely } B_\alpha \in \mathcal{B}_{A_\alpha} \text{, and remaining } B_\alpha = A_\alpha \} & &\text{basis of product topology } \Pi_\alpha A_\alpha \\
    &\mathcal{B}_{\Pi A_\alpha}^{(s)} = \{ B \cap \Pi_\alpha A_\alpha \mid B \in \mathcal{B}_{\Pi X_\alpha} \} & &\text{basis of the subspace induced by } \Pi_\alpha X_\alpha
\end{aligned}$$
It suffices to show $\mathcal{B}_{\Pi A_\alpha} = \mathcal{B}_{\Pi A_\alpha}^{(s)}$.

Observe $X_\alpha \cap A_\alpha = A_\alpha$, and that for $B_\alpha \in \mathcal{B}_{X_\alpha}$ it follows $B_\alpha \cap A_\alpha$ is a basis element of $\mathcal{B}_{A_\alpha}$.

### 6

Take arbitrary $\mathbf{x} \in \prod X_\alpha$ and consider any neighbourhood $U$. Then we have a basis element $B$ where $x \in B \subset U$. By definition $B = \prod U_\alpha$ where finitely many $U_i$ are open in $X_i$ for $i=1, \dots, k$, and remainings are exactly $X_\alpha$. For each $i$, and by hypothesis, all but finitely many $x_n^{(i)}$ are in $U_i$. Let $U'_i = \{ \mathbf{x}_n \mid x_n^{(i)} \in U_i \}$ and take $U' = \bigcap_{i=1}^k U'_i$. Observe all $(\mathbf{x}_n)$ except finite $U'$ are in $U$. $\blacksquare$

Not true for box topology. As a counter example, from analysis we know $f_i(n) = \dfrac{i}{n}$ is point-wise convergent to $0$ but not uniformly convergent to it. Accordingly set $x_n^{(i)} = \dfrac{i}{n}$ for product topology $\mathbb{R}^\omega = \prod_{n \in Z_+} \mathbb{R}$. $\blacksquare$

### 7

We show $R^\infty$ is closed to conclude $cl \left ( R^\infty \right ) = R^\infty$.

Let $\mathbf{x} = (x_1, x_2, \dots)$ be a limit point of $R^\infty$. Then for each $x_i$, we can choose small enough $(a_i,b_i) \ni x_i$, to form an open $U = \prod_i (a_i,b_i)$ of $R^\omega$. It follows, some $\mathbf{x'} = (x'_1, x'_2, \dots) \in U \cap R^\infty$. By definition, $\mathbf{x'}$ has some index $k$ whereby $x'_j = 0$ for all $j \geq k$. But if $0 = x'_j \in (a_j,b_j)$ for arbitrarily small $(a_j,b_j) \ni x_j$, then necessarily $x_j = 0$. So for $\mathbf{x}$ we have $x_j = 0$ for all $j \geq k$, concluding $\mathbf{x} \in R^\infty$. $\blacksquare$

### 10

#### (a)

Consider the set $\mathcal{S} = \bigcup_\alpha \{ f_\alpha^{-1}(U_\alpha) \mid U_\alpha \text{ open in } X_\alpha \}$. The set of all topologies $\Tau_\beta$ containing $\mathcal{S}$ is non-empty as witnessed by the discrete topology. Taking $\bigcap_\beta \Tau_\beta$ is the unique coarsest topology containing $\mathcal{S}$.

The argument follows the same line of reasoning of *exercise 4* in *section 13*.

#### (b)

$\mathbf{\Tau_\mathcal{S}} \supseteq \bigcap_\beta \Tau_\beta$

Generate a topology $\Tau_\mathcal{S}$ by $\mathcal{S}$ as a subbasis. Then by definition it contains all elements of $\mathcal{S}$.

$\mathbf{\Tau_\mathcal{S}} \subseteq \bigcap_\beta \Tau_\beta$

Consider any topology $\Tau_\beta$ containing $\mathcal{S}$. Then by topology's axioms, $\Tau_\beta$ contains finite intersections of $\mathcal{S}$, and in turn arbitrary unions of those intersections. Hence $\Tau_\mathcal{S} \subseteq \Tau_\beta \, \forall \beta$. It follows $\Tau_\mathcal{S} \subseteq \bigcap_\beta \Tau_\beta$.

#### (c)

$(\rightarrow)$ Fix $\alpha$. Take $U_\alpha$ open in $X_\alpha$. Then $f_\alpha^{-1}(U_\alpha)$ is open in $A$ relative to topology $\Tau$. By hypothesis $g^{-1}(f_\alpha^{-1}(U_\alpha))= (f_\alpha \circ g)^{-1}(U_\alpha)$ is open in $Y$.

$(\leftarrow)$ Consider a basis element $B$ in $A$. Relative to topology $\Tau$, we know $B = f^{-1}_{\alpha_1}(U_{\alpha_1}) \cap f^{-1}_{\alpha_2}(U_{\alpha_2}) \cap \dots \cap f^{-1}_{\alpha_k}(U_{\alpha_k})$. For $i = 1, \dots, k$, since $U_{\alpha_i}$ is open in $X_{\alpha_i}$, by hypothesis we have $(f_{\alpha_i} \circ g)^{-1}(U_{\alpha_i}) = g^{-1}(g^{-1}_\alpha (U_\alpha))$ is open.

By topology's axioms, $g^{-1}(f^{-1}_{\alpha_1}(U_{\alpha_1})) \cap \dots \cap g^{-1}(f^{-1}_{\alpha_k}(U_{\alpha_k}))$ is open. Since $g$ is a well-defined function, uniquely assigning elements, $g^{-1}$ is injective. It follows
$$
g^{-1}(f^{-1}_{\alpha_1}(U_{\alpha_1})) \cap \dots \cap g^{-1}(f^{-1}_{\alpha_k}(U_{\alpha_k})) = g^{-1}( f^{-1}_{\alpha_1}(U_{\alpha_1}) \cap \dots \cap f^{-1}_{\alpha_k}(U_{\alpha_k})) \quad \blacksquare
$$

#### (d)

**Proposition.** If function $f: X \rightarrow Y$ maps each basis element $B$ of $X$ to a basis element $B'$ of $Y$, then $f(U)$ is open in $Y$ for every open $U$ in $X$.

**Lemma.** For a fixed $\alpha$, the image of $f^{-1}_\alpha (U_\alpha)$ in $\Tau$, is a basis element of $\Tau_Z$.

Observe the basis of $\Tau_Z$ is $\{ \prod_\alpha U_\alpha \cap Z \mid \text{all are } X_\alpha \text{ except finitely } U_\alpha \text{ are open} \}$.

Fix $\alpha$ and consider $f^{-1}_\alpha(U_\alpha)$ in $\Tau$. Accordingly, consider $\prod_\beta U_\beta \cap Z$ where $U_\beta = X_\beta$ for $\beta \neq \alpha$. Note it is a basis element of $\Tau_Z$.

We claim $f(f^{-1}_\alpha (U_\alpha)) = \prod_\beta U_\beta \cap Z$.

$(\rightarrow )$ $f_\alpha(x) \in U_\alpha$ for $x \in f^{-1}_\alpha (U_\alpha)$.

$(\leftarrow)$ For arbitrary $y$ in the R.H.S, it has at index $\alpha$ an element in $U_\alpha$. So $y = f(x)$ where $x \in f^{-1}(U_\alpha)$.

**Corollary.** The image of a basis element of $A$ is a basis element of $\Tau_Z$.

Following the same line of reasoning it can be shown a finite intersection $f^{-1}_\alpha (U_\alpha) \cap \dots \cap f^{-1}_\alpha (U_\alpha)$ is a basis element of $\Tau_Z$.

**Theorem.** Main problem.

Follows by the *corollary* alongside the *proposition*.
