n, m, l, x, y = map(int, input().split())
#n -> number of buses
#m -> number of people
#l -> length of the route
#x -> speed of the bus
#y -> speed of the people

busTimePerMeter = 1/x
peopleTimePerMeter = 1/y

buses = []
for _ in range(n):
    a, b = map(int, input().split())
    buses.append((a, b))

buses.sort()

peoples = []
for _ in range(m):
    p = int(input())
    peoples.append(p)

for p in peoples:

    minValue = (l-p) * peopleTimePerMeter

    for b in buses:
        if b[1] <= p:
            continue
        elif b[0] > p:
            break
        else:
            waitingTime = (p-b[0]) * busTimePerMeter
            possibleTime = waitingTime + (b[1]- p)*busTimePerMeter  + (l - b[1]) * peopleTimePerMeter
            if possibleTime < minValue:
                minValue = possibleTime

    print(minValue)