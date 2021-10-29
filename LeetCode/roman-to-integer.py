class Solution:
    def romanToInt(self, s: str) -> int:
        data = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        total = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and \
                (
                    (s[i] == 'I' and s[i+1] in {'V', 'X'}) or \
                    (s[i] == 'X' and s[i+1] in {'L', 'C'}) or \
                    (s[i] == 'C' and s[i+1] in {'D', 'M'})
                ):
                total += data[s[i+1]] - data[s[i]]
                i += 2
                continue
            total += data[s[i]]
            i += 1
        return total
