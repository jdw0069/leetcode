from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
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