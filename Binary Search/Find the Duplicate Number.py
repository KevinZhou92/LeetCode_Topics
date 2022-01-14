"""
Solution 1:
Iterative Approach.

Sort the array first and check if there are consecutive elements that are identical. But this approach requires us
to modify the array.

Time Complexity: O(nlogn)
Space Complexity: O(1)
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        
        for index in range(len(nums)):
            if index > 0 and nums[index - 1] == nums[index]:
                return nums[index]
        
        return -1


"""
Solution 2:
Binary Search + Loop

Binary search between [1, n], for any number TARGET, if there is duplicate before this number, then if we loop
over the entire array and count for number that is less than or equal to TARGET,
we will find at least [target + 1] amount of numbers that are less than or equal to TARGET

Time Complexity: O(nlogn)
Space Complexity: O(1)
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        max_num = len(nums) - 1
        start, end = 1, max_num
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.contains_duplicate(mid, nums):
                end = mid
            else: 
                start = mid
            
        if self.contains_duplicate(start, nums):
            return start
        
        return end
    
    def contains_duplicate(self, target, nums):
        return len([num for num in nums if num <= target]) > target

"""
Solution 3:
Exchange Numbers

Start from index 0, move every number to the index [number - 1], since we have n + 1 numbers and the range
of numbers is in [1, n], after we put the first occurence of the duplicate in the correct place, we will find
that the number is already in place when we encounter the second occurence of the duplicate

Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        index = 0
        while True:
            while nums[index] - 1 != index:
                target_index = nums[index] - 1
                if target_index != index and nums[target_index] == nums[index]:
                    return nums[index]
                nums[index], nums[target_index] = nums[target_index], nums[index]
            index += 1
                
        return -1