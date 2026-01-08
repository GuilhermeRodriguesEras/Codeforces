for _ in range(int(input())):

    a, x, y = map(int, input().split()) 

    x, y = min(x, y), max(x, y)

    if x <= a and a <= y:
        aliceMinDistance = min((abs(y-a), abs(x-a)))

        middlePoint = (x + y) // 2

        bobMaxDistance = max(abs(middlePoint - x), abs(middlePoint - y))

        if aliceMinDistance <= bobMaxDistance:
            print("NO")
        else:
            print("YES")
        
    else:
        print("YES")