"""
[X] Solution 1: Binary Seach

Time Complexity: O(logn), worst case O(n) if all elements are identical
Space Complexity: O(1)

Note: The difference is we have duplicate in the arrary so we need to have
3 cases here:
Case 1. nums[mid] > nums[end]
Case 2. nums[mid] < nums[end]
Cas3 3. nums[mid] == nums[end]

Tricky part is case 3, in this case, we don't know if the section between
mid element and end element contains non descending subarrary or the subarray is descending 
and then ascending.

For example:
Array1 [3 3 1 3]
Array2 [1 3 3 3]
When mid index is 1, we can tell if we should search minimum element in the left part
or the right part cause nums[mid] == nums[end]. In this case, we can remove 1 duplicate by
reducing end by 1
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] > nums[end]:
                start = mid
            elif nums[mid] < nums[end]:
                end = mid
            else:
                end -= 1
                
        if nums[start] < nums[end]:
            return nums[start]

        return nums[end]