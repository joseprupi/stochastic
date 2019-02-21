# Some intuition behind random walks #

[Independent and identically distributed random variables](#independent-and-identically-distributed-random-variables)

[Law of large numbers](#law-of-large-numbers)

[From Law of large numbers to Central Limit thorem](#from-law-of-large-numbers-to-central-limit-thorem)

[Central limit theorem](#central-limit-theorem)

[Random walk](#random-walk)

#### Independent and identically distributed random variables ####

[Independent and identically distributed random variables (i.i.d.) ](https://en.wikipedia.org/wiki/Independent_and_identically_distributed_random_variables) are a set of random variables that have same distribution and are independent. Some exmaples of i.i.d. are tossing a coin or rolling a dice
n times, each event is mutually independent from the other ones so the result when tossing the coin is not affected by any other event having all of them same distribution.

#### Law of large numbers ####

From a high level prospective [this law](https://en.wikipedia.org/wiki/Law_of_large_numbers) is quite intuitive, and it says that when having a sequence of i.i.d. the average of all results will converge to the mean of the distribution of the variables.

The easiest example I can think about would be tossing a coin and accumulate the result of doing it, if it lands with head upwards we sum 1 to our result otherwise we add 0 and calculate the average. It easy to see that as we keep repeating the experiment the result will get closer to 0.5.

In a formal way we can write the Law of Large Numbers as:

$$\lim_{n\to\infty}Pr(|\overline{X_n}-\mu| \geq\epsilon) = 0 \text{  for any  }\epsilon$$


