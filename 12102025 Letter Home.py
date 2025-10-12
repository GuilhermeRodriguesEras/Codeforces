for i in range(int(input())):

    vals=list(map(int,input().split()))
    x=list(map(int,input().split()))

    t1 = abs(vals[1] - x[0]) + abs(x[0] - x[-1])
    t2 = abs(vals[1] - x[-1]) + abs(x[0] - x[-1])

    print(min(t1,t2))
