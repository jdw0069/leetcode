class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0
        #convert integer to binary number
        n = bin(n)
        for i in n:
            if i == "1":
                counter = counter + 1
        return counter