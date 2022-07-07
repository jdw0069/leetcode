class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        counter = 0
        nums.sort()
        for i in nums:
            if i != counter:
                return i - 1
            counter = counter + 1
            
        return counter