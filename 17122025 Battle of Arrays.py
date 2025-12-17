for t in range(int(input())):

    agrs = list(map(int, input().split()))
    arrA = list(map(int, input().split()))
    arrB = list(map(int, input().split()))

    turn = 1

    while len(arrA) > 0 and len(arrB) > 0:
        Alice_max = max(arrA)
        Bob_max = max(arrB)

        if turn == 1:
            if Alice_max >= Bob_max:
                arrB.remove(Bob_max)
            else:
                arrB.remove(Bob_max)
                arrB.append(Bob_max - Alice_max)
        
            turn = 0

        else:
            if Bob_max >= Alice_max:
                arrA.remove(Alice_max)
            else:
                arrA.remove(Alice_max)
                arrA.append(Alice_max - Bob_max)
        
            turn = 1
        
    if len(arrA) == 0:
        print("Bob")
    else:
        print("Alice")