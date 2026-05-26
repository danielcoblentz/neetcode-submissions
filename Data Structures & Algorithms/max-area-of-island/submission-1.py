class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if not grid or not grid[0]:
            return 0

        
        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0

        def dfs(r, c):
            directions = [[1,0], [0,1], [-1,0],[0,-1]]
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0):
                return 0

            grid[r][c] = 0
            area = 1
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            return area



        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    max_area = max(area, max_area)

        return max_area