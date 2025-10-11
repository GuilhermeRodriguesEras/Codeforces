s = input()

sites = []

for i in range(int(input())):
    readEntry = input()

    pos = readEntry.find(s)
    if(pos == 0):
        sites.append(readEntry)

if(len(sites) == 0):
    print(s)
else:
    sites.sort()
    print(sites[0])