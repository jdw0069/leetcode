from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        #base case
        if len(nums) == 1:
            return nums
       #non-optimal
       # for i in range(len(nums)):
       #     for j in range(len(nums) - 1):
       #         if nums[j] <= nums[j+1]:
       #             tmp = nums[j]
       #             nums[j] = nums[j+1]
       #             nums[j+1] = tmp
       #optimal
        leftPointer = 0
        for rightPointer in range(len(nums)):
            if nums[rightPointer] != 0:
                temp = nums[leftPointer]
                nums[leftPointer] = nums[rightPointer]
                nums[rightPointer] = temp
                leftPointer = leftPointer + 1       
        
        return nums

print(Solution().moveZeroes([0,1,0,3,12]))