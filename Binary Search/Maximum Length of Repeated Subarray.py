"""
Solution 1:
Brute Force

Time Complexity: O(m * n * m), where m and n are length of two arrays and m is the smaller length
Space complexity : O(1)
"""


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1

        res = 0
        for index1, num1 in enumerate(nums1):
            for index2, num2 in enumerate(nums2):
                if num1 == num2:
                    res = max(res, self.search_subarray(
                        nums1, nums2, index1, index2))

        return res

    def search_subarray(self, nums1, nums2, index1, index2):
        count = 0
        while index1 < len(nums1) and index2 < len(nums2) and nums1[index1] == nums2[index2]:
            index1 += 1
            index2 += 1
            count += 1

        return count
