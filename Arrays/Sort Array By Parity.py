"""
Solution 1:

Two pointer

Time Complexity: O(n)
Space complexity : O(1)
"""
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        
        head, tail = 0, len(nums) - 1
        while head < tail:
            if nums[head] % 2 == 0:
                head += 1
            else:
                nums[head], nums[tail] = nums[tail], nums[head]
                
            if nums[tail] % 2 != 0:
                tail -= 1
            else:
                nums[head], nums[tail] = nums[tail], nums[head]
        
        return nums