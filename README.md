# Stochastic processes #

[Wiener proces](#wiener-process)

#### Wiener process ####

An intuitive way of understanding [a Wiener process](https://en.wikipedia.org/wiki/Wiener_process) is seeing it as a limit of [random walk](https://github.com/joseprupi/randomwalk). From wikipedia:

**Let <img src="/tex/77f80dcb57870d15d47ff42fd83925b9.svg?invert_in_darkmode&sanitize=true" align=middle width=65.30938425pt height=22.831056599999986pt/> be i.i.d. random variables with mean 0 and variance 1. For each n, define a continuous time stochastic process:**


<p align="center"><img src="/tex/cbe2baa9af8de8d6361d646248ceadf3.svg?invert_in_darkmode&sanitize=true" align=middle width=271.98184695pt height=45.002035649999996pt/></p>

**This is a random step function. Increments <img src="/tex/fc848c2ebd267b4cd8b5bd06be9b2816.svg?invert_in_darkmode&sanitize=true" align=middle width=23.65115609999999pt height=22.465723500000017pt/> are independent because the <img src="/tex/44d9dddc6e2b61323f5595edb826a9f3.svg?invert_in_darkmode&sanitize=true" align=middle width=14.45784119999999pt height=22.831056599999986pt/> are independent. For large n, <img src="/tex/4a3405f5321fcb2629bfb24d3ba53383.svg?invert_in_darkmode&sanitize=true" align=middle width=108.24977789999998pt height=24.65753399999998pt/> is close to <img src="/tex/f7399f5fa2339fb9cc91ed56a55a7e6b.svg?invert_in_darkmode&sanitize=true" align=middle width=77.04326189999999pt height=24.65753399999998pt/> [by the central limit theorem](https://github.com/joseprupi/randomwalk#central-limit-theorem). Donsker's theorem proved that as <img src="/tex/ef14b5590a55d11e5c8dd5b37eb6fdf2.svg?invert_in_darkmode&sanitize=true" align=middle width=51.87587954999999pt height=14.15524440000002pt/> , <img src="/tex/fc848c2ebd267b4cd8b5bd06be9b2816.svg?invert_in_darkmode&sanitize=true" align=middle width=23.65115609999999pt height=22.465723500000017pt/> approaches a Wiener process, which explains the ubiquity of Brownian.**

And also from wikipedia, a Wiener process has to follow below properties:

* <img src="/tex/8bbb73a94710de20f4c34bd07424b785.svg?invert_in_darkmode&sanitize=true" align=middle width=53.03643344999998pt height=22.465723500000017pt/> a.s.
* <img src="/tex/84c95f91a742c9ceb460a83f9b5090bf.svg?invert_in_darkmode&sanitize=true" align=middle width=17.80826024999999pt height=22.465723500000017pt/> has independent increments: for every <img src="/tex/5a55f30e694820fa3f61e00fd5ba99cd.svg?invert_in_darkmode&sanitize=true" align=middle width=40.639161749999985pt height=21.18721440000001pt/> the future increments <img src="/tex/13b9a8515ad4a4e22699dd4336e6d8bd.svg?invert_in_darkmode&sanitize=true" align=middle width=85.14657689999999pt height=22.465723500000017pt/> <img src="/tex/132671665582964132d1164d1b7ce344.svg?invert_in_darkmode&sanitize=true" align=middle width=44.11333739999999pt height=21.18721440000001pt/>, are independent of the past values <img src="/tex/6f2643c8656a032332a5f9107be11fbf.svg?invert_in_darkmode&sanitize=true" align=middle width=40.12543094999999pt height=20.221802699999984pt/>
* {\displaystyle W} W has Gaussian increments: {\displaystyle W_{t+u}-W_{t}} {\displaystyle W_{t+u}-W_{t}} is normally distributed with mean {\displaystyle 0} {\displaystyle 0} and variance {\displaystyle u} u, {\displaystyle W_{t+u}-W_{t}\sim {\mathcal {N}}(0,u).} {\displaystyle W_{t+u}-W_{t}\sim {\mathcal {N}}(0,u).}
{\displaystyle W} W has continuous paths: With probability {\displaystyle 1} 1, {\displaystyle W_{t}} W_{t} is continuous in {\displaystyle t} t.