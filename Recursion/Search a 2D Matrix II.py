"""
Solution 1:

Recursion. 
Find the pivot point of the matrix, split the matrix into four sub matricies and rule out the impossible 1.
Keep searching in the sub matrix.

The tricky part is the border of the matrix
http://bookshadow.com/weblog/2015/07/23/leetcode-search-2d-matrix-ii/

Time Complexity: O(mn)
Space complexity : O(min(logm, logn))
"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        rowCount = len(matrix)
        colCount = len(matrix[0])
        return self.search(matrix, 0, rowCount - 1, 0, colCount - 1, target)

    def search(self, matrix, rowStart, rowEnd, colStart, colEnd, target):
        if rowStart == rowEnd and colStart == colEnd:
            return matrix[rowStart][colStart] == target

        if rowStart > rowEnd or colStart > colEnd:
            return False

        midRow = rowStart + (rowEnd - rowStart) // 2
        midCol = colStart + (colEnd - colStart) // 2

        if matrix[midRow][midCol] == target:
            return True
        elif matrix[midRow][midCol] > target:
            return self.search(matrix, rowStart, midRow - 1, colStart, midCol - 1, target) or self.search(matrix, midRow, rowEnd, colStart, midCol - 1, target) or self.search(matrix, rowStart, midRow - 1, midCol, colEnd, target)
        else:
            return self.search(matrix, midRow + 1, rowEnd, midCol + 1, colEnd, target) or self.search(matrix, rowStart, midRow, midCol + 1, colEnd, target) or self.search(matrix, midRow + 1, rowEnd, colStart, midCol, target)


"""
Solution 2:

Binary Search
Iterate over each row and do binary search against each row

Time Complexity: O(m*logn) Assume it's a m * n matrix
Space complexity : O(1)
"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        rowCount = len(matrix)
        for rowIndex in range(0, rowCount):
            if matrix[rowIndex][0] > target:
                break

            if self.binarySearch(matrix[rowIndex], target):
                return True

        return False

    def binarySearch(self, nums, target):
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid

        return nums[start] == target or nums[end] == target


"""
Solution 3:

Search Space Reduction

Time Complexity: O(m + n)
Space complexity : O(1)
"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        rowCount = len(matrix)
        colCount = len(matrix[0])
        # Start from bottom left corner since it's the biggest num in its column, the smallest num in it's row
        # We can compare the num with target to decide if we need to eliminate the row/column
        curRow, curCol = rowCount - 1, 0
        while curRow >= 0 and curCol < colCount:
            if matrix[curRow][curCol] == target:
                return True
            elif matrix[curRow][curCol] > target:
                curRow -= 1
            else:
                curCol += 1

        return False
