"""
Solution 1:

Backtracking

Time Complexity: O(2^n)
Space complexity : O(n)
"""


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        if not candidates:
            return res

        candidates.sort()
        self.search(candidates, 0, target, [], res)

        return res

    def search(self, candidates, startIndex, remain, cur, res):
        if remain == 0:
            res.append(copy.copy(cur))
            return

        for index in range(startIndex, len(candidates)):
            if index > startIndex and candidates[index] == candidates[index - 1] or candidates[index] > remain:
                continue
            cur.append(candidates[index])
            self.search(candidates, index + 1, remain -
                        candidates[index], cur, res)
            cur.pop()
