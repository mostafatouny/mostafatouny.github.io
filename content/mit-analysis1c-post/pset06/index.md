---
title: Problem Set 06
math: true
date: "2023-04-23"
---

## Problem. 1 {#problem.-1 .unnumbered}

## Problem. 2 {#problem.-2 .unnumbered}

## Problem. 3 {#problem.-3 .unnumbered}
The first part is solved by a trivial set-theoretic operations. The second is postponed.

Observe if $x \in f(\overline{E})$ then $x = f(p)$ for some $p \in \overline{E}$. To prove $x \in \overline{f(E)}$ it suffices to have $f(p) \not\in f(E)$. By contrapositive, It follows by the given $p \not\in E$.

Note the proof is independent of continuity.


## Problem. 4 {#problem.-4 .unnumbered}
**Observation.** In case of a continuous function $f$ at point $p$, If we have a sequence $\{x_i\}$ converging to $p$ and $\{f(x_i)\}$ converges to $a$ then $a = f(p)$.

**Theorem.** Our approach is proving the definition of a closed-set is satisfied. Namely, If $p$ is a limit point of of $Z(f)$ then $p \in Z(f)$. Fix $p$ and suppose $\forall \epsilon > 0$ $\exists x \in Z(f)$ such that $d(x,p) < \epsilon$. We can construct a sequence $x_i$ arbitrarily close to $p$ where $f(x_i)  = 0$. By the above observation it must be the case $f(p) = 0$, and hence $p \in Z(f)$.
