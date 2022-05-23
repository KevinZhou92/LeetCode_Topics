"""
Solution 1:

DFS Brute-Force

TLE

Time Complexity: O(n^2)
Space complexity : O(n)
"""


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 0:
            return 0

        comb = self.getCombinations(n)

        return comb[k - 1]

    def getCombinations(self, n):
        if n == 1:
            return '0'

        subRes = self.getCombinations(n - 1)
        res = ''
        for char in subRes:
            if char == '0':
                res += '01'
            if char == '1':
                res += '10'

        return res


"""
Solution 1-2:

DFS
Find pattern
https://www.cnblogs.com/grandyang/p/9027098.html


Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 0:
            return 0

        if k % 2 == 0:
            return 1 if self.kthGrammar(n - 1, k // 2) == 0 else 0
        else:
            return 0 if self.kthGrammar(n - 1, (k + 1) // 2) == 0 else 1
