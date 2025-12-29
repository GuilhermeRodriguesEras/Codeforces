import random

numeros = [i for i in range(1, 61)]
escolhidos = random.sample(numeros, 6)
escolhidos.sort()

print(escolhidos)