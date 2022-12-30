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
                
"""

Notice that p2 is equal to the length of the arrary but not the index of the last
element in the array

This is because we are treating p2 as number of elements that are not equal to the target value
And it let us check if the element p1 points to equals to the target value

Example:
[3, 3]
p1, p2 = 0, 2

when p1 = 0, p2 = 1, we check that if elements at 0 is equal to target val, if so, decrease count by 1

"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        
        p1, p2 = 0, len(nums)
        while p1 < p2:
            if nums[p1] == val:
                nums[p1] = nums[p2 - 1]
                p2 -= 1
            else:
                p1 += 1

        return p2        