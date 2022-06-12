import os
import pytest
from linkedListCycle import Solution
from linkedListCycle import ListNode

solution = Solution()

def test_example1():
    three = ListNode(3)
    two = ListNode(2)
    zero = ListNode(0)
    negativeFour = ListNode(-4)

    head = three
    head.next = two
    two.next = zero
    zero.next = negativeFour
    negativeFour.next = two 
    expected = True
    actual = solution.hasCycle(head)
    assert actual == expected
    