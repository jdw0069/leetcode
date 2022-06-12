# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #start at root noded
        current = root
        #start loop
        while current != None:
            #go to left sub tree
            if current.val > p.val and current.val > q.val:
                #update node
                current = current.left
             #go to right sub tree
            elif current.val < p.val and current.val < q.val:
                #update node
                current = current.right
            #found the split/lca
            else:
                return current