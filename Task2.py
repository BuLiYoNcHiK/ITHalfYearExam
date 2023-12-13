from random import * 

n=30
a = [0] * n
for i in range(n):
    a[i] = randint(50, 200)

s = sum(a)
print(s)
