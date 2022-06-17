class Solution:
    def climbStairs(self, n: int) -> int:
        #use bottom up DP approach
        one = 1
        two = 1
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one