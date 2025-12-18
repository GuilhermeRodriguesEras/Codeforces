import math

for t in range(int(input())):

    num = int(input())

    sumTotal = (num*num + num)/2
    aux = math.floor(math.log2(num))

    sumTotal -= 2*((2**(aux +1) -1))

    print(f"{sumTotal:.0f}")