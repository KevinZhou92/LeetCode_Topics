"""
Solution 1:

Three pointers, start from the back since the back of nums1 is 0 and it's ok to override them.


Time Complexity: O(m + n)
Space complexity : O(1)
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        res = []
        index1, index2 = len(nums1) - len(nums2) - 1, len(nums2) - 1
        curIndex = len(nums1) - 1
        while index1 >= 0 and index2 >= 0:
            if nums1[index1] < nums2[index2]:
                nums1[curIndex] = nums2[index2]
                index2 -= 1
            else:
                nums1[curIndex] = nums1[index1]
                index1 -= 1
            curIndex -= 1
                
        while index1 >= 0:
            nums1[curIndex] = nums1[index1]
            index1 -= 1
            curIndex -= 1
        
        while index2 >= 0:
            nums1[curIndex] = nums2[index2]
            index2 -= 1
            curIndex -= 1
            

        
            