a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO
a = int(a)
b = int(b)

def f(x, y):
    if x < y: #xが大きい方、yが小さい方の数字に直す
        z = x
        x = y
        y = z

    while True:
        if x == y:
            result = x
            break
    
        z = x - y

        if z == 1:
            result = 1
            break

        elif z >= y:
            x = z

        elif y > z:
            x = y
            y = z

    return result

print(f(a, b))