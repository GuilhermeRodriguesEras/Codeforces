n = int(input())

title = list(input())

i = 0
l, r = 0, len(title) - 1
letter = 65
arr = [0] * n
possible = True
futureDefination = 0

while l <= r:
    l += 1
    r -= 1
    
    if title[l-1] == '?' and title[r+1] == '?':
        futureDefination += 1
        continue

    if title[l-1] == '?':
        title[l-1] = title[r+1]

    elif title[r+1] == '?':
        title[r+1] = title[l-1]
    
    elif title[l-1] != title[r+1]:
        possible = False
        break

    arr[ord(title[l-1])- 97] = 1

if possible:
    missingLetter = []
    for i in range(n):
        if arr[i] == 0:
            missingLetter.append(chr(i+97))
            
    repertorio = len(missingLetter)
    l, r = 0, len(title) - 1
    while l <= r:
        l += 1
        r -= 1

        if title[l-1] == "?":
            if repertorio > futureDefination:
                possible = False
                break
            elif repertorio == futureDefination:
                title[l-1] = missingLetter.pop(0)
                title[r+1] = title[l-1]
            else:
                title[l-1], title[r+1] = 'a', 'a'
                futureDefination -= 1
    
    if possible and len(missingLetter) == 0:
        print(''.join(title))
    else:
        print("IMPOSSIBLE")
else:
    print("IMPOSSIBLE")