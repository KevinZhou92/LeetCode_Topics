"""
Solution 1:
Linear Approach.

Note: We can create only 1 hashmap against the smaller array, and iterate bigger array, find occurence,
and decrement count in hash map.
https://leetcode.com/problems/intersection-of-two-arrays-ii/solution/


Time Complexity: O(m + n), where m and n are lengths of two lists
Space complexity : O(m + n) in the worst case when all elements in the arrays are different.
"""
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1_freq = self.get_num_freq(nums1)
        num2_freq = self.get_num_freq(nums2)
        
        search_dict = num1_freq if len(num1_freq) < len(num2_freq) else num2_freq
        target_dict = num2_freq if len(num1_freq) < len(num2_freq) else num1_freq
        res = []
        for num, freq in search_dict.items():
            if num not in target_dict:
                continue
            res += min(freq, target_dict.get(num)) * [num]
            
        return res  
    
    def get_num_freq(self, nums):
        freq = {}
        for num in nums: 
            freq[num] = freq.get(num, 0) + 1

        return freq

"""
Solution 2:
Binary Search Approach.

Note: A little variation, since we allow duplication here, so we need to somehow mask the element we've already
searched, so we will return as many times as the element appears in both arrays.

Time Complexity: O(nlogn + mlogn), where m and n are lengths of two lists, while n is a smaller number
Space complexity : O(n) in the worst case when all elements in the arrays are different.
"""
class Solution2:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        small_array, big_array = nums1, nums2
        if len(nums1) > len(nums2):
            small_array, big_array = nums2, nums1
            
        small_array.sort()
        big_array.sort()
        res = []
        for num in big_array:
            if self.binary_search(small_array, num):
                res.append(num)
                
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
                
        if nums[start] == target:
            nums[start] = -1
            return True
        
        if nums[end] == target:
            nums[end] = -1
            return True
        
        return False

"""
Solution 3:
Two Pointer.

Time Complexity: O(nlogn + mlogm), where m and n are lengths of two lists, while n is a smaller number
Space complexity : O(n) in the worst case when all elements in the arrays are different.
"""
class Solution3:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        
        res = []
        start1, start2 = 0, 0
        while start1 < len(nums1) and start2 < len(nums2):
            if nums1[start1] < nums2[start2]:
                start1 += 1
            elif nums1[start1] > nums2[start2]:
                start2 += 1
            else:
                res += [nums1[start1]]
                start1 += 1
                start2 += 1
        
        return res

"""
Solution 3 Optimization:

Use the compared area of one of the arrays to store our result to save memory
"""
class Solution3_1:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        
        res = []
        start1, start2 = 0, 0
        tail = 0
        while start1 < len(nums1) and start2 < len(nums2):
            if nums1[start1] < nums2[start2]:
                start1 += 1
            elif nums1[start1] > nums2[start2]:
                start2 += 1
            else:
                nums1[tail] = nums1[start1]
                tail += 1
                start1 += 1
                start2 += 1
        
        return nums[:tail]
        