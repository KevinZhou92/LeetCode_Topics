"""
Solution 1:
Linear Approach.

Time Complexity: min(O(m), O(n)), where m and n are lengths of two lists
"""
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        
        return nums1.intersection(nums2) if len(nums1) < len(nums2) else nums2.intersection(nums1)
        