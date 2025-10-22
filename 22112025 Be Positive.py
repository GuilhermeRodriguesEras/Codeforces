for i in range(int(input())):
    size = int(input())
    arr = list(map(int, input().split()))

    numberOfMinus1 = arr.count(-1)
    sum = arr.count(0)    

    if numberOfMinus1 % 2 == 1:
        sum += 2
    
    print(sum)