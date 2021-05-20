# https://www.codechef.com/viewsolution/43538437

from math import inf

for _ in range(int(input())):
    n, egg, bar, a, b, c = map(int, input().split())

    refer = {}
    costs = {'a': a, 'b': b, 'c': c}
    costs = dict(sorted(costs.items(), key=lambda i: i[1]))
    mini = inf

    if egg < n and bar < n:
        print(-1)
        continue
    elif egg == bar == n:
        print(c * n)
        continue
    else:
        for cake in range(min(egg, bar, n), -1, -1):
            refer['c'] = cake
            refer['a'] = (egg - cake) // 2
            refer['b'] = (bar - cake) // 3

            currCost = 0
            n_ = n
            if sum(refer.values()) >= n:
                for cost, val in costs.items():
                    if n_ > 0:
                        nrem = n_
                        n_ -= min(n_, refer[cost])
                        if n_ == 0:
                            currCost += nrem * val
                            break
                        currCost += refer[cost] * val

                mini = min(mini, currCost)

    print(-1 if mini == inf else mini)