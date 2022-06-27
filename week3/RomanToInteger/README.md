# Approach
### Description
We start by creating a hashmap that maps the roman numerals to correct integer values. To take care of cases where certain strings contain smaller roman numerals before larger roman numerals, we check each i + 1 position to see if the next value is greater thant the current value. If it is greater, we will add a negative number to our result variable. If it is not greater, then we can add a positive number to our result variable.

#### Algorithm
1. Create hashmap for roman numerals to integer values
2. Check if current character in the strings is greater/smaller than next character
3. If greater, search hashmap for integer value and add it to the result
4. If smaller, add a negative value to the result

#### Time Complexity
Our time complexity is **O(n)** since we have to add/lookup in n number of characters in the string s.
#### Space Complexity
Our space complexity is **O(1)** since we are using a hashmap with a finite size.

#### Code
```python
class Solution:
    def romanToInt(self, s: str) -> int:
        #hashmap to store roman numeral to integer conversions
        romanNumeralDict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        for i in range(len(s)):
            #if the current value is smaller than the next value: add a negative value to the stack
            if i + 1 < len(s) and romanNumeralDict[s[i]] < romanNumeralDict[s[i+1]]:
                result = result + (- romanNumeralDict[s[i]])
            else:
                #current value is greate than the next calue: add a postive value to the stack
                result = result + romanNumeralDict[s[i]]
        return result
```