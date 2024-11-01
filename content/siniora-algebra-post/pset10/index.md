---
title: Chapter 10
math: true
date: "2023-12-18"
---

## Problems {#problems .unnumbered}

### 8 {#section .unnumbered}

Homomorphism. If $\sigma_1$ and $\sigma_2$ are both even or both odd, then $\sigma_1 \sigma_2$ is even and $sgn(\sigma_1) sgn(\sigma_2) = 1$. If one of them is even and the other is odd, then $\sigma_1 \sigma_2$ is odd and $sgn(\sigma_1) sgn(\sigma_2) = 1 * -1 = -1$.

Kernel. $Ker \, sgn$ is the subgroup of even permutations of $G$.

$A_n$ is a normal subgroup of $S_n$. When $G = S_n$, $Ker \, sgn = A_n$. By *corollary* (page 198), $Ker \, sgn$ is a normal subgroup.

_Ex 23_ in _Ch 05_. Now consider the homomorphism $sgn$ on arbitrary subgroup $H$. We know the identity must be $sgn(H)$. If $sgn(H) = \{ 1 \}$ then all permutations of H are even. Otherwise $sgn(H) = \{ 0, 1\}$. By *property 5* in *theorem 10.2* (page 197), we have n-to-1 mapping from even permutations, and n-to-1 mapping from odd permutations. Hence exactly half of $H$ are even.

### 12 {#section-1 .unnumbered}

By definition, $Z_n/\langle k \rangle = \{ x + \langle k \rangle \mid x \in \mathcal{Z}_n \}$. But by *Euclid's Division*, $x + \langle k \rangle = (kq + r) + \langle k \rangle = r + (kq + \langle k \rangle) = r + \langle k \rangle$. It follows $\mathcal{Z}_n / \langle k \rangle = \{ x + \langle k \rangle \mid x \in \mathcal{Z}_k \}$.

Now define $\phi: \mathcal{Z}_n / \langle k \rangle \rightarrow \mathcal{Z}_k$ by $\phi(x + \langle k \rangle) = x$. It is injective as $\phi(x + \langle k \rangle) = \phi(y + \langle k \rangle)$ implies $x = y$. Surjective as for any $y \in \mathcal{Z}_k$ we have $\phi(y + \langle k \rangle = y$. Finally it preservers the operation as $\phi(x + \langle k \rangle) + \phi(y + \langle k \rangle) = x + y = \phi( (x+y) + \langle k \rangle )$.

### 15 {#section-2 .unnumbered}

Let $x$ be arbitrary such that $\phi(x) = 9$. Then
$$
\begin{aligned}
    \phi(x) - \phi(23) &= 9 - 9 = 0 \\
    \phi(x - 23) &= 0 \\
    x - 23 &\in \\{ 0, 10, 20 \\} \\
    x + 7 &\in \\{ 0, 10, 20 \\} \\
    x &\in \\{ 23, 3, 13 \\}
\end{aligned}
$$

### 16 {#section-3 .unnumbered}

Let $\phi$ be an arbitrary homomorphism.

Since both $\mathcal{Z}_8 \oplus \mathcal{Z}_2$ and $\mathcal{Z}_4 \oplus \mathcal{Z}_4$ have exactly 16 elements, the surjectivity of homomorphism $\phi$ implies isomorphism.

Recall *property 5*, of *Theorem 6.2* (page 126) which states isomorphism preserves orders. So $8 = |(1,0)| = |\phi(1,0)|$. So there is some element in $\mathcal{Z}_4 \oplus \mathcal{Z}_4$ which is of order 8. Contradiction.

Observe all elements of $Z_4$ are of orders $1,2,4$. Since all of them divides $4$, The order of any element of $\mathcal{Z}_4 \oplus \mathcal{Z}_4$ is at most $4$.

### 20 {#section-4 .unnumbered}

**(1).** $\mathcal{Z}_{20}$ onto $\mathcal{Z}_8$.

Let $\phi$ be an arbitrary homomorphism. By surjectivity we know $\phi(\mathcal{Z}_{20}) = \mathcal{Z}_8$. By theorem 10.2, 5 (page 197), $20$ is a multiple of $8$. Contradiction. It follows the number of homomorphisms is zero.

P.S. The TA Ibrahim notified me Math is not about hacking puzzles but seeing the structure behind. He told me an alternative proof by cosets and quotient groups. For academic integrity I present the proof I discovered on my own.

**(2).** $\mathcal{Z}_{20}$ to $\mathcal{Z}_8$.

Let $\phi: \mathcal{Z}_{20} \rightarrow \mathcal{Z}_8$ be an arbitrary homomorphism. We follow the procedure of example 10 (page 199). Let $\phi(1) = a$. Then $|a|$ divides both $20$ and $8$. It follows $|a| \in \{1, 2, 4\}$ and in turn $a \in \{ 0, 2, 4, 6 \}$. Since $\phi(1)$ decides the homomorphism, There are 4 possible homomorphisms.

### 24 {#section-5 .unnumbered}

**(a).** In light of *property 2* of *theorem 10.1* (page 196), Observe $6 = \phi(7) = \phi(7 \cdot 1) = 7 \cdot \phi(1)$. But $13 \cdot 7 \mod 15 = 1$. It follows $\phi(1) = 13 \cdot 6 = 3$. Therefore $\phi(x) = \phi(1 \cdot x) = \phi(1) \cdot x = 3x$.

**(b).** The image is all multiples of 3 strictly less than 15.

**(c).** By definition we are looking for $x \in \mathcal{Z}_{50}$ such that $\phi(x) = 3x = 0$. But $3x \equiv 0$ if and only if $3x - 0 = 3x$ is a multiple of $15$ if and only if $x = 5i$. In other words the kernel are multiples of 5 strictly less than $50$.

**(d).** We want to characterize $x$ such that $\phi(x) = 3$. But by definition we know $\phi(x) = 3x$. Then
$$
\begin{aligned}
    3 &\equiv 3x \mod 15 \\
    3x - 3 &= 15i \\
    x - 1 &= 5i \\
    x &= 5i + 1
\end{aligned}
$$
So $\phi^{-1}(3) = \\{ 5i + 1 \mid 0 \leq i \leq 9 \\}$
