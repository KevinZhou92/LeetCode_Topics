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

        self.res = []
        self.search(n, k, 1, 0, [])

        return self.res

    def search(self, n, k, startNum, count, curList):
        if count == k:
            self.res.append(copy.copy(curList))
            return

        for num in range(startNum, n + 1):
            curList.append(num)
            self.search(n, k, num + 1, count + 1, curList)
            curList.pop()
