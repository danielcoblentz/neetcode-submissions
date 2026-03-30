class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for i in range(n)]
        col = set()
        posDiag = set() # (r + c)
        negDiag = set() # (r - c)
        res = []

        def backtrack(row):
            if row == n:
                # Use "".join to match the required output format
                copy = ["".join(r) for r in board]
                res.append(copy)
                return

            for c in range(n):
                # FIXED: Check the correct diagonal sets
                if c in col or (row + c) in posDiag or (row - c) in negDiag:
                    continue 

                col.add(c)
                posDiag.add(row + c)
                negDiag.add(row - c) # FIXED: changed + to -
                board[row][c] = "Q"

                backtrack(row + 1)

                # Backtrack: Clean up the state
                col.remove(c)
                posDiag.remove(row + c)
                negDiag.remove(row - c) # FIXED: changed + to -
                board[row][c] = "."

        # Start the recursion and then return the result
        backtrack(0)
        return res