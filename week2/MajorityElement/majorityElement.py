from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        highestFrequency = 0
        result = 0
        #load character counts into dictionary
        for letter in nums:
            if letter not in counter:
                counter[letter] = 0
            counter[letter] += 1
        #check for highest character counter
        for key, value in counter.items():
            if counter[key] >= highestFrequency:
                highestFrequency = value
                result = key
        return result