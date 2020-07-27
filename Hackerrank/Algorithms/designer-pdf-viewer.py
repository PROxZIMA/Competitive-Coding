h = list(map(int, input().split()))
word = input()

l = (h[ord(i)-97] for i in word)

print(max(l)*len(word))
