"""
Solution 1:
Brute-Force
Generate All possible results and find kth smallest distance

Time Complexity: O(n^2), where m and n are lengths of two lists
Space complexity : O(n^2)
"""


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        distances = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                distances.append(abs(nums[i] - nums[j]))
        distances.sort()
        return distances[k - 1]


"""
Solution 2:
Brute-Force 2
Generate All possible results and generate 

Time Complexity: O(n^2), where m and n are lengths of two lists
Space complexity : O(n^2)
"""


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        diff_buckets = {}
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                diff_buckets[abs(
                    nums[i] - nums[j])] = diff_buckets.get(abs(nums[i] - nums[j]), 0) + 1

        print(diff_buckets)
        for i in range(nums[-1] - nums[0] + 1):
            k -= diff_buckets.get(i, 0)
            print(k)
            if k <= 0:
                return i
        return 0


"""
Solution 3:
Sort + Sliding Window
Generate All possible results and generate 

Time Complexity: O(nlogn + n logw), where n is the length of the array and w is the max difference between two elements
Space complexity : O(1) for sorting


We will use a sliding window approach to count the number of pairs with distance <= guess.
For every possible right, we maintain the loop invariant: left is the smallest value such that nums[right] - nums[left] <= guess. 
Then, the number of pairs with right as it's right-most endpoint is right - left, and we add all of these up.


"""


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        start, end = 0, nums[-1] - nums[0]
        print(nums)
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.hasKDistances(mid, k, nums):
                end = mid
            else:
                start = mid

        if self.hasKDistances(start, k, nums):
            return start

        if self.hasKDistances(end, k, nums):
            return end

        return 0

    def hasKDistances(self, target, k, nums):
        l, r = 0, 1
        count = 0
        while l < len(nums):
            while r < len(nums) and nums[r] - nums[l] <= target:
                r += 1
            count += (r - l - 1)
            l += 1

        return count >= k


"""
Solution 3 - 1:
Sort + Sliding Window(Variation)
Generate All possible results and generate 

Time Complexity: O(nlogn), where m and n are lengths of two lists
Space complexity : O(1) for sorting
"""


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        start, end = 0, nums[-1] - nums[0]
        print(nums)
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.hasKDistances(mid, k, nums):
                end = mid
            else:
                start = mid

        if self.hasKDistances(start, k, nums):
            return start

        if self.hasKDistances(end, k, nums):
            return end

        return 0

    def hasKDistances(self, target, k, nums):
        r, count = 0, 0
        for l in range(len(nums)):
            while r < len(nums) and nums[r] - nums[l] <= target:
                r += 1
            count += r - l - 1
        return count >= k
