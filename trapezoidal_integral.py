from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------
from math import pi
from math import e

def g(f, a=0, b=1, n=100):
    H = (b - a) / n
    S = 0
    for i in range(n):
       S = S + (H / 2) * (f(a + i * H) + f(a + (i + 1) * H))
    
    return S

def h(x):
    return sin(x)

def i(x):
    return (4 / (1 + x **2))

def j(x):
    return (pi ** (1/2)) * (e ** ((-1) * (x ** 2)))

print(g(h, 0, pi/2, 50))
print(g(i, 0, 1, 100))
print(g(j, -100, 100, 1000))