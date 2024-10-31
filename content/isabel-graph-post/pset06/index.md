---
title: Homework 06
math: true
date: "2024-06-01"
---

## Exercises {#exercises .unnumbered}

### 1 {#section .unnumbered}

$(\rightarrow).$ Assume connected $G$ has an Eulerian trail. If $G$ has also an Eulerian circuit then we are done by *theorem 3.5*. Then we have trail $t = (v_1, v_2, \dots, v_k)$ where $t$ is not a circuit, i.e $v_1 \neq v_k$.

Since the graph is connected, We know all vertices do appear in $t$. For any interior vertex $u$ in $t$ we know it counts two edges by the definition of a trail and the prohibition of self-loops. It follows any vertex $u \neq v_1, v_k$ is of even degree, As its degree is 2 times the number of times it appears in $t$. Moreover $v_1$ counts an additional single edge since the trail starts with it, So its degree is odd. Similarly $v_k$ is of an odd degree.

$(\leftarrow).$

*Case 1.* All vertices have even degrees.

Then by *theorem 4.5*, $G$ is Eulerian, So it has an Eulerian trail.

*Case 2.* Exactly 2 vertices have odd degrees. Call them $v_1$ and $v_2$.

*Case 2.1.* Edge $\{ v_1, v_2 \} \in E(G)$.

Define $H = G - \{v_1,v_2\}$, Removing the edge in $G$. Then all vertices have even degrees. By *Theorem 3.5* $H$ contains an Eulerian circuit $c = (v_1, u_1, u_2, \dots, v_1)$. It follows $G$ has the trail $t = c + (v_1, v_2)$.

*Case 2.2.* Edge $\{ v_1, v_2 \} \notin E(G)$.

Define $H = G + \{v_1,v_2\}$, Adding the edge to $G$. Then all vertices have even degrees. By *Theorem 3.5* the graph contains an Eulerian circuit $c = (u_1, u_2, \dots, u_{k-1}, u_1)$, Since it covers all the edges, WLOG $(v_1, v_2)$ is contained in it.

Construct a new trail $t$ from the circuit $c$, starting at $v_2$ and ending at $v_1$. Clearly $t$ is a trail in $G$. $\blacksquare$
