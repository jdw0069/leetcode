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