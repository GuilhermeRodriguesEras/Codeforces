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

for _ in range(int(input())):
    args = list(map(int, input().split()))

    if args[0] == 1 and args[1] == 2:
        print("YES")
    elif args[1] != 1:
        print("NO")
    elif eh_primo(args[0]):
        print("YES")
    else:
        print("NO")

