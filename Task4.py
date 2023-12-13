from random import * 

n = int(input())
a = [0] * n
for i in range(n):
 a[i] = randint(1,10)
print()
for i in range(n-1):
 imax = i
 for j in range(i+1, n):
  if a[j] > a[imax]:
   imax = j
  a[i], a[imax] = a[imax], a[i]
print (*a)
