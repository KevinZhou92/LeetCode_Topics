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
Try to convert the problem to a regular binary search, we just need to figure out the offset each element is being moved
Then we can convert the index we caculated during binary search to be a index in the ascending array
Then we can treat this problem as a regular binary search
"""
class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        
        # This is also implicitly the offset of how many steps the array rotated
        min_num_index = self.get_min_num_index(nums)
        while start + 1 < end:
            mid = start + (end - start) // 2
            origin_mid = nums[(mid + min_num_index) % len(nums)]
            if origin_mid < target:
                start = mid
            elif origin_mid == target:
                return (mid + min_num_index) % len(nums)
            else:
                end = mid
        
        if nums[(start + min_num_index) % len(nums)] == target:
            return (start + min_num_index) % len(nums)
        
        if nums[(end + min_num_index) % len(nums)] == target:
            return (end + min_num_index) % len(nums)
        
        return -1
        
    
    def get_min_num_index(self, nums):
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            # edge case, what is array is ascending order, we need to find out the unsorted part
            # we cannot use if nums[mid] > nums[start]:, since the arrary might not be rotated
            # 
            # More explanation: originally, the array is not rotated and we have nums[mid] > nums[start]
            # It would be impossible to simply set start = mid if nums[mid] > nums[start] since it's the 
            # same case no matter the array is rotated or not
            # But if nums[mid] > nums[end], then we must know right side of mid is unordered
            if nums[mid] > nums[end]:
                start = mid
            else:
                end = mid
            
        if nums[start] > nums[end]:
            return end

        return start
        