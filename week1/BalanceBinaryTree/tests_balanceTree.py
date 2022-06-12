import os
import pytest
from balanceTree import Solution
from balanceTree import TreeNode



def test_example1():
    #       3
    #      / \
    #     9   20
    #        /  \
    #       15   7
    three = TreeNode(3)
    nine = TreeNode(9)
    twenty = TreeNode(20)
    fifteen = TreeNode(15)
    seven = TreeNode(7)

    root = three
    root.left = nine
    root.right = twenty
    twenty.left = fifteen
    twenty.right = seven 

    actual = Solution().isBalanced(root)
    expected = True
    assert actual == expected


    