"""
Solution 1:

A key insight to avoid generating any redundant permutation is that at each step rather than viewing each number as a candidate, 
we consider each unique number as the true candidate. For instance, at the very beginning, given in the input of [1, 1, 2], we have only two true candidates instead of three.

https://leetcode.com/problems/permutations-ii/solution/

Time Complexity: O()
Space complexity : O()
"""


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # since there is duplicate, as long as the number is place in
        # current position, we don't need to put the same number in the same position again
        res = []
        if not nums:
            return res

        nums.sort()
        visited = [0 for _ in range(len(nums))]
        self.search(nums, visited, [], res)

        return res

    def search(self, nums, visited, cur, res):
        if len(cur) == len(nums):
            res.append(copy.copy(cur))
            return

        for index in range(len(nums)):
            # we can't use duplicate num in same location
            # two case
            # 1. we use the same number from the parnet recursion, so we should not skip adding the number in
            # current situation
            # 2. current number is used, we shouldn't be duplicating it
            if index != 0 and nums[index] == nums[index - 1] and not visited[index - 1] or visited[index]:
                continue
            visited[index] = 1
            cur.append(nums[index])
            self.search(nums, visited, cur, res)
            cur.pop()
            visited[index] = 0
