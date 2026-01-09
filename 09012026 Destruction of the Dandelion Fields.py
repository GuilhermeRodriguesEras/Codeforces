for _ in range(int(input())):

    s = int(input())
    arr = list(map(int, input().split()))

    evenNumbers = [num for num in arr if num % 2 == 0]
    oddNumbers = [num for num in arr if num % 2 != 0]
    oddNumbers.sort()

    if len(oddNumbers) == 0:
        print(0)
        continue

    totalDandelions = sum(evenNumbers) + sum(oddNumbers[len(oddNumbers)//2:])
    
    print(totalDandelions)