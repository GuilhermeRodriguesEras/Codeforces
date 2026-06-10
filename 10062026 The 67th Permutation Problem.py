for _ in range(int(input())):

    n = int(input())

    start = 1
    end = n*3

    for _ in range(n):
        print(f"{start} {end-1} {end}", end=" ")
        start += 1
        end -= 2

