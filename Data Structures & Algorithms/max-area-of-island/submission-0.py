class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0


        ROWS, COLS, max_area = len(grid), len(grid[0]), 0

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0):
                return 0

            
            # mark as visited
            grid[r][c] = 0


            area = 1
            area += dfs(r + 1, c) 
            area += dfs(r - 1, c) 
            area += dfs(r, c + 1) 
            area += dfs(r, c - 1)

            return area 


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    temp = dfs(r, c)
                    max_area = max(temp, max_area)

        return max_area # final area copmuted
                    