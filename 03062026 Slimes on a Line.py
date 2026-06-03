import math

for _ in range(int(input())):
    size = int(input())
    arr = list(map(int, input().split()))

    biggest = max(arr)
    slower = min(arr)

    print(math.ceil((biggest - slower) / 2))