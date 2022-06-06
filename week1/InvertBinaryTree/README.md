# Iterative Approach
### Description
For this solution, we start by creating a queue that will store our visted Nodes and we will use **Level Order Traversal** when iterating through the given binary tree. Assuming we get a binary tree that is not empty, we add our root Node to the queue and beginning iterating through the binary tree as long as our queue is not empty (if empty, we have visted all nodes in tree). We start by popping the first node from the queue (FIFO) and store is left child in a variable. From there, we save this values (to preserve the left side of the tree) and beginning swapping the current Nodes left and right values (inverting the tree). Once we have swapped these values, we will add the current Nodes left and right children to our queue and continue iterating over the binary tree. We continue to repeat this process until we have visted all Nodes in the binary tree and finally return the root Node.

#### Algorithm
1. Return None if the tree is empty
2. Store the root node in the queue and iterate the loop till the queue is not empty
3. During each iteration
4.        Pop a node from the queue
5.        Swap left and right child
6.        Insert the left and right child into the queue
7. Return root node

#### Time Complexity
For every node in the tree, we perform the queue operations(enqueue and dequeue) only once, and therefore, the time complexity of the above approach is **O(n)**, where n is the total number of nodes in the tree. 

#### Space Complexity
The space complexity of this solution is **O(n)** as it requires a queue of size n to store all the nodes of the binary tree.

#### Code
```python
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #base case if given Tree is null
        if (root == None):
            return root
        #hold visited Nodes in queue
        queue = collections.deque()
        #add root to queue
        queue.append(root)
        #loop through tree
        while (len(queue) != 0):
            #get element of end of queue
            currentNode = queue.pop()
            #save left side of tree
            tempNode = currentNode.left
            #swap nodes
            currentNode.left = currentNode.right
            currentNode.right = tempNode
            #add child nodes to queue
            if (currentNode.left != None):
                queue.append(currentNode.left)
            if(currentNode.right != None):
                queue.append(currentNode.right)
        return root
```


---

# Recursive Approach
### Description
The key insight here is to realize that in order to invert a binary tree we only need to swap the children and recursively solve the two smaller sub-problems (same problem but for smaller input size) of left and right sub-tree. This looks similar to the idea of pre-order traversal.

#### Algorithm
1. When the tree is empty return None. This is also our base case to stop recursive calls.
2. Traverse the binary tree using **pre-order traversal**.
3. Swap left and right child for every node encountered before inverting its left and right sub-tree recursively.

#### Time Complexity
Our time complexity is **O(n)**. We are traversing each node of the tree only one time.

#### Space Complexity
Our space complexity is **O(h)**. This proportional to the maximum depth of recursion tree generated which is equal to the height of the tree (h).


#### Code
```python
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
```