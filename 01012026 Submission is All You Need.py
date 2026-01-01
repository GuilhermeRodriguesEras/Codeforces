for _ in range(int(input())):
    s = int(input())
    arr = list(map(int, input().split()))

    countZero = 0
    
    try:
        countZero = arr.count(0)
    except:
        pass

    print(sum(arr)+ countZero)
