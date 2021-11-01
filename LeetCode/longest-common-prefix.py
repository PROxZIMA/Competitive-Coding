class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        
        for s in strs:
            i = 0
            while i < min(len(s), len(prefix)):
                if s[i] != prefix[i]:
                    break
                i += 1
            prefix = s[:i]
            
        return prefix
