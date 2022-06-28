# Approach
### Description
This problem can be solved by using stacks to add each character in the string we visit to the stacks. As long as the character is not a "#" we append to the top of the stack. If we see a "#" then we pop the top element off the stack and continue. Finally, compare the two stacks to see if they match.

#### Algorithm
1. Create two stacks for each given string
2. If we see a "#" character remove it from the stack
3. Else, add it to the stack
4. Compare each stack to see if they are equal

#### Time Complexity
Our time complexity is **O(n)** since we have to loop through each n character in the given strings.
#### Space Complexity
Our space complexity is **O(n)** since we are two stacks that could hold n number of characters.

#### Code
```python
def backspaceCompare(self, s: str, t: str) -> bool:
        stackS = []
        stackT = []
        
        for i in s:
            if i == "#" and len(stackS) > 0:
                stackS.pop()
            if i != "#":
                stackS.append(i)
        for i in t:
            if i == "#" and len(stackT) > 0:
                stackT.pop()
            if i != "#":
                stackT.append(i)
        
        if stackS == stackT:
            return True
        return False
```