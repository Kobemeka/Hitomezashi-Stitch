from numpy.random import randint as t
import matplotlib.pyplot as p
e = enumerate
r = range

def s(n,m):
    return [([0,1]*((n // 2) + 1))[0+i:n+i] for i in [t(0,2) for _ in r(m+1)]]

def u(s,x,a):
    [[x.plot(*[[i, i + 1],[b,b]][::a]) for i,k in e(l) if k == 1] for b,l in e(s)]

def hitomezashi(z):
    _,x = p.subplots()
    [u(s(*z[::d]),x,d) for d in [-1,1]]
    p.show()