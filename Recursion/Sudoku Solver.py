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


"""
Solution 3:

Recursion Simplified and Optimized for checking a grid's validity 
Used Set to cache result so we can get O(1) time complexity while checking if a grid is valid
for placing a number or not. This is slightly better than O(9)

https://leetcode.com/problems/sudoku-solver/solution/

Time Complexity: O()
Space complexity : O()
"""


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)

        rows, cols, boxes = collections.defaultdict(
            set), collections.defaultdict(set), collections.defaultdict(set)

        for r in range(n):
            for c in range(n):
                if board[r][c] == '.':
                    continue

                v = int(board[r][c])
                rows[r].add(v)
                cols[c].add(v)
                boxes[(r // 3) * 3 + c // 3].add(v)

        def is_valid(r, c, v):
            box_id = (r // 3) * 3 + c // 3
            return v not in rows[r] and v not in cols[c] and v not in boxes[box_id]

        def backtrack(r, c):
            if r == n - 1 and c == n:
                return True
            elif c == n:
                c = 0
                r += 1

            # current grid has been filled
            if board[r][c] != '.':
                return backtrack(r, c + 1)

            box_id = (r // 3) * 3 + c // 3
            for v in range(1, n + 1):
                if not is_valid(r, c, v):
                    continue

                board[r][c] = str(v)
                rows[r].add(v)
                cols[c].add(v)
                boxes[box_id].add(v)

                if backtrack(r, c + 1):
                    return True

                # backtrack
                board[r][c] = '.'
                rows[r].remove(v)
                cols[c].remove(v)
                boxes[box_id].remove(v)

            return False

        backtrack(0, 0)
