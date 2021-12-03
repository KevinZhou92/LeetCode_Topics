"""
Solution 1:
Linear Approach.

Time Complexity: O(m + n), where m and n are lengths of two lists
Space complexity : O(m + n) in the worst case when all elements in the arrays are different.
"""
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        
        return nums1.intersection(nums2) if len(nums1) < len(nums2) else nums2.intersection(nums1)


"""
Solution 2:
Binary Search Approach.

Time Complexity: O(nlogn + mlogn), where m and n are lengths of two lists, while n is a smaller number
Space complexity : O(n) in the worst case when all elements in the arrays are different.
"""
class Solution2:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        small_array, big_array = nums1, nums2
        if len(nums1) > len(nums2):
            small_array, big_array = nums2, nums1
            
        small_array.sort()
        res = set()
        for num in big_array:
            if self.binary_search(small_array, num):
                res.add(num)
                
        return res
    
    def binary_search(self, nums, target):
        if target > nums[-1] or target < nums[0]:
            return False
        
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] < target:
                start = mid
            else:
                end = mid
                
        if nums[start] == target or nums[end] == target:
            return True
        
        return False

"""
Solution 3:
Two Pointer.

Time Complexity: O(nlogn + mlogm), where m and n are lengths of two lists, while n is a smaller number
Space complexity : O(n) in the worst case when all elements in the arrays are different.
"""
class Solution3:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        
        res = set()
        start1, start2 = 0, 0
        while start1 < len(nums1) and start2 < len(nums2):
            if nums1[start1] < nums2[start2]:
                start1 += 1
            elif nums1[start1] > nums2[start2]:
                start2 += 1
            else:
                if nums1[start1] not in res:
                    res.add(nums1[start1])
                start1 += 1
                start2 += 1
        
        return res
        