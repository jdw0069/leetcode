from typing import Optional
import collections
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
         #recursively repeat for the left subtree
         left = self.invertTree(root.left)
         #recursivley repeat for the right subtree
         right = self.invertTree(root.right)

         #swap nodes
         root.left = right
         root.right = left
        
         return root

#    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#        #base case if given Tree is null
#        if (root == None):
#            return root
#        #hold visited Nodes in queue
#        queue = collections.deque()
#        #add root to queue
#        queue.append(root)
#        #loop through tree
#        while (len(queue) != 0):
#            #get element of end of queue
#            currentNode = queue.pop()
#            #save left side of tree
#            tempNode = currentNode.left
#            #swap nodes
#            currentNode.left = currentNode.right
#            currentNode.right = tempNode
#            #add child nodes to queue
#            if (currentNode.left != None):
#                queue.append(currentNode.left)
#            if(currentNode.right != None):
#                queue.append(currentNode.right)
#       
#        return root