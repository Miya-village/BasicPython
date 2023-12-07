import sys

def f(n):
    
    if not(n == int(n)) or not((n >= 1) == True): #nが自然数であることを確認
        print("変数に自然数を入れてください")
        sys.exit()

    if n == 1:
        return False
    
    else:
        s = 0
        i = 1
        while i <= (n ** (1/2)): #√n以下の自然数でnを割り切れるか試す
            i = i + 1
            if n % i == 0:
                s = 1
                break

        if s == 0:
            return True
    
        else:
            return False