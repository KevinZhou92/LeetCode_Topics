"""
Solution 1:

Recursion
https://leetcode.com/problems/combinations/solution/

Time Complexity: O(https://leetcode.com/problems/combinations/solution/)
Space complexity : O(https://leetcode.com/problems/combinations/solution/)
"""


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 0 or n == 0:
            return []

        # start from 1, add each number to list and back track,
        # add entire list when there is k elements in the list and return
        self.res = []
        self.search(n, 1, k, [])
        return self.res

    def search(self, n, startNum, totalCount, res):
        if len(res) == totalCount:
            self.res.append(copy.copy(res))
            return

        for candidate in range(startNum, n + 1):
            res.append(candidate)
            self.search(n, candidate + 1, totalCount, res)
            res.pop()
