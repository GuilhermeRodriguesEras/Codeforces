InicalPos = list(map(ord, list(input())))
FinalPosList = list(map(ord, list(input())))

InicalPos[0] -= 97
FinalPosList[0] -= 97
InicalPos[1] -= 49
FinalPosList[1] -= 49

dist = max(abs(FinalPosList[0] - InicalPos[0]), abs(FinalPosList[1] - InicalPos[1]))
print(dist)

for _ in range(dist):
    if FinalPosList[0] > InicalPos[0]:
        InicalPos[0] += 1
        step_x = 'R'
    elif FinalPosList[0] < InicalPos[0]:
        InicalPos[0] -= 1
        step_x = 'L'
    else:
        step_x = ''

    if FinalPosList[1] > InicalPos[1]:
        InicalPos[1] += 1
        step_y = 'U'
    elif FinalPosList[1] < InicalPos[1]:
        InicalPos[1] -= 1
        step_y = 'D'
    else:
        step_y = ''

    print(step_x + step_y)