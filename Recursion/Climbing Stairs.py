"""
Solution 1:

DFS with Memorization

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        return self.climb(n, memo)

    def climb(self, n, memo):
        if n <= 2:
            return n

        if n in memo:
            return memo[n]

        res = self.climb(n - 1, memo) + self.climb(n - 2, memo)
        memo[n] = res

        return res


"""
Solution 2:

DP

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        dp = [0, 1, 2]
        for i in range(3, n + 1):
            dp.append(dp[i - 1] + dp[i - 2])

        return dp[n]
