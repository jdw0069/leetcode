class Solution:
#    def isValid(self, s: str) -> bool:
#        #create stack using list
#        stack = []
#        #if open bracket, append to stack
#        for char in s:
#            if char == "(" or char == "{" or char == "[":
#                stack.append(char)
#            #if closed bracket, check if stack isn't empty
#            elif char == ")" or char == "}" or char == "]":
#                #if stack is empty return false
#                if len(stack) == 0:
#                    return False
#                #if stack is not empty, pop the last value off the stack
#                lastBracket = stack.pop()
#                #check for matching brackets
#                if   lastBracket == "[" and char != "]": return False
#                elif lastBracket == "(" and char != ")": return False
#                elif lastBracket == "{" and char != "}": return False
#        #if all chars have been popped off the stack, then return true, otherwise return false
#        if len(stack) == 0:
#            return True
#        else:
#            return False
                
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






                
                

print(Solution().isValid("()][{})("))
