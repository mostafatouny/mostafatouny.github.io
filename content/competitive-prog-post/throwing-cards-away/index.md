---
title: UVa 10940, Throwing Cards Away II
subtitle: Math is not routine calculations at all.
summary: Math is not routine calculations at all.

math: true

date: "2020-06-11T00:00:01Z"
---

### First Trial

At each step we discard a card away, and move the new card at the top to the bottom of the deck. That suggests we eliminate half of the deck for one iteration. Consider the following deck

|   |    |
| - | -  |
| 1 | x  |
| 2 | -&gt; |
| 3 | x  |
| 4 | -&gt; |
| 5 | x  |
| 6 | -&gt; |
| 7 | x  |
| 8 | -&gt; |

Here, We have a deck of eight cards whereby card number one is at the top of the deck. _x_ indicates the card is to be thrown away, while _-&gt;_ indicates the card to be moved to the bottom. Note that in this case, None of the _-&gt;_ cards are going to be thrown away due to later _x_. It is easy to see that the result is as follows

|   |    |
| - | -  |
| 2 |  |
| 4 |  |
| 6 |  |
| 8 |  |

Similarly to the first iteration, the second one would be

|   |    |
| - | -  |
| 2 | x  |
| 4 | -&gt; |
| 6 | x  |
| 8 | -&gt; |

yielding

|   |  |
| - | -|
| 4 |  |
| 8 |  |

Finally, Getting _card eight_ as the answer.

So, On each iteration, we divided the dick by half and still got an even number of cards. It is clear that is attributed to the fact that _eight_ is a power of two. Otherwise, On some iteration we would end-up with an odd number of cards. That iteration is not the last one in which we have the last remaining card. You could see if we have a deck whose cards number is some power of two, Then the answer would be the last card at the bottom. In other words, if our cards number is $n = 2^k$ for some _k_, Then the correct answer of the problem, i.e the last remaining card after discarding cards and moving them to the bottom, is $2^k$.

### More Justification of First Trial's Observation
Let's try to take a deeper look at why do we always obtain the last bottom card as the remaining one in case the deck is some power of two, As illustrated earlier. Consider our $2^3 = 8$ deck but represented differently

On **First Iteration**:

|   |    |
| - | -  |
| $2^0 \times 1$ | x  |
| $2^0 \times 2$ | -&gt; |
| $2^0 \times 3$ | x  |
| $2^0 \times 4$ | -&gt; |
| $2^0 \times 5$ | x  |
| $2^0 \times 6$ | -&gt; |
| $2^0 \times 7$ | x  |
| $2^0 \times 8$ | -&gt; |

On **Second Iteration**:

|   |    |
| - | -  |
| $2^1 \times 1$ | x  |
| $2^1 \times 2$ | -&gt; |
| $2^1 \times 3$ | x  |
| $2^1 \times 4$ | -&gt; |

On **Third Iteration**:

|   |   |
| - | - |
| $2^2 \times 1$ | x |
| $2^2 \times 2$ | -&gt;|

Remarkably, Cards multiplied by an odd number gets thrown away, while cards multiplied by an even number gets moved to the bottom and survives to the next iteration. You could also see that $2^{k_0} \times (2k_1) = 2^{k_0+1}$. The even number increases the power of two by one. That correspoinds with our observation that each iteration's power is increased by one than its predocessor's power. Clearly, Continuing in this way ends us up with the greatest power of two in the whole deck, which is also the last bottom card.

### Generalizing for None Power of Two
Our solution for the generalized case is in fact an extension of the special case of deck's whose number is a power of two. Let's begin from where we ended up.

#### A Deck of Seven Cards

On **First Iteration**:

|   |    |
| - | -  |
| 1 | x  |
| 2 | -&gt; |
| 3 | x  |
| 4 | -&gt; |
| 5 | x  |
| 6 | -&gt; |
| 7 |  |

Note that I intentionally did not mark _card seven_. Otherwise, The second iteration would have the first card marked as _-&gt;_, violating consistency of marking among iterations. In case cards number is odd, as in this case, We prefer to avoid marking the last card, and get the second iteration as

