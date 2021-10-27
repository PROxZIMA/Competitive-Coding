from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0

        track = defaultdict(lambda: -1)
        maxL, a = 0, 0
        for i in range(len(s)):
            trackOfSi = track[s[i]]
            if trackOfSi != -1:
                a = max(a, trackOfSi)
            track[s[i]] = i + 1
            maxL = max(maxL, i - a + 1)

        return maxL
