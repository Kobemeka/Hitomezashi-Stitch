from numpy.random import randint as t
import matplotlib.pyplot as p
e = enumerate
z = 20
_,x = p.subplots()
x.set_aspect(1)
[[[x.plot(*[[i, i+1],[b,b]][::d],color="k") for i,k in e(l) if k==1] for b,l in e([([0,1]*((z//2)+1))[0+i:z+i] for i in [t(0,2) for _ in range(z+1)]])] for d in [-1,1]]
p.axis("off")
p.savefig(f"hitomezashi-stitch-{z}.png",dpi=120)
p.show()
