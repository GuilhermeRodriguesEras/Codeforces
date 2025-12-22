for _ in range(int(input())):

    num = int(input())

    if num < 2020:
        print("NO")
    else:
        div = num // 2020
        res = num % 2020

        if res <= div:
            print("YES")
        else:
            print("NO")