for t in range(int(input())):
    num = int(input())

    result = num // 4
    num = num % 4
    result += num / 2

    print(f"{result:.0f}")
