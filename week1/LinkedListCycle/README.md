# Iterative Approach
### Description
For this solution, we start by accounting for any base cases. Next, we create two pointers that will both point to the starting node. We increment both pointers throughout the linked list with one being the slow pointer (only increment by one) and the other being a fast pointer (increment by two). If at anyone point, the fast pointer catches up to the slow pointer, and the values match, then we know that we have found a cycle in the linked list. This is Floyd's cycle detection algorithm

#### Algorithm
1. Create two pointers both starting at the beginning
2. Loop through linked list
3. Have the fast pointer incrementing by two and the slow pointer incrementing by one
4. Check if the fast and slow pointers ever match and if so, return True

#### Time Complexity
Our time complexity is **O(n)**. We use a single loop that must traverse all n nodes in linked list.

#### Space Complexity
Our space complexity is **O(1)** since we are only use two variables.

#### Code
```python
def hasCycle(self, head: Optional[ListNode]) -> bool:
        #base case
        if head == None or head.next == None:
                return False
        #set fast and slow pointers to start of linked list       
        slowPointer = head
        fastPointer = head
        #loop through linked list while we haven't reached the end
        while fastPointer and fastPointer.next:
            #increment slow pointer buy one and fast pointer by two
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
            #if the pointers ever catch up to each other, then we know there is a cycle
            if slowPointer == fastPointer:
                return True
            return False 
```