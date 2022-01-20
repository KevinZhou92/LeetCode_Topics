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
