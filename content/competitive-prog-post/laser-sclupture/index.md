---
title: 11683 UVa, Laser Sculpture
subtitle: Challenging my self to prove its correctness via formal logic.
summary: Challenging my self to prove its correctness via formal logic.

math: true

date: "2020-05-01T00:00:01Z"

---

## Proposed Solution, Intuitively
Before delving into mathematical rigour details, Let me give you an intuitive description of the solution and why it works.

Note that the laser only sculpts a layer of height equal to one while it is still on. If we wish to sculpts a layer of height 2, Then the laser must be toggled on and off twice. That suggests each layer intended to be sculpted counts on the laser to be turned on after being on off state. What if there are more than one sculpture on the same layer, but separated by couple of unsculpted units? then each sculpture on this layer counts per se.

Think of the following, where _b_ indicates a sculpted unit and _x_ indicates an unsculpted unit. A height equal to three is made here for a simple illustration.

| X_i  | X_i+1 |
| ---- |:-----:|
| b | b |
| x | b |
| x | x |

if $X_i$ here is $X_1$, then certainly the blank unit counts as a laser is turned on. What about $X_1$, Would the two blank units count each on laser? Considering the fact that a laser could move horizontally while it is still being turned on allows two blanks crossing $X_0$ and $X_1$ to be sculpted on one count. What about the second blank of $X_1$? Clearly, The laser must sculp the blank above it first, So the second blank would be an additional count. Seemingly, We came across a condition here. if a blank in $X_i+1$ came after a blank in $X_i$, Then it should not count but if it came after an unsculpted unit, Then it counts.

The observation suggests the following. A column which tracks counts on each layer, and the state of the last scanned unit, i.e whether it is sculpted or not. Initially, It would be

| count  | unit |
| ---- |:-----:|
| 0 | x |
| 0 | x |
| 0 | x |

_x_ units initialized here are on behalf of the left most outer border. We proceed as follows, For a given _X_i_ determine units _b_ sculpted and units _x_ unsculpted. If a unit is _x_, Then leave count as it is. If a unit is _b_, Then check the unit before it, If it is _b_ leave count but if it is _x_ increment count by one. Afterward, Update unit column with the new unit. Do these steps on all vertical units. Repeat the procedure on each $X_i$. The correct result is the sum of all counts.

We could furtherly improve. Why do we need to track each layer on a separated _count_ for it? Instead, We could define only one variable which gets incremented whenever any layer detects a new laser sculpture. In addition, For the unit column, We do not need to check every unit and compare it with the previous one in order to find blank units preceeded by unsculpted x units. max(0, $X_i$ - $X_{i+1}$) would do the trick of finding blank units b in $X_{i+1}$ preceeded by x unit.

## Source Code
```
#include <stdio.h>
#include <algorithm>
#define usi unsigned short int

int main() {
  usi h, w;
  int X_bef, X_cur, cou;

  while(true) {
    scanf("%hu %hu", &h, &w);

    if (h == 0)
      break;

    cou = 0;
    X_bef = h;
    
    for (usi i=0; i<w; ++i) {
      scanf("%d", &X_cur);
      cou = cou + std::max(0, X_bef-X_cur);
      X_bef = X_cur;
    }

    printf("%d\n", cou);
  }
  
  return 0;
}
```

## Formal Logic
Here comes the formal-logic based proof of our algorithm's correctness. Kindly, note that it might still be flawed. However, If it is not, Then we guarantee the algorithm to yield the correct answer without any bugs or errors. Anyway, Before getting into the proof, We need to rigoursly model the problem of _Laser Sculpture - 11683_. Those rigor definitions and constraints are derived from our understanding of the problem.

### Definitions
For the following, We assume $h$, $w$ $\in \mathcal{N}$

**Board**: A 2d-array-alike corresponding to overall units. board is $b = (h \times w)$, units $u_{i,j}$ indexed (labeled) by a cartesian product of board's height and width. 

$X_0$: We define an imaginary height equal to $h$ of a given board. It serves on behalf the left most outer border for the first iteration of our algorithm.

