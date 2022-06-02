from multiprocessing import dummy
from typing import Optional
# Definition for singly-linked list.
class ListNode:     
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
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
        #if list1 or list2 are empty, find non-empty list and return it
        if list1:
            #insert nodes in list1 to new list
            tempTraversalNode.next = list1
        #if list1 is empty, return list2
        else:
             #insert nodes in list1 to new list
            tempTraversalNode.next = list2
        return dummyNode.next
