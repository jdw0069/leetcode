from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
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


oneP = TreeNode(1)
rootP = oneP
twoP = TreeNode(2)
threeP = TreeNode(3)
oneP.left = twoP
oneP.right = threeP

oneQ = TreeNode(1)
rootQ = oneQ
twoQ = TreeNode(2)
threeQ = TreeNode(3)
oneQ.left = twoQ
oneQ.right = threeQ

print(Solution().isSameTree(rootP, rootQ))
