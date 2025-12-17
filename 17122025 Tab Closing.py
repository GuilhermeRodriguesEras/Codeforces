for t in range(int(input())):
    args = list(map(int, input().split()))
    a, b, n = args[0], args[1], args[2]

    moves = 0

    if n*b <= a or a == b:
        moves = 1
    else:
        moves = 2
    print(moves)