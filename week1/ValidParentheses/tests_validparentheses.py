import os
import pytest
from validParentheses import Solution

solution = Solution()

def test_example1():
    s = "()"
    actual = solution.isValid(s)
    expected = True
    assert expected == actual

def test_example2():
    s = "()[]{}"
    actual = solution.isValid(s)
    expected = True
    assert expected == actual
 
def test_example3():
    s = "(]"
    actual = solution.isValid(s)
    expected = False
    assert expected == actual


def test_example4():
    s = "()][{})("
    actual = solution.isValid(s)
    expected = False
    assert expected == actual
def test_example5():
    s = "{[]}"
    actual = solution.isValid(s)
    expected = True
    assert expected == actual

