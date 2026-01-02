for _ in range(int(input())):

    val = int(input())

    if val == 1:
        print(1)
        continue

    if val <= 4:
        print(2)
        continue

    firstOperation = 2
    oneCounts = 4
    actualZeros = val - oneCounts

    while actualZeros > 0:
        firstOperation += 1
        oneCounts += 1
        oneCounts *= 2
        actualZeros = val - oneCounts

    print(firstOperation)