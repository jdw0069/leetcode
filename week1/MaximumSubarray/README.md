# Brute Force Approach
### Description
This approach tries every possible sub-array in nums and chooses the one with the maximum sum.
#### Algorithm
1. Create two variable to store the current and max sums
2. Loop through the array twice to calculate all sums of the array
3. If maximum sum has changed will lopping, update maximum sum
4. On second loop, go through each subarray and check for maximum sum
5. Once both loops are complete, return the maxSub variable
#### Time Complexity
Our time complexity is **O(n^2)** since we are considering every subarray and choosing maximum of it. (Two nested for loops)

#### Space Complexity
Our space complexity is **O(1)** since we are only storing a constant space for the variables.

#### Code
```python
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
```

---

# Optimal Approach
### Description
We can use Kadanes's Algorithm to help speed up this solution. See here for a great explenation --> https://www.enjoyalgorithms.com/blog/maximum-subarray-sum  

### Algorithm
1. Declare variables for max (just set to first element in list) and current sum
2. Iterate through the array
3. If at any point our current sum is negative reassign it to 0
4. Keep updating current sum with the next element in the array
5. Compare if current sum is greater than previous max sum
6. Return largest sub array.

#### Time Complexity
Our time complexity is **O(n)** as we only visit each element in the list once (one for loop)

#### Space Complexity
Our space complexity is **O(1)** since we are only storing a constant space for the variables.

#### Code
```python
   def maxSubArray(self, nums: List[int]) -> int:
        #base case
        if len(nums) == 1:
            return nums[0]
        #just pick the starting number in list as the max 
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
```