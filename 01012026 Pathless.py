def printList(arr):
    for i in arr:
        print(i, end=" ")
    print()


for _ in range(int(input())):

    n, s = map(int, input().split())
    arr = list(map(int, input().split()))

    soma = sum(arr)

    if(soma > s):
        printList(arr)
        continue

    if(soma == s):
        print(-1)
        continue

    if s - soma != 1:
        print(-1)
        continue

    count0 = arr.count(0)
    count1 = arr.count(1)
    count2 = arr.count(2)

    printList([0]*count0 + [2]*count2 + [1]*count1)
    