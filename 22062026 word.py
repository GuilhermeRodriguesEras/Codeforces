word = input()

lowerCount = 0
upCount = 0

for x in word:
    if 65 <= ord(x) and ord(x) <= 90:
        upCount += 1
    else:
        lowerCount += 1

if lowerCount >= upCount:
    print(word.lower())
else:
    print(word.upper())