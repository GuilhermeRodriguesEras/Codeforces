for _ in range(int(input())):

    code = input()

    currentNumber = 1
    time = 0

    for x in code:
        num = ord(x) - 48
        
        if(num == 0):
            num += 10
        
        time += abs(num - currentNumber) + 1
        currentNumber = num
    
    print(time)

