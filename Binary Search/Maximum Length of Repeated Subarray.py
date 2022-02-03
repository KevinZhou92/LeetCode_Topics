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

"""
Solution 2:
DFS + Memorization

!!!Notice here we are looking for contiguous subarray, not for disconnect sequence.

So for index1, index2, the sub problem is what is the Maximum Length of Repeated Subarray in subarray
nums1[index1:] and nums2[index2:], if nums1[index1] == nums2[index2], then the result is 1 + output
from sub problem nums1[index1 + 1:] and nums2[index2 + 2:], else we just return 0, which means it is not 
possible to extend the same subarray at index1, index2, so we return to the caller stack.

Time Complexity: O()
Space complexity : O()
"""
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        if not nums1 or not nums2:
            return 0
            
        res = 0
        mems = [[-1] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        for index1 in range(len(nums1)):
            for index2 in range(len(nums2)):
                if len(nums1) - index1 + 1 < res or len(nums2) - index2 + 1 < res:
                    continue
                res = max(res, self.search(nums1, nums2, index1, index2, mems))
                
        return res
    
    def search(self, nums1, nums2, index1, index2, mems):   
        if mems[index1][index2] != -1:
            return mems[index1][index2]
        
        if index1 == len(nums1) or index2 == len(nums2):
            mems[index1][index2] = 0
            return 0
            
        if nums1[index1] == nums2[index2]:
            mems[index1][index2] = self.search(nums1, nums2, index1 + 1, index2 + 1, mems) + 1
            return mems[index1][index2]
        
        mems[index1][index2] = 0
        return 0
