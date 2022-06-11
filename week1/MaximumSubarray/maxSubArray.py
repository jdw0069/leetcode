from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #base case
        if len(nums) == 1:
            return nums[0]
        #set inital max to first element in list
        maxSub = nums[0]
        #outer loop
        for i in range(0,len(nums)):
            #update sum after each iteration of sub arrays 
            currentSum = 0
            #inner loop
            for j in range(i, len(nums)):
                #add previous sum to current element
                currentSum = currentSum + nums[j]
                #comparison for bigger value
                if currentSum > maxSub:
                    maxSub = currentSum
        return maxSub

################################################################
        
        #base case
        if len(nums) == 1:
            return nums[0]
        #just pick the starting number in list as the max and set max to 0
        maxSub = nums[0]
        currentSum = 0
        for i in nums:
            #if we see a negative prefix, remove from currentSum
            if currentSum < 0 :
                currentSum = 0
            #add current element
            currentSum = currentSum + i
            #compute max between currenet element and previous max
            maxSub = max(maxSub, currentSum)
        return maxSub
