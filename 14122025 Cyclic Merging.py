for t in range(int(input())):
    size = int(input())
    arr  = list(map(int, input().split()))

    aux = [max(arr[i], arr[i+1]) for i in range(len(arr)-1)]
    aux.append(max(arr[0],arr[-1]))

    maxVal = max(aux)
    index = aux.index(maxVal)
    aux.pop(index)

    print(sum(aux))