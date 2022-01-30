"""
Solution 1:
Binary Search

Time Complexity: O(logn) for binary search
Space complexity : O(1)
"""


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid

        if nums[start] >= target:
            return 0

        if nums[end] < target:
            return end + 1

        return end
