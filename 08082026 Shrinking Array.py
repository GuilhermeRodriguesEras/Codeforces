for _ in range(int(input())):
    s = int(input())
    arr = list(map(int, input().split()))

    sorted = True
    beautiful = False

    for i in range(s-1):
        if abs(arr[i] - arr[i+1]) <= 1:
            beautiful = True
            break
        
        if arr[i] > arr[i+1]:
            sorted = False
    
    if beautiful:
        print(0)
    elif not sorted and s > 2:
        print(1)
    else:
        print(-1)