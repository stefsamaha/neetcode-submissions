class MinStack:

    def __init__(self):
        self.stack = [] # stores all pushed values
        self.minStack = [] # stores minimum so far at each level 
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)


    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.minStack[-1]
