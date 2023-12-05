a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO
a = int(a)
b = int(b)

def f(n):
    s = 0
    i = 1
    while i <= (n ** (1/2)): #√n以下の自然数でnを割り切れるか試す
        i = i + 1
        if n % i == 0:
            s = 1
            break

    if s == 0:
        print(f"{n}" + "は素数です")
    
    else:
        print(f"{n}" + "は素数ではありません")

f(a)
f(b)