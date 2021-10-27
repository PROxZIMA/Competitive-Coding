import math

class MinStack:

    def __init__(self):
        self.min = math.inf
        self.stack = []

    def push(self, val: int) -> None:
        if self.min >= val:
            self.stack.append(self.min)
            self.min = val

        self.stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.min:
            self.stack.pop(-1)
            self.min = self.stack[-1]

        return self.stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
