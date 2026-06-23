for _ in range(int(input())):

    n = int(input())
    s = input()

    a, b = s.count('('), s.count(')')

    if a == b:
        print("YES")
    else:
        print("NO")