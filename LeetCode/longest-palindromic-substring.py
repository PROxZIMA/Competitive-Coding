class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ''
        for i in range(len(s)):
            result = max(result, self.checkPalindrome(s, i, 'even'), self.checkPalindrome(s, i, 'odd'), key = len)
        return result

    def checkPalindrome(self, s, left, state):
        right = left if state == 'odd' else left + 1

        while (0 <= left)       and \
              (right < len(s)) and \
              s[left] == s[right]:
            left -= 1
            right += 1

        return s[left + 1 : right]
