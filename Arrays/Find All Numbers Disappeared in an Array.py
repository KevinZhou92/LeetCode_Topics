"""
Solution 1:

Exchange Numbers

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


"""
Solution 2:

Negating Numbers

If a number between [1, n] show up, then we can mark index n - 1 as visited by negating the number at that index
In the end, we can find out indicies with values greater than 0, which means the corresponding number doesn't show up
in the array. 

Time Complexity: O(n)
Space complexity : O(n)
"""
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        for index in range(len(nums)):
            nextIndex = abs(nums[index]) - 1
            
            if nums[nextIndex] > 0:
                nums[nextIndex] *= -1
                    
        res = []
        for index, val in enumerate(nums):
            if val > 0:
                res.append(index + 1)
                
        return res
            
            