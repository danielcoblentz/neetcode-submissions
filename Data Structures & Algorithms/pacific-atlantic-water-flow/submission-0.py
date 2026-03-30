class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
        input:
        output:
        edge cases:

        time:
        space:

        sol:
        we start in the top left conditions ot know we cna only move ot a neightboring cell if the vlaeu if that cel lis lower or equal to the current cell
        pacific starts from hte frist row and first col and as long as we land anywhere in the last col and row if we find a path then we append the urrent r, c as a list to a result array

        logic:
        iterate over the fisrt row and col -1 so we are not out of bounds

        '''
        if not heights:
            return []

        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()


        def dfs(r, c, visit, prevHeight):
            if ((r,c) in visit or r < 0 or c < 0 or r == ROWS or c == COLS or
            heights[r][c] < prevHeight):
                return

            visit.add((r,c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
            

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS-1][c])


        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])

        return res