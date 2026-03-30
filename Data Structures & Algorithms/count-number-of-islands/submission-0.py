class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # first if we hit a 1 then we need ot call dfs on it and explore all other connected islands
        if not grid or not grid[0]:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        islands = 0


        def dfs(r, c):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == '0'):
                return

            # make current cell a 0 to mark as visited and prevent inf loop
            grid[r][c] = '0'

            #search all possible directions
            dfs(r + 1, c) 
            dfs(r - 1, c) 
            dfs(r, c + 1) 
            dfs(r, c - 1) 


        

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1': # we found an island inc count and explore it
                    islands += 1
                    dfs(r, c)
        return islands


