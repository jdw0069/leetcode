# Approach
### Description
https://www.youtube.com/watch?v=hTM3phVI6YQ&t=902s

#### Algorithm
1. Use DFS and left and right subtrees and return the largest

#### Time Complexity
Our time complexity is **(n)** since we have to search each n nodes in the Binary Tree

#### Space Complexity
Our space complexity is **O(1)** since we aren't using any auxilary data structures.

#### Code
```python
 def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left = Solution().maxDepth(root.left)
        right = Solution().maxDepth(root.right)
        #single node has depth of one so always add 1
        return max(left,right) + 1
```