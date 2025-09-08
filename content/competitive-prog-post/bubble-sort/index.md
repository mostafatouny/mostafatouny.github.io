---
title: UVa 120004, Bubble Sort
subtitle: Math is not routine calculations at all.
summary: Math is not routine calculations at all.

math: true

date: "2020-06-11T00:00:01Z"

---

### Restructuring The Problem, More Conveniently
Before tackling a solution, We need to reformulate the given problem. You might consider this a reduction to a form which is more convenient to solve. The problem states We are given an array of size _n_ whose elements are {1, 2, .., n} and are distinct. That concludes the given array _a_ is a permutation of {1, 2, .., n}. If we listed all these permuations and computed _bubbleCounts_ on each, Then taken their average, That would be the answer to UVa's problem. _Running findSwaps() infinitely_ is just a fancy way of describing our

**Definition**: Average _bubble counts_ of all permutations.

### Observations

On **n = 2**,

|   |   | bubbleCount |
| - | - | :-: |
| 1 | 2 |  0  |
| 2 | 1 |  1  |

average = $\frac{0+1}{2}$ = $\frac{1}{2}$

On **n = 3**,

|   |   |   | bubbleCount  |
| - | - | - | :-: |
| 1 | 2 | 3 | 0 |
| 1 | 3 | 2 | 1 |
| 2 | 1 | 3 | 1 |
| 2 | 3 | 1 | 2 |
| 3 | 1 | 2 | 2 |
| 3 | 2 | 1 | 3 |

average = $\frac{0+1+1+2+2+6}{6}$ = 2

On **n = 4**,

|   |   |   |   | bubbleCount  |
| - | - | - | - | :-:       |
| 1 | 2 | 3 | 4 | 0 |
| 1 | 2 | 4 | 3 | 1 |
| 1 | 3 | 2 | 4 | 1 |
| 1 | 3 | 4 | 2 | 2 |
| 1 | 4 | 2 | 3 | 2 |
| 1 | 4 | 3 | 2 | 3 |
| 2 | 1 | 3 | 4 | 1 |
| 2 | 1 | 4 | 3 | 2 |
| 2 | 3 | 1 | 4 | 2 |
| 2 | 3 | 4 | 1 | 3 |
| 2 | 4 | 1 | 3 | 3 |
| 2 | 4 | 3 | 1 | 4 |
| 3 | 1 | 2 | 4 | 2 |
| 3 | 1 | 4 | 2 | 3 |
| 3 | 2 | 1 | 4 | 3 |
| 3 | 2 | 4 | 1 | 4 |
| 3 | 4 | 1 | 2 | 4 |
| 3 | 4 | 2 | 1 | 5 |
| 4 | 1 | 2 | 3 | 3 |
| 4 | 1 | 3 | 2 | 4 |
| 4 | 2 | 1 | 3 | 4 |
| 4 | 2 | 3 | 1 | 5 |
| 4 | 3 | 1 | 2 | 5 |
| 4 | 3 | 2 | 1 | 6 |

average = $\frac{0+1+1+2+2+3+1+2+2+3+3+4+2+3+3+4+4+5+3+4+4+5+5+6}{24}$ = 3

### Symmetry
Consider the case of $n=3$. Notice that the least _bubbleCount_ is the first one accounting for zero, and the greatest _bubbleCount_ is the last one accounting for 3. You could see that for each permutation of _bubbleCount_ 1, There is a corresponding permutation of _bubbleCount_ 2. The sum of 1 and 2 is also 3 !

Note also that the corresponding permutation is exactly like the other one but inversed. For instance permutation _&lt;3, 1, 2&gt;_ is the inversed in order of _&lt;2, 1, 3&gt;_.

So, we could divide our list of permutations into two halves such that a pair's sum equals $min(bubbleCount) + max(bubbleCount)$. Clearly, There are a total of $n!$ permutations. The number of those pairs is half of total permutations. Hence, total sum of bubble counts is $\frac{n!}{2} \times (min(bubbleCount) + max(bubbleCount))$. Now we divide that total sum on total number of permutations to get the average of all _bubbleCounts_. So, The formula is now $\frac{(min(bubbleCount) + max(bubbleCount))}{2}$.  Clearly, least _bubbleCount_ is always zero, As we have the permutation which is already sorted. What about the greatest one? The worst case is the permutation sorted inversely. In such case, The first iteration, i.e outer loop, accounts for $(n-1)$ bubbles. The second itertaion accounts for $(n-2)$, and so on untill an iteration accounts for exactly one bubble. So, $max(bubbleCount)$ = (n-1) + (n-2) + .. + 1 = $\frac{n \times (n-1)}{2}$. Hence, Our **conjectured** formula is

$$\frac{0 + \frac{n(n-1)}{2} }{2} = \frac{n(n-1)}{4}$$

Check [this](https://en.wikipedia.org/wiki/Carl_Friedrich_Gauss#Anecdotes) for more information about gaussian's famous equation.

### More Justification on Symmetry
We have shown that least _bubbleCount_ and greatest _bubbleCount_ among all permutations are equal to zero and (n-1) + (n-2) + .. + 1, respectively. Let's take a deeper and more general look on why we could divide our permutations list into two halfs whereby each pair's sum is equal to greatest _bubbleCount_. That pair's permutations are also inverse of each other.

For the case of $n=3$, Pick up two permutations which are inverse of each other and try to run _bubbleSort_ algorithm on both of them. You shall find for a permutation, The bubble counted on some pair of numbers, is not counted in the other corresponding permutation. For instance, permutation _&lt;1, 3, 2&gt;_ needs one _bubble swap_ in _&lt;3, 2&gt;_ pair. For the permutation's inverse _&lt;2, 3, 1&gt;_, There's no need to bubble swap _&lt;2, 3&gt;_ pair. That saves us one bubble swap out of three which is the maximum _bubbleCount_. 3 - 1 = 2, The bubbleCount of _&lt;2, 3, 1&gt;_. The same applies for any two pairs of permutations which are inverse of each other.

### Accepted Source Code on UVa
```
#include &lt;cstdio&gt;

#define ll long long
#define ull unsigned ll

using namespace std;

bool checkIthBit (int n, int i) {
  if( n &amp; (1 &lt;&lt; i) )
    return true;
  return false;
}


int main() {
  int t, cou = 1;

  scanf("%d", &amp;t);

  while (cou &lt;= t) {
    int n;
    ull numerator; int denominator;

    scanf("%d", &amp;n);

    numerator = ((ull)n*(ull)(n-1));
    denominator = 4;

    // check if nume is div by 2, and simplify rational form
    for (int i=0; i&lt;2; ++i) {
      if (!checkIthBit(numerator, 0)) {
	numerator = numerator/2;
	denominator = denominator/2;
      }
    }

    if (denominator == 1) printf("Case %d: %llu\n", cou, numerator);
    else printf("Case %d: %llu/%d\n", cou, numerator, denominator);

    cou++;
  }
  return 0;
}
```

___

Many of those who do not appreciate math, think of it as a routine where you just follow a systematic order of operations on numbers. If you are one those, I hope this article changed, at least doubted, how you perceive it. There are a whole deep and elegant adventures still awaiting you if you delved more deeply.
</pre></body></html>
