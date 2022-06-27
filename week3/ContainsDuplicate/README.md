# Approach
### Description
Check if the length of the given array and the set conversion of the given array are equal. We could also solve this problem using hashtable/set and check for the amount of occurences for each given integer.

#### Algorithm
1. Check if the length of the given array and the set conversion of the given array are equal

#### Time Complexity
Our time complexity is **O(n)** since we have to convert the given array to a set.
Our space complexity is **O(1)** since we aren't using any auxilary data structures.

#### Code
```python
def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) > len(set(nums)):
            return True
        else:
            return False
```