# TODO
s=0
i=0
while 1 + (1/2) ** i > 1:
    i = i + 1

i = i - 1                   #　1 + (1/2) ** i > 1 が満たされるように一つ戻す

result = (1/2) ** i

print("εは1/2の" + f"{i}" + "乗")
print(result)