for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort()

    bigger = arr[-1]

    somaDosTermos = sum([((-1)**(i+1))*arr[i] for i in range(len(arr) - 1)])

    x = bigger - somaDosTermos

    result = [bigger] + [x] + arr[:-1]

    for x in range(len(result)-1):
        print(result[x], end=" ")

    print(result[-1])