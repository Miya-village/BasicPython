from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------
from math import pi

def f(a, b, N):
    h = (b - a) / N
    S = 0
    for i in range(N):
       S = S + (h / 2) * (sin(a + i * h) + sin(a + (i + 1) * h))
    
    return S

print(f(0, (pi/2), 100))