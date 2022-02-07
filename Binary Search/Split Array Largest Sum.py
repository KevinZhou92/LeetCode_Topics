"""
https://leetcode.com/problems/split-array-largest-sum/solution/
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
Solution 1 - 2:
Prefix + DFS Memorization + Prune

Calculate a prefix sum array and then dfs the array to calculate for given [Start_Index, Remaining_Splits],
what is the minimum maximum value in that subarray.


Time Complexity: Each state is defined by the values currIndex and subarrayCount. 
As such, there are N⋅M possible states, and we must visit almost every state in order to solve the original problem. 
Each state (subproblem) requires O(N) time because we have a for loop from currIndex to N - subarrayCount. 
Thus the total time complexity is equal to O(N^2 * M)
 ⋅M).
Space complexity : O(M * N) because we need to create a memorization matrix

"""


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        prefix_sums = [0] * (len(nums) + 1)
        for i in range(len(nums) + 1):
            prefix_sums[i] = prefix_sums[i - 1] + nums[i - 1]

        return self.search(nums, 0, prefix_sums, m - 1, {})

    def search(self, nums, start_index, prefix_sums, remaining_splits, mems):
        if (start_index, remaining_splits) in mems:
            return mems[(start_index, remaining_splits)]

        if remaining_splits == 0:
            return prefix_sums[-1] - prefix_sums[start_index]

        res = float('inf')
        for i in range(start_index, len(nums)):
            current_sum = prefix_sums[i + 1] - prefix_sums[start_index]
            res = min(res, max(current_sum, self.search(
                nums, i + 1, prefix_sums, remaining_splits - 1, mems)))
            if current_sum > res:
                break

        mems[(start_index, remaining_splits)] = res

        return res


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
            if self.possible(guess, nums, m - 1):
                end = guess
            else:
                start = guess

        if self.possible(start, nums, m - 1):
            return start

        return end

    def possible(self, guess, nums, remaining_splits):
        current_sum = 0
        for num in nums:
            if num + current_sum <= guess:
                current_sum += num
            else:
                current_sum = num
                remaining_splits -= 1

            if current_sum > guess:
                return False

        return remaining_splits >= 0


"""
Solution 3:
DP
https://leetcode-cn.com/problems/split-array-largest-sum/solution/er-fen-cha-zhao-he-dong-tai-gui-hua-jie-fa-by-anti/

Need to find the state transfer function. How to convert from small state to bigger state

Time Complexity: O(nm^2)`
Space complexity : O(nm)

"""


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        prefix_sums = [0]
        for num in nums:
            prefix_sums.append(prefix_sums[-1] + num)

        dp = [[float('inf')] * (m + 1) for _ in range(len(nums) + 1)]
        dp[0][0] = 0
        for i in range(1, len(nums) + 1):
            dp[i][1] = prefix_sums[i]
            for subarray_cnt in range(2, min(i, m) + 1):
                for j in range(i):
                    dp[i][subarray_cnt] = min(dp[i][subarray_cnt], max(
                        dp[j][subarray_cnt - 1], prefix_sums[i] - prefix_sums[j]))

        return dp[len(nums)][m]
