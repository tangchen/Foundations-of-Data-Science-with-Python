## Random Experiments

We have seen that simulation is a simple and powerful tool to answer questions about random experiments. The coin flipping experiment involved a very simple phenomena for which the experiment could be accurately simulated inside the computer. In this book, we will show that similar techniques can be used with real data sets with unknown random behavior to answer many different kinds of statistical questions.

Before we can do that, though, we need to take a step back to carefully define terminology and concepts that we will be using.

**Randomness** is surprisingly hard to define, and there are different philosophies (i.e., mental models) about what it means for something to be random! For now, we can use the following definition for a random experiment:

````{panels}
DEFINITION
^^^
random experiments 
: an experiment in which the result is not completely predictable to an observer based on the observer's knowledge of the system and its inputs.
````



**Examples of random experiments:**

* **E1** A die is rolled, and the number on the top face is noted
* **E2** A standard coin is flipped, and the top face (heads or tails) is noted
* **E3** The temperature in your town is to be recorded at 10 AM tomorrow
* **E4** The value of the Dow Jones Industrial Index is to be noted at the end of the year

Above we used the word *result* to denote something that we observe when we conduct or observe a random experiment. To be able to understand, model, simulate, and analyze random experiments we will need to introduce some much more precise language about what we can observe.  We start with defining an *outcome* of a random experiment:

````{panels}
DEFINITION
^^^
outcome 
: An outcome is a non-decomposable result (or output) of a random experiment.
````

It is useful to have a reference for all possible outcomes of an experiment:
````{panels}
DEFINITION
^^^
set
: an unordered collection of *unique* items

sample space (or universal set)
: the set of all possible outcomes of a random experiment
````

We will denote the sample space $S$. Another common notation is $\Omega$ (a Greek capital omega). This book assumes readers are familiar with sets and set operations. A review of basic set operations is given in **APPENDIX A (TO BE MADE)**.


In the experiments above,the results are all examples of outcomes. Not everything that we might observe or ask about the result of a random experiment is an outcome, though. The following are **not** outcomes:
* Whether the result of experiment **E1** is even 
* Whether the result of experiment **E3** is less than 70F
* Whether the result of experiment **E4** is within 100 points of the value at the beginning of the  year

Each of these examples are not outcomes because they can be decomposed into a **set** of outcomes:

* The result of experiment **E1** being even is the same as asking whether the outcome is in the set $\{2,4,6\}$.
* The results of experiment **E3** being less than 70 is the same as asking whether the outcome is in the set $\{x \vert x \in \mathbb{R}, x \le 70 \}$.
* The result of experiment **E4** being greater than the value at the beginning of the year can be written as follows: Let $d_0$ denote the value of the index at the beginning of the year, which is assumed known. Then we are asking if the final value is in the set $\left\{x \vert x \in \left[d_0-100, d_0+100\right] \right\}$.  

````{panels}
DEFINITION
^^^
event 
: any possible set of outcomes of an experiment to which we will assign probability
````

Although the definition of *event* may seem pretty straight-forward, there is actually a very subtle nuance. The definition does not say that every possible set of outcomes can be an event. We will only call a set of outcomes an event if we assign it probability. If we consider experiments which have an uncountably infinite **Add footnote: see Appendix A if you are not familiar with this terminology** set of outcomes, contradictions occur if we allow any possible set of outcomes to be events. Although this issue is important to achieve true mathematical rigor, the types of sets that we will not allow to be outcomes are so exotic that we can ignore this issue for the rest of the book.


**EXAMPLE**

Consider flipping a coin and observing the top face:

**(a)** If the coin is flipped one time what is the sample space?

When the outcomes of an experiment are not numbers, then it is best to introduce mathematical notation to represent the outcomes.  For a coin experiment, the outcomes are heads and tails, and almost everyone uses the notation $H$=heads and $T$=tails.  Then
$$
S_a= \{H,T\}
$$

**(b)** What if the coin is flipped four times, and the ordered sequence of heads and tails is recorded?

