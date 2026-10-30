import math

n = int(input())
s = 0

for d in str(n):
    s += math.factorial(int(d))

if s == n:
    print("Strong")
else:
    print("Not Strong")
