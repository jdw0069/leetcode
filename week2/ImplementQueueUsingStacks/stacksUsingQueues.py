class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def push(self, x: int) -> None:
        #add all elements of stack1 to stack 2
        while len(self.stack1) != 0:
            self.stack2.append(self.stack1.pop())
            
        #add parameter to the top of stack2
        self.stack1.append(x)
        
        #push everything back to stack1 to maintain order
        while len(self.stack2) != 0:
            self.stack1.append(self.stack2.pop())

    def pop(self) -> int:
        #since stack1 always maintains queue, pop first item off the top
        return self.stack1.pop()
            
        

    def peek(self) -> int:
        #return last item on stack
        return self.stack1[-1]
        

    def empty(self) -> bool:
        #if stack 1 is empty return False
        if len(self.stack1):
            return False
        else:
            return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()