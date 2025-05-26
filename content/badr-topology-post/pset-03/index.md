---
title: Homework 03
math: true
date: "2025-05-26"
---

## Exercises

### 6

The following are based on the equivalence of *theorem 17.5*.

**(a)**

Take $x \in Cl(A)$. By definition $\forall U \ni x$ open, $U$ meets $A$. Take $U \ni x$ arbitrary. Then $\exists y \in U \cap A$. Since $A \subseteq B$, we get $y \in U \cap B$.

**(b)**

$(\leftarrow)$ Take $x \in Cl(A) \cup Cl(B)$. WLOG assume $x \in Cl(A)$. Then if we took open $U \ni x$ arbitrary, we get $y \in U \cap A$. It follows $y \in U \cap (A \cup B)$.

$(\rightarrow)$ We show the contrapositive. Assume we have open $U_0 \ni x$ and open $U_1 \ni x$ with $U_0 \cap A = \phi$ and $U_1 \cap A = \phi$. Take the intersection $U = U_0 \cap U_1$ which is open. Clearly $U \cap (A \cup B) = \phi$.

**(c)**

If $x \in \bigcup_\alpha Cl(A_\alpha)$, then for some $\alpha_0$, $x \in A_{\alpha_0}$, and the proof follows similarly to *(b)*.

For a counter-example of equality, Take $X = \mathcal{R}$ and observe $(0,1) = \underset{0 \leq x \leq 1}{\bigcup} (0, x)$ but $1 \in [0, 1] \neq \underset{0 \leq x \leq 1}{\bigcup} [0, x] \not\ni 1$. Note $[0,x]$ is the closure of $(0,x)$ as any closed set containing $(0,x)$ must contain $0$ and $x$.

### 8

**(a)**

$Cl(A \cap B) \subseteq Cl(A) \cap Cl(B)$.

By *6-a*, and since $A \cap B \subseteq A$ and $A \cap B \subseteq B$, It follows $Cl(A \cap B) \subseteq Cl(A)$ and $Cl(A \cap B) \subseteq Cl(B)$.

$Cl(A \cap B) \nsupseteq Cl(A) \cap Cl(B)$.

In $X = \mathcal{R}$, Observe $Cl(0,1) \cap Cl(1,2) = [0,1] \cap [1,2] = \{1\} \neq Cl( (0,1) \cap (1,2) ) = Cl( \phi ) = \phi$.

**(b)**

$Cl(\bigcap_\alpha A_\alpha) \subseteq \bigcap_\alpha Cl(A_\alpha)$.

