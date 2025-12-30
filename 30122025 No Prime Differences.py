import math

def eh_primo(numero):
    if numero <= 1:
        return False
    if numero == 2:
        return True

    limite = int(math.sqrt(numero)) + 1
    for i in range(2, limite):
        if numero % i == 0:
            return False
    return True

def NormalRes(n, m):
    for i in range(n):
        for j in range(m):
            print(f"{(j + 1) + i * m}", end=" ")
        print()

def PrimoRes(n, m):
    buffer = []
    res = ""

    for i in range(n//2, n):
        for j in range(m):
            res = res + f"{(j + 1) + i * m} "
        buffer.append(res)
        res = ""
    
    for i in range(n//2):
        for j in range(m):
            res = res + f"{(j + 1) + i * m} "
        buffer.append(res)
        res = "" 
    
    for i in range(n//2):
        print(buffer[i])
        print(buffer[(n//2) + i])

for _ in range(int(input())):

    args = list(map(int, input().split()))

    if not eh_primo(args[1]):
        NormalRes(args[0], args[1])