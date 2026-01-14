arr = list(map(int, input().split()))

arr.sort()

if(arr[2] - arr[0] >= 10):
    print("check again")
else:
    print(f"final {arr[1]}")