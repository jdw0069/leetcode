class Solution:
   def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    magazineDict = {}
    for i in range(len(magazine)):
        if magazine[i] in magazineDict:
            magazineDict[magazine[i]] = magazineDict.get(magazine[i]) + 1
        else:
            magazineDict[magazine[i]] = 1

    for i in range(len(ransomNote)):
        if ransomNote[i] in magazineDict and magazineDict[ransomNote[i]] > 0:
            magazineDict[ransomNote[i]] = magazineDict.get(ransomNote[i]) - 1
        else:
            return False
    return True
        

