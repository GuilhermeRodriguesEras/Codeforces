for _ in range(int(input())):

    args = list(map(int, input().split()))
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    possibilities = 0

    if args[2] < 2:
        print(0)
        continue

    grauBoys  = [0 for _ in range(args[0])]
    grauGirls = [0 for _ in range(args[1])]

    for i in range(args[0]):
        grauBoys[i] = count = arr1.count(i + 1)
    
    for i in range(args[1]):
        grauGirls[i] = count = arr2.count(i + 1)
    
    for i in range(len(arr1)):
        possibilities += args[2] - grauBoys[arr1[i] - 1] - grauGirls[arr2[i] - 1] + 1
    
    print(possibilities // 2)