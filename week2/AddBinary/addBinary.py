#Binary addition
# 0 + 0 = 0
# 0 + 1 = 1
# 1 + 0 = 1
# 1 + 1 = 10
class Solution:
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







        


        



print(Solution().addBinary("11", "1"))