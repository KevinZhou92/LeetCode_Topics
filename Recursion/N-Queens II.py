"""
Solution 1:

Recursion - Top Down


https://leetcode.com/problems/n-queens-ii/solution/

Time Complexity: O(n!)
Space complexity : O(n)
"""


class Solution:
    def totalNQueens(self, n: int) -> int:
        # rowIndex, cols
        if n <= 1:
            return n

        cols = []
        self.count = 0
        self.placeQueen(0, n, cols)

        return self.count

    def placeQueen(self, rowIndex, n, cols):
        if rowIndex == n:
            self.count += 1
            return

        for colIndex in range(n):
            if not self.isValidPos(rowIndex, colIndex, n, cols):
                continue
            cols.append(colIndex)
            self.placeQueen(rowIndex + 1, n, cols)
            cols.pop()

    def isValidPos(self, rowIndex, colIndex, n, cols):
        for prevRow, prevCol in enumerate(cols):
            if prevCol == colIndex:
                return False
            if abs(rowIndex - prevRow) / abs(colIndex - prevCol) == 1:
                return False

        return True


"""
Solution 1 - 2:

Recursion - Bottom Up

Time Complexity: O(n!)
Space complexity : O(n)
"""


class Solution:
    def totalNQueens(self, n: int) -> int:
        # rowIndex, cols
        if n <= 1:
            return n

        cols = []

        return self.placeQueen(0, n, cols)

    def placeQueen(self, rowIndex, n, cols):
        if rowIndex == n:
            return 1

        res = 0
        for colIndex in range(n):
            if not self.isValidPos(rowIndex, colIndex, n, cols):
                continue
            cols.append(colIndex)
            res += self.placeQueen(rowIndex + 1, n, cols)
            cols.pop()

        return res

    def isValidPos(self, rowIndex, colIndex, n, cols):
        for prevRow, prevCol in enumerate(cols):
            if prevCol == colIndex:
                return False
            if abs(rowIndex - prevRow) / abs(colIndex - prevCol) == 1:
                return False

        return True
