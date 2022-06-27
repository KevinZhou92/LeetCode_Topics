"""
Solution 1:

Backtracking
backtracking is a general algorithm for finding all (or some) solutions to some computational problems. 
The idea is that it incrementally builds candidates to the solutions, and abandons a candidate ("backtrack") as soon as it determines that this candidate cannot lead to a final solution.

!We don't add the precedent numbers into the current node, since they would have been explored in the nodes in the left part of the subtree

Time Complexity: O()
Space complexity : O()
"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # iterate over the array, keep tracking of the sum
        # if sum is over target, prune
        # if sum is equal to target, add it to the res and return
        res = []
        if not candidates:
            return res

        # candidates, startIndex, target, cur, res
        self.search(candidates, 0, target, [], res)
        return res

    def search(self, candidates, startIndex, remain, cur, res):
        if remain == 0:
            res.append(copy.copy(cur))

        for index in range(startIndex, len(candidates)):
            if candidates[index] > remain:
                continue
            remain -= candidates[index]
            cur.append(candidates[index])
            self.search(candidates, index, remain, cur, res)
            cur.pop()
            remain += candidates[index]
