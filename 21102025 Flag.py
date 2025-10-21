vals=list(map(int,input().split()))

flags =[]
for i in range(vals[0]):
    flags.append(input())

cond = True

for i in range(vals[0] - 1):
    if flags[i].count(flags[i][0]) != vals[1] or flags[i][0] == flags[i+1][0]:
        cond = False
        break

if flags[-1].count(flags[-1][0]) != vals[1]:
    cond = False

if cond:
    print("YES")
else:
    print("NO")