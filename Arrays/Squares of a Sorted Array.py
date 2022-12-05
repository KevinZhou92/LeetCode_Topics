"""
Solution 1:
Use the already sorted array, we just need to find the minimum element in the array with all absolute values.

Then the question is kind of a merge sort issue, we just pick smallest element from left and right array.

Time Complexity: O(n)
Space complexity : O(1)
"""
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        if len(nums) == 0:
            return res
        
        min_num, min_num_index = abs(nums[0]), 0
        for index, num in enumerate(nums):
            if abs(num) < min_num:
                min_num = abs(num)
                min_num_index = index
                
        left = min_num_index - 1
        right = min_num_index + 1
        res.append(min_num ** 2)
        while left >= 0 and right < len(nums):
            if abs(nums[left]) < abs(nums[right]):
                res.append(nums[left] ** 2)
                left -= 1
            else:
                res.append(nums[right] ** 2)
                right += 1
        
        while left >= 0:
            res.append(nums[left] ** 2)
            left -= 1
            
        while right < len(nums):
            res.append(nums[right] ** 2)
            right += 1
            
        return res
                