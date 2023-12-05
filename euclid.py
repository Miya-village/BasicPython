#問3
def f(a, b):
    if a < b: #aが大きい方、bが小さい方の数字に直す
        c = a
        a = b
        b = c

    while True:
        if a == b:
            result = a
            break
    
        c = a - b

        if c == 1:
            result = 1
            break

        elif c >= b:
            a = c

        elif b > c:
            a = b
            b = c

    return result

#問4
def g(a, b):

    if f(a, b) == 1:
        return True
    
    else:
        return False

#エクストラ問題
import random
from math import pi

s = 0
for i in range(100000):
    x = random.randint(1, 10000)
    y = random.randint(1, 10000)
    
    if g(x, y) == True:
        s = s + 1

P = s / 100000
print(P)                #互いに素な確率
print(P - 6/(pi ** 2))  #理論値とのズレ