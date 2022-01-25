"""
Solution 1:
Brute Force

Iterate to find all possible split sum combinations, and find out the minimum max value from those combinations.
For example:
[7, 2, 5, 10] and m = 2 will results in 3 combination sums
[7, 17], [9, 14], [14, 10], the minimum max sub array sum out of these three combinations is 14

Time Complexity: 
Space complexity : 


Problem: TLE
"""


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        res = float('inf')
        for combination_sum in self.search(nums, 0, m):
            res = min(max(combination_sum), res)

        return res

    def search(self, nums, start_index, required_sum_count):
        if required_sum_count == 1:
            return [[sum(nums[start_index:])]]

        combination_sums = []
        current_sum = 0
        for i in range(start_index, len(nums)):
            if len(nums) - i < required_sum_count:
                continue
            current_sum += nums[i]
            for combination_sum in self.search(nums, i + 1, required_sum_count - 1):
                combination_sums.append(combination_sum + [current_sum])

        return combination_sums


"""
Solution 1 - 1:
Brute Force + Memorization

Iterate to find all possible split sum combinations, and find out the minimum max value from those combinations.
For example:
[7, 2, 5, 10] and m = 2 will results in 3 combination sums
[7, 17], [9, 14], [14, 10], the minimum max sub array sum out of these three combinations is 14

Add a map to cache the result that has been calculated already

Time Complexity: 
Space complexity : 


Problem: MLE
"""


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        res = float('inf')
        for combination_sum in self.search(nums, 0, m):
            res = min(max(combination_sum), res)

        return res

    def search(self, nums, start_index, required_sum_count):
        if required_sum_count == 1:
            return [[sum(nums[start_index:])]]

        combination_sums = []
        current_sum = 0
        for i in range(start_index, len(nums)):
            if len(nums) - i < required_sum_count:
                continue
            current_sum += nums[i]
            for combination_sum in self.search(nums, i + 1, required_sum_count - 1):
                combination_sums.append(combination_sum + [current_sum])

        return combination_sums
