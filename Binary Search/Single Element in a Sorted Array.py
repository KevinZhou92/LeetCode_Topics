"""
Solution 1:
Use a set.

Time Complexity: O(n)
Space complexity : O(n) the worst case
"""


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        nums_set = set()
        for num in nums:
            if num not in nums_set:
                nums_set.add(num)
            else:
                nums_set.remove(num)

        return nums_set.pop()


"""
Solution 2:
Binary Search

Time Complexity: O(log(n))
Space complexity : O(1)
"""


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if mid % 2 == 0:
                if nums[mid] == nums[mid + 1]:
                    start = mid
                else:
                    end = mid
            else:
                if nums[mid] == nums[mid - 1]:
                    start = mid
                else:
                    end = mid

        if start > 0 and nums[start] == nums[start - 1]:
            return nums[end]

        return nums[start]


"""
Solution 3:
https://bear-1111.medium.com/540-single-element-in-a-sorted-array-8d71d781d2df

Time Complexity: O(log(n))
Space complexity : O()
"""


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        start, end = 0, len(nums) // 2
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[2 * mid] != nums[2 * mid + 1]:
                end = mid
            else:
                start = mid

        if nums[2 * start] != nums[2 * start + 1]:
            return nums[2 * start]

        return nums[2 * end]
