class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ''' 
        thoughts:
        simialr ot max area island excpet we need ocheck if there is an X on each of hte bounds outside the curernt island
        once we hit a 'O' we can begin hte dfs we continue to check how can we 

        '''

        if not board or not board[0]:
            return []

        ROWS, COLS = len(board), len(board[0])

        def capture(r, c):
            if (r < 0 or c <0 or r == ROWS or c == COLS or board[r][c] != "O"):
                return
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        # (DFS) get unsurroudned regions change them into T's O --> T
        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == "O" and (r in [0, ROWS - 1]) or c in [0, COLS - 1]):
                    capture(r, c)

        
        # capture surrounded regions convert O into X's

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"

        # uncapture the unsurroundeed regions T's --> O's