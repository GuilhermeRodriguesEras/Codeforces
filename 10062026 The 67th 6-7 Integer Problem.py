for _ in range(int(input())):
    
    arr = list(map(int, input().split()))

    arr.sort()

    soma = sum(arr)*(-1) + (arr[-1]*2)

    print(soma)