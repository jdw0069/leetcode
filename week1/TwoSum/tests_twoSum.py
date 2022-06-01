import os
import pytest
from twoSum import Solution

solution = Solution()

def test_example1():
    nums = [2,7,11,15] 
    target = 9
    actual = solution.twoSum(nums, target)
    expected = [0,1]
    assert expected == actual

def test_example2():
    nums = [3,2,4] 
    target = 6
    actual = solution.twoSum(nums, target)
    expected = [1,2]
    assert expected == actual

def test_example3():
    nums = [3,3] 
    target = 6
    actual = solution.twoSum(nums, target)
    expected = [0,1]
    assert expected == actual

def test_example4():
    nums = [2,5,5,11] 
    target = 10
    actual = solution.twoSum(nums, target)
    expected = [1,2]
    assert expected == actual