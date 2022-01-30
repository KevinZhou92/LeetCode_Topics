"""
Solution 1:
Binary Search

Time Complexity: O(log(n*m)) for binary search, while n is the length of row, m is the length of column
Space complexity : O(1)
"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_count = len(matrix)
        col_count = len(matrix[0])

        start, end = 0, row_count * col_count - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            mid_val = self.get_val_from_matrix(mid, matrix)
            if mid_val <= target:
                start = mid
            else:
                end = mid

        if self.get_val_from_matrix(end, matrix) == target:
            return True

        if self.get_val_from_matrix(start, matrix) == target:
            return True

        return False

    def get_val_from_matrix(self, combined_index, matrix):
        row_index = combined_index // len(matrix[0])
        col_index = combined_index % len(matrix[0])

        return matrix[row_index][col_index]


"""
Solution 2:


Time Complexity: O(m + n)
Space complexity : O(1)
"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_count = len(matrix)
        col_count = len(matrix[0])

        row_index, col_index = 0, 0
        while row_index < row_count - 1:
            if matrix[row_index][-1] < target:
                row_index += 1
            else:
                break

        while col_index < col_count - 1:
            if matrix[row_index][col_index] < target:
                col_index += 1
            else:
                break

        return matrix[row_index][col_index] == target
