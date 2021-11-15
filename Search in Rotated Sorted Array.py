"""
Solution 1:
Though the sorted array is rotated, but we can still find two sorted subarray from the original array.
Using regular binary search method, now we need to see if the left side of mid point is sorted or right side 
is sorted. Then we need to see if the target falls in the sorted range. We are kind of doing this recursively
to find out the solution. In each iteration, we will need to find out the sorted subpart in the array and
check to see if the target falls in that range. If so, we do a normal binary searh, otherwise we will keep
looking for such a scenario.
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[start] < nums[mid]:
                if target <= nums[mid] and target >= nums[start]:
                    end = mid
                else:
                    start = mid
            else:
                if target >= nums[mid] and target <= nums[end]:
                    start = mid
                else:
                    end = mid
            
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        
        return -1

"""
Solution 2:
"""