**Sculpture set on board**: A family of sets where each set is the set of units sculpted by the laser while it is still on. The sculpture set is $S = ${$ S_1, S_2, .., S_k$} such that $\cup S \subseteq b$, $S_i \cap S_j = \phi$ for any distinct i and j, $S_i \neq \phi$ for any i. That says sculptures are subset of the original board units, no two sculptures are intersecting, and there's no empty sculpture. That conforms with our understanding that a unit cannot be shot twice by a laser, and a laser is not going to be turned on without sculpting some unit.

**Top-first**: That is a condition which ensures no sculpture occurs on some layer before the layer above it is sculptured. For any $S_q \in S$, $\forall u_{i,j} \in S_q( ${$ u_{x,j} \in b | x < i $}$ \subseteq S_{q-1} \cup S_{q-2} \cup .. \cup S_{1} )$.

**One-row**: That is a condition which ensures a continuous row of units are sculptured at once, not sculptured on multiple times in which the laser is turned on and off multiple times as well. For any two distinct $S_k$ and $S_q$, $\neg( \exists j_0  \exists j_1, u_{i_0,j_0} \in S_q \wedge u_{i_1,j_1} \in S_k \wedge j_1=j_0+1)$ for some $u_{i_0,j_0}$ and $u_{i_1,j_1}$.

**Uniqueness**: It is assumed that there is a unique number of times for the laser to be toggled on and off regardless of of the _sculpture set_. In other words, Even if there are two possible different sculptures which achieve the desired X's, The number of times the laser needs to be toggled on and off is the same.

**Existince of a Solution**: It is assumed that given height $h$, and width $w$ of the whole board $b$, and given heights $X_1$, $X_2$, .., $X_w$ of position $i$ in the board, There exists a _sculpture set_ $S$ _on board_ $b$ such that $b - S = \cup_{p \in 1, 2, .., w }$ {$ u_{i,p} \in b $} whereby each set {$ u_{i,p_0} \in b $} has a cardinality of $X_{p_0}$. In other words, The set yielded from subtracting the board from sculpture set is composed of units conforming to desired $X$'s heights.

**Principal Problem Statement** (finally): Given a board $b_{h \times w}$ of height $h$ and width $w \in \mathcal{Z}^+$, and given heights $X_1$, $X_2$, .., $X_w$, The cardinality of $\textit{sculpture set on board}$ $b$ is equal to $\Sigma_{i=0}^{w-1}min(0, X_i-X_{i+1})$

### Proof

**Lemma**: For $b-S$, where $b$ is a board of height $h$ and width $w \geq 2$ and $S$ is a _sculpture set on_ $b$ conforming to given heights of unsculpted units of last two board columns $X_{w-1}$ and $X_w$,

**(1)** if $X_{w} < i \leq X_{w-1}$, a unit $u_{i, w}$ is contained in some $S_k$ and no other unit is in $S_k$. That is, for some $S_k \in S$, $S_k = ${$ u_{i, w} $}.

