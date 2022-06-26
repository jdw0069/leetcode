# Approach
### Description
https://www.youtube.com/watch?v=keuWJ47xG8g

#### Algorithm
https://www.youtube.com/watch?v=keuWJ47xG8g

#### Time Complexity
Our time complexity is **(n)** since we have to search each n characters in a string

#### Space Complexity
Our space complexity is **O(1)** since we aren't using any auxilary data structures.

#### Code
```python
def addBinary(self, a: str, b: str) -> str:
        result = ""
        carry = 0
        #reverse both strings
        a = a[::-1]
        b = b[::-1]
        #pick biggest string and iterate through it
        for i in range(max(len(a), len(b))):
            #check if we are the end of a string
            if i < len(a):
                digitA = int(a[i])
            #we are out of bounds
            else:
                digitA = 0
            if i < len(b):
                digitB = int(b[i])
            else:
                digitB = 0

            #sum digits together
            total = digitA + digitB + carry
            #since they are binary digits (aka base 2) mod total by 2 (aka binary addition)
            char = total % 2
            #we don't want integer, convert to string
            charString = str(char)
            #add character to result string defined earlier (digit by digit)
            result = charString + result
            #update carry value (if total = 2, carry of 1, if total = 3, carry of 1, if total = 1, no carry)
            carry = total // 2
        
        #at the very end, if we have a carry value, add it to the beginning of our result string
        if carry:
            result = "1" + result
        return result
```