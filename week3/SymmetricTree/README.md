# Approach
### Description
https://www.youtube.com/watch?v=XV7Sg2hJO3Q

#### Algorithm
1. Use Recursion

#### Time Complexity
Our time complexity is **O(n)** where h is the hnumber of nodes in the tree.
#### Space Complexity
Our space complexity is **O(h)** where h is the height of the tree.

#### Code
```python
def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        else:
            return self.isMirror(root.left, root.right)
    
    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        elif left != None and right != None and left.val == right.val:
                outPair = self.isMirror(left.left, right.right)
                inPiar = self.isMirror(left.right, right.left)
                return outPair and inPiar
        else:
            return False
```