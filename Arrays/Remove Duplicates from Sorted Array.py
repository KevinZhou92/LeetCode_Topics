"""
Solution 1:

Two Pointer

Time Complexity: O(n)
Space complexity : O(1)
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0 or not nums:
            return 0
        slow, fast = 0, 1
        while fast < len(nums):
            if nums[fast] != nums[fast - 1]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        
        return slow + 1