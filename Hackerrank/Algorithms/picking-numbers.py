n = int(input())
a = list(map(int, input().split()))
maxi = max(a)
l = [0]*(maxi+1)

for i in a:
    l[i] += 1
count = (l[i]+l[i+1] for i in range(maxi))

print(max(count))
