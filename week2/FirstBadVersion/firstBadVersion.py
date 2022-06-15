# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        #left and right pointers
        start = 1
        end = n
        #loop through whole list and do binary search
        while start < end:
            mid = start + (end - start) // 2
            #cut out right side
            if isBadVersion(mid) == True:
                end = mid 
            #cut out left side
            elif isBadVersion(mid) == False:
                start = mid + 1
            #return element that is bad
        return start