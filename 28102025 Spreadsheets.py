def whatFormat(line):
    posLetra = -1
    posNumber = -1

    for i in range(len(line)):
        if line[i].isdigit() and posNumber == -1:
            posNumber = i
        if line[i].isupper():
            posLetra = i

    if posNumber < posLetra:
        return False, posLetra
    return True, posLetra

def lettersToRXCY(line, division):
    part1 = line[:division+1]
    part1 = part1[::-1]
    part2 = line[division+1:]

    columnValue = 0
    for i in range(len(part1)):
        columnValue += (26**i) * (ord(part1[i]) - 64)
    
    return f"R{part2}C{columnValue}"

def ConvertCoordenatesLetterToNumbers(n):
    result = ""
    
    while(n != 0):
        if n % 26 != 0:
            result = str(chr((n%26) + 64)) + result
            n = n // 26
        else:
            result = str(chr(90)) + result
            n = (n -1) // 26
    
    return result

def RXCYToLetters(line, division):
    part1 = line[1:division]
    part2 = line[division+1:]

    return f"{ConvertCoordenatesLetterToNumbers(int(part2))}{part1}"

for _ in range(int(input())):
    line = input()
    cond, division = whatFormat(line)

    if(cond):
        print(lettersToRXCY(line, division))
        
    else:
        print(RXCYToLetters(line, division))