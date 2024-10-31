---
title: "Problem Set 10"
math: true
date: "2023-08-06"
---

$\newcommand{\ddfrac}[2]{\frac{\displaystyle{#1}}{\displaystyle{#2}}}$

## Exercises

### Ex. 1

Done


## Problems

### Prob. 1

#### a

The proof is identical to slide 15. Note the symmetric structure of the ring where, as all processes are identical they send the same message to their right port and receive the same message from their left port.


#### b

A randomized algorithm identical to slide 18, satisfies all the problem's requirements.

The sole difference is the subroutine which exchanges all UIDs. In round $1$, A process sends its randomly generated UID to the right port. In round $r > 1$, The received message from the left port in the previous round is sent to the right port. All processes record received UIDs and stop after recording $n$ of them.

That subroutine consumes $\mathcal{O}(n)$ rounds and $\mathcal{O}(n^2)$ messages.


#### c

I conjecture the answer there is no such algorithm; I couldn't come-up with a rigorous proof. Here is an insight justifying my stance.

The only way processes can know each other's UIDs is by circulating their UIDs. They cannot ever know whether the whole ring is covered. For example, If a process recorded $(a,b,c,a)$ then it can be tricked by the actual complete ring $(a,b,c,a,d)$ whose size is $5$. It is trivial to generalize the trick to accommodate any number of loops of $a$, like $(a,b,c,a,b,c,a)$ tricked by ring $(a,b,c,a,b,c,a,d)$.


### Prob. 2

#### a

I am not sure what is the sufficent degree of clarity the instructor is looking for. Neither do I claim my argument to be formally rigorous or even convincing. However, We hope it fulfills all the practical purposes of two introductory lectures.

The key idea is for processes, not to send *search* unless the root $v_0$ broadcasts *ready*. Also, *ready* is broadcasted by $v_0$ only if all of its neighbours signaled level $i$ updated their parents.


#### b {#b-1 .unnumbered}

**Time.** For each level, the root $v_0$ broadcasts *ready* and receives a response, Accounting for $diam \cdot 2(diam)$ edges traversed. That concludes the desired $\mathcal{O}(diam^2 \cdot d)$ upper-bound.

**Messages.** For each level, At most all vertices, both receive and send a message, Accounting for $diam \cdot 2n$.
