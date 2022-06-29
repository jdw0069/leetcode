# Approach
### Description
Convert int to binary represation using bin() function and loop over each string character adding up the 1's

#### Algorithm
1. Convert int to binary represation using bin() function and loop over each string character adding up the 1's

#### Time Complexity
Our time complexity is **O(n)** since we have to look at each n numbers.
#### Space Complexity
Our space complexity is **O(1)** since we aren't using any auxialry data structures.

#### Code
```python
 def hammingWeight(self, n: int) -> int:
        counter = 0
        #convert integer to binary number
        n = bin(n)
        for i in n:
            if i == "1":
                counter = counter + 1
        return counter
```