# Iterative Approach
### Description
 For Binary search tree, while traversing the tree from top to bottom the first node which lies in between the two numbers p and q is the LCA of the nodes, i.e. the first node n with the lowest depth which lies in between p and q (p<=n<=q) p < q. So just recursively traverse the BST in, if node’s value is greater than both p and q then our LCA lies in the left side of the node, if it’s is smaller than both p and q, then LCA lies on the right side. Otherwise, the root is LCA (assuming that both p and q are present in BST).

#### Algorithm
1. If the value of the current node is less than both p and q, then LCA lies in the right subtree. 
2. If the value of the current node is greater than both p and q, then LCA lies in the left subtree. 
3. If both the above cases are false then return the current node as LCA.

#### Time Complexity
Our space complexity is **O(h)** where h is the height of the tree as we might potentially have to search all nodes in tree.

#### Space Complexity
Our space complexity is **O(1)** as we aren't using an auxilary data structures to store data.

#### Code
```python
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
```

---

# Recursive Approach
### Description
 



#### Time Complexity


#### Space Complexity


#### Code
```python

```