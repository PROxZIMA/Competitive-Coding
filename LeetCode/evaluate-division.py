from collections import defaultdict, deque

class Solution:
    def getRelation(self, eqMap, x, y):
        if x not in eqMap or y not in eqMap:
            return -1

        variables = deque([(x, 1.0)])
        visited = set()

        while variables:
            var, product = variables.popleft()

            if var == y:
                return product
            visited.add(var)

            for relationTo, value in eqMap[var]:
                if relationTo not in visited:
                    variables.append([relationTo, product*value])

        return -1

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        eqMap = defaultdict(list)
        for i in range(len(values)):
            x, y = equations[i]
            eqMap[x].append([y, values[i]])
            eqMap[y].append([x, 1/values[i]])

        sol = []
        for query in queries:
            x, y = query
            sol.append(self.getRelation(eqMap, x, y))

        return sol
