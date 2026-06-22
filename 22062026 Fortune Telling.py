n = int(input())
arr = list(map(int, input().split()))

sizeOdds = 0
sumOdds = 0
lowerOdd = 200
even = 0

for element in arr:
    if element % 2 == 0:
        even += element

    else:
        if element < lowerOdd:
            lowerOdd = element
        sizeOdds += 1
        sumOdds += element

if sizeOdds == 0:
    print(0)
elif sizeOdds % 2 == 1:
    print(even + sumOdds)
else:
    print(even + sumOdds - lowerOdd)