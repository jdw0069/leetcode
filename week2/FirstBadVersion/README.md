# Approach
### Description
For this solution, we use binary search in order to get the first bad element from the array that does not sastify our conditions. Here, we know that we can use binary search since we are given an array that is guaranteed to be sorted. 

#### Algorithm
1. Use binary search

#### Time Complexity
Our time complexity is **O(log n)** since we are using binary search to search through an array with n elements in it.

#### Space Complexity
Our space complexity is **O(1)** since we aren't using any auxilary data structures.

#### Code
```python
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

def firstBadVersion(self, n: int) -> int:
    #left and right pointers
    start = 1
    end = n
    #loop through whole list and do binary search
    while start < end:
        mid = start + (end - start) // 2
        #cut out right side
        if isBadVersion(mid) == True:
            end = mid 
        #cut out left side
        elif isBadVersion(mid) == False:
            start = mid + 1
        #return element that is bad
    return start
```