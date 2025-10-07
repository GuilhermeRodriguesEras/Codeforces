def fixEntry(txt : str) -> list[int]:
    """
    For a string entry then have ints separeded by " ", split then and return a list with all of then
    """
    vals = txt.split()

    return list(map(int, vals))

tests = int(input())

for i in range(tests):
    vals = fixEntry(input())
    moves = input()

    top, maybeTop, botton, maybeBotton = 0, 0, vals[0] -1, vals[0] -1

    for move in moves:
        if move == '0':
            top+=1
            maybeTop+=1
        elif move == '1':
            botton-=1
            maybeBotton-=1
        else:
            maybeTop+=1
            maybeBotton-=1
    
    for j in range(vals[0]):
        if top > maybeBotton:
            print("-",end="")
        elif j < top:
            print("-",end="")
        elif j > botton:
            print("-",end="")
        elif top <= j and j < maybeTop:
            print("?",end="")
        elif maybeTop <= j and j <= maybeBotton:
            print("+",end="")
        else:
            print("?",end="")
    print()