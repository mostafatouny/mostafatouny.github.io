---
title: 573 UVa, The Snail
subtitle: Not based on fancy algorithms or data structures.
summary: Not based on fancy algorithms or data structures.

math: true
mmark: true

date: "2020-04-26T00:00:01Z"

---

### My Proposed Solution
Probably, You thought of the straight forward solution of just simulating the height reached by the snail day by day till some condition applies. So, your computation would look like
$$ (u_1 - fatigue_1 - d_1) + (u_2 - fatigue_2 - d_2) + .. + (u_n - fatigue_n - d_n) $$

In this solution I claim determining whether the snail succeeded or failed could be done in $O(1)$ !! (that discovery was a surprise for me, as well). In a nutshell, We shall derive a formula which computes the snail's height on any given day. Then we find the day in which the snail's height is at its peak. By plugging in that day in the formula, we compute the height peak of the snail. if that height peak is greater than $h$, the weight of the well, then we conclude the snail at some point exceeds the well. If the height peak is equal or less than $h$, Then we conclude the snail shall not exceed the well.

Let's begin by finding the formula. I noticed a pattern. That computation you probably first thought of is exactly like 
$$ (u_1 + u_2 + .. + u_n) - (d_1 + d_2 + .. + d_n) - (fatigue_1 + fatigue_2 + .. + fatigue_n) $$
$$ = (u \times i) - (d \times i) - (\text{total fatigue up to day i})$$
So, instead of looping in a complexity of $\omega(n)$, One equation could achieve the same result in a complexity of $O(1)$. The first and second parts are obvious, but how do we find the third one? First, Assume $f=1$, then $$fatigue_1=0.01 * u * 1, fatigue_2=0.01 * u * 2 , .. , fatigue_n=0.01 * u * i$$
As each day we increase fatigue by $f$, day number $i$ should be equal to $i$ times $f$. $0.01$ and $u$ are common factors, so we could re-write this as
$$(0.01*u)(1 + 2 + .. + i)$$
the right part of the equation is where the magic happens. Friedrich Gauss, The legendary mathematician discovered that it is equal to 
$$\frac{n(n+1)}{2}$$
He made it when he was a kid as his teacher tried to preoccupy his time with tedious math calculation! read his story [here](https://en.wikipedia.org/wiki/Carl_Friedrich_Gauss#Anecdotes).
So, the final pattern looks like this
$$ (u_1 + u_2 + .. + u_n) - (d_1 + d_2 + .. + d_n) - \frac{n(n+1)}{2} $$
So far, that equation applies when $f=1$ but the The _Snail - 573_ problem asks for a general value of $f$. Let me get you through the proof of Guassian's equation briefly, and see how could we generalize it to a general value of $f$. Assume we wish to calculate $2 \times (1+2+ .. + n)$. That could be re-written as
$$ 1 + 2 + .. + n $$
$$ + $$
$$ n + (n-1) + .. + 1 $$
Try to interpret both of these equations as $n$ columns of two rows. The first column is $1+n$, second is $2+(n-1)$, .. , nth day is $n+1$. All of the $n$ columns are equal to $n+1$. Therefore
$$2 \times (1+2+ .. + n) = n(n+1)$$
Divide both sides by two, and the proof of Guassian's equation is done. QED. Now, instead of incrementing by one, the value of %f%, assume %f=x% where x is an arbitrary value. Let's try to re-apply the proof again. This is time we calculate $2 \times (x+2x+ .. + nx)$. We re-write it as
$$ x + 2x + .. + nx $$
$$ + $$
$$ nx + (n-1)x + .. + x $$
Similarly, $(x+nx) + (2x+(n-1)x) + .. + (nx+x) = n(nx+x)$, As each term of the n terms is equal to $(x+nx)$. Dividing by two yields us the final magical equation as follows
$$ (u \times n) - (d \times n) - \frac{n(nx+x)}{2} $$
That justifies _totalHeight_ and _fOnDay_ functions in my source code (see them below). So now, we could find the height of the snail at any day by just plugging-in a formula in a complexity of $O(1)$.

How are we going to use the formula we just derived? Are we going to loop on each day, applying the formula then checking for some conditions? That would account for complexity of $\omega(n)$ which saves us nearly nothing. As I promised you before, We find the day in which the snail reaches its peak. Then we plug-in that day in the formula we just derived to find the greatest possible height the snail ever reached. Finally, we compare that with $h$ to reach our conclusion of whether the snail succeeded.

Take a look at the following equation. Recall that $u$, $d$ and $f$ are given in _The Snail - 573_ problem.
$$ (i*f)*u = (u-d) $$
So, The only unknown is $i$ which could be easily computed. What we are trying to find out here is the day $i$ for which _fatigue_ is equal to the total increment the snail achieves. in other words, we are looking for the day in which fatigue totally cancels out any upwards increment. The upwards increase of $u-d$ keeps decaying due to fatigue till no possible upwards increment is possible. Hence, day $i$ in the above equation is the day in which the snail reaches its peak! That justifies my function _dayOfNonIncrease_ in the source code below. Now, we could find out the maximum possible height reached by the snail.

At this point, I delivered my promise that we could find out whether the snail failed or succeeded in $O(1)$. _The Snail_ problem asks for more than that, namely, the day in which the snail succeeded or failed.

There is a catch in our approach. According to _The Snail - 573_ problem, the fatigue cannot result in negative upwards increment, As stated _The snail never climbs a negative distance_. Our formula does not take into its account that the max possible fatigue is 100%. Nonetheless, That would not disrupt we could find out whether the snail succeeded or failed in $O(1)$ as illustrated above. That could be clearly seen as we do not need to compute up to days in which fatigue exceeds 100%.

However, We are going to rectify that limitation in order to complete solving _The Snail_ problem. We divide the computation of total height in a given day by two parts. The first part is computed exactly as mentioned before and applies on a day $i$ which is equal or less than the day _maxFatDay_ in which fatigue is 100%. the second part handles days in which fatigue exceeds 100%. For the second part, total height could be clearly found by $(i-maxFatDay) \times d$, As fatigue would totally cancel out upwards climb. In other words, In these days, the snail would just be dropping down without any climb. By summing both of these parts we could find out the height of any given day, Even if that day is beyond maxFatDay in which fatigue reached its maximum. Note that _maxFatDay_ might not be exactly 100% as $f$ might not divides 100. In this case, It would be the maximum fatigue equal or less than 100%. That justifies my function _totalHeightAnyDay_ in source code below.

So far, We are still computing in a complexity of $O(1)$ !! The last scene is finding the day the snail first exceeded $h$ or dropped to a negative height. Unfortunately, I could not find a way but to keep looping, beginning from the day of snail reaching its peak, till its height is either below $h$ or negative. That is the last part of my source code below. Could you improve upon this solution to maintain a complexity of $\omega(1)$?


### Source Code
```
#include <stdio.h>
#include <algorithm>

// total u's from day 1 to day i
int uOnDay(int u, int i) {
  return u*i;
}

// total d's from day 1 to day i
int dOnDay(int d, int i) {
  return d*i;
}

// total fatigue percentage from day 1 to day i
// it is a generalization of gaussian's famous equation n(n+1)/2 = 1 + 2 + .. + n
float fOnDay(float f, int i) {
  return (i*((i*f)+f))/2;
}

// we find day i such that
// i * (fPercent*u) = u - d
int dayOfNonIncrease(int u, int d, float fPercent) {
  float res = (float)(u-d)/(float)(fPercent*u);
  return std::max(int(res), 0);
}

// we find day i such that
// i * fPercent = 1
int findDayOfMaxF(float fPercent) {
  int res = (float)1/fPercent;
  return res;
}

// height at day i, in case no fatigue is more than 100% from day 1 up to day i
// totalF is total fatigue percentage from day 1 up to i
float totalHeight(int u, int d, int i, float totalF) {
  return (float)uOnDay(u, i) - (float)dOnDay(d, i) - totalF;
}

// height at day i. no constraints here
float totalHeightAnyDay(int u, int d, float fPercent, int peakHeightDay, int dayOfMaxFat, int i) {
  float totalF, tot;
  
  if (i <= dayOfMaxFat) {
    totalF = (float)u*fOnDay(fPercent, i-1);
    tot = totalHeight(u, d, i, totalF);
    return tot;
  }
  else {
    totalF = (float)u*fOnDay(fPercent, dayOfMaxFat-1);
    tot = totalHeight(u, d, dayOfMaxFat, totalF);
    int daysRng = i - dayOfMaxFat;

    // after dayOfMaxFat, fatigue would be more than 100% if same function is applied
    // max fatigue possible is 100%
    totalF = ((float)u*1)*daysRng;
    tot += totalHeight(u, d, daysRng, totalF);
    
    return tot;
  }
}

int main() {
  int h, u, d, f;
  
  while(true) {

    scanf("%d %d %d %d", &h, &u, &d, &f);
    if (h==0)
      break;

    // f as a percentage
    float fPercent = (float)f/(float)100;
    // day in which snail reached its peak
    int peakHeightDay = dayOfNonIncrease(u, d, fPercent);
    peakHeightDay += 1;
    // day in which snail fatigue reached its highest possible value
    int dayOfMaxFat = findDayOfMaxF(fPercent);
    dayOfMaxFat += 1;

    // calculate height at day of maximum possible height
    float peakHeight =  totalHeightAnyDay(u, d, fPercent, peakHeightDay, dayOfMaxFat, peakHeightDay) + d;


    // if peak is greater than h, then the snail succeeded
    // if not, then the snail shall never exceed h
    
    float tot;
    if (peakHeight > h) {
      int i=peakHeightDay;
      // keep moving days backwards till the snail's height is less than h
      do {
	i--;
	if (i<1)
	  break;
	tot = totalHeightAnyDay(u, d, fPercent, peakHeightDay, dayOfMaxFat, i) + d;
      }
      while(tot > h);

      // the day after catched day above, is the one in which snail first exceeded h
      printf("success on day %d\n", i+1);
    }
    else {
      int i = peakHeightDay;
      // keep moving days upwards till the snail's height is negative
      do {
	tot = totalHeightAnyDay(u, d, fPercent, peakHeightDay, dayOfMaxFat, i);
	i++;
      }
      while(tot >= 0);

      // the day catched above is greater than the day in which snail's height became negative by one
      printf("failure on day %d\n", i-1);
    }
    
  }
  
  return 0;
}

```
