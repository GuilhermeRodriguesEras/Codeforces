for _ in range(int(input())):

    n = int(input())
    y, r = map(int, input().split())

    maximum = r
    
    if n - r > y // 2:
        maximum += y//2

    else:
        maximum += n - r

    print(maximum)