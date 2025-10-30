vals = input().split()
n, m, presidentColor = int(vals[0]), int(vals[1]), vals[2]
M = []
Condition = [[0 for _ in range(m)] for _ in range(n)]
posFisrtPresidentPos = (0,0)
find = False

def seeAdjacents(Matrix, C, President, i, j, nessesaryDict, n, m):
    if C[i][j] == 1:
        return i, j, nessesaryDict, C

    C[i][j] = 1

    if Matrix[i][j] != '.':
        nessesaryDict[Matrix[i][j]] = 1
    if Matrix[i][j] == President:
        if i > 0:
            _, _, nessesaryDict, C = seeAdjacents(Matrix, C, President, i-1, j, nessesaryDict, n, m)
        if i < n:
            _, _, nessesaryDict, C = seeAdjacents(Matrix, C, President, i+1, j, nessesaryDict, n, m)
        if j > 0:
            _, _, nessesaryDict, C = seeAdjacents(Matrix, C, President, i, j-1, nessesaryDict, n, m)
        if j < m:
            _, _, nessesaryDict, C = seeAdjacents(Matrix, C, President, i, j+1, nessesaryDict, n, m)

    return i, j, nessesaryDict, C

for i in range(n):
    string = input()
    M.append(string)
    
    if not find:
        see = string.find(presidentColor)
        if see != -1:
            posFisrtPresidentPos = (i, see)
            find = True

if not find:
    print(0)
else:
    _, _, colors, _ = seeAdjacents(M, Condition, presidentColor, posFisrtPresidentPos[0], posFisrtPresidentPos[1], {}, n-1, m-1)
    print(len(colors)-1)