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


"""
Solution 3:
https://leetcode.com/problems/largest-rectangle-in-histogram/solution/

Be careful with edge cases

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        if not heights:
            return res

        # index, value
        # monolithic stack(increasing order)
        # we need to know the left limit and right limit for a bar
        stack = [(-1, -1)]
        for index, height in enumerate(heights):
            # keep pushing if the stack is increasing
            # if the cur height is smaller or equal to the top of the stack
            # we known the right limit for all previous bars is the cur index
            # we should calculate all values for previous bars
            while stack[-1][1] >= height:
                barIndex, barHeight = stack.pop()
                leftIndex = stack[-1][0]
                res = max(res, barHeight * (index - leftIndex - 1))
            stack.append((index, height))

        # if the height of bar keeps increasing, we need to calculate the remaining bars
        # in the stack
        # the right limit will always be the length of the height array
        while stack[-1][1] >= 0:
            barIndex, barHeight = stack.pop()
            leftIndex = stack[-1][0]
            res = max(res, barHeight * (len(heights) - leftIndex - 1))

        return res
