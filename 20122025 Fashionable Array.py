for t in range(int(input())):

    s = int(input())
    arr = list(map(int, input().split()))

    arr.sort()

    paridadeFirst = arr[0] % 2
    paridadeLast = arr[-1] % 2

    numChanges = 0

    forFirst = s-1
    forLast = 0

    while True:
        if (arr[forFirst] % 2) == paridadeFirst or (arr[forLast] % 2) == paridadeLast:
            break
        else:
            forFirst -= 1
            forLast += 1
            numChanges += 1

    print(numChanges)
