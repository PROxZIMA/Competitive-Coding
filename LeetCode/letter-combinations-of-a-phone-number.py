class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        key_pad = {
            '2': 'abc' ,
            '3': 'def' ,
            '4': 'ghi' ,
            '5': 'jkl' ,
            '6': 'mno' ,
            '7': 'pqrs',
            '8': 'tuv' ,
            '9': 'wxyz'
        }

        result = ['']
        for i in digits:
            result = [x+y for x in result for y in key_pad[i]]

        return [] if result == [''] else result
