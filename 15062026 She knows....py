MOD = 1000000007

t = int(input())

for _ in range(t):
    n, m, k = map(int, input().split())

    good = 0
    total_sum = 0

    for _ in range(k):
        x, y, c = map(int, input().split())

        is_corner = (
            (x == 1 and y == 1) or
            (x == 1 and y == m) or
            (x == n and y == 1) or
            (x == n and y == m)
        )

        if is_corner:
            continue

        if x == 1 or y == 1 or x == n or y == m:
            good += 1
            total_sum += c

    if good == 2 * (n + m - 4):
        ans = 0 if total_sum % 2 else pow(2, n * m - k, MOD)
    else:
        ans = pow(2, n * m - k - 1, MOD)

    print(ans)