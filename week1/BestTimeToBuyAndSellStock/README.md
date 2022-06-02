# Approach
### Description
For this problem, we will be using a very popular startegy named two pointers. We start by creates a left pointer (index 0) to represent the day we buy and a right pointer to represent the day we sell (index 1). Next, we loop through the list starting with a difference comparison of the right pointer minus the left pointer. Since we want to buy low and then sell high, we know that if this comparison returns a negative value, then we do not want to buy and we shift our right pointer one index to the right and update our left pointer to match the current updated index of our right pointer. Once we find two values to where the left pointer and less than the right pointer (i.e. a buying opportunity as the difference between right - left is >= 0), we caculate the difference. We then compare this difference to our current max profit variable and update this value if the new max profit is bigger. Finally, after all values have been looped through in the list, we return our largest max profit from the given list.

#### Algorithm
1. Using two pointer strategy, we create a left pointer (buy) and a right pointer (sell)
2. Loop from right pointer (index 1) till end of list
3. Compare if left pointer is smaller than right pointer (bottom price)
4. If this is the case, calculate differenct between right minus left and get profit result
5. Compare profit result to previous max profit and if bigger, update max profit
6. If right pointer > left pointer, shift left pointer to match current index of right pointer
7. Increase right index pointer by one

#### Time Complexity
Our time complexity is **O(n)**. We use one while loop to potentially check every n element in the entire prices list.

#### Space Complexity
Our space complexity is **O(1)** since we are only storing variables and not any additional data structures.

#### Code
```python
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
```