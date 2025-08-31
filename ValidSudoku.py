from typing import List


class Solution:

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def backtrack():
            empty = self.find_empty(board)
            if not empty:
                return True
            row, col = empty
            for num in map(str, range(1, 10)):
                board[row][col] = num
                if self.isValidSudoku(board):
                    if backtrack():
                        return True
                board[row][col] = "."
            return False
        backtrack()
        print(board)

    def find_empty(self, board: List[List[str]]) -> tuple | None:
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == ".":
                    return (row, col)
        return None

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = [x for x in board[i] if x != "."]
            if len(set(row)) != len(row):
                return False
            col = [board[j][i] for j in range(9) if board[j][i] != "."]
            if len(set(col)) != len(col):
                return False
        for box_row in range(3):
            for box_col in range(3):
                block = []
                for i in range(3):
                    for j in range(3):
                        val = board[3*box_row+i][3*box_col+j]
                        if val != ".":
                            block.append(val)
                if len(set(block)) != len(block):
                    return False
        return True


s = Solution()

board_3 = [
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

s.solveSudoku(board_3)

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

print(s.isValidSudoku(board_2))

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

print(s.isValidSudoku(board_1))
