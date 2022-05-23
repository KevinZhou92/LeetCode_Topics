"""
Solution 1:

Merge Sort - Top Down

Time Complexity: O(nlogn)
Space complexity : O(n)
"""


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        return self.mergeSort(nums, 0, len(nums) - 1)

    def mergeSort(self, nums, start, end):
        if start == end:
            return [nums[start]]

        pivot = (start + end) // 2
        leftRes = self.mergeSort(nums, start, pivot)
        rightRes = self.mergeSort(nums, pivot + 1, end)

        return self.merge(leftRes, rightRes)

    def merge(self, leftRes, rightRes):
        res = []
        lIndex, rIndex = 0, 0
        while lIndex < len(leftRes) and rIndex < len(rightRes):
            if leftRes[lIndex] < rightRes[rIndex]:
                res.append(leftRes[lIndex])
                lIndex += 1
            else:
                res.append(rightRes[rIndex])
                rIndex += 1

        res.extend(leftRes[lIndex:])
        res.extend(rightRes[rIndex:])

        return res


"""
Solution 2:

Merge Sort - Bottom Up

Time Complexity: O(nlogn)
Space complexity : O(n)
"""


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums:
            return

        temp = [0 for _ in range(len(nums))]
        step = 1
        while step < len(nums):
            for start in range(0, len(nums), step * 2):
                start, mid, end = start, min(
                    start + step, len(nums)), min(start + 2 * step, len(nums))
                self.merge(nums, start, mid, end, temp)
            step *= 2

        return nums

    def merge(self, nums, start, mid, end, temp):
        left, right = start, mid
        index = left
        while left < mid and right < end:
            if nums[left] < nums[right]:
                temp[index] = nums[left]
                left += 1
            else:
                temp[index] = nums[right]
                right += 1
            index += 1

        while left < mid:
            temp[index] = nums[left]
            left += 1
            index += 1

        while right < end:
            temp[index] = nums[right]
            right += 1
            index += 1

        for index in range(start, end):
            nums[index] = temp[index]
