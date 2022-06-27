"""
Solution 1:

Recursion
For each number, we either pick or not pick it, which in turn translates to two path


Time Complexity: O(N * 2^n)
Space complexity : O(n)
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # for each number, we either add or skip the number
        # once we reach the end of the arrary, we add current comb into res
        res = []
        if not nums:
            res.append([])
            return res

        self.search(nums, 0, [], res)

        return res

    def search(self, nums, startIndex, cur, res):
        if startIndex == len(nums):
            res.append(copy.copy(cur))
            return

        # path 1 pick current number
        cur.append(nums[startIndex])
        self.search(nums, startIndex + 1, cur, res)
        cur.pop()

        # path 2 skip current number
        self.search(nums, startIndex + 1, cur, res)


"""
Solution 1-2:

Recursion
For every number, we pick it and then do a recursion, after the recursion, we pop the number from
the path and do another recursion without the number

Time Complexity: O()
Space complexity : O()
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # for each number, we either add or skip the number
        # once we reach the end of the arrary, we add current comb into res
        res = []
        self.search(nums, 0, [], res)

        return res

    def search(self, nums, startIndex, cur, res):
        res.append(copy.copy(cur))

        for index in range(startIndex, len(nums)):
            cur.append(nums[index])
            self.search(nums, index + 1, cur, res)
            cur.pop()