Trivially $\bigcap_\alpha A_\alpha \subseteq A_{\alpha'} \; \forall \alpha'$. By *6-a*, $Cl(\bigcap_\alpha A_\alpha) \subseteq Cl(A_{\alpha'}) \; \forall \alpha'$.

$Cl(\bigcap_\alpha A_\alpha) \nsupseteq \bigcap_\alpha Cl(A_\alpha)$.

Follows by *(a)*.

**(c)**

$Cl(A-B) \supseteq Cl(A) - Cl(B)$.

Take $x \in Cl(A)$ and $x \not\in Cl(B)$. Then (1) $\forall U \ni x$ open where $U \cap A \neq \phi$. Moreover (2) we get $U_0 \ni x$ open where $U_0 \cap B = \phi$.

Consider arbitrary open $U \ni x$. Take open $U_1 = U \cap U_0$ containing $x$. Then $U_1 \cap B = \phi$ by (2), and substituting in (1), we get $U_1 \cap A \neq \phi$. It follows $U_1 \cap (A-B) \neq \phi$. As $U_1 \subseteq U$, thereby $U \cap (A - B) \neq \phi$.

$Cl(A-B) \nsubseteq Cl(A) - Cl(B)$.

In $X = \mathcal{R}$, $Cl( (0,2) - (1,2) ) = Cl( (0,1] ) = [0,1] \nsubseteq Cl(0,2) - Cl(1,2) = [0,2] - [1,2] = [0,1)$.

### 9

$(\rightarrow)$. let $x = (x_0, x_1) \in Cl(A \times B)$. Then for all open $U$ and open $U'$ where $U \times U' \ni (x_0, x_1)$, it follows $(U \times U') \times (A \times B) \neq \phi$.

Take arbitrary open $U \ni x_0$ and $U' \ni x_1$ in $A$ and $B$, respectively. Then $U \times U' \ni (x_0, x_1)$. By hypothesis, there are $(y_0, y_1) \in (U \times U') \cap (A \times B)$. Hence $y_0 \in U \cap A$ and $y_1 \in U' \cap B$, concluding $x_0 \in Cl(A)$ and $x_1 \in Cl(B)$. i.e $x = (x_0, x_1) \in Cl(A) \times Cl(B)$.

$(\leftarrow)$. Symmetric.

### 13

Observe $\Delta$ is closed iff $X \times X - \Delta = \{ (x,y) \mid x \neq y \}$ is open.

$(\rightarrow)$ Consider $x \neq y$. By hypothesis there are open $U_x \ni x$ and $U_y \ni y$ where $U_x \cap U_y = \phi$. It follows $U_x \times U_y \ni (x,y)$ and $U_x \times U_y \subseteq X \times X - \Delta$. Hence $\underset{x \neq y}{\bigcup} U_x \times U_y = X \times X - \Delta$ is open.

$(\leftarrow)$ Consider $x \neq y$ arbitrary of $X$. Then $(x,y) \in X \times X - \Delta$, and then there exists a basis element $U_x \times U_y$ of $X \times X$ where $U_x \ni x$, $U_y \ni y$, and $U_x \times U_y \subseteq X \times X - \Delta$. If $\exists z \in U_x \cap U_y$ we would have $(z,z) \in X \times X - \Delta$ but by definition that's prohibited. Therefore $U_x \cap U_y = \phi$.

### 19

**(a)**

$$\begin{aligned}
    &Int \, A \cap Bd \, A \\
    &= Int \, A \cap ( Cl(A) \cap Cl(X-A) ) \\
    &= (Int \, A \cap Cl(A)) \cap Cl(X-A) \\
    &= Int \, A \cap Cl(X-A) \\
    &= Int \, A \cap (X - Int \, A) \\
    &= \phi
\end{aligned}$$

$$\begin{aligned}
    &Int \, A \cup Bd(A) \\
    &= Int \, A \cup ( Cl(A) \cap Cl(X-A) ) \\
    &= (Int \, A \cup Cl(A) ) \cap ( Int \, A \cup Cl(X - A) ) \\
    &= Cl(A) \cap (Int \, A \cup Cl(X-A)) \\
    &= Cl(A) \cap (Int \, A \cup (X - Int \, A)) \\
    &= Cl(A) \cap X \\
    &= Cl(A)
\end{aligned}$$

### 20

**(a)**

For arbitrary $U \times V \subseteq Int \, A$, we have $V \subseteq \{0\}$. But then $V = \phi$ and $U \times \phi = \phi$, concluding $\bigcup \phi = \phi$. Thereby $Int \, A = \phi$.

$Cl(A) = A$. By *19-a*, $Bd(A) = Cl(A) - Int(A) = Cl(A) - \phi = A$.

**(b)**

Consider open $U = \bigcup \{ (0,x) \mid x > 0 \}$ and open $V = \bigcup \{ (0,x) \mid x > 0 \} \cup \bigcup \{ (x,0) \mid x < 0 \}$. Observe $U \times V = B$, thereby $Int \, B = B$.

$Cl(B) = B$. By *19-a*, $Bd(B) = Cl(B) - Int(B) = B - B = \phi$.

**(c)**

Clearly $\bigcup \{ (0,x) \mid x > 0 \} \times \mathcal{R} \subseteq Int \, C$.

We shall show equality. Assume towards contradiction there is an $(x,y) \in Int \, C$ not in the L.H.S set. Then $x \leq 0$ and $y = 0$ by definition of $C$. Since $Int \, C$ is open there is an open set $U \times V$ of $\mathcal{R}^2$ that contains $(x,0)$. But then $V$ contains $y \neq 0$. It follows $(x,y) \in C$ for $x \leq 0$ and $y \neq 0$. Contradiction.

By *6-b*, $Cl(A \cup B) = Cl(A) \cup Cl(B) = A \cup B$. By *19-a*, $Bd(A \cup B) = Cl(A \cup B) - Int(A \cup B) = A \cup B - \bigcup \{ (0,x) \mid x > 0 \}$.
