import sys

def p_judge(n):
    if n == 1:
        print("1は素数ではありません")

    elif n == 2:
        print("2は素数です")

    else:
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

p_judge(a)
p_judge(b)

