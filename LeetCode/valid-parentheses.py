class Solution:
    def __init__(self):
        self.data = {'()', '[]', '{}'}

    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if stack and self.opposite(stack[-1], char):
                stack.pop()
            else:
                stack.append(char)
        return not stack

    def opposite(self, recent, char):
        return (recent+char in self.data)
