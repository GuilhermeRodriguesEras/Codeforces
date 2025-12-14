for t in range(int(input())):

    arr     = list(map(int,input().split()))
    numbers = list(map(int,input().split()))

    firstOne, lastOne = None, None

    for x in enumerate(numbers):
        if(x[1] == 1):
            lastOne = x[0]
            if(firstOne == None):
                firstOne = x[0]

    if firstOne == None:
        print("YES")
    
    else:
        difference = lastOne - firstOne + 1

        if difference <= arr[1]:
            print("YES")
        else:
            print("NO")