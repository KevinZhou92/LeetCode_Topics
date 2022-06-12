"""
Solution 1:

Incorrect Solution

We should try to fill empty block 1 by 1 and we should not start from the starting point and only
scan the sub matrix, we will miss empty cells this way.

Time Complexity: O()
Space complexity : O()
"""


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) != 9 or len(board[0]) != 9:
            return

        self.solve(board, 0, 0)

    def solve(self, board, rowIndex, colIndex):

        if rowIndex == len(board) and colIndex == len(board[0]):
            return True

        for row in range(rowIndex, 9):
            for col in range(colIndex, 9):
                for candidate in '123456789':
                    if not self.check(board, row, col, candidate):
                        continue
                    board[row][col] = candidate
                    if self.solve(board, row, col):
                        return True
                    board[row][col] = '.'

        return False

    def check(self, board, rowIndex, colIndex, candidate):
        if board[rowIndex][colIndex] != '.':
            return False

        if candidate in board[rowIndex]:
            return False

        for i in range(9):
            if board[i][colIndex] == candidate:
                return False

        boxRow = (rowIndex // 3) * 3
        boxCol = (colIndex // 3) * 3

        for row in range(boxRow, boxRow + 3):
            for col in range(boxCol, boxCol + 3):
                if board[row][col] == candidate:
                    return False

        return True


"""
Solution 2:

Recursion

Time Complexity: O()
Space complexity : O()
"""


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) != 9 or len(board[0]) != 9:
            return

        self.solve(board, 0, 0)

    def solve(self, board, rowIndex, colIndex):
        if rowIndex == len(board) and colIndex == 0:
            return True

        newRowIndex = rowIndex + 1 if colIndex + \
            1 == len(board[0]) else rowIndex
        newColIndex = 0 if colIndex + 1 == len(board[0]) else colIndex + 1
        if board[rowIndex][colIndex] != '.':
            return self.solve(board, newRowIndex, newColIndex)

        for candidate in '123456789':
            if not self.check(board, rowIndex, colIndex, candidate):
                continue
            board[rowIndex][colIndex] = str(candidate)
            if self.solve(board, newRowIndex, newColIndex):
                return True
            board[rowIndex][colIndex] = '.'

        return False

    def check(self, board, rowIndex, colIndex, candidate):
        if board[rowIndex][colIndex] != '.':
            return False

        if candidate in board[rowIndex]:
            return False

        for i in range(9):
            if board[i][colIndex] == candidate:
                return False

        boxRow = (rowIndex // 3) * 3
        boxCol = (colIndex // 3) * 3

        for row in range(boxRow, boxRow + 3):
            for col in range(boxCol, boxCol + 3):
                if board[row][col] == candidate:
                    return False

        return True
