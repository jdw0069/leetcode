import os
import pytest
from isPalidrome import Solution

solution = Solution()

def test_example1():
    s = "A man, a plan, a canal: Panama"
    actual = solution.isPalindrome(s)
    expected = True
    assert expected == actual

def test_example2():
    s = "race a car"
    actual = solution.isPalindrome(s)
    expected = False
    assert expected == actual

def test_example3():
    s = " "
    actual = solution.isPalindrome(s)
    expected = True
    assert expected == actual

