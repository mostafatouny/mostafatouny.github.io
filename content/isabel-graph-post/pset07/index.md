---
title: Homework 07
math: true
date: "2024-06-01"
---

## Exercises {#exercises .unnumbered}

### 1 {#section .unnumbered}

**(a).** Yes. Let $v_1, \dots, v_n, u_1, \dots, u_n$ be the vertices. Then the cycle $(v_1, u_1, v_2, u_2, \dots, v_n, u_n, v_1)$ is hamiltonian.

**(b).**

**(c).** No. A counter example is the graph whose vertices are $v_1, v_2, v_3$ and edges are $\\{ v_1, v_2 \\}$.

### 2 {#section-1 .unnumbered}

**(a).** If $S$ is independent in $G$ then for any $u,v \in S$, $\\{u, v\\} \not\in E(G)$. By definition $\\{u, v\\} \in E(\overline{G})$. So $\\{ u,v \\} \in \langle S \rangle^{\overline{G}}$. The converse holds by symmetry.

**(b).** If $G$ is not $E_k-free$ then $G$ has $E_k$ as an induced subgraph, which in turn is an independent set. It follows $\alpha(G) \geq k$. If $G$ is $E_k-free$ then by definition it does not contain an independent subgraph whose order is at least $k$. So the largest possible independent subgraph is strictly less than $k$. It follows $\alpha(G) < k$.

### 3 {#section-2 .unnumbered}

The statement is true. If a graph contains a claw as an induced subgraph, Then some vertex has three edges. In other words, Its degree is at least 3. So $\Delta(G) \not \leq 2$. If $\Delta(G) > 2$ then the graph has a vertex with at least 3 edges. The graph induced by that vertex alongside its 3 neighbour vertices is a claw. So $G$ is not claw-free.

### 4 {#section-3 .unnumbered}

Denote the vertices of $H$ by $u_1, u_2, \dots, u_n$. Construct $G$, containing $H$ as a subgraph, but with new vertices $\\{ v_i \\}$ and new edges of the path $(v_1, u_1, v_2, u_2, \dots, v_n, u_n, v_1)$. 
