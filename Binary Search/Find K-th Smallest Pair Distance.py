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


"""
Solution 3 - 2:
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
        l, count = 0, 0
        for r in range(len(nums)):
            while nums[r] - nums[l] > target:
                l += 1
            count += r - l
        return count >= k


"""
Solution 4:
Sort + Prefix(Variation)

Let prefix[v] be the number of points in nums less than or equal to v. Also, let multiplicity[j] be the number of points i with i < j and nums[i] == nums[j]. 
We can record both of these with a simple linear scan.

Iterate over the sorted array, for each element e, and for a specific distance value v, then we can caculate how many possible pairs
are there by prefix[min(e + v, max(nums))] - prefix[e] using element e as an anchor.
Note, in this piece of calculation, we are not counnt the pair between same elements since prefix[i] means the count of elements
smaller than value i, which will remove all duplicate for value i

Therefore, we would also need to consider if there is any duplicate in the array:
For example:
[1 1 1 2 3]
While we are at index 2 like below:
[1 1 1 2 3]
     ^
Then we need to count for pairs (1, 2) (1, 3) plus (1, 1), (1, 1). Since while we were at index 1, we only 
count for (1, 2) and (1, 3), not the (1, 1) for 1 at index 1 and index 2

Time Complexity: O(nlogn), where m and n are lengths of two lists
Space complexity : O(1) for sorting
"""


class Solution:
    def smallestDistancePair(self, nums, k):
        nums.sort()
        length = len(nums)
        max_val = max(nums)

        # Prefix record for a given index i, how many elements are smaller than i
        prefix = [0] * (max_val + 1)
        left = 0
        for i in range(0, max_val + 1):
            while left < length and nums[left] <= i:
                left += 1
            prefix[i] = left

        # Prefix record for a given index i, j, i < j, nums[i] == nums[j]
        multiplicity = [0] * len(nums)
        for i in range(length):
            if i and nums[i] == nums[i - 1]:
                multiplicity[i] = multiplicity[i - 1] + 1

        start, end = 0, max_val + 1
        while start + 1 < end:
            guess = start + (end - start) // 2
            if self.hasKDistances(guess, k, nums, prefix, multiplicity, max_val):
                end = guess
            else:
                start = guess

        if self.hasKDistances(start, k, nums, prefix, multiplicity, max_val):
            return start
        if self.hasKDistances(end, k, nums, prefix, multiplicity, max_val):
            return end

        return 0

    def hasKDistances(self, guess, required_count, nums, prefix, multiplicity, max_val):
        count = 0
        for i in range(len(nums)):
            count += prefix[min(nums[i] + guess, max_val)] - \
                prefix[nums[i]] + multiplicity[i]

        return count >= required_count
