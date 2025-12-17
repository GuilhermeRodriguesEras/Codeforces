for t in range(int(input())):

    s = int(input())
    string = input()

    count = string.count(string[-1])

    print(s - count)