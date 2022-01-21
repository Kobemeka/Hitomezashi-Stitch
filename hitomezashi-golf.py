from numpy.random import randint as t
import matplotlib.pyplot as p
e = enumerate
z = [20,15]
_,x = p.subplots()
x.set_aspect(z[1]/z[0])
[[[x.plot(*[[i, i + 1],[b,b]][::d],color="k") for i,k in e(l) if k==1] for b,l in e([([0,1]*((z[::d][0]//2)+1))[0+i:z[::d][0]+i] for i in [t(0,2) for _ in range(z[::d][1]+1)]])] for d in [-1,1]]
p.axis("off")
p.savefig(f"hitomezashi-stitch-{z[0]}-{z[1]}.png",dpi=120)
p.show()
