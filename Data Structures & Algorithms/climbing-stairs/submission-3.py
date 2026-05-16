class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        oneB = 2
        twoB = 1
        curr = 0

        for i in range(3, n + 1):
            curr = twoB + oneB
            twoB = oneB
            oneB = curr
        
        return curr
            