|   |    |
| - | -  |
| 7 | x |
| 2 | -&gt; |
| 4 | x |
| 6 | -&gt; |

We have got here cards of some power of two. Following our illustrated observation in the previous section, We could conclude the last remaining card is _card six_.

For eight cards deck, The second iteration was _&lt;2, 4, 6, 8&gt;_. Removing _card eight_ from the deck resulted in having _card seven_ as a remainder from the first iteration, and shifting _&lt;2, 4, 6, 8&gt;_ one position to the right. As a result, We have _card six_ as the last one in _second iteration_

For eight cards deck, The last remaining card was _eight_. For seven cards deck, the last remaining card is _six_. Removing one card from the _eight cards deck_ yielded the same remaining card but subtracted by two. In other words, $8 - 1$ cards deck yields the last remaining card _sevenCardsAnswer_ = _eightCardsAnswer_ - (2 * removedCards) = 8 - (2 * 1) = 6. Let's try more trials and see how they relate with the case of _eight cards deck_

#### A Deck of Six Cards

On **First Iteration**:

|   |    |
| - | -  |
| 1 | x  |
| 2 | -&gt; |
| 3 | x  |
| 4 | -&gt; |
| 5 | x  |
| 6 | -&gt; |

On **Second Iteration**:

|   |    |
| - | -  |
| 2 | x |
| 4 | -&gt; |
| 6 | x |

So, we end-up with _card four_. Again, $8 - 2$ cards deck yields the last remaining card _sixCardsAnswer_ = _eightCardsAnswer_ - (2 * removedCards) = 8 - (2 * 2) = 4. Here, unlike the case of _seven cards deck_, There is no remainder from the first iteration so that we end up with four cards in the second iteration. As two cards are removed from _eight cards deck_, we have three cards in second iteration rather than four. _card six_ here is in an odd position, so it gets thrown away. The last remaining card is _card four_. In other words, It seems removing two cards from _eight cards deck_ shifted our _&lt;2, 4, 6, 8&gt;_ a position to the right in addition to removing the last card.

#### A Deck of Five Cards

On **First Iteration**:

|   |    |
| - | -  |
| 1 | x  |
| 2 | -&gt; |
| 3 | x  |
| 4 | -&gt; |
| 5 |  |

As in the case of _seven cards deck_, We do not mark _card five_ in the first iteration. Recall the the last card is not marked whenever we have an odd number of cards in an interation.

On **Second Iteration**:

|   |    |
| - | -  |
| 5 | x |
| 2 | -&gt; |
| 4 | x |

Again, $8 - 3$ cards deck yields the last remaining card _fiveCardsAnswer_ = _eightCardsAnswer_ - (2 * removedCards) = 8 - (2 * 3) = 2. It seems removing two cards shifted _&lt;2, 4, 6, 8&gt;_ on position to the right, and removing an additional card shifted it another position to the right but with a remainder, namely _card five_. So, we get _card two_ as the answer.

### Magical Formula
The illustrated reasoning **SEEMS** to work on not just $2^3 = 8$ but any power of two. For an arbitrary number of deck cards $n$, We find the power of two greater than or equal to $n$, Then compute the answer for $n$ by _nCardsAnswer_ = _Power2CardsAnswer_ - (2 * (Power2Cards - nCards)). So, How do find the power of two equal or greater than $n$? Here is a trick: $2^{ceil(log_2(n))}$. So, The final formula would be

$$2^{ceil(log_2(n))} - (2 \times (2^{ceil(log_2(n))} - n)) = 2 \times (n-2^{ceil(log_2(n))-1})$$

### Accepted Source Code on UVa
```
#include &lt;cstdio&gt;
#include &lt;math.h&gt;

using namespace std;

int main() {
  int n, res;

  scanf("%d", &amp;n);

  res = 2*(n-pow(2, (ceil(log2(n))-1)));
  
  if (n == 1) printf("1\n");
  else printf("%d\n", res);
  
  return 0;
}

```