As before, we will use $H$ and $T$ to denote the outcomes from one flip. The result of multiple flips can be recorded using a *tuple*: the mathematical object -- not the Python data type. Mathematical tuples are very similar to Python tuples: both represent ordered sequences, enclosed by parentheses, with the individual elements separated by commas.

The resulting sample space is
\begin{align*}
S_b= \{&(T,T,T,T),~~ (T,T,T,H),~~ (T,T,H,T),~~ (T,T,H,H) \\
&(T,H,T,T),~~ (T,H,T,H),~~ (T,H,H,T),~~ (T,H,H,H) \\
&(H,T,T,T),~~ (H,T,T,H),~~ (H,T,H,T),~~ (H,T,H,H) \\
&(H,H,T,T),~~ (H,H,T,H),~~ (H,H,H,T),~~ (H,H,H,H) 
\}
\end{align*}

**(c)** For the experiment of part (b), give a description in words of an event that is not an outcome.

There is an even number of heads on the four flips.

When defining events, it is again helpful to introduce mathematical notation. Thus, we can define $E$ to be the event that an even number of heads occurs. 

Then $E$ can be written as a set of outcomes as
\begin{align*}
E= \{&(T,T,T,T),~~ (T,T,H,H),~~  (T,H,T,H),~~ (T,H,H,T) \\
&(H,T,T,H),~~ (H,T,H,T),~~ (H,H,T,T),~~ (H,H,H,H) 
\}
\end{align*}

````{panels}
DEFINITION
^^^
event class
: A collection of all events to which we assign probability. For our purposes, it is a set of subsets of $S$. 
````
If $S$ is finite, then the event class can be taken to be the power set of $S$ (the set of **all** subsets of $S$) **ADD REF TO APPENDIX**

**Example:** What is the event class for flipping a coin and observing the top face?

The sample space can be represented as $S={H,T}$. The event class is the power set of $S$, which is
$$
\mathcal{F}=\bigl\{ \emptyset, H, T, \left\{H,T\right\} \bigr\}
$$

Note that both the null set (or empty set), $\emptyset$, and the entire sample space $S=\{H,T\}$ are members of the event class. 


**Example:** What is the event class for rolling a die and observing the top face?

The sample space can be written as $S=\{1,2,3,4,5,6\}$. Then the event class is the power set. Because the power set contains $2^6=64$ members, we use Python to print out its members. (This implementation is based on an analogy between the members of the set and the binary representations of the numbers 0 to 63. **See Appendix A for details.**)

set_size=6
table_width=8

print("Event class contains:", end="")
num_entries=2**set_size
for i in range(num_entries):
    if i%table_width ==0:
        print()
    result="{"
    first=True
    for j in range(set_size):
        if i & (2**j) !=0:
            if first:
                first=False
            else:
                result+=","
            result+=str(j+1)
    result+="}"
    if i < num_entries-1:
        result+=","
    entry_width=2*set_size+1
    print(f"{result : <{entry_width}}", end="")

## Fair Experiments

Some experiments are said to be *fair*, which intuitively means that there is no bias toward one outcome over another. We can define this more precisely as follows:

````{panels}
DEFINITION
^^^
fair experiment
: an experiment is *fair* if every outcome has the same probability of occurring.
````

The following are types of experiments that people assume to be fair unless otherwise specified:
* Flipping a coin
* Rolling a die
* Picking a number from 1 to 10

We are interested in fair experiments because calculating the probabilities for such an experiment is very straight-forward. To do this, we first introduce some useful concepts, terminology, and notation.

We start with the following basic principal:

**The probabilities of the outcomes of an experiment sum to 1.**

Consider a fair experiment with $N$ outcomes, and let $p_i$ denote the probability of outcome $i$, then

$$
\sum_{i=1}^{N} p_i = 1 \\
\sum_{i=1}^{N} p_1 = 1 \\
Np_1=1\\
p_1 = \frac 1 N\\
p_i = \frac 1 N\\
$$

