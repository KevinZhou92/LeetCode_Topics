"""
Solution 1:
One Pass

Time Complexity: O(n)
Space complexity : O(1)
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        if len(nums) == 0:
            return 0
        
        count = 0
        for index in range(len(nums)):
            if index == 0 and nums[index] == 1:
                count = 1
            if index > 0:
                if nums[index - 1] == nums[index] and nums[index] == 1:
                    count += 1
                elif nums[index] == 1:
                    count = 1
            res = max(res, count)
            
        return res

"""
Solution 2:
One Pass

Time Complexity: O(n)
Space complexity : O(1)
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        if len(nums) == 0:
            return 0
        
        count = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                count = 0
            res = max(res, count)
            
        return res
        

"""
Solution 3:
Two Pointer

Time Complexity: O(n)
Space complexity : O(1)
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        if len(nums) == 0:
            return 0
        
        left, right = 0 , 0
        while right < len(nums):
            while left < len(nums) and nums[left] == 0:
                left += 1
            # The key step 1: reset right pointer whnever we found a starting one
            right = left
            while right < len(nums) and nums[right] == 1:
                right += 1
            res = max(res, right - left)
            # The key step 2: reset left pointer whnever we found an ending one
            left = right  
            
        return res