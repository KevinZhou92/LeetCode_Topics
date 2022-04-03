"""
Solution 1:

DFS + Memorization(Top Down Search) Can iterate from this approach to develop a dp solution

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return n

        memo = {}

        return self.countTrees(1, n, memo)

    def countTrees(self, start, end, memo):
        if start >= end:
            return 1

        if (start, end) in memo:
            return memo[(start, end)]

        res = 0
        for rootVal in range(start, end + 1):
            left = self.countTrees(start, rootVal - 1, memo)
            right = self.countTrees(rootVal + 1, end, memo)
            res += left * right

        memo[(start, end)] = res

        return res
