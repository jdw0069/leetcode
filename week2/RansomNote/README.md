# Approach
### Description
For this solution, we start off by creating a dictionary that will hold the charcters in the magazine string. We loop through the maganize string and add each occurence of each character to it. Using this new dictionary, we then loop through the ransomeNote string and compare each character to see if it exists in our dictionary and that the number of occurences of that character is greater than if so. If it exsits, we decrement the counter of that character by one and keep repeating. If we find that a single characters does not exist in our dictionary, then we return False. Else, after our loop is complete and we have challed all of the characters in the ransomeNote string, we return True.

#### Algorithm
1. Create dictionary to hold characters in magazine string
2. Loop through magazine string add each character and the number of occureneces of that character
3. Loop through the ransomNote string and check to see if that character exists in our dictionary
4. If it exsits, and the number of occuerences is greater than zero, decrement the number of occurences by one
5. If it does not exists, return False
6. Else, the loop has fully gone through the ransomNote string and return True

#### Time Complexity
Our time complexity is **O(m + n)** where m is the number of characters in the ransomeNote string and n is the number of characters in the magazine string since we must loop through each of these strings.

#### Space Complexity
Our space complexity is **O(n)** since we are using an a hashmap that will store n number of characters.

#### Code
```python
def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    #create empty dict to hold characters in magazine
    magazineDict = {}
    #loop through magazine string and put the number of occurences of each character in the dictionary
    for i in range(len(magazine)):
        if magazine[i] in magazineDict:
            magazineDict[magazine[i]] = magazineDict.get(magazine[i]) + 1
        else:
            magazineDict[magazine[i]] = 1

    #loop through ransonNote
    for i in range(len(ransomNote)):
        #check each character and see if it present in the dictionary
        if ransomNote[i] in magazineDict and magazineDict[ransomNote[i]] > 0:
            #if charcter is in dictionary, decrement the count of character by one
            magazineDict[ransomNote[i]] = magazineDict.get(ransomNote[i]) - 1
        #if character not in dictionary return False
        else:
            return False
    return True 
```