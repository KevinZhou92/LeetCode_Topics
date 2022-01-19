"""
Solution 1:
findMedian -> findKth
Since both arrayd are sorted, we can rule out k // 2 elements every iteration by comparing
A[A_Start + k // 2] and B[B_Start + k // 2]


Time Complexity: O(log(m + n)), where m and n are lengths of two lists
Space complexity : O(1) 
"""


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_len = len(nums1) + len(nums2)
        if total_len % 2 == 1:
            return self.findKthNum(nums1, 0, nums2, 0, total_len // 2 + 1)
        return (self.findKthNum(nums1, 0, nums2, 0, total_len // 2) + self.findKthNum(nums1, 0, nums2, 0, total_len // 2 + 1)) / 2

    def findKthNum(self, A, A_start, B, B_start, target):
        if len(A) == A_start:
            return B[B_start + target - 1]
        if len(B) == B_start:
            return A[A_start + target - 1]
        if target == 1:
            return min(A[A_start], B[B_start])

        A_mid = A[A_start + target // 2 -
                  1] if (A_start + target // 2 - 1) < len(A) else None
        B_mid = B[B_start + target // 2 -
                  1] if (B_start + target // 2 - 1) < len(B) else None

        if A_mid is None:
            return self.findKthNum(A, A_start, B, B_start + target // 2, target - target // 2)
        if B_mid is None:
            return self.findKthNum(A, A_start + target // 2, B, B_start, target - target // 2)

        if A_mid < B_mid:
            return self.findKthNum(A, A_start + target // 2, B, B_start, target - target // 2)
        else:
            return self.findKthNum(A, A_start, B, B_start + target // 2, target - target // 2)


"""
Solution 2:
Binary Search

Time Complexity: O(min(log(m) + log(n))), where m and n are lengths of two lists
Space complexity : O(1) 
"""


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        total_len = len(nums1) + len(nums2)
        l, r = 0, len(nums1)
        while l <= r:
            partition_1 = l + (r - l) // 2
            partition_2 = (total_len + 1) // 2 - partition_1
            if partition_1 == 0:
                nums1_left_max = float('-inf')
            else:
                nums1_left_max = nums1[partition_1 - 1]

            if partition_1 == len(nums1):
                nums1_right_min = float('inf')
            else:
                nums1_right_min = nums1[partition_1]

            if partition_2 == 0:
                nums2_left_max = float('-inf')
            else:
                nums2_left_max = nums2[partition_2 - 1]

            if partition_2 == len(nums2):
                nums2_right_min = float('inf')
            else:
                nums2_right_min = nums2[partition_2]

            if max(nums1_left_max, nums2_left_max) <= min(nums1_right_min, nums2_right_min):
                if total_len % 2 == 1:
                    return max(nums1_left_max, nums2_left_max)
                return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2
            elif nums1_left_max > nums2_left_max:
                r = partition_1 - 1
            else:
                l = partition_1 + 1

        return 0
