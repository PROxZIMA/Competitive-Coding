# https://www.codechef.com/viewsolution/63814402

for _ in range(int(input())):
    m, x, y = map(int, input().split())
    copHouse = list(map(int, input().split()))

    houses = set(range(1, 101))
    dist = x * y

    for house in copHouse:
        left = max(house - dist, 1)
        right = min(house + dist, 100)
        houses -= set(range(left, right + 1))

    print(len(houses))
