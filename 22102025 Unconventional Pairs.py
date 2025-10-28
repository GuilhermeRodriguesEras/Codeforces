for i in range(int(input())):
    size = int(input())
    arr = list(map(int, input().split()))

    arr.sort()

    bigger = 0
    for j in range(0, len(arr), 2):
        if abs(arr[j] - arr[j+1]) > bigger:
            bigger = abs(arr[j] - arr[j+1])
        
    print(bigger)