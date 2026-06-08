'''

input: 2D array 'matrix' where each sublist is sorted in acending order, a 'target' we must check if exists in the matrix
want: boolean represting if the target value is present in the matrix, T is yes F if no

edge case(s): empty input, not found, only ints no other vlaues, and always in this representation?


time, space: target time of O(log(m * n))
    we compress the 2D representation into a single 1D array and search it like that using ROWS, COLS to determine the midpoint

exp:
above
how to compress it?  - 
id_idx = (row * cols) + col
r = id_idx / COLS
col = id_idx % COLS

while l < = r:
    id_idx = (ROWS * COLS)
    row, col = ()
'''









class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, rows * cols - 1

        while l <= r:
            m = l + (r - l) // 2
            row, col = m // cols, m % cols
            if target > matrix[row][col]:
                l = m + 1
            elif target < matrix[row][col]:
                r = m - 1
            else:
                return True
        return False
        