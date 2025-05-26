---
title: Homework 06
math: true
date: "2025-05-26"
---

# Exercises

## Section 20

### 3

**(a)**

By theorem *18.1 (4)* it suffices to take $d(x,x') \in (a,b)$ for $(x,x') \in X \times X$, and then construct a neighbourhood $U \times U'$ of $(x,x')$ such that $d(U,U') \subset (a,b)$.

Observe if $\varepsilon = \varepsilon' \leq \dfrac{b - d(x,x')}{4}$, then taking $(x_0,x_1) \in B(x, \varepsilon) \times B(x', \varepsilon')$, yields
$$\begin{aligned}
    d(x_0,x_1) &\leq d(x_0,x) + d(x,x') + d(x',x_1) & &\text{triangular inequality} \\
               &\leq \dfrac{b-d(x,x')}{4} + \dfrac{b-d(x,x')}{4} + d(x,x') \\
               &\leq \dfrac{b-d(x,x')}{2} + d(x,x') \\
               &< b - d(x,x') + d(x,x') = b
\end{aligned}$$
Similarly $\varepsilon = \varepsilon' \leq \dfrac{d(x,x') - a}{4}$ yields
$$\begin{aligned}
    d(x,x') &\leq d(x,x_0) + d(x_0,x_1) + d(x_1,x') & &\text{triangular inequality}\\
            &\leq \dfrac{d(x,x') - a}{2} + d(x_0,x_1) \\
    d(x_0,x_1) &\geq d(x,x') - \dfrac{d(x,x') - a}{2} \\
               &> d(x,x') - d(x_0,x_1) + a = a
\end{aligned}$$
Taking the minimum values for $\varepsilon$ and $\varepsilon'$ concludes $d(  B(x,\varepsilon) \times B(x',\varepsilon') ) \subset (a,b)$.

**(b)**

### 4a

Consider $g(t) = (t, t, \dots)$ alongside continuity equivalence of *theorem 18.1 (4)*.

It is continuous in the product topology. For open neighbourhood $V$ around $(t, t, \dots)$, all are $X$ except finitely many open $V_\alpha$. for $t \in (a_\alpha, b_\alpha)$, consider the distance $c_\alpha = \min \{ t-a_\alpha, b_\alpha-t \}$. So we can take the minimum along these finite $c_\alpha$ and construct a neighbourhood $U$ around $t$ such that $f(U) \subset V$.

Not continuous in the box topology. A counter-example is $g(0) = (0, 0, \dots)$ with $V_\alpha = \left ( \dfrac{-1}{n}, \dfrac{1}{n} \right )$. Taking any open $(a,b) \ni 0$ implies $\exists x > 0 \; \forall n, \; x \in \left ( \dfrac{-1}{n}, \dfrac{1}{n} \right )$. Contradiction.

Not continuous in the uniform topology. Consider $x \in \mathbb{R}^\omega$ such that $x_0 = 0$ and $x_\alpha \rightarrow 1/2$. Observe $f(0) = (0, 0, \dots) \in B(x, 1/2)$ as $\forall \alpha \; x_\alpha < 1/2$. Following the same line of reasoning of the preceeding case, we no open neighbourhood $U$ of $0$ satisfies $f(U) \subset B(x, 1/2)$.

### 4b

The sequence $(1, 1, \dots)$ is trivially convergent to $1$ in all of product, box, and uniform topologies of $\mathbb{R}^\omega$.

### 5

We characterize the set of limit points.

**Lemma.** A sequence $x = (x_1, x_2, \dots)$ whereby $x_i \not\rightarrow 0$ is not a limit point of $\mathbb{R}^\infty$.

By definition, there is a fixed $\varepsilon_0$, such that for each index $\alpha$, there is some $i > \alpha$ where $| x_i - 0 | > \varepsilon_0$. Consider neighbourhood $B \left (x, \dfrac{\varepsilon_0}{2} \right )$. It follows no element of $\mathbb{R}^\infty$ is in it.

**Lemma.** A sequence $x = (x_1, x_2, \dots)$ whereby $x_i \rightarrow 0$ is a limit point of $\mathbb{R}^\infty$.

For any neighbourhood $B ( x, \varepsilon )$, by the convergence of $x_i$ to $0$, there is some $N_0$, such that $\forall j \geq N_0$, $0 \in (x_j - \varepsilon, x_j + \varepsilon)$. Consider the element $x'$ whereby $x'_i = x_i$ for $i < N_0$ and $x'_i = 0$ for $i \geq N_0$. Observe $x'$ is both in $\mathbb{R}^\infty$ and $B(x,\varepsilon)$.

**Theorem.** The closure is $R^\infty$ alongside its limit points.

## Section 21

### 3

**(a)**

For $\rho(x,x)$, we have $\forall i \; d_i(x,x) = 0$, hence their maximum is $0$.

For $\rho(x,y) = 0$, we have some $d_i(x,y) = 0$, hence $x = y$.

We know $\forall i \; d_i(x,y) \geq 0$, so their maximum is at least $0$, hence $\rho(x,y) \geq 0$.

We know $\forall i \; d_i(x,y) = d_i(y,x)$, so $\rho(x,y) = \max_i \{ d_i(x,y) \} = \max_i \{ d_i(y,x) \} = \rho(y,x)$.

Observe $\rho(x,y) = \max \{ d_i(x,y) \} \leq \max \{ d_i(x,z) + d_i(z,y) \} \leq \max \{ d_i(x,z) \} + \max \{ d_i(z,y) \} = \rho(x,z) + \rho(z,y)$.

**(b)**

For $D(x,x)$, we have $d_i(x,x) = 0$, so $\overline{d_i}(x,x)/i = 0$, and their supremum is $0$.

If $D(x,y) = 0 = \sup_i \{ \overline{d_i}(x,y)/i \}$, then $d_i(x,y) = 0$, since $\overline{d_i}(x,y)/i \geq 0$. Hence $x = y$.

We know some $d_i(x,y) \geq 0$, so $\overline{d_i}(x,y)/i \geq 0$, hence the supremum is at least $0$.

Since $d_i(x,y) = d_i(y,x)$ so does $\overline{d_i}(x,y) = \overline{d_i}(y,x)$, and in turn their supremum. i.e $D(x,y) = D(y,x)$.

Observe $D(x,y) = \sup \{ \overline{d_i}(x,y)/i \} \leq \sup \left \{ \dfrac{\overline{d_i}(x,z)}{i} + \dfrac{\overline{d_i}(z,y)}{i} \right \} \leq \sup \left \{ \dfrac{\overline{d_i}(x,z)}{i} \right \} + \sup \left \{ \dfrac{\overline{d_i}(z,y)}{i} \right \} = D(x,z) + D(z,y)$.

### 5

Follows trivially by the author's hints alongside *theorem 21.3*. For example,
$x_n + y_n = f(x_n \times y_n) \rightarrow f(x \times y) = x + y$.
