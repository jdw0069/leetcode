class Solution:
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

#        return sorted(s) == sorted(t)

         