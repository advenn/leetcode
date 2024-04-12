from typing import List
from icecream import ic


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Each row must contain the digits 1-9 without repetition.
        Each column must contain the digits 1-9 without repetition.
        Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

        board.length == 9
        board[i].length == 9
        board[i][j] is a digit 1-9 or '.'.
        """
        col_len = len(board)
        row_len = len(board[0])
        row_elements = list()
        col_elements = list()
        sub_boxes = [[] for _ in range(9)]
        for row in range(row_len):
            for col in range(col_len):
                # ic((row, col), (col,row))
                # continue
                sub_box = (col // 3) * 3 + row // 3
                row_elem = board[row][col]
                col_elem = board[col][row]
                # ic(row_elements, col_elements, row_elem, col_elem)
                if row_elem not in row_elements and row_elem != ".":
                    row_elements.append(row_elem)
                elif row_elem in row_elements:
                    return False
                if col_elem not in col_elements and col_elem != ".":
                    col_elements.append(col_elem)
                elif col_elem in col_elements:
                    return False
                if row_elem not in sub_boxes[sub_box] and row_elem != ".":
                    sub_boxes[sub_box].append(row_elem)
                elif row_elem in sub_boxes[sub_box]:
                    return False
            print(sub_boxes)
            row_elements.clear()
            col_elements.clear()
        return True
        # for row in range(row_len):
        #     row_ = board[row]
        #     row_elements = set()
        #     for col_elem in row_:
        #         if col_elem not in row_elements and col_elem != ".":
        #             row_elements.add(col_elem)
        #         else:
        #             return False
        # for col in range(col_len):
        #     row_elements = set()
        #     for row_elem in range(row_len):


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
s = Solution()
print(s.isValidSudoku(board))
