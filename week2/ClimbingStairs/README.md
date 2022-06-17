# Approach
### Description
https://www.youtube.com/watch?v=Y0lT9Fck7qI
https://www.youtube.com/watch?v=NFJ3m9a1oJQ

#### Algorithm
1. Use Dynamic Programming (Bottom up approach)

#### Time Complexity
Our time complexity is **O(n)** since we have n elements we have to loop through.

#### Space Complexity
Our space complexity is **O(1)** since we are just using variables.

#### Code
```python
 def climbStairs(self, n: int) -> int:
        #use bottom up DP approach
        one = 1
        two = 1
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one
```