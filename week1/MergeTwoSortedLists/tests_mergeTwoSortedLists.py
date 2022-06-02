import os
import pytest
from mergeTwoSortedLists import Solution
from mergeTwoSortedLists import ListNode

solution = Solution()

def compare_list(list1, list2):
    now1 = list1
    now2 = list2

    while now1 != None and now2 != None:
        if now1.val != now2.val:
            return 0
        now1 = now1.next
        now2 = now2.next

    if now1 != None or now2 != None:
        return 0

    return 1

def test_example1():
    node6 = ListNode(4)
    node5 = ListNode(3)
    node4 = ListNode(1)
    node4.next = node5
    node5.next = node6
    node3 = ListNode(4)
    node2 = ListNode(2)
    node1 = ListNode(1)
    node1.next = node2
    node2.next = node3
    list1 = node1
    list2 = node4
    actual = solution.mergeTwoLists(list1, list2)
    resultNode6 = ListNode(4)
    resultNode5 = ListNode(4)
    resultNode4 = ListNode(3)
    resultNode3 = ListNode(2)
    resultNode2 = ListNode(1)
    resultNode1 = ListNode(1)
    resultNode1.next = resultNode2
    resultNode2.next = resultNode3
    resultNode3.next = resultNode4
    resultNode4.next = resultNode5
    resultNode5.next = resultNode6
    expected = resultNode1
    assert compare_list(actual, expected) == 1
    