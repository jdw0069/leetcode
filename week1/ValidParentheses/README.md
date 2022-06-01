# Brute Force Approach
### Description
Every time we see an open bracket, we push the current element to a stack (LIFO)that is implemented using an array data structure. If we ever see a closing bracket, then we first check to make sure that the stack is not empty. If we know that the stack is currently empty on this step, then there cannot be a matching bracket and therefore we return false. Given that our stack is not empty, we pop the previous bracket off the stack and check to see if it is a matching pair given our current closing bracket that we are comparing agaisnt. We repeat this cycle until all brackets have been checked and if our final stack is empty, then we know that the given string has matching brackets and we return true. If our string is not empty, then we return false.

#### Algorithm
1. Create stack that we will push and pop individual chars from the given string to
2. Loop through string starting at the first character
3. If character is an open bracket, add it to the stack
4. If character is a closed bracket, check to make sure stack isn't empty
5. If stack isn't empty, pop the last value off the stack and check for matching pair
6. Repeat this process and if all stack is empty after looking at entire string (string had all matching pairs), return true. Otherwise, return false

#### Time Complexity
Our time complexity is **O(n)**. This is due to the fact that we must check all n characters in our given string.

#### Space Complexity
Our space complexity is **O(n)** since we are storing each character in the string using a stack that will be potentially of size n depending on how large the string is.

#### Code 
```python
 def isValid(self, s: str) -> bool:
        #create stack using list
        stack = []
        #if open bracket, append to stack
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            #if closed bracket, check if stack isn't empty
            elif char == ")" or char == "}" or char == "]":
                #if stack is empty return false
                if len(stack) == 0:
                    return False
                #if stack is not empty, pop the last value off the stack
                lastBracket = stack.pop()
                #check for matching brackets
                if   lastBracket == "[" and char != "]": return False
                elif lastBracket == "(" and char != ")": return False
                elif lastBracket == "{" and char != "}": return False
        #if all chars have been popped off the stack, return true, else return false
        if len(stack) == 0:
            return True
        else:
            return False
```

---

# Optimized Approach
### Description
While this solution is not optimized for time and space complexity,our approach uses a dictionary/hashmap to help speed up lookups for our matching brackets while reducing the amount of code needed vs our previous solution. Here, we use a dictionary to store the corresponding opening and closing brackets with the closing brackets being the keys, and the opening brackets being the value. Once we come across a character that is a closing bracket, we check to see if our previous value in the stack is a matching pair. If the length of the stack is 0, or our current value it is not a matching pair, we return false. Otherwise, it is either a matching pair and we pop these brackets off the stack, or the current character is an opening bracket and we add it to our stack. We repeat this process for know good test cases until we have looped through every character in our given string. At the end, if our stack is empty, then we know that the given string has matching brackets and we return true. Otherwise, we return false.

#### Algorithm
1. Create dictionary that stores key/value pairs of closing/opening brackets
2. Create stack to store chars in string
3. Loop through each character in string starting at the beginning
4. Check if current character is a closing bracket by comparing it to dictionary
5. If opening bracket, add it to the stack
6. If closing bracket and not stack isn't empty, and a match, pop current value from the stack (opening bracket as we must have hit a match), otherwise return false
7. After all characers have been checked in the string, check whether stack is empty
8. If stack is empty, then string must have contained all match pairs, otherwise, return false

#### Time Complexity
Our time complexity is still **O(n)**. This is due to the fact that we must potentially check all n characters in our given string.

#### Space Complexity
Our space complexity is **O(n)** since we are storing each character in the string using a stack that will be potentially of size n depending on how large the string is.


```python
def isValid(self, s: str) -> bool:
        #create hashmap that maps closing brackets to open brackets
        bracketDict = {")": "(", "}": "{", "]": "["}
        #create stack for storing chars in string s
        stack = []
        #loop through each character
        for char in s:
            #check if current character is a closing bracket (check key in dict)
            if char in bracketDict:
                #if brackets match, pop last value in stack
                if len(stack) != 0 and stack[-1] == bracketDict[char]:
                    stack.pop()
                #if current stack state is empty or no match, return false
                else:
                    return False
            #check if current character is a opening brakcet, add it to stack
            else:
                stack.append(char)
        #if stack is empty after going through each character in string, return true
        if len(stack) == 0:
            return True
        else:
            return False
```