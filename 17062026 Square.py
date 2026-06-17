for _ in range(int(input())):

    arr = list(map(int, input().split()))

    if arr[0] == arr[1] and arr[1] == arr[2] and arr[2] == arr[3]:
        print("YES")
    else:
        print("NO")