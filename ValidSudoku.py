from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for index in range(0, len(board)):
            if index % 3 == 0:
                sub_box: list = []
                for count in range(0, 3):
                    sub_box = board[3 * count][index : index + 3]
                    sub_box += board[3 * count + 1][index : index + 3]
                    sub_box += board[3 * count + 2][index : index + 3]
                    if any(x != "." and sub_box.count(x) > 1 for x in sub_box):
                        return False

            if any(x != "." and board[index].count(x) > 1 for x in board[index]):
                return False

            column_list: list = []
            for index_y in range(0, len(board)):
                column_list.append(board[index_y][index])
            if any(x != "." and column_list.count(x) > 1 for x in column_list):
                return False

        return True


s = Solution()

board_3 = [
    [".", ".", ".", ".", "5", ".", ".", "4", "."],
    [".", "4", ".", "3", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "4", ".", ".", "1"],
    ["8", ".", ".", ".", ".", ".", ".", "2", "."],
    [".", ".", "2", ".", "7", ".", ".", ".", "."],
    [".", "1", "5", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "2", ".", ".", "."],
    [".", "2", ".", "9", ".", ".", ".", ".", "."],
    [".", ".", "4", ".", ".", ".", ".", ".", "."],
]

print(s.isValidSudoku(board_3))

board_1 = [
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

# print(s.isValidSudoku(board_1))


board_2 = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

# print(s.isValidSudoku(board_2))
