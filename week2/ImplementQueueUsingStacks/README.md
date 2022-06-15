# Approach
### Description
For this solution, we make sure that oldest entered element is always at the top of stack 1, so that pop operation just pops from stack1. To put the element at top of stack1, stack2 is used.

#### Algorithm
1. Create two stacks
2. Using one stack to hold all elements
3. When new element is pushed, put all current items from stack 1 to stack 2
4. Add new element to stack 1 and push all elements from stack 2 onto stack one
5. All other operations are trivial

#### Time Complexity
Our time complexity is **O(n)** for the push operations as we have to move n number of elements. The time complexity for the pop operation is **O(1)** since we already know where the last element in the stack is.

#### Space Complexity
Our space complexity is **O(n)** since we are using an extra stack to store n elements.

#### Code
```python
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
```