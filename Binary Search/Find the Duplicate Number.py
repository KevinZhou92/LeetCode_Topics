"""
Solution 1:
Iterative Approach.

Sort the array first and check if there are consecutive elements that are identical. But this approach requires us
to modify the array.

Time Complexity: O(nlogn)
Space Complexity: O(1) 
O(logn) for sort
"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()

        for index in range(len(nums)):
            if index > 0 and nums[index - 1] == nums[index]:
                return nums[index]

        return -1


"""
Solution 2:
Set Approach.

Use a set to check if there is any duplicate

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        num_set = set()
        for num in nums:
            if num in num_set:
                return num
            num_set.add(num)

        return -1


"""
Solution 3:
Binary Search + Loop

Binary search between [1, n], for any number TARGET, if there is duplicate before this number, then if we loop
over the entire array and count for number that is less than or equal to TARGET,
we will find at least [target + 1] amount of numbers that are less than or equal to TARGET

Time Complexity: O(nlogn)
Space Complexity: O(1)
"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        max_num = len(nums) - 1
        start, end = 1, max_num

        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.contains_duplicate(mid, nums):
                end = mid
            else:
                start = mid

        if self.contains_duplicate(start, nums):
            return start

        return end

    def contains_duplicate(self, target, nums):
        return len([num for num in nums if num <= target]) > target


"""
Solution 4:
Exchange Numbers

Start from index 0, move every number to the index [number - 1], since we have n + 1 numbers and the range
of numbers is in [1, n], after we put the first occurence of the duplicate in the correct place, we will find
that the number is already in place when we encounter the second occurence of the duplicate

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        index = 0
        while True:
            while nums[index] - 1 != index:
                target_index = nums[index] - 1
                if target_index != index and nums[target_index] == nums[index]:
                    return nums[index]
                nums[index], nums[target_index] = nums[target_index], nums[index]
            index += 1

        return -1


"""
Solution 5:
Negative Numbers

There are n + 1n+1 positive numbers in the array (numsnums) (all in the range [1, n][1,n]). 
Since the array only contains positive integers, we can track each number (numnum)
that has been seen before by flipping the sign of the number located at index |num|∣num∣, 
where ||∣∣ denotes absolute value.

For example, if the input array is [1, 3, 3, 2][1,3,3,2], then for 11, flip the number at index 11, 
making the array [1,-3,3,2][1,−3,3,2]. Next, for -3−3 flip the number at index 33, 
making the array [1,-3,3,-2][1,−3,3,−2]. Finally, when we reach the second 33, 
we'll notice that nums[3]nums[3] is already negative, indicating that 3
 has been seen before and hence is the duplicate number.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            cur = num
            if nums[cur] < 0:
                break
            nums[cur] = - nums[cur]

        for index in range(len(nums)):
            nums[index] = abs(nums[index])

        return cur


"""
Solution 6:
Sum of Set Bits

Check https://leetcode.com/problems/find-the-duplicate-number/solution/

Time Complexity: O(nlogn)
Space Complexity: O(1)
"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        bit_length = n.bit_length()
        duplicate = 0
        for offset in range(bit_length):
            mask = 1 << offset
            base_cnt = 0
            num_cnt = 0
            for i in range(n):
                if i & mask:
                    base_cnt += 1

                if nums[i] & mask:
                    num_cnt += 1

            if num_cnt - base_cnt > 0:
                duplicate |= mask

        return duplicate


"""
Solution 7:
Floyd's Tortoise and Hare (Cycle Detection)

Check https://leetcode.com/problems/find-the-duplicate-number/solution/

Need to understand the logic behind cycle detection
Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        slow = 0
        while nums[slow] != nums[fast]:
            slow = nums[slow]
            fast = nums[fast]

        return nums[slow]
