class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0,1], [0,-1],[1,0],[-1,0]]
        q = deque()
        INF = 2147483647

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])

        dist = 0
        while q:
            dist += 1
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = dr + r, dc + c

                    if (row < 0 or row >= ROWS or col < 0 or col >= COLS or grid[row][col] != INF):
                        continue
                    grid[row][col] = dist
                    q.append([row, col])

        return None