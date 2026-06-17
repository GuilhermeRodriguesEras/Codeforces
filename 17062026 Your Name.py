for _ in range(int(input())):

    n = int(input())

    words = input().split()

    arr1 = [0]*26
    arr2 = [0]*26

    for letter in words[0]:
        arr1[ord(letter)-97] += 1
    for letter in words[1]:
        arr2[ord(letter)-97] += 1

    cond = True
    for i in range(26):
        if arr1[i] != arr2[i]:
            cond = False
            break

    if cond:
        print("YES")
    else:
        print("NO")