So, for instance, the probability of getting any number on a fair die is 1/6. Let's compare these to the relative frequencies:

First let's see some ways to count the number of unique outcomes from rolling a fair die:

num_sims=1000
rolls=[]
for sim in range(num_sims):
    die=random.choice(range(1, 7))
    rolls+=[die]
for j in range(1, 7):
    print(j, ":", rolls.count(j))

Because the die is fair, we expect the counts to be close to each other. If we increase the number of simulations the relative difference between different counts will get smaller.


## An Aside: Accelerating Simulations using NumPy

The simulation above is a perfectly valid way to roll a die and tabulate the counts of each outcome. However, we are going to demonstrate that it is also relatively slow, in the sense that the same simulation can be implemented much faster. We begin by determining the execution time of the current simulation (excluding the counting and printing). 

To do this, let's make the actualy die roll simulation into a function:

def diesim1(num_sims=1_000_000):
    rolls=[]
    for sim in range(num_sims):
        die=random.choice(range(1, 7))
        rolls+=[die]

%timeit diesim1()

When I wrote this, my computer took an average of about 1.05 to 1.1 seconds to roll the dice one million times. This is certainly fast enough for the simple cases like this, but as we build more complex simulations, the time to get accurate results will greatly increase.

A general rule of thumb is that `for` loops make simulations slower. It is much better to call a function that can return all the simulated values at once:

def dieroll2(num_sims=1_000_000):
    rolls=random.choices(range(1,7), k=num_sims)

%timeit dieroll2()

By eliminating the `for` loop, we have reduced the execution time to 1/4 of what it was previously. Another source of inefficiency for this simulation is `random.choices()`. Because `random.choices()` must be able to handle general lists of items, it will not be as fast as if we choose a method that is tuned for providing a list of integers. 

NumPy is the Numerical Python library, and it provides a broad range of functions for working with numbers. The `numpy.random` module contains those functions that generate different types of random numbers. Because we use numpy.random a lot, we will use npr for the namespace of its functions:

import numpy as np
import numpy.random as npr

def dieroll3(num_sims=1_000_000):
    rolls=npr.randint(1, 7, size=num_sims)

%timeit dieroll3()

The new version runs over 20 times faster than the previous and is around 100 times faster than the original version of the simulation. 

NumPy also provides efficient ways to do the counting of the results, as shown below:

def dieroll4(num_sims=1_000_000):
    rolls = npr.randint(1, 7, size=num_sims)
    vals, counts = np.unique(rolls, return_counts=True)
    for i, val in enumerate(vals):
        print(val, ":", counts[i])

dieroll4()



Let's try that for our experiment where we flip a coin 20 times:

num_sims=1000000
flips=20
counts=[]
for sim in range(num_sims):
    coins=random.choices(faces,k=flips)
    num_heads=coins.count('H')
    counts+=[num_heads]
    
vals,counts=np.unique(counts,return_counts=True)
for i in range(len(vals)):
    print(vals[i],counts[i]/num_sims)

This is an example of **binary hypothesis testing**. In this case, we set up two hypothesis:

$H_0$: (the *null hypothesis*) is that the observed effect is just caused by randomness in the sampling. It is not real in the underlying system or data. For this exampe, our null hypothesis is that the coin is actually fair

$H_1$: (the *alternative hypothesis*) is that the observed effect is not just caused by random sampling. In this example, the coin is biased toward Tails.

In classical statistics/hypothesis testing, we say that an effect is statistically significant if the probability of observing an effect of that size under the null hypothesis is smaller than some small value $p$. Typical values of $p$ are 0.05 or 0.01, but many argue for even smaller values now. **The threshold to determine statistical significance must always be determined before the experiment is conducted -- otherwise, there is too much temptation to adjust the threshold based on the observed $p$-value.**

In classical hypothesis testing, we do *not* test the alternative hypothesis directly, nor can we utilize side information that we may already have about the two hypotheses

?np.unique

