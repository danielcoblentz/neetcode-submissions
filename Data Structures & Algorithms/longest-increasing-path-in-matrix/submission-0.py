'''
input - m * n grid (matrix) 
output - longest path that contians increasing numbers
edge case(s) - empty matrix, all zeros? and all ints?

time, space

notes:
its a DAG problem because the path amkes a natural way to follow hte numbers giving it direction
we check each ROW, COL and if the nei is more than hte current then that is a possible path (need ot check all directions)
if we find a vlaid path we can do all 4 dires + 1 where 1 represents that new lenght of the path because we are at that new postiion
'''
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix[0] or not matrix:
            return 0

        g = matrix
        ROWS, COLS = len(g), len(g[0])
        ans = 0
        memo = {}

        def dfs(r,c):
            max_len = 1
            if (r, c) in memo:
                return memo[(r, c)]
            directions = [[1,0], [0,1], [-1,0],[0,-1]]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and g[r][c] < g[nr][nc]:
                    path_from_neighbor = 1 + dfs(nr, nc)
                    max_len = max(max_len, path_from_neighbor)
            memo[(r, c)] = max_len
            return max_len

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c)
                ans = max(ans, dfs(r,c))
        return ans

