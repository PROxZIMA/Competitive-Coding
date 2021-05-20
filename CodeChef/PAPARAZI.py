# https://www.codechef.com/viewsolution/43653449

for _ in range(int(input())):
    n = int(input())
    height = tuple(enumerate(map(int, input().split())))

    if n == 2:
        print('1')
        continue

    currMax = list(height[:2])
    maxDist, count = 1, 2

    for i in range(2, n):
        while (count >= 2):
            slope1 = (currMax[-2][1] - currMax[-1][1]) / (currMax[-2][0] - currMax[-1][0])
            slope2 = (height[i][1] - currMax[-1][1]) / (height[i][0] - currMax[-1][0])

            if slope1 <= slope2:
                currMax.pop()
                count -= 1
            else:
                break

        currMax.append(height[i])
        count += 1

        maxDist = max(maxDist, currMax[-1][0] - currMax[-2][0])

    print(maxDist)