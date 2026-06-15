for _ in range(int(input())):

    k = int(input())
    arr = list(map(int,input().split()))

    arr.sort(reverse=True)
    cond = True

    for i in range(k-2):
        if arr[i] % arr[i+1] != arr[i+2]:
            cond = False
            print("-1")
            break

    if cond:
        print(f"{arr[0]} {arr[1]}")