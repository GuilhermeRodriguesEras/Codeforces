for t in range(int(input())):
    args = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    if sum(arr) / len(arr) == args[1]:
        print("YES")
    else:
        print("NO")