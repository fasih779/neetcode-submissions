class MinStack:

    def __init__(self):
        self.stack1 = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack1.append(val)
        if not self.minStack:
            self.minStack.append(val)
        elif val < self.minStack[-1]:
            self.minStack.append(val)
        else:
            self.minStack.append(self.minStack[-1])

    def pop(self) -> None:
        self.stack1.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack1[-1]

    def getMin(self) -> int:
        return self.minStack[-1]