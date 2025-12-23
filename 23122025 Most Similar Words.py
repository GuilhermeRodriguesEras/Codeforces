def difference(word1, word2):
    sum = 0
    for i in range(len(word1)):
        sum += abs(ord(word1[i]) - ord(word2[i]))

    return sum

for _ in range(int(input())):
    args = list(map(int, input().split()))

    words = []
    for _ in range(args[0]):
        words.append(input())
    
    min_diff = 10**9 + 1

    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            diff = difference(words[i], words[j])
            if diff < min_diff:
                min_diff = diff
    
    print(min_diff)
