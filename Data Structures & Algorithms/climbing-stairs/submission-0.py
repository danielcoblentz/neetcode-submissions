class Solution:
    def climbStairs(self, n: int) -> int:
        def solve(i):
            if i == n:
                return 1
            if i > n:
                return 0

            return solve(i + 1) +  solve(i + 2)

        return solve(0)


        