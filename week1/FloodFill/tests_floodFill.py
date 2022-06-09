import os
import pytest
from floodFill import Solution

solution = Solution()

def test_example1():
    actual = solution.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1,1,2)
    expected = [[2,2,2],[2,2,0],[2,0,1]]
    assert actual == expected