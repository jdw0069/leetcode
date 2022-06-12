# Approach
### Description
https://www.youtube.com/watch?v=LU4fGD-fgJQ

#### Algorithm
1. Use recurusion (DFS) function
2. Recursively iterate through the left subtree
3. Recursively iterate through the right subtree
4. At each subtree, each whether the subtrees are balanced
5. Check height of each subtree
6. If balanced, return True. Else, return False

#### Time Complexity
Our time complexity is **O(n)**, where n is the total number of nodes in the tree since we have to traverse each node in the tree. 

#### Space Complexity
The space complexity of this solution is **O(h)** where h is the height of the tree (how big of a tree we are given).

#### Code
```python
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
     def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            #base case to check if nodes are null and if so, null nodes are balanced so return 0
            if root is None:
                return 0
            #go down left subtree and get height
            heightOfLeft = dfs(root.left)
            #go down right subtree and get height
            heightOfRIght = dfs(root.right)
            #check if subtrees are balanced
            if abs(heightOfLeft - heightOfRIght) > 1 or heightOfLeft == -1 or heightOfRIght == -1:
                return -1
            #return largest subtree height
            return max(heightOfLeft, heightOfRIght) + 1
       #if -1, return False, else, return True 
        return dfs(root) != -1 
```


