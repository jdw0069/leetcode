import os
import pytest
from invertTree import Solution
from invertTree import TreeNode



def test_example1():
    root  = TreeNode(4)
    two   = TreeNode(2)
    seven = TreeNode(7)
    one   = TreeNode(1)
    three = TreeNode(3)
    six   = TreeNode(6)
    nine  = TreeNode(9)

    root.left = two
    root.right = seven
    two.left = one
    two.right = three
    seven.left = six
    seven.right = nine

    actual = Solution().invertTree(root)

    expectedRoot = root
    expectedRoot.left = seven
    expectedRoot.right = two
    seven.left = nine
    seven.right = six
    two.right = one
    two.left = three
    expected = expectedRoot
    assert actual == expected


    