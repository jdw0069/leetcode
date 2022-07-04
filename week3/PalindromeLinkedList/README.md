# Non-Optimal Approach
### Description
Convert the linked list to an array and check for palindrome. https://www.youtube.com/watch?v=yOzXms1J6Nk

#### Algorithm
1. Conver linked list to an array and check for palindrome
#### Time Complexity
Our time complexity is **O(n)** since we might search through each integer in the list.
#### Space Complexity
Our space complexity is **O(n)** since we are using an array of size n number of integers.
#### Code
```python
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
```