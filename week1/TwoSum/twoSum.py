from typing import List

from pip import main
class Solution:

   #Brute Force: O(n^2) 
    #def twoSum(self, nums: List[int], target: int) -> List[int]:
    #    for i in range(0, len(nums)):
    #        for j in range(i + 1, len(nums)):
    #            if nums[i] + nums[j] == target:
    #                return [i, j]

    #Optimized: O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}
        for i in range(len(nums)):
            if target - nums[i] in myDict:
                return [myDict[target-nums[i]], i]
            else:
                myDict[nums[i]] = i