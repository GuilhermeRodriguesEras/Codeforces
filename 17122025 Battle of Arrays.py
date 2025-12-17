import heapq

for t in range(int(input())):
    agrs = list(map(int, input().split()))
    
    arrA = [-x for x in map(int, input().split())]
    arrB = [-x for x in map(int, input().split())]
    
    heapq.heapify(arrA)
    heapq.heapify(arrB)

    turn = 1

    while len(arrA) > 0 and len(arrB) > 0:

        Alice_max = -heapq.heappop(arrA)
        Bob_max = -heapq.heappop(arrB)

        if turn == 1:
            if Alice_max >= Bob_max:
                heapq.heappush(arrA, -Alice_max)
            else:
                heapq.heappush(arrB, -(Bob_max - Alice_max))
                heapq.heappush(arrA, -Alice_max)
        
            turn = 0

        else:
            if Bob_max >= Alice_max:
                heapq.heappush(arrB, -Bob_max)
            else:
                heapq.heappush(arrA, -(Alice_max - Bob_max))
                heapq.heappush(arrB, -Bob_max)
        
            turn = 1
        
    if len(arrA) == 0:
        print("Bob")
    else:
        print("Alice")