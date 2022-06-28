# Approach
### Description
https://www.youtube.com/watch?v=RyBM56RIWrM
#### Algorithm
1. Use DP
#### Time Complexity
Our time complexity is **O(n)** since we have to check all n elements in the array.
#### Space Complexity
Our space complexity is **O(n)** since we are storing the result in an array of size n.

#### Code
```python
def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i-offset]
        return dp
```