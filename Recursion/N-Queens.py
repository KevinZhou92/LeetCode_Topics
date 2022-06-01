"""
Solution 1:

DFS

Be careful for corner cases

Time Complexity: O(n!) 
While it costs O(N^2) to build each valid solution, the amount of valid solutions S(N)
does not grow nearly as fast as N!, so O(N! + S(N) * N^2) = O(N!)
Space complexity : O(n)
"""


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        if n <= 0:
            return self.res

        cols = []
        self.placeQueen(0, n, cols, res)

        return res

    def placeQueen(self, rowIndex, n, cols, res):
        if rowIndex == n:
            res.append(self.buildBoard(cols, n))
            return

        for colIndex in range(n):
            if not self.isValidPos(rowIndex, colIndex, cols):
                continue
            cols.append(colIndex)
            self.placeQueen(rowIndex + 1, n, cols, res)
            cols.pop()

    def isValidPos(self, rowIndex, colIndex, cols):
        for prevRow, prevCol in enumerate(cols):
            if prevCol == colIndex:
                return False

            if abs(prevRow - rowIndex) / abs(prevCol - colIndex) == 1:
                return False

        return True

    def buildBoard(self, cols, n):
        return [''.join(['Q' if cols[rowIndex] == colIndex else '.' for colIndex in range(n)]) for rowIndex in range(n)]
