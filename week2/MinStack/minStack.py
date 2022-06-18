class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        #add val to normal stack
        self.stack.append(val)
        #comapre if current val < val on top of the minStack
        if len(self.minStack) != 0:
            val = min(val, self.minStack[-1])
        else:
            val = val
        #update minStack with new lowest val
        self.minStack.append(val)
        
            

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()