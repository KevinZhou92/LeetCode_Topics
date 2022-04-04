"""
Solution 1:

DFS + Memorization(Top Down Search) Can iterate from this approach to develop a dp solution


!!!Note!!!: 
Before Memoization.....
Runtime: O(N^N), because there are N branches and N depth. Think O(branches^depth)
Space: O(N), because the call stack will go only N high

After Memoization......
Runtime: O(N^2), because we calculate result for each value of N just once. And each calculation costs O(N) time.
Space: O(N), because of the call stack


Time Complexity: O(n^2)
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


"""
Solution 2:

Dynamic Programming
https://leetcode.com/problems/unique-binary-search-trees/solution/

Time Complexity: O(n^2)
Space complexity : O(n)
"""


class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return n

        dp = [0 for _ in range(n + 1)]
        dp[0], dp[1] = 1, 1

        for count in range(2, n + 1):
            for rootNode in range(1, count + 1):
                dp[count] += dp[rootNode - 1] * dp[count - rootNode]

        return dp[n]
