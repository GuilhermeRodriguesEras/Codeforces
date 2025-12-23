for _ in range(int(input())):
    string = input()

    char_list = list(string)
    numbers = list(map(int, char_list))

    left  = sum(numbers[:(int(len(numbers)/2))])
    right = sum(numbers[(int(len(numbers)/2)):])

    if left == right:
        print("YES")
    else:
        print("NO")