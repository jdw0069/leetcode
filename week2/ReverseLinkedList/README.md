# Approach
### Description
We will use an iterative approach and take advantage of a two pointer strategy. We can create two pointer variables (previous and current) and set the current to the head of linked list. We can iterate through the linked list swapping around pointers and updating our previous/current variables. Once we reach the end of the linked list (when current == None), we return the previous variable which is now the new head of our reversed linked list.

#### Algorithm
1. Use two pointer strategy and create two variable setting them to null and the current start of the linked list
2. Loop through linked list swapping pointers and updating varibles
3. Once we reach the end, return the new head of the reversed linked list
#### Time Complexity
Our time complexity is **O(n)** since we have n number of Nodes we must reverse in the linked list.

#### Space Complexity
Our space complexity is **O(1)** since we are only updating pointers and not using an auxiliary data structures.

#### Code
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #base case
        if head == None:
            return head
        
        #use two pointer strategy and start at first Node
        previous = None
        current = head
        
        while(current != None):
            #tmp variable so we don't overwrite .next
            nextTmp = current.next
            #take next pointer and revierse it
            current.next = previous
            #update previous pointer
            previous = current
            #increment by one Noe
            current = nextTmp
        return previous
```