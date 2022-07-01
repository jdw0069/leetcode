# Approach
### Description
https://www.youtube.com/watch?v=0sWShKIJoo4

#### Algorithm
1. Loop through each string in list and check if the current character in string is the same

#### Time Complexity
Our time complexity is **O(n*m )** where n is the length of the array and m is the length of the shortest string,
#### Space Complexity
Our space complexity is **O(1)** since we aren't using any auxialry data structures.

#### Code
```python
def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return result
            result = result + strs[0][i]
        return result
```