# https://www.codechef.com/viewsolution/63834761

n = int(input())
ans, currSum = 0, int(input())

for _ in range(n - 1):
    curr = int(input())
    ans += curr * currSum
    currSum += curr

print(2)
print(ans)
