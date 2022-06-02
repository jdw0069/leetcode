# Iterative Approach
### Description
For this solution, we start by creating two temporary nodes that will help us solve a few edge cases and keep our code clean. You can view more about the design choice for this by referencing the following links: https://stackoverflow.com/questions/58715870/explanation-about-dummy-nodes-and-pointers-in-linked-lists#:~:text=1%20Answer&text=dummy%20and%20cur%20both%20point,because%20it's%20the%20same%20list.&text=you're%20not%20creating%20a,pointer%20down%20the%20existing%20listz and https://leetcode.com/problems/merge-two-sorted-lists/discuss/759870/Python3-Solution-with-a-Detailed-Explanation-dummy-explained. Next, we check to make sure if list1 and list2 are not empty. If one of them are empty, we check to see which one is empty so we can return the non-empty sorted linked list. Asumming that list1 and list2 both have nodes, we start by comparing the first nodes in each linked list so we can update our traversal node pointer. From there, we simply walk through both linked lists adding a each smaller or equal value to the traversal node. Finally, we return the dummy node's next value as this node is still pointed to the head of our linked list while our traversal node has iterated through both of list1 and list2.

#### Algorithm
1. Create dummy node and traversal nodes
2. Check to make sure list1 and list2 are not null. If one is null, return the list that isn't empty
3. Iterate through the corresponding lists and start at the smallest first value
4. Add smaller node to traversal nodes path
5. Update list pointer
6. Update traversal node pointer for next set of comparisons between list1 and list2
7. Return dummy node's .next value that has not traveresd through and is pointed at the start of our new linked list that has been updated with merged sorted linked list

#### Time Complexity
Our time complexity is **O(n)**. We use a single loop that must traverse all n nodes in the two sorted linked lists.

#### Space Complexity
Our space complexity is **O(n)** since we are creating a new linked list of size n nodes.

#### Code
```python
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
         #create dummy node to store head value and create temp node for traversal
        dummyNode = tempTraversalNode = ListNode()
         #check to make sure given lists are not empty
        while list1 != None and list2 != None:
            #check list1 and list2 first node to see which list we need to start at
            if list1.val < list2.val:
                #add current list1 node to new list
                tempTraversalNode.next = list1
                #update pointer
                list1 = list1.next
            else:
                #add current list2 node to new list
                tempTraversalNode.next = list2
                #update pointer
                list2 = list2.next
            #update traversal pointer to make next comparison
            tempTraversalNode = tempTraversalNode.next
        #if list1 or list2 are empty (we reached the end of one list or a given paramater list is empty), find non-empty list and return it
        if list1:
            #insert nodes in list1 to new list
            tempTraversalNode.next = list1
        #if list1 is empty, return list2 to new list
        else:
             #insert nodes in list2 to new list
            tempTraversalNode.next = list2
        #return final result as dummy node is at the head of list
        return dummyNode.next
```


---

# Recursive Approach
### Description


#### Algorithm


#### Time Complexity
 

#### Space Complexity


#### Code
