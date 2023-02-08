"""
Solution 1:


Time Complexity: O(n)
Space complexity : O(n)
"""
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        targetValue = None
        for index in range(len(nums)):
            while targetValue != nums[index] or nums[index] != index + 1:
                targetIndex = nums[index] - 1
                targetValue = nums[targetIndex]
                if targetValue == nums[index]:
                    break
                nums[index], nums[targetIndex] = targetValue, nums[index]
                
                
        res = []
        for index, val in enumerate(nums):
            if index + 1 != val:
                res.append(index + 1)
                
        return res
            