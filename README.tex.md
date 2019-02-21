# Stochastic processes #

[Wiener proces](#wiener-process)

#### Wiener process ####

An intuitive way of understanding [a Wiener process](https://en.wikipedia.org/wiki/Wiener_process) is seeing it as a limit of [random walk](https://github.com/joseprupi/randomwalk). From wikipedia:

**Let $\xi_1, xi_2, ...$ be i.i.d. random variables with mean 0 and variance 1. For each n, define a continuous time stochastic process:**


$$W_{n}(t)={\frac {1}{\sqrt {n}}}\sum \limits _{1\leq k\leq \lfloor nt\rfloor }\xi _{k},\qquad t\in [0,1]$$

**This is a random step function. Increments $W_{n}$ are independent because the $\xi _{k}$ are independent. For large n, $W_{n}(t)-W_{n}(s)$ is close to $N(0,t-s)$ [by the central limit theorem](https://github.com/joseprupi/randomwalk#central-limit-theorem). Donsker's theorem proved that as $n\to \infty$ , $W_{n}$ approaches a Wiener process, which explains the ubiquity of Brownian.**

And also from wikipedia, a Wiener process has to follow below properties:

$W_{0}=0$ a.s.
$W$ has independent increments: for every $\t>0,$ the future increments $W_{t+u}-W_{t},$ $u\geq 0,$, are independent of the past values $ s<t.$
{\displaystyle W} W has Gaussian increments: {\displaystyle W_{t+u}-W_{t}} {\displaystyle W_{t+u}-W_{t}} is normally distributed with mean {\displaystyle 0} {\displaystyle 0} and variance {\displaystyle u} u, {\displaystyle W_{t+u}-W_{t}\sim {\mathcal {N}}(0,u).} {\displaystyle W_{t+u}-W_{t}\sim {\mathcal {N}}(0,u).}
{\displaystyle W} W has continuous paths: With probability {\displaystyle 1} 1, {\displaystyle W_{t}} W_{t} is continuous in {\displaystyle t} t.