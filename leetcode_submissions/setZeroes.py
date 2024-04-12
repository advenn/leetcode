from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col_len = len(matrix)
        row_len = len(matrix[0])
        zero_cols = []
        zero_rows = []
        for row in range(row_len):
            for col in range(col_len):
                row_elem = matrix[col][row]
                if row_elem == 0:
                    zero_rows.append(row)
                    zero_cols.append(col)
        for row in range(row_len):
            for col in range(col_len):
                if row in zero_rows or col in zero_cols:
                    matrix[col][row] = 0

        return matrix


matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
s = Solution()
print(s.setZeroes(matrix))
