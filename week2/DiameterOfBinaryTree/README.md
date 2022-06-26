# Approach
### Description
https://www.youtube.com/watch?v=bkxqA8Rfv04

#### Algorithm
https://www.youtube.com/watch?v=bkxqA8Rfv04

#### Time Complexity
Our time complexity is **O(n)** since we have n number of Nodes we must traverse.

#### Space Complexity
Our space complexity is **O(1)** since we are only updating pointers and not using an auxiliary data structures.

#### Code
```python
def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def longestPath(node):
            #needed for nested function variables
            nonlocal ans
            if not node: 
                return 0
            #go down left and right subtrees getting height
            left = longestPath(node.left)
            right = longestPath(node.right)
            #get diameter and update to largest
            ans = max(ans, left + right)
            #compare height and return largest height   
            return max(left, right) + 1
        
        ans = 0
        longestPath(root)
        return ans
```