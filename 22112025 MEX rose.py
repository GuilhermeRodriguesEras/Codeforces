for i in range(int(input())):
    vals = list(map(int, input().split()))
    k = vals[1]
    arr = list(map(int, input().split()))

    arr.append(k)
    arr.sort()
    
    MEX = 0
    aux = 0

    occorence = arr.index(k)
    if occorence >= k:
        MEX = arr.count(k) - 1
    else:
        aux = k - occorence
        if (arr.count(k) - 1) > aux:
            MEX = arr.count(k) - 1
        else:
            MEX = aux
    
    print(MEX)
