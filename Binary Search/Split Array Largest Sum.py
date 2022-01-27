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
        for combination_sum in self.search(nums, 0, m, {}):
            res = min(max(combination_sum), res)

        return res

    def search(self, nums, start_index, required_sum_count, mems):
        if required_sum_count == 1:
            return [[sum(nums[start_index:])]]

        if (start_index, required_sum_count) in mems:
            return mems[(start_index, required_sum_count)]

        combination_sums = []
        current_sum = 0
        for i in range(start_index, len(nums)):
            if len(nums) - i < required_sum_count:
                continue
            current_sum += nums[i]
            for combination_sum in self.search(nums, i + 1, required_sum_count - 1, mems):
                combination_sums.append(combination_sum + [current_sum])
        mems[(start_index, required_sum_count)] = combination_sums

        return combination_sums


"""
Solution 2:
Binary Search + Loop(First hard question solved by myself!)

Using Binary Search to find the minimum largest sum. The start would be 0 and end would be the sum of the array
since the largest sum is the sum of the array itself.

For every possible guess, we will iterate through the array and check if we can find such a split that each subarray
of the array has a sum that is less than the guessed sum.


Time Complexity: O(nlgW), where W is the sum of the array and n is the legth of the array
Space complexity : O(1)

"""


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        start, end = 0, sum(nums)
        while start + 1 < end:
            guess = start + (end - start) // 2
            if self.possible(guess, nums, m):
                end = guess
            else:
                start = guess

        if self.possible(start, nums, m):
            return start

        return end

    def possible(self, guess, nums, required_count):
        tmp_sum, index = 0, 0
        while index < len(nums):
            if nums[index] + tmp_sum <= guess:
                tmp_sum += nums[index]
            else:
                tmp_sum = nums[index]
                required_count -= 1
            index += 1

            if tmp_sum > guess:
                return False

            if required_count == 1:
                return sum(nums[index - 1:]) <= guess

        return True
