from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        n = len(matrix)
        Do not return anything, modify matrix in-place instead.
        (0,0) -> (0, 2)
        (0,1) -> (1, 2) ...
        1st side -> i, j -> j, n
        2nd side -> i, j -> j, i
        3rd side -> i, j -> j, 0
        """
        # print(*matrix, sep='\n')
        n = len(matrix)
        new = [[0 for i in range(n)] for _ in range(n)]
        # print(*new, sep='\n')
        count = 0
        for i in range(n):
            for j in range(n):
                # print(i, j, '\t', j, n - count - 1)
                new[i][j] = matrix[j][n - count - 1]
            count += 1

        print(*new, sep='\n')
        # failed


arr1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
arr2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
s = Solution()
s.rotate(arr1)
# s.rotate(arr2)
