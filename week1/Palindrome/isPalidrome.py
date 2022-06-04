from typing import List

from pip import main
class Solution:
    def isPalindrome(self, s: str) -> bool:
        #if null return True (base case)
        if len(s) == 0:
            return True
        #convert everything to lowercase
        inputString = s.lower()
        #remove non-alphanumeric characters
        for i in inputString:
            if not i.isalnum():
               inputString = inputString.replace(i, "")
        #test for palidrome using two pointer strategy
        for i in range(len(inputString)):
            if inputString[i] != inputString[-i - 1]:
                return False
        return True

