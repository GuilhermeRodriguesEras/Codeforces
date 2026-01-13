s = int(input())
arr = list(map(int, input().split()))

num_max = max(arr)
count = 0 
for num in arr:
    count += num_max - num

print(count)