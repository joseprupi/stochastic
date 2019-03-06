# Stochastic processes #

[Wiener proces](#wiener-process)

#### Wiener process ####

An intuitive way of understanding [a Wiener process](https://en.wikipedia.org/wiki/Wiener_process) is seeing it as a limit of [random walk](https://github.com/joseprupi/randomwalk). From wikipedia:

**Let $\xi_1, xi_2, ...$ be i.i.d. random variables with mean 0 and variance 1. For each n, define a continuous time stochastic process:**


$$W_{n}(t)={\frac {1}{\sqrt {n}}}\sum \limits _{1\leq k\leq \lfloor nt\rfloor }\xi _{k},\qquad t\in [0,1]$$

**This is a random step function. Increments $W_{n}$ are independent because the $\xi _{k}$ are independent. For large n, $W_{n}(t)-W_{n}(s)$ is close to $N(0,t-s)$ [by the central limit theorem](https://github.com/joseprupi/randomwalk#central-limit-theorem). Donsker's theorem proved that as $n\to \infty$ , $W_{n}$ approaches a Wiener process, which explains the ubiquity of Brownian.**

And also from wikipedia, a Wiener process has to follow below properties:

* $W_{0}=0$ a.s.
* $W$ has independent increments: for every $t>0,$ the future increments $W_{t+u}-W_{t},$ $u\geq 0,$, are independent of the past values $W_s, s<t.$
* $W$ has Gaussian increments: $W_{t+u}-W_{t}$ is normally distributed with mean $0$ and variance $u$, $W_{t+u}-W_{t}\sim {\mathcal {N}}(0,u).$
* $W$ has continuous paths: With probability $1$, $W_{t}$ is continuous in $t$.

So, with all this properties and as is stated at *Hull's Options, Futures, and Other Derivatives* we can say that a variable $z$ follows a Wiener process if:

* The change $\Delta z$ during a small period of time $\Delta t$ is: $\Delta z = \epsilon\sqrt{\Delta t}$ where $\epsilon$ has a normal distribution of $\phi(0,1)$. So $\Delta z$ will have a mean of $0$ and a variance of $\Delta t$
* The values of $\Delta z$ for any two different short intervals of time, $\Delta t$, are independent.