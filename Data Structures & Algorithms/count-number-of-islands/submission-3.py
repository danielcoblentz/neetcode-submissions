class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0
        ans = 0

        def dfs(row, col):
            dirs = [[0,1], [1,0], [-1,0], [0,-1]]

            if (row < 0 or row >= ROWS or col < 0 or col >= COLS or grid[row][col] == '0'): return

            grid[row][col] = '0'
            for nr, nc in dirs:
                dfs(row + nr, col + nc)

        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    ans += 1
                    dfs(r, c)
        return ans