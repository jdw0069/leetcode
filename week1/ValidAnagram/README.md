# Approach
### Description
We create two hashmaps/dictionaries to store each occurence of a given character for string s and string t. Next, we loop through the strings and add each characters and its count. Finally, we compare each key/value pair in both hashmaps to ensure they match. If they do match, then we return True. Otherwise, we return False.

#### Algorithm
1. Check to make sure both strings are of the same size
2. Create two dictionaries to store each occurence of character in string s and t
3. Loop through strings adding characters and counts
4. Check both dictionaries to ensure each key/value pair matches

#### Time Complexity
Our time complexity is **O(n)**. We must loop through each n number of characters in both strings s and t.

#### Space Complexity
Our space complexity is **O(n)** since we are creating hashmaps of size n to store each characters in the given strings.

#### Code
```python
 def isAnagram(self, s: str, t: str) -> bool:
    #base case
        if len(s) != len(t):
            return False
        
        #create two dictionaries to store number of each occurence
        #of characters
        sDict = {}
        tDict = {}

        #loop through strings
        for i in range(len(s)):
            #add count of character to dictionaries
            sDict[s[i]] = sDict.get(s[i], 0)
            tDict[t[i]] = tDict.get(t[i], 0)

        #check each key to make sure count of characters is the same
        for j in sDict:
            if sDict[j] != tDict.get(i,0):
                return False
        return True
```

---

# Alternative Solution
### Description
We can sort each string using python's built in function **sorted**. We can then compare each string to see if they are equal. Note that the interviewer might ask you to come up with your own sorting algorithm.

#### Algorithm
1. Sort each string
2. Check to see if they are equal

#### Time Complexity
Our time complexity is **O(N)** since we still have to check each N characters in the given strings and sort them.

#### Space Complexity
Our space complexity is **O(1)**. This will depend on the sorting algorithm used but for the best case, we can assume **O(1)** since we will not use extra memory.

#### Code
```python
    def isAnagram(self, s: str, t: str) -> bool:
         #base case
         if len(s) != len(t):
            return False
        #sort each string and then compare
        return sorted(s) == sorted(t)
```