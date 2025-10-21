import math
from functools import reduce

for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    gcd = 0
    lcm = 1
    for i in range(n-1,-1,-1):
        gcd = math.gcd(gcd, arr[i])
        lcm = math.lcm(lcm, arr[i] // gcd)
    print(lcm)