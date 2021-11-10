class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip(' ')
        s = s.rstrip('.')
        lens = len(s)

        if (not s) or s[0].isalpha() or (lens == 1 and not s[0].isdecimal()):
            return 0

        string, i = '', 0
        if s[0] in {'-', '+'}:
            i = 1
            string += s[0]

        while i < lens:
            char = s[i]
            if char.isdecimal():
                string += char
            else:
                break
            i += 1

        if (not string) or (len(string) == 1 and not string[0].isdecimal()):
            return 0

        sol, mini, maxi = int(string), -2147483648, 2147483647

        if sol < mini:
            return mini
        elif sol > maxi:
            return maxi
        else:
            return sol
