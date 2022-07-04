# Approach
### Description
https://www.youtube.com/watch?v=aayNRwUN3Do

#### Algorithm
1. Use variation of quicksort
#### Time Complexity
Our time complexity is **O(n)** since we might have to traverse all integers in the list.
#### Space Complexity
Our space complexity is **O(1)** since we aren't using an auxialry data structures.

#### Code
```python
def moveZeroes(self, nums: List[int]) -> None:
    for rightPointer in range(len(nums)):
            if nums[rightPointer] != 0:
                temp = nums[leftPointer]
                nums[leftPointer] = nums[rightPointer]
                nums[rightPointer] = temp
                leftPointer = leftPointer + 1       
        
        return nums
```