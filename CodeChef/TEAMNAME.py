# https://www.codechef.com/viewsolution/42711622

from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    funnyWords = input().split()

    words = defaultdict(set)
    for word in funnyWords:
        words[word[0]].add(word[1:])

    prefix = list(words.keys())

    total = 0
    for i in prefix:
        for j in prefix[prefix.index(i):]:
            val1 = len(words[j] - words[i])
            val2 = len(words[i] - words[j])
            total += (val1 * val2 * 2)

    print(total)