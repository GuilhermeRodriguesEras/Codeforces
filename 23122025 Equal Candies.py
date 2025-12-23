for _ in range(int(input())):

    s = int(input())
    arr = list(map(int, input().split()))

    total = 0
    min = 10**9 + 1

    for i in range(s):
        total += arr[i]
        if arr[i] < min:
            min = arr[i]

    print(total - s * min)