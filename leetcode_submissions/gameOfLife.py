from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> list:
        """
        Do not return anything, modify board in-place instead.
        """

        import copy

        board_ = copy.deepcopy(board)
        height = len(board)
        width = len(board[0])
        for h in range(height):
            for w in range(width):
                summ = 0
                rows = []
                cols = []
                if h == 0:
                    rows.extend([h, h + 1])
                elif h == height - 1:
                    rows.extend([h - 1, h])
                else:
                    rows.extend([h - 1, h, h + 1])
                if w == 0:
                    cols.extend([w, w + 1])
                elif w == width - 1:
                    cols.extend([w - 1, w])
                else:
                    cols.extend([w - 1, w, w + 1])
                for row in rows:
                    for col in cols:
                        if (row, col) != (h, w):
                            try:
                                summ += board_[row][col]
                            except:
                                pass
                if summ < 2 and board_[h][w] == 1:
                    board[h][w] = 0
                elif summ > 3 and board_[h][w] == 1:
                    board[h][w] = 0
                elif (summ == 2 or summ == 3) and board_[h][w] == 1:
                    board[h][w] = 1
                elif summ == 3 and board_[h][w] == 0:
                    board[h][w] = 1
        return board


s = Solution()
# print(s.gameOfLife([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]))

# print(s.gameOfLife([[1, 1], [1, 0]]))

print(
    *s.gameOfLife(
        [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 0],
            [0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]
    ),
    sep="\n"
)
print()
print(
    *s.gameOfLife(
        [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 0],
            [0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]
    ),
    sep="\n"
)
print()
print(
    *[
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ],
    sep="\n"
)
