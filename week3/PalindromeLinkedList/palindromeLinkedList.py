# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next == None:
            return True
        
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        
        left = 0
        right = len(arr) - 1
        
        while left <= right:
            if arr[left] != arr[right]:
                return False
            left = left + 1
            right = right - 1
        
        return True