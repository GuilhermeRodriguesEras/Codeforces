def fixEntry(txt : str) -> list[int]:
    """
    For a string entry then have ints separeded by " ", split then and return a list with all of then
    """
    vals = txt.split()
    
    return list(map(int, vals))

n = int(input())

days = fixEntry(input())

restCount = 0

gym, contest = True, True

while(len(days) > 0):
    if(days[0] == 0):
        restCount += 1
        gym, contest = True, True
        days.pop(0)

    elif(days[0] == 1):
        gym = True
        if(contest):
            contest = False
        else:
            restCount+=1
            contest = True
        days.pop(0)

    elif(days[0] == 2):
        contest = True
        if(gym):
            gym = False
        else:
            restCount+=1
            gym = True
        days.pop(0)

    else:
        if(not gym):
            contest = False
            gym = True
            days.pop(0)
        elif(not contest):
            gym = False
            contest = True
            days.pop(0)
        else:
            gymindex, contestindex = 101, 101
            try:
                gymindex = days.index(2)
            except:
                pass
            try:
                contestindex = days.index(1)
            except:
                pass
        
            if(gymindex == 101 and contestindex == 101):
                gym = True
                contest = False
            elif(gymindex < contestindex):
                if(gymindex % 2 == 0):
                    gym, contest = False, True
                else:
                    gym, contest = True, False
            else:
                if(contestindex % 2 == 0):
                    gym, contest = True, False
                else:
                    gym, contest = False, True

            days.pop(0)

print(restCount)