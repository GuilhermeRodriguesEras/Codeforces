for _ in range(int(input())):
    n, k = map(int, input().split())

    string = input()

    count = 0
    cooldown = 0

    for i in range(n):
        if string[i] == '1':
            cooldown = k + 1
        elif cooldown <= 0:
            count += 1
        
        cooldown -= 1
    
    print(count)