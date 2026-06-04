for _ in range(int(input())):
    size = int(input())
    arr = list(map(int, input().split()))

    count = 1 if arr[-1] > 0 else 0

    for i in range(size-2, -1, -1):
        if arr[i+1] >0:
            arr[i] += arr[i+1]
        
        if arr[i] > 0:
            count += 1

    print(count)