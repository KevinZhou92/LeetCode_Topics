"""
Solution 1:
Iterative Approach.
Note: A very important prerequisite here is we assume the element to the left of nums[0] is negative infinite.
And the element to the right of nums[len(nums) - 1] is negative infinite. So we can compare the mid element with 
the element next to it.
"""
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid + 1]:
                start = mid
            else:
                end = mid
        
        if nums[start] < nums[end]:
            return end
        
        return start

"""
Solution 2:
Recursive Approach.
Note: A very important prerequisite here is we assume the element to the left of nums[0] is negative infinite.
And the element to the right of nums[len(nums) - 1] is negative infinite. So we can compare the mid element with 
the element next to it.
"""
class Solution2:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        return self.binary_search(nums, 0, len(nums) - 1)

    def binary_search(self, nums, left, right):
        if left + 1 == right:
            return left if nums[left] > nums[right] else right
        
        mid = left + (right - left) // 2
        if nums[mid] < nums[mid + 1]:
            return self.binary_search(nums, mid, right)
        
        return self.binary_search(nums, left, mid)
                
        