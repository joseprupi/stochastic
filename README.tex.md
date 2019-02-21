# Stochastic processes #

[Wiener proces](#wiener-process)

[Law of large numbers](#law-of-large-numbers)

[From Law of large numbers to Central Limit thorem](#from-law-of-large-numbers-to-central-limit-thorem)

[Central limit theorem](#central-limit-theorem)

[Random walk](#random-walk)

#### Wiener process ####

An intuitive way of understanding [a Wiener process](https://en.wikipedia.org/wiki/Wiener_process) is seeing it as a limit of [random walk](https://github.com/joseprupi/randomwalk). From wikipedia:

**Let $\xi_1, xi_2, ...$ be i.i.d. random variables with mean 0 and variance 1. For each n, define a continuous time stochastic process:**


$$W_{n}(t)={\frac {1}{\sqrt {n}}}\sum \limits _{1\leq k\leq \lfloor nt\rfloor }\xi _{k},\qquad t\in [0,1]$$
