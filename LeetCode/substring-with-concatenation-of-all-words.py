from collections import defaultdict

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordsLen = len(words)
        wordLen = len(words[0])
        subStringLen = wordLen * wordsLen

        sol = []
        Map = defaultdict(int)
        for word in words:
            Map[word] += 1

        for i in range(len(s) - subStringLen + 1):
            tempMap = Map.copy()
            flag = True
            for j in range(i, i + subStringLen, wordLen):
                word = s[j:j+wordLen]
                if word in tempMap:
                    tempMap[word] -= 1
                    if tempMap[word] == 0:
                        tempMap.pop(word, None)
                else:
                    flag = False
                    break
            if flag and (not bool(tempMap)):
                sol.append(i)

        return sol
