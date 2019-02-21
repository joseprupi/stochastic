# Stochastic processes #

[Wiener proces](#wiener-process)

#### Wiener process ####

An intuitive way of understanding [a Wiener process](https://en.wikipedia.org/wiki/Wiener_process) is seeing it as a limit of [random walk](https://github.com/joseprupi/randomwalk). From wikipedia:

**Let $\xi_1, xi_2, ...$ be i.i.d. random variables with mean 0 and variance 1. For each n, define a continuous time stochastic process:**


$$W_{n}(t)={\frac {1}{\sqrt {n}}}\sum \limits _{1\leq k\leq \lfloor nt\rfloor }\xi _{k},\qquad t\in [0,1]$$

**This is a random step function. Increments $W_{n}$ are independent because the $\xi _{k}$ are independent. For large n, $W_{n}(t)-W_{n}(s)$ is close to $N(0,t-s)$ by the central limit theorem. Donsker's theorem proved that as $n\to \infty$ , $W_{n}$ approaches a Wiener process, which explains the ubiquity of Brownian.**