import os
import pytest
from buyAndSellStock import Solution

solution = Solution()

def test_example1():
    prices = [7,1,5,3,6,4]
    actual = solution.maxProfit(prices)
    expected = 5
    assert expected == actual

def test_example2():
    prices = [7,6,4,3,1] 
    actual = solution.maxProfit(prices)
    expected = 0
    assert expected == actual

def test_example3():
    prices = [2,4,1] 
    actual = solution.maxProfit(prices)
    expected = 2
    assert expected == actual
