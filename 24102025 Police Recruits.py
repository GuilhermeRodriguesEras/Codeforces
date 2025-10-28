n = int(input())
 
arr = list(map(int, input().split()))
 
crimesUntreated = 0
notBusyOfficer = 0
 
for i in range(len(arr)):
    if arr[i] > 0:
        notBusyOfficer += arr[i]
    
    else:
        if notBusyOfficer != 0:
            notBusyOfficer -= 1
        else:
            crimesUntreated += 1
 
print(crimesUntreated)