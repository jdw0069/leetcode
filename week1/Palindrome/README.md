# Brute Force Approach
### Description
We use the two pointer strategy for this problem and compare the outermost two characters moving inwards until we meet in the middle. First, we convert the input string into all lowercase values and loop through string removing any non alpha-numeric characters and store that result in a new string. Next, we take the new string and start one pointer at the first character and the another pointer at the ending character. Working our way inwards of the string, we compare each character to ensure they match and if so, we return True. Otherwise, we return False

#### Algorithm
1. Check base case for empty string
2. Convert string to lowercase
3. Loop through each character in string and remove non alpha-numeric characters 
4. Loop through formated string with two pointers (one at the starting character and another at the last character) and working our way inwards, compare each character to see if they match.
5. If pointers/characters match, return true. Otherwise, return False

#### Time Complexity
Our time complexity is **O(N)**. We use single for loops to iterate over n characters of the string.

#### Space Complexity
Our space complexity is **O(N)** since we are only storing a new copy of a formatted string of size n.

#### Code
```python
 def isPalindrome(self, s: str) -> bool:
        #if null return True (base case)
        if len(s) == 0:
            return True
        #convert everything to lowercase
        inputString = s.lower()
        #remove non-alphanumeric characters
        for i in inputString:
            if not i.isalnum():
               inputString = inputString.replace(i, "")
        #test for palidrome using two pointer strategy
        for i in range(len(inputString)):
            if inputString[i] != inputString[-i - 1]:
                return False
        return True
```

---

# Optimized Approach
### Description
We use the two pointer strategy for this problem and compare the outermost two characters moving inwards until we meet in the middle. We skip over non-alpha-numeric chracters and compare the lowercase versions of the letters/numbers when we do our comparisons.


#### Algorithm
1. Create two pointers (one at start and one at end of string)
2. Loop through each character
3. Check if character fits base case of alpha-numeric character
4. If characters doesn't pass base case, increment pointer and repeat cycle.
5. If character passes base case, do the comparison for each pointer/character.
6. If any character doesn't match, return False. 
7. Otherwise, we will have checked each character in string and determined that the given string is a palidrome and we return True.

#### Time Complexity
Our time complexity is **O(N)** since we still have to check each N elements in the string, but here we are using only one for loop to iterate through the string.

#### Space Complexity
Our space complexity is **O(1)** since we are only storing varibales and not any additional data structures.

#### Code
```python
def isPalindrome(self, s: str) -> bool:
        # i starts at beginning of s and j starts at the end         
        i, j = 0, len(s) - 1
        # While i is still before j        
        while i < j:
            # If i is not an alpha-numeric character then advance i            
            if not s[i].isalnum():
                i += 1
            # If j is not an alpha-numeric character then advance i
            elif not s[j].isalnum():
                j -= 1
            # Both i and j are alpha-numeric characters at this point so if they do not match return the fact that input was non-palendromic
            elif s[i].lower() != s[j].lower():
                return False
            # Otherwise characters matched and we should look at the next pair of characters
            else:
                i, j = i + 1, j - 1
        # The entire stirng was verified and we return the fact that the input string was palendromic         
        return True
```