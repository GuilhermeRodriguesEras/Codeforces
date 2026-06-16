for _ in range(int(input())):

    a, b, c = map(int, input().split())

    aux = b - a
    a, c = a + aux, c - aux

    if c == a:
        print("YES")

    elif c < a or (c-a)%3 != 0:
        print("NO")
    else:
        print("YES")