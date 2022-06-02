from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #use two pointer strategy
        leftPointer = 0
        rightPointer = 1
        #temp variable for profit
        maxProfit = 0
        #loop through entire list starting at the right pointer
        while rightPointer < len(prices):
            #compare left pointer and right pointer
            if prices[leftPointer] < prices[rightPointer]:
                #calculate difference between the right pointer and left pointer
                profit = prices[rightPointer] - prices[leftPointer]
                #compare current profit to previous max profit and store result
                maxProfit = max(maxProfit, profit)
            #if left pointer > right pointer, shift left pointer to match right pointer
            else:
                leftPointer = rightPointer
            #always increment right pointer to check new values in the list
            rightPointer = rightPointer + 1

        return maxProfit
