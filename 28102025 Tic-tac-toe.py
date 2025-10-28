line1 = input()
line2 = input()
line3 = input()

allLines = line1 + line2 + line3
countX = allLines.count('X')
count0 = allLines.count('0')
countPoint = allLines.count('.')

def playerWin(player, lines):
    if player == 1:
        symbol = 'X'
    else:
        symbol = '0'
    
    for i in range(3):
        if lines[i*3] == symbol and lines[i*3 + 1] == symbol and lines[i*3 + 2] == symbol:
            return True
        if lines[i] == symbol and lines[i + 3] == symbol and lines[i + 6] == symbol:
            return True
    if lines[0] == symbol and lines[4] == symbol and lines[8] == symbol:
        return True
    
    if lines[2] == symbol and lines[4] == symbol and lines[6] == symbol:
        return True
    return False

if countX - count0 != 1 and countX - count0 != 0:
    print("illegal")
else:
    Xwin = playerWin(1, allLines)
    Owin = playerWin(0, allLines)

    if(Xwin and Owin):
        print("illegal")
    elif(Xwin and countX == count0):
        print("illegal")
    elif(Xwin):
        print("the first player won")
    elif(Owin and count0 < countX):
        print("illegal")
    elif(Owin):
        print("the second player won")
    elif(countPoint == 0):
        print("draw")
    elif(countX > count0):
        print("second")
    else:
        print("first")