**(2)** if $X_{w} \leq X_{w-1} < i$, a unit $u_{i, w}$ is contained in some $S_k$ which is per se contains an element of $\textit{board}$ $b^{'} = b_{h \times w-1}$.

**(1) Solution**: Assume $X_{w} < i \leq X_{w-1}$. Clearly, unit $u_{i, w} \in \cup S$, As it is above height of column $X_w$. So, $u_{i, w} \in S_k$ for some $S_k \in S$. $S_k$ does not contain other units  which are above, below, or diagonal to $u_{i, w}$. Otherwise, $\textit{top first}$ or $\textit{one row}$ conditions shall be violated. Also, no other units are left to $u_{i, w}$ in $S_k$, As $i \leq X_{w-1}$. Hence, $S_k = ${$ u_{i, w} $}.

**(2) Solution**: Assume $X_{w} \leq X_{w-1} < i$. Similar to $\textbf{(1) solution}$, unit $u_{i, w} \in \cup S$, As it is above height of column $X_w$. So, $u_{i, w} \in S_k$ for some $S_k \in S$. $S_k$ does not contain other units  which are above, below, or diagonal to $u_{i, w}$. Otherwise, $\textit{top first}$ or $\textit{one row}$ conditions shall be violated. However, unlike $\textbf{(1) solution}$, Nothing precludes a unit left to $u_{i, w}$ to be contained in $S_k$, As $X_{w-1} < i$. On the contrary, if $S_k = ${$ u_{i, w} $} then $\textit{one row}$ condition shall be violated as two sculptures are going to be on the same row without any non-blank separator between them. Through $\textit{proof by contradiction}$, $S_k \neq ${$ u_{i, w} $}. Hence, there are some units $u \in S_k$. Since units from all directions are excluded, except only the left direction, $u_{i, w-1} \in S_k$, which is clearly a unit of $\textit{board}$ $b^{'} = b_{h \times w-1}$.

**Corollary**: From **Lemma (1)**, Obviously, $S_k$ is not an element of $\textit{sculpture set on board}$ $b^{'} = b_{h \times w-1}$ due to the fact that $S_k \not\subseteq b^{'}$

**Problem Statement** (main proof): First we re-write the statement defined above in a more convenient form for induction proof.

for $w \in \mathcal{Z}^+$, \
Given $h \in \mathcal{N}$, and heights $X_1$, $X_2$, .., $X_w$, sculpture set on board $b_{h \times w}$ has a cardinality of $\Sigma_{i=0}^{w-1}min(0, X_i-X_{i+1})$.

**Solution**: \
base, for $w = 1$, \
Assume we are given $h \in \mathcal{N}$, and heights $X_1$, $X_2$, .., $X_w$. A board $b_{h \times w}$ has a sculpture set on it, by assumption.
Assume $X_{1} < i$. By definition $X_0 = h$. So, $X_1 < i < X_0$. via $\textbf{Lemma (1)}$, each unit $u_{i, 1}$ is contained in some $S_k$ and no other unit is in $S_k$. In other words, cardinality of {$ u_{i, 1} | X_1 < i $} is equal to $S$, the sculpture set on board $b$. clearly, it is also equal to ($X_0$ - $X_1$). since $X_0 \geq X_1$, ($X_0$ - $X_1$) = min(0, $X_0$ - $X_1$) which justifies our problem statement.

induction hypothesis, for $w^{'} \in \mathcal{Z}^+$ we assume problem statement's validity.

induction step, for $w = w^{'}+1$, \
Assume we are given $h \in \mathcal{N}$, and heights $X_1$, $X_2$, .., $X_w$. A board $b_{h \times w}$ has a sculpture set on it, by assumption.
Assume $X_{w} < i$. \
$\textbf{case 1}$: if it is the case the $i \leq X_{w-1}$, then similarly to base case, each unit $u_{i, w}$ counts a new element in $S$, the sculpture set on board $b$. Recall from $\textbf{corollary}$ that those are not in $S^{'}$, sculpture set on board $b^{'}_{h \times w-1}$. cardinality of units $u_{i, w}$ are clearly equal to $X_{w-1} - X_{w}$. Also, It is clear that $X_{w-1} > X_{w}$, Hence, $X_{w-1} - X_{w}$ = $min(0, X_{w-1} - X_{w})$.

$\textbf{case 2}$: But if $i > X_{w-1}$, then by $\textbf{lemma (1)}$ each unit $u_{i, w}$ is contained in some $S_k$ which is per se an element of $S^{'}$, the sculpture set on board $b^{'}_{h \times w-1}$. Hence, Those units do not contribute new counts to $S$, the sculpture set on board $b_{h \times w}$ than counted in $S^{'}$. On the other hand, It is clear that $X_{w-1} \leq X_{w}$, So $X_{w-1} - X_{w} \leq 0$. So, $min(0, X_{w-1} - X_{w}) = 0$ which conforms with what we just proved that no new sculptures are added than those in board $b^{'}$.

From **case 1** and **case 2**, $min(0, X_{w-1} - X_{w})$ is equal to new sculptures not in sculpture set $S^{'}$ on board $b^{'}_{h \times w-1}$. Therefore, cardinality of set $S$ is equal to cardinality set $S^{'}$ plus $min(0, X_{w-1} - X_{w})$. via induction hypothesis, cardinality of $S^{'} = \Sigma_{i=0}^{w^{'}-1}min(0, X_i-X_{i+1})$. So, cardinality of $S = \Sigma_{i=0}^{w-2}min(0, X_i-X_{i+1}) + min(0, X_{w-1}-X_{w}) = \Sigma_{i=0}^{w-1}min(0, X_i-X_{i+1})$
QED
