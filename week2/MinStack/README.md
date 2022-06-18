# Approach
### Description
Since we are required to complete all operations in **O(1)** time, we have to trade time for extra space. Here, we will use another stack (minStack) that will store the current minimum number in our normal stack. This way, we can just pop off the top of the minStack our minium value and all other operations are trivial.

#### Algorithm
1. Create two stacks. One to hold all values and another to hold just the minium element
2. For push, append the current val to normal stack and then compare current val to val in minStack
3. If the current val is smaller, update the minStack with smallest val and append val to minStack
4. Pop operation is trivial
5. Top operations is trivial
6. getMin operation is trivial since we have extra stack to keep track of our minimum value

#### Time Complexity
Per the requirements of the problem, all of our operations are **O(1)**.

#### Space Complexity
We had to trade extra space for a faster runtime so we had a to create another stack (minStack), that will hold n number of elements. Therefore, our space complexity is **O(n)**.

#### Code
```python
class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minStack) != 0:
            val = min(val, self.minStack[-1])
        else:
            val = val
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
   
```