import os
import pytest
from lcaBST import Solution
from lcaBST import TreeNode

solution = Solution()

def test_example1():
    root  = TreeNode(6)
    two   = TreeNode(2)
    eight = TreeNode(8)
    zero  = TreeNode(0)
    four  = TreeNode(4)
    seven = TreeNode(7)
    nine  = TreeNode(9)
    three = TreeNode(3)
    five = TreeNode(5)

    root.left = two
    root.right = eight
    two.left = zero
    two.right = four
    four.left = three
    four.right = five
    eight.left = seven
    eight.right = nine

    actual = Solution().lowestCommonAncestor(root)
    expected = root
    assert actual == expected