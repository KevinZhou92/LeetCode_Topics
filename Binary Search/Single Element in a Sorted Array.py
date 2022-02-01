"""
Solution 1:
Use a set.

Time Complexity: O(n)
Space complexity : O(n) the worst case
"""


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        nums_set = set()
        for num in nums:
            if num not in nums_set:
                nums_set.add(num)
            else:
                nums_set.remove(num)

        return nums_set.pop()
