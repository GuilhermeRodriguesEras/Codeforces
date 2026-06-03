for _ in range(int(input())):
    size = int(input())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    for i in range(size):
        if a[i] > b[i]:
            a[i], b[i] = b[i], a[i]

    print(f"{max(a)+sum(b):.0f}")