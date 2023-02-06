"""
Solution 1:

Sort and check

Note the edge case, if there is no third maximum, we need to return the maximum of the array

Time Complexity: O(nlogn)
Space complexity : O(n)
"""
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse=True)
        
        count = 1
        res = nums[0]
        maxNum = max(nums)
        for index in range(1, len(nums)):
            if nums[index] == nums[index - 1]:
                continue
            else:
                count += 1
                res = nums[index]
            
            if count == 3:
                break
            
        return res if count == 3 else maxNum         
        
"""
Solution 2:

Three Pointers

!We need to update second and third maximum if the first maximum changed

Time Complexity: O(n)
Space complexity : O(n)
"""
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        maxNum = max(nums)
        first = second = third = min(nums)
        
        for num in nums:
            if num > first:
                third = second
                second = first
                first = num
            
            if first > num and num > second:
                third = second
                second = num
                
            if second > num and num > third:
                third = num
                
        if first != second and second != third:
            return third
        else:
            return maxNum
        