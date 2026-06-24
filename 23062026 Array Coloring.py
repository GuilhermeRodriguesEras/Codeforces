for _ in range(int(input())):

    s = int(input())
    arr = list(map(int, input().split()))
    cond = True

    for i in range(s-1):
        if arr[i] % 2 == 1 and arr[i+1] % 2 == 1:
            cond = False
            break
        elif arr[i] % 2 == 0 and arr[i+1] % 2 == 0:
            cond = False
            break
    
    if cond:
        print("YES")
    else:
        print("NO")