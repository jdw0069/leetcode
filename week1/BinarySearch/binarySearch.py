from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #set low and high of list
        low = 0
        high = len(nums) - 1
        #low looping through list
        while (low <= high):
            #calculate middle
            middle = int((low + high) / 2)
            #check to see if we hit the target:
            if (nums[middle] == target):
                return middle
            #if number lower than target, search right subarray
            elif (nums[middle] < target):
                low = middle + 1
            #if number higher than target, search left subarray
            elif (nums[middle] > target):
                high = middle - 1
        #didn't find target
        return -1
