import os
import pytest
from binarySearch import Solution

solution = Solution()

def test_example1():
    nums = [-1,0,3,5,9,12] 
    target = 9
    actual = solution.search(nums, target)
    expected = 4
    assert expected == actual

def test_example2():
    nums = [-1,0,3,5,9,12]
    target = 2
    actual = solution.search(nums, target)
    expected = -1
    assert expected == actual