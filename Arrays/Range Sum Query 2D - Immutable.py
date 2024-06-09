"""
Solution 1:

Build a 2d prefix array so we can get sum of range efficiently.

Here are two tricks, first is how to use existing information to calcualte area of (0, 0, row, col), it actually equals to
(0, 0, row - 1, col) + (0, 0, row, col -  1) - (0, 0, row - 1, col - 1) + matrix[row - 1][col - 1]

Second is how do we calculate area for (row1, col1, row2, col2) using pre_sum array, it actually equals to
(0, 0, row2 + 1, col2 + 1) - (0, 0, row2 + 1, col1) - (0, 0, row1, col2 + 1) + (0, 0, row1, col1)


The consistency of the index is very important. In this solution, we are using 1-based indexing so area(1, 1) represent the area covered by the top left cell.

Time Complexity: O(1)
Space complexity : O(mn)
"""
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        prefix_sum = [(len(matrix[0]) + 1) * [0] for _ in range(len(matrix) + 1)]
        for row in range(1, len(matrix) + 1):
            for col in range(1, len(matrix[0]) + 1):
                prefix_sum[row][col] = prefix_sum[row - 1][col] + prefix_sum[row][col - 1] + matrix[row- 1][col - 1] - prefix_sum[row - 1][col - 1]

        self.prefix_sum = prefix_sum 

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix_sum[row2 + 1][col2 + 1] - self.prefix_sum[row2 + 1][col1] - self.prefix_sum[row1][col2 + 1] + self.prefix_sum[row1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)