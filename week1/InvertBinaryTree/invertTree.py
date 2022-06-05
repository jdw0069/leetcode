from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #make sure root is not null
        if not root:
            return None
        #swap left child with right child and store temporary variable to hold left value before swap
        tmp = root.left
        root.left = root.right
        root.right = tmp
        
        #recursively repeat for the left subtree
        self.invertTree(root.left)
        #recursivley repeat for the right subtree
        self.invertTree(root.right)

        return root

def fromlist(values):
        def create(it):
            value = next(it)
            return None if value is None else TreeNode(value)
            
        if not values:
            return None
        it = iter(values)
        root = TreeNode(next(it))
        nextlevel = [root]
        try:
            while nextlevel:
                level = nextlevel
                nextlevel = []
                for node in level:
                    if node:
                        node.left = create(it)
                        node.right = create(it)
                        nextlevel += [node.left, node.right]
            
        except StopIteration:
            return root
        raise ValueError("Invalid list")

print(Solution().invertTree([4,2,7,1,3,6,9]))




        