# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

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
        #return second to last variable which is the new head
        return previous
            