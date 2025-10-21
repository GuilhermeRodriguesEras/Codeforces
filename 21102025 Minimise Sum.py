for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    if arr[0] <= arr[1]:
        print(2*arr[0])

    else:
        print(arr[1] + arr[0])