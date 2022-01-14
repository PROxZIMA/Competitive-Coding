from collections import deque, defaultdict

class Solution:
    def ladderLength(self, B: str, E: str, wordList: List[str]) -> int:
        d = self.construct_dict(set(wordList))
        queue, visited = deque([(B, 1)]), set()
        while queue:
            word, path = queue.popleft()
            if word not in visited:
                visited.add(word)
                if word == E:
                    return path
                for i in range(len(word)):
                    s = word[:i] + '*' + word[i+1:]
                    for neighbor in d[s]:
                        if neighbor not in visited:
                            queue.append((neighbor, path + 1))
        return 0
        
    def construct_dict(self, wordList: set) -> defaultdict:
        d = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                s = word[:i] + '*' + word[i+1:]
                d[s].append(word)
        return d
