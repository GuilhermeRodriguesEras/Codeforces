for t in range(int(input())):

    n = int(input())

    arr = list(range(1,n+1, 2)) + list(range(2,n+1, 2))[::-1]
    
    for x in range(len(arr)-1):
        print(arr[x], end=" ")

    print(arr[-1])