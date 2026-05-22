class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0


        ans = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            dirs = [[1,0],[0,1],[-1,0],[0,-1]]

            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == '0'): return

            grid[r][c] = '0'
            for nr, nc in dirs:
                dfs(r + nr, c + nc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    ans += 1
                    dfs(r, c)
        return ans
