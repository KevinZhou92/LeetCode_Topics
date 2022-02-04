"""
Solution 1:
Brute Force
https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/solution/zui-chang-zhong-fu-zi-shu-zu-by-leetcode-solution/

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
            mems[index1][index2] = self.search(
                nums1, nums2, index1 + 1, index2 + 1, mems) + 1
            return mems[index1][index2]

        mems[index1][index2] = 0
        return 0


"""
Solution 3:
Dynamic Programming
https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/solution/zhe-yao-jie-shi-ken-ding-jiu-dong-liao-by-hyj8/

https://segmentfault.com/a/1190000021665249
https://codeantenna.com/a/mVwlWwTdHO
https://www.cnblogs.com/r1-12king/p/15726654.html

Time Complexity: O(m*n)
Space complexity : O(m*n)
"""


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        if not nums1 or not nums2:
            return 0

        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]

        res = 0
        for index1 in range(1, len(nums1) + 1):
            for index2 in range(1, len(nums2) + 1):
                dp[index1][index2] = 1 + dp[index1 - 1][index2 -
                                                        1] if nums1[index1 - 1] == nums2[index2 - 1] else 0
                res = max(res, dp[index1][index2])

        return res


"""
Solution 3:
Dynamic Programming With Space Optimization

dp[i][j] only depends on dp[i - 1][j - 1], we can use a 1 dimension array to record the dp state 


Time Complexity: O()
Space complexity : O()
"""


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        if not nums1 or not nums2:
            return 0

        dp = [0] * (len(nums2) + 1)

        res = 0
        for index1 in range(1, len(nums1) + 1):
            for index2 in range(len(nums2), 0, -1):
                if nums1[index1 - 1] == nums2[index2 - 1]:
                    dp[index2] = dp[index2 - 1] + 1
                else:
                    dp[index2] = 0
                res = max(res, dp[index2])

        return res


"""
Solution 4:
Sliding Window
https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/solution/zui-chang-zhong-fu-zi-shu-zu-by-leetcode-solution/

This problem is to find the maximum length common subarray, which means there will be two subarray that are completely the same
They key idea of the sliding window here is to slide one array into another array, during the sliding period, there will be 
a position that the common subarray are aligned, and we will get the max length from it.

For example: B slides through A
A:           |1|2|3|4|
B: |5|1|2|3|6|2|
            ↓
A:       |1|2|3|4|
B: |5|1|2|3|6|2|

A:     |1|2|3|4|
B: |5|1|2|3|6|2|
            ↓
A:   |1|2|3|4|
B: |5|1|2|3|6|2|


Time Complexity: O(m + n) * O(min(m + n))
Space complexity : O(1)
"""


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        if not nums1 or not nums2:
            return 0

        res = 0
        for index in range(len(nums1)):
            res = max(res, self.search(nums1, index, nums2, 0))

        for index in range(len(nums2)):
            res = max(res, self.search(nums2, index, nums1, 0))

        return res

    def search(self, src_nums, src_index, target_nums, target_index):
        res = 0
        count = 0
        while src_index < len(src_nums) and target_index < len(target_nums):
            if src_nums[src_index] == target_nums[target_index]:
                count += 1
            else:
                count = 0
            res = max(res, count)
            src_index += 1
            target_index += 1

        return res


"""
Solution 5:
Binary Search + String Hash
https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/solution/zui-chang-zhong-fu-zi-shu-zu-by-leetcode-solution/

This method is very trick and useful. It can achieve O(m + n) for compare two strings

Time Complexity: O(m + n) * log(min(m, n))
Space complexity : O(m + n)
"""


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        if not nums1 or not nums2:
            return 0

        min_len, max_len = 0, min(len(nums1), len(nums2))

        while min_len + 1 < max_len:
            length = min_len + (max_len - min_len) // 2
            if self.possible_length(nums1, nums2, length):
                min_len = length
            else:
                max_len = length

        if self.possible_length(nums1, nums2, max_len):
            return max_len

        if self.possible_length(nums1, nums2, min_len):
            return min_len

        return 0

    def possible_length(self, nums1, nums2, length):
        base, mod = 31, 10 ** 12

        # Multiplier for the first element in array with length 'length'
        multi = 1
        for _ in range(length - 1):
            multi = (multi * base) % mod

        hash1_map = {}
        hash1 = 0
        # Hash for nums1
        for i in range(len(nums1)):
            if i < length:
                hash1 = (hash1 * base + nums1[i]) % mod
            else:
                hash1_map[hash1] = i - length
                hash1 = (
                    (hash1 - (multi * nums1[i - length]) % mod) * base + nums1[i]) % mod
        hash1_map[hash1] = len(nums1) - length

        hash2_map = {}
        hash2 = 0
        # Hash for nums2
        for i in range(len(nums2)):
            if i < length:
                hash2 = (hash2 * base + nums2[i]) % mod
            else:
                hash2_map[hash2] = i - length
                hash2 = (
                    (hash2 - (multi * nums2[i - length]) % mod) * base + nums2[i]) % mod
        hash2_map[hash2] = len(nums2) - length

        for key1 in hash1_map.keys():
            if key1 in hash2_map and self.verify(nums1, hash1_map[key1], nums2, hash2_map[key1], length):
                return True

        return False

    def verify(self, nums1, index1, nums2, index2, length):
        return nums1[index1: index1 + length] == nums2[index2: index2 + length]
