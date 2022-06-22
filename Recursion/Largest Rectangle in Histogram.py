"""
Solution 1:

Brute-Force 
For loop each possible range and calculate the area, find the maximum out of it.

TLE

Time Complexity: O(n^2)
Space complexity : O(2)
"""


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = float('-inf')
        if not heights:
            return 0

        for startIndex in range(len(heights)):
            minHeight = float('inf')
            for endIndex in range(startIndex, len(heights)):
                minHeight = min(minHeight, heights[endIndex])
                res = max(res, (endIndex - startIndex + 1) * minHeight)

        return res


"""
Solution 2:

Recursion
Divide and Conquer
3 cases to consider:
1. The widest possible rectangle with height equal to the height of the shortest bar.
2. The largest rectangle confined to the left of the shortest bar(subproblem).
3. The largest rectangle confined to the right of the shortest bar(subproblem).

Time Complexity: O(nlogn) worst case O(n^2)
Space complexity : O(n)
"""


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0

        return self.calculateArea(heights, 0, len(heights) - 1)

    def calculateArea(self, heights, start, end):
        if start > end:
            return 0

        if start == end:
            return heights[start]

        minIndex, minHeight = start, heights[start]
        for index in range(start, end + 1):
            if heights[index] < minHeight:
                minHeight = heights[index]
                minIndex = index

        return max(minHeight * (end - start + 1),
                   self.calculateArea(heights, start, minIndex - 1),
                   self.calculateArea(heights, minIndex + 1, end))
