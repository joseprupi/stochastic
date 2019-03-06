# Stochastic processes #

[Wiener proces](#wiener-process)

#### Wiener process ####

An intuitive way of understanding [a Wiener process](https://en.wikipedia.org/wiki/Wiener_process) is seeing it as a limit of [random walk](https://github.com/joseprupi/randomwalk). From wikipedia:

**Let <img src="/tex/77f80dcb57870d15d47ff42fd83925b9.svg?invert_in_darkmode&sanitize=true" align=middle width=65.30938425pt height=22.831056599999986pt/> be i.i.d. random variables with mean 0 and variance 1. For each n, define a continuous time stochastic process:**


<p align="center"><img src="/tex/cbe2baa9af8de8d6361d646248ceadf3.svg?invert_in_darkmode&sanitize=true" align=middle width=271.98184695pt height=45.002035649999996pt/></p>

**This is a random step function. Increments <img src="/tex/fc848c2ebd267b4cd8b5bd06be9b2816.svg?invert_in_darkmode&sanitize=true" align=middle width=23.65115609999999pt height=22.465723500000017pt/> are independent because the <img src="/tex/44d9dddc6e2b61323f5595edb826a9f3.svg?invert_in_darkmode&sanitize=true" align=middle width=14.45784119999999pt height=22.831056599999986pt/> are independent. For large n, <img src="/tex/4a3405f5321fcb2629bfb24d3ba53383.svg?invert_in_darkmode&sanitize=true" align=middle width=108.24977789999998pt height=24.65753399999998pt/> is close to <img src="/tex/f7399f5fa2339fb9cc91ed56a55a7e6b.svg?invert_in_darkmode&sanitize=true" align=middle width=77.04326189999999pt height=24.65753399999998pt/> [by the central limit theorem](https://github.com/joseprupi/randomwalk#central-limit-theorem). Donsker's theorem proved that as <img src="/tex/ef14b5590a55d11e5c8dd5b37eb6fdf2.svg?invert_in_darkmode&sanitize=true" align=middle width=51.87587954999999pt height=14.15524440000002pt/> , <img src="/tex/fc848c2ebd267b4cd8b5bd06be9b2816.svg?invert_in_darkmode&sanitize=true" align=middle width=23.65115609999999pt height=22.465723500000017pt/> approaches a Wiener process, which explains the ubiquity of Brownian.**

And also from wikipedia, a Wiener process has to follow below properties:

* <img src="/tex/8bbb73a94710de20f4c34bd07424b785.svg?invert_in_darkmode&sanitize=true" align=middle width=53.03643344999998pt height=22.465723500000017pt/> a.s.
* <img src="/tex/84c95f91a742c9ceb460a83f9b5090bf.svg?invert_in_darkmode&sanitize=true" align=middle width=17.80826024999999pt height=22.465723500000017pt/> has independent increments: for every <img src="/tex/5a55f30e694820fa3f61e00fd5ba99cd.svg?invert_in_darkmode&sanitize=true" align=middle width=40.639161749999985pt height=21.18721440000001pt/> the future increments <img src="/tex/13b9a8515ad4a4e22699dd4336e6d8bd.svg?invert_in_darkmode&sanitize=true" align=middle width=85.14657689999999pt height=22.465723500000017pt/> <img src="/tex/132671665582964132d1164d1b7ce344.svg?invert_in_darkmode&sanitize=true" align=middle width=44.11333739999999pt height=21.18721440000001pt/>, are independent of the past values <img src="/tex/2513f91cdbcc53200ac80c43ba9b8f7e.svg?invert_in_darkmode&sanitize=true" align=middle width=69.98273205pt height=22.465723500000017pt/>
* <img src="/tex/84c95f91a742c9ceb460a83f9b5090bf.svg?invert_in_darkmode&sanitize=true" align=middle width=17.80826024999999pt height=22.465723500000017pt/> has Gaussian increments: <img src="/tex/fbcb88fe306c040c20f19a7b64955fda.svg?invert_in_darkmode&sanitize=true" align=middle width=79.75845734999999pt height=22.465723500000017pt/> is normally distributed with mean <img src="/tex/29632a9bf827ce0200454dd32fc3be82.svg?invert_in_darkmode&sanitize=true" align=middle width=8.219209349999991pt height=21.18721440000001pt/> and variance <img src="/tex/6dbb78540bd76da3f1625782d42d6d16.svg?invert_in_darkmode&sanitize=true" align=middle width=9.41027339999999pt height=14.15524440000002pt/>, <img src="/tex/3c1fa16ad4db2427564f1a3a7a16b94c.svg?invert_in_darkmode&sanitize=true" align=middle width=160.69486124999997pt height=24.65753399999998pt/>
* <img src="/tex/84c95f91a742c9ceb460a83f9b5090bf.svg?invert_in_darkmode&sanitize=true" align=middle width=17.80826024999999pt height=22.465723500000017pt/> has continuous paths: With probability <img src="/tex/034d0a6be0424bffe9a6e7ac9236c0f5.svg?invert_in_darkmode&sanitize=true" align=middle width=8.219209349999991pt height=21.18721440000001pt/>, <img src="/tex/dc92b47a36c3a7e426608cd76609eb7f.svg?invert_in_darkmode&sanitize=true" align=middle width=20.49092594999999pt height=22.465723500000017pt/> is continuous in <img src="/tex/4f4f4e395762a3af4575de74c019ebb5.svg?invert_in_darkmode&sanitize=true" align=middle width=5.936097749999991pt height=20.221802699999984pt/>.

So, with all this properties and as is stated at *Hull, Options, Futures, and Other Derivatives* we can say that a variable <img src="/tex/f93ce33e511096ed626b4719d50f17d2.svg?invert_in_darkmode&sanitize=true" align=middle width=8.367621899999993pt height=14.15524440000002pt/> follows a Wiener process if:

* The change <img src="/tex/d8cdb2a4c018cdd28ba3a4b7d3fa7f9e.svg?invert_in_darkmode&sanitize=true" align=middle width=22.06629479999999pt height=22.465723500000017pt/> during a small period of time <img src="/tex/5a63739e01952f6a63389340c037ae29.svg?invert_in_darkmode&sanitize=true" align=middle width=19.634768999999988pt height=22.465723500000017pt/> is: <img src="/tex/694b2fafa6accba266408c65e17861e8.svg?invert_in_darkmode&sanitize=true" align=middle width=83.98975364999998pt height=29.150579699999998pt/> where <img src="/tex/7ccca27b5ccc533a2dd72dc6fa28ed84.svg?invert_in_darkmode&sanitize=true" align=middle width=6.672392099999992pt height=14.15524440000002pt/> has a normal distribution of <img src="/tex/c87ec632ce2bc4e792521d06d1c250e8.svg?invert_in_darkmode&sanitize=true" align=middle width=46.32427964999999pt height=24.65753399999998pt/>. So <img src="/tex/d8cdb2a4c018cdd28ba3a4b7d3fa7f9e.svg?invert_in_darkmode&sanitize=true" align=middle width=22.06629479999999pt height=22.465723500000017pt/> will have a mean of <img src="/tex/29632a9bf827ce0200454dd32fc3be82.svg?invert_in_darkmode&sanitize=true" align=middle width=8.219209349999991pt height=21.18721440000001pt/> and a variance of <img src="/tex/5a63739e01952f6a63389340c037ae29.svg?invert_in_darkmode&sanitize=true" align=middle width=19.634768999999988pt height=22.465723500000017pt/>
* The values of <img src="/tex/d8cdb2a4c018cdd28ba3a4b7d3fa7f9e.svg?invert_in_darkmode&sanitize=true" align=middle width=22.06629479999999pt height=22.465723500000017pt/> for any two different short intervals of time, <img src="/tex/5a63739e01952f6a63389340c037ae29.svg?invert_in_darkmode&sanitize=true" align=middle width=19.634768999999988pt height=22.465723500000017pt/>, are independent.