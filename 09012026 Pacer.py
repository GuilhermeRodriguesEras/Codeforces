for _ in range(int(input())):
    n, m = map(int, input().split())
    Matrix = [list(map(int, input().split())) for _ in range(n)]

    count = 0
    actualSide = 0
    actualMinute = 0

    for i in range(n):
        if (Matrix[i][0] - actualMinute) % 2 == 0 and Matrix[i][1] == actualSide:
            count += Matrix[i][0] - actualMinute
        elif (Matrix[i][0] - actualMinute) % 2 == 0 and Matrix[i][1] != actualSide:
            count += Matrix[i][0] - actualMinute - 1
        elif (Matrix[i][0] - actualMinute) % 2 == 1 and Matrix[i][1] == actualSide:
            count += Matrix[i][0] - actualMinute - 1
        else:
            count += Matrix[i][0] - actualMinute

        actualMinute = Matrix[i][0]
        actualSide = Matrix[i][1]

    count += m - actualMinute
    print(count)