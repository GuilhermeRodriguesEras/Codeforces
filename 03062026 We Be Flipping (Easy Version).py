for _ in range(int(input())):
    size = int(input())
    arr = list(map(int, input().split()))
    output = []
    flipNumbers = 0

    for i in range(size-1, -1, -1):
        if (arr[i] > 0 and flipNumbers%2 == 0) or (arr[i] < 0 and flipNumbers%2 == 1):
            output.append(i+1)
            flipNumbers += 1

    print(len(output))
    for x in output:
        print(x, end=" ")