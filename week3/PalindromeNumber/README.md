# Approach
### Description
Use two pointer strategy and check if first and last character match
#### Algorithm
1. Use two pointer strategy and check if first and last character match
#### Time Complexity
Our time complexity is **O(n)** since we have to search through each n characters in the string
#### Space Complexity
Our space complexity is **O(1)** since we aren't using an auxialry data structures.

#### Code
```python
def isPalindrome(self, x: int) -> bool:
        x = str(x)
        left = 0
        right = len(x) - 1
        while left <= right:
            if x[left] != x[right]:
                return False
            left = left + 1
            right = right - 1
            
        return True
```