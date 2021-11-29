"""
Solution 1:
Two Sub Problems:
1. Find fisrt occurence of target in sorted array
2. Find last occurence of target in sorted array

Note: Handle edge case, for example, when input array is empty
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        if len(nums) == 0:
            return res
        
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] >= target:
                end = mid
            else: 
                start = mid
                
        if nums[start] == target:
            res[0] = start
        elif nums[end] == target:
            res[0] = end
        
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] <= target:
                start = mid
            else: 
                end = mid
                
        if nums[end] == target:
            res[1] = end
        elif nums[start] == target:
            res[1] = start
            
        return res
        
        