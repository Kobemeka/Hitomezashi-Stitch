from numpy.random import randint as t
import matplotlib.pyplot as p
e = enumerate

def hitomezashi(z):
    [[[p.plot(*[[i, i + 1],[b,b]][::d]) for i,k in e(l) if k == 1] for b,l in e([([0,1]*((z[::d][0]//2)+1))[0+i:z[::d][0]+i] for i in [t(0,2) for _ in range(z[::d][1]+1)]])] for d in [-1,1]]
    p.show()

hitomezashi([20,20])