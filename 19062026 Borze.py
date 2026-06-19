string = input()
out = ""

aux = 0
while aux < len(string):
    if string[aux] == '.':
        out = out + "0"
        aux += 1
    elif string[aux+1] == '.':
        out = out + "1"
        aux += 2
    else:
        out = out + "2"
        aux += 2

print(out)