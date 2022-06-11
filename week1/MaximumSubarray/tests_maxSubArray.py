import os
import pytest
from maxSubArray import Solution

solution = Solution()

def test_example1():
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    actual = solution.maxSub(nums)
    expected = 6
    assert expected == actual

def test_example2():
    nums = [1]
    actual = solution.maxSub(nums, target)
    expected = 1
    assert expected == actual

def test_example3():
    nums = [5,4,-1,7,8]
    actual = solution.maxSub(nums)
    expected = 23
    assert expected == actual

def test_example4():
    nums = [-2,-1]
    actual = solution.maxSub(nums)
    expected = -1
    assert expected == actual