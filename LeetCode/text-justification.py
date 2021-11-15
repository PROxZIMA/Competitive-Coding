class Solution:
    def split(self, spaces: int, sets: int) -> Iterable[int]:
        if (spaces % sets == 0):
            rem = spaces // sets
            return (rem for i in range(sets))
        else:
            rem, bigRem = sets - (spaces % sets), spaces//sets
            return (bigRem + 1 if (i >= rem) else bigRem for i in range(sets-1,-1,-1))

    def merge(self, words: List[str], maxWidth: int, last: int = None) -> str:
        if last:
            s = ' '.join(words)
            return s + ' ' * (maxWidth - len(s))
        lenw, lenEachw = len(words), sum(len(i) for i in words)
        if lenw == 1:
            return words[0] + ' ' * (maxWidth - lenEachw)
        spaceSet = self.split(maxWidth - lenEachw, lenw - 1)
        return ''.join((word + ' ' * spaceLen for word, spaceLen in zip(words, spaceSet))) + words[-1]

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lenw, i, sol = len(words), 0, []
        while i < lenw:
            maxLen, j = maxWidth, i
            while maxLen >= -1 and j < lenw:
                maxLen -= (len(words[j]) + 1)
                j += 1
            if j >= lenw and maxLen >= -1:
                sol.append(self.merge(words[i:], maxWidth, 'last'))
                break
            else:
                sol.append(self.merge(words[i : j-1], maxWidth))
            i = j-1
        return sol
