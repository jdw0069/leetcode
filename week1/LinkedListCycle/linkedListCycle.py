from typing import Optional

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
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
        