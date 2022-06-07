import os
from platform import architecture
import pytest
from validAnagram import Solution

solution = Solution()

def test_example1():
    input1 = "anagram"
    input2 = "nagaram"
    actual = solution.isAnagram(input1,input2)
    expected = True
    assert actual == expected


def test_example2():
    input1 = "rat"
    input2 = "car"
    actual = solution.isAnagram(input1,input2)
    expected = False
    assert actual == expected


def test_example3():
    input1 = "aa"
    input2 = "a"
    actual = solution.isAnagram(input1,input2)
    expected = False
    assert actual == expected