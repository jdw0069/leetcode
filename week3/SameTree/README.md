# Approach
### Description
https://www.youtube.com/watch?v=vRbbcKXCxOw

#### Algorithm
1. Use DFS
#### Time Complexity
Our time complexity is **O(p + q)** since we might have to traverse all nodes in p and q.
#### Space Complexity
Our space complexity is **O(1)** since we aren't using an auxialry data structures

#### Code
```python
def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #base case, check for null
        if p == None and q == None:
            return True
        #base case, is one tree empty
        if p == None or q == None:
            return False
        #base case, values are not the same
        if p.val != q.val:
            return False
        
        #depth first search
        left  = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        
        #left and right subtrees have to be true (return true), else return false
        return left and right
```