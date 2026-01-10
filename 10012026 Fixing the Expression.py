for _ in range(int(input())):

    string = input()

    firstNumber = int(string[0])
    lastNumber  = int(string[2])
    operation   = string[1]

    if operation == '>':
        if firstNumber > lastNumber:
            print(string)
        elif firstNumber == lastNumber:
            print(f"{string[0]}={string[2]}")
        else:
            print(f"{string[0]}<{string[2]}")
    
    elif operation == '<':
        if firstNumber < lastNumber:
            print(string)
        elif firstNumber == lastNumber:
            print(f"{string[0]}={string[2]}")
        else:
            print(f"{string[0]}>{string[2]}")
    
    else:
        if firstNumber == lastNumber:
            print(string)
        elif firstNumber > lastNumber:
            print(f"{string[0]}>{string[2]}")
        else:
            print(f"{string[0]}<{string[2]}")