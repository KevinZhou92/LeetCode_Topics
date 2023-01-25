"""
Solution 1:

Two pointers

Time Complexity: O(n)
Space complexity : O(n)
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # head to track the last non-zero elem, tail to point the cur elem
        if not nums:
            return
        
        head, tail = 0, 0
        while tail < len(nums):
            if nums[tail] != 0:
                nums[head], nums[tail] = nums[tail], nums[head]
                head += 1
            tail += 1
                
        return