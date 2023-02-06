"""
Solution 1:

Brute Force

For every left pointer, count from left till the end of the array

Time Complexity: O(n^2)
Space complexity : O(n)
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        maxLength = 0
        right = 0
        for left in range(len(nums)):
            numOfZeros = 0
            for right in range(left, len(nums)):
                if numOfZeros == 2:
                    break
                    
                if nums[right] == 0:
                    numOfZeros += 1
                
                if numOfZeros < 2 :
                    maxLength = max(maxLength, right - left + 1)
                    
        return maxLength
            

"""
Solution 2:

Two Pointer

Use a sliding window to track a sequence and calculate the maximum leghth with only 1 zero in the sequence.

Time Complexity: O()
Space complexity : O()
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        maxLength = 0
        left, right = 0, 0
        numOfZeros = 0
        while right < len(nums):
            if nums[right] == 0:
                numOfZeros += 1
                
            if numOfZeros < 2:
                maxLength = max(maxLength, right - left + 1)
            
            while numOfZeros == 2:
                if nums[left] == 0:
                    numOfZeros -= 1
                left += 1
            right += 1
            
        return maxLength
            
            