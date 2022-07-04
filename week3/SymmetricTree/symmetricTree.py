# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
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
