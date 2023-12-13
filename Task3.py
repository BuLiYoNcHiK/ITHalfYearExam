from random import * 

s = 0
n=50
a = [0] * n

for i in range(n):
    a[i] = randint(150,200)
    if a[i] >= 170:
        s+=1

print(s)
