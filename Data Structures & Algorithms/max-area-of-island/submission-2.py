class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        ROWS, COLS = len(grid), len(grid[0])
        ans = 0

        def dfs(r, c):
            count = 1
            # compute max within function and return to user
            dirs = [[1,0], [0,1],[-1,0],[0,-1]]
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0):
                return 0

            grid[r][c] = 0
            for nr, nc in dirs:
               count += dfs(r + nr, c + nc)
                
            return count

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    ans = max(dfs(r, c), ans)
        return ans
