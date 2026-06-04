def aux(arr):
    number = 0

    for x in arr:
        if number-1 == x:
            continue
        if number == x:
            number += 1
        if number < x:
            break

    return number



for _ in range(int(input())):

    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort()

    magicValue = aux(arr)

    if arr[-1] == 1 and magicValue > 0:
        count = (n -1)*3 + 1
    elif arr[-1] == 0:
        count = n
    else:
        if magicValue == n:
            count = int(arr[-1]*n + ((n*(n-1))/2) + 1)

        else:
            count = int(arr[-1]*n + ((magicValue*(magicValue+1)/2)) + magicValue*(n-(magicValue+1)))
            if magicValue == arr[-1] + 1:
                count += 1

    print(count)