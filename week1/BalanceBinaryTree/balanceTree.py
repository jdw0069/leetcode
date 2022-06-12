from typing import Optional
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
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

#       3
#      / \
#     9   20
#        /  \
#       15   7
three = TreeNode(3)
nine = TreeNode(9)
twenty = TreeNode(20)
fifteen = TreeNode(15)
seven = TreeNode(7)

root = three
root.left = nine
root.right = twenty
twenty.left = fifteen
twenty.right = seven

print(Solution().isBalanced(root))
