# Approach
### Description
We will use an iterative approach and take advantage of a two pointer strategy. We can create two pointer variables (slow and fast) and increment them accordingly. Once the fast pointer reaches the end of the list, we know that the slow pointer is at the middle because we incremented the fast pointer at 2x the speed of the slow pointer.
#### Algorithm
1. Use two pointer strategy and create two variable setting them to the head of the linked list
2. Loop through linked list increment the fast pointer at 2x the speed of the slow pointer
3. Once we reach the end, return the slow pointer since it is in the middle
#### Time Complexity
Our time complexity is **O(n)** since we have n number of Nodes we must check in the linked list.
#### Space Complexity
Our space complexity is **O(1)** since we are only updating pointers and not using an auxiliary data structures.

#### Code
```python
def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #use two pointer strategy
        slow = head
        fast = head
        
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow
```