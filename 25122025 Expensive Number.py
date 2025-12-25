for _ in range(int(input())):

    string = input()

    char_list = list(string)
    numbers = list(map(int, char_list))

    res = 0

    while True:
        if numbers[-1] == 0:
            numbers.pop()
            res += 1
        else:
            break

    res += len(numbers) - numbers.count(0)
    print(res - 1)