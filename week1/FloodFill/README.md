# Approach
### Description
To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor. The big idea here is recursion implemented using Depth First Search.
#### Algorithm
 1. Ensure image is valid (base case)
 3. Perform Flood-fill one step to the south of node.
 4. Perform Flood-fill one step to the north of node
 5. Perform Flood-fill one step to the west of node
 6. Perform Flood-fill one step to the east of node
 7. Return.

#### Time Complexity
Our time complexity is **O(m*n)**, where m*n is the number of pixels in the image. We might process every pixel.

#### Space Complexity
Our space complexity is **O(m*n)**, the size of the implicit call stack when calling dfs.
#### Code
```python
 def twoSum(self, nums: List[int], target: int) -> List[int]:
     def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        #base case checks for null and if element is already new color
        if image == None or image[sr][sc] == newColor:
            return image
        #start recursive calles
        self.fill(image, sr, sc, image[sr][sc], newColor)
        #final result
        return image
        
    def fill(self, image, row, column, initialColor, newColor):
        #The base case check to make sure current element isn't out of bounds
        if row < 0 or column < 0 or row >= len(image) or column >= len(image[0]) or image[row][column] != initialColor:
            return
        #Mark element as visited
        image[row][column] = newColor
        #make recursive calls (DFS)
        self.fill(image, row + 1, column, initialColor, newColor) #up
        self.fill(image, row - 1, column, initialColor, newColor) #down
        self.fill(image, row, column + 1, initialColor, newColor) #right
        self.fill(image, row, column - 1, initialColor, newColor) #left 
```

#### Code
