# Brute Force Approach
### Description

#### Algorithm

#### Time Complexity

#### Space Complexity

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

---

# Optimized Approach
### Description

#### Algorithm

#### Time Complexity

#### Space Complexity

#### Code