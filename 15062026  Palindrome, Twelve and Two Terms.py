for _ in range(int(input())):

    n = int(input())

    if n < 12:
        if n == 10:
            print("-1")
        else:
            print(f"{n} {0}")
        continue

    b = (n // 12) * 12
    a = n - b

    if a != 10:
        print(f"{a} {b}")

    else:
        print(f"{a+12} {b-12}")
