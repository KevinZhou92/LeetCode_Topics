"""
Solution 1:

Two Pointers

Start from both sides of the array, remove target from front and use the value from back side to fill the 
gap in front side.

Time Complexity: O(n)
Space complexity : O(1)
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        
        p1, p2 = 0, len(nums) - 1
        while p1 <= p2:
            while p1 <= p2 and  nums[p1] != val:
                p1 += 1
            while p1 <= p2 and nums[p2] == val:
                p2 -= 1
            if p1 > p2:
                break
            nums[p1], nums[p2] = nums[p2], nums[p1]
            
        return p1
                
            