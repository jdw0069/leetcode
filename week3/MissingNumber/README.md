# Approach
### Description
Sort the array and use a counter to check for next number
#### Algorithm
1. Sort the array and use a counter to check for next number
#### Time Complexity
Our time complexity is **O(nlogn)** since we are using the sorting function
#### Space Complexity
Our space complexity is **O(1)** since we aren't using an auxialry data structures.

#### Code
```python
 def missingNumber(self, nums: List[int]) -> int:
        counter = 0
        nums.sort()
        for i in nums:
            if i != counter:
                return i - 1
            counter = counter + 1
            
        return counter
```