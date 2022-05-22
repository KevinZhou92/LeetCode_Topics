"""
Solution 1:

DFS without memorization

Time Complexity: O(2^n)
Space complexity : O(n)
"""


class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        return self.fib(n - 1) + self.fib(n - 2)


"""
Solution 2:

Bottom-Up Solution

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def fib(self, n: int) -> int:
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[i - 1] + fib[i - 2])

        return fib[n]


"""
Solution 2-2:


Time Complexity: O(n)
Space complexity : O(1)
"""


class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        first, second = [0, 1]
        for i in range(2, n + 1):
            first += second
            first, second = second, first

        return second
