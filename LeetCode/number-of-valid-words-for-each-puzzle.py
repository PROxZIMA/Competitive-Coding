from collections import defaultdict

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        def convertToBit(s: str) -> str:
            bits = 0
            for i in set(s):
                bits |= 1 << (ord(i) - 97)
            return bits

        bitFreq = defaultdict(int)
        for word in words:
            bitFreq[convertToBit(word)] += 1

        sol = [0] * len(puzzles)
        for i, puzzle in enumerate(puzzles):
            firstBit = ord(puzzle[0]) - 97
            puzzleBit = convertToBit(puzzle)
            tempBit = puzzleBit

            while tempBit:
                if (tempBit >> firstBit) & 1:
                    sol[i] += bitFreq[tempBit]
                tempBit = (tempBit - 1) & puzzleBit

        return sol
