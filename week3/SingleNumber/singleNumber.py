from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #Non-optimal Approach
        # if len(nums) == 1:
        #def singleNumber(self, nums: List[int]) -> int:
        # matchingDict = {}
        # for i in range(len(nums)):
        #     if nums[i] not in matchingDict:
        #         matchingDict[nums[i]] = 1
        #     else:
        #         matchingDict[nums[i]] = matchingDict.get(nums[i]) + 1
        # for key,value in matchingDict.items():
        #     if value == 1:
        #         return key

        #Optimal Approach
        result = 0
        for n in nums:
           result = n ^ result
        return result

