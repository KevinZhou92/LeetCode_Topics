"""
Solution 1:

DFS

Time Complexity: O(logn)
Space complexity : O(logn)
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.myPow(x, -n)

        if n == 0:
            return 1

        res = self.myPow(x, n // 2)
        if n % 2 == 0:
            return res * res
        else:
            return res * res * x


"""
Solution 2:

Iterative
https://leetcode.cn/problems/powx-n/solution/powx-n-by-leetcode-solution/

Time Complexity: O(logn)
Space complexity : O(1)
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.myPow(x, -n)

        if n == 0:
            return 1

        res = 1
        currentProduct = x
        while n > 0:
            if n % 2 == 1:
                res *= currentProduct
            currentProduct *= currentProduct
            n //= 2

        return res
