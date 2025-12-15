for t in range(int(input())):
    args = list(map(int, input().split()))

    if args[1] % 2 == 1:
        arr = [args[0] for _ in range(args[0]-1)]
        arr.append(args[0]-1)

    else:
        arr = [args[0]-1 for _ in range(args[0]-2)]
        arr.append(args[0])
        arr.append(args[0]-1)

    for x in range(len(arr)-1):
        print(arr[x], end=" ")

    print(arr[-1])