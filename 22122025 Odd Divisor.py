import math 

for t in range(int(input())):

    n = int(input())

    log2 = math.log2(n)

    if log2.is_integer():
        print("NO")
    else:
        print("YES")