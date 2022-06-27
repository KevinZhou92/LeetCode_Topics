"""
Solution 1:


Time Complexity: O(n * 2 ^n)
Space complexity : O()
"""
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        # now we have duplicate, for example, 1, 1 ,2
        # we should have [1],[1, 1] [1, 2], [2], we should not have two [1, 2]s
        nums.sort()
        self.search(nums, 0, [], res)

        return res
        
    def search(self, nums, startIndex, cur, res):
        res.append(copy.copy(cur))
        
        for index in range(startIndex, len(nums)):
            if index != startIndex and nums[index] == nums[index - 1]:
                continue
            cur.append(nums[index])
            self.search(nums, index + 1, cur, res)
            cur.pop()