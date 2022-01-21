from numpy.random import randint as t
import matplotlib.pyplot as p
e = enumerate

s = lambda n,m: [([0,1]*((n // 2) + 1))[0+i:n+i] for i in [t(0,2) for _ in range(m+1)]]
def hitomezashi(z):
    [[[p.plot(*[[i, i + 1],[b,b]][::d]) for i,k in e(l) if k == 1] for b,l in e(s(*z[::d]))] for d in [-1,1]]
    p.show()

hitomezashi([20,20])