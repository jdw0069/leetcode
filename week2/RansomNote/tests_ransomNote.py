import pytest
from ransomNote import Solution

def test_example1():
    ransomNote = "a"
    magazine = "b"
    actual = Solution().canConstruct(ransomNote, magazine)
    expected = False
    assert expected == actual

def test_example2():
    ransomNote = "aa"
    magazine = "ab"
    actual = Solution().canConstruct(ransomNote, magazine)
    expected = False
    assert expected == actual

def test_example3():
    ransomNote = "aa"
    magazine = "aab"
    actual = Solution().canConstruct(ransomNote, magazine)
    expected = True 
    assert expected == actual
