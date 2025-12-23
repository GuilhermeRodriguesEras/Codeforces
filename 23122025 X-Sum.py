for _ in range(int(input())):
    args = list(map(int, input().split()))

    matrix = []

    for i in range(args[0]):
        matrix.append(list(map(int, input().split())))

    verticalMaxWhite   = [0, None]
    verticalMaxBlack   = [0, None]

    horizontalMaxWhite = [0, None]
    horizontalMaxBlack = [0, None]
    
    for j in range(args[0]):
        for i in range(args[1]):
            somaTotal = 0
            aux = 0
            while True:
                somaTotal += matrix[j+aux][i+aux]
                aux += 1
                
                if j+aux == args[0] or aux+i == args[1]:
                    break
            
            if (i+j) % 2 == 0 and somaTotal > verticalMaxWhite[0]:
                verticalMaxWhite[0] = somaTotal
                verticalMaxWhite[1] = (j, i)
            elif (i+j) % 2 == 1 and somaTotal > verticalMaxBlack[0]:
                verticalMaxBlack[0] = somaTotal
                verticalMaxBlack[1] = (j, i)


    for j in range(args[0]):
        for i in range(args[1]-1, -1, -1):
            somaTotal = 0
            aux = 0
            while True:
                somaTotal += matrix[j+aux][i-aux]
                aux += 1
                
                if j+aux == args[0] or i-aux == -1:
                    break
            
            if (i+j) % 2 == 0 and somaTotal > horizontalMaxWhite[0]:
                horizontalMaxWhite[0] = somaTotal
                horizontalMaxWhite[1] = (j, i)
            elif (i+j) % 2 == 1 and somaTotal > horizontalMaxBlack[0]:
                horizontalMaxBlack[0] = somaTotal
                horizontalMaxBlack[1] = (j, i)

    print(verticalMaxWhite)
    print(verticalMaxBlack)
    print(horizontalMaxWhite)
    print(horizontalMaxBlack)

