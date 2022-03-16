"""
Solution 1:
Hashmap

Time Complexity: O(n) for building hashmap, O(1) for pick
Space complexity : O(n) for hashmap
"""


class Solution:

    def __init__(self, nums: List[int]):
        index_map = {}
        for index, num in enumerate(nums):
            # list concatenation will be a deep copy, high complexity
            index_map[num] = index_map.get(num, []) + [index]
        self.index_map = index_map

    def pick(self, target: int) -> int:
        if target not in self.index_map:
            return None

        target_indices = self.index_map[target]
        return target_indices[random.randint(0, len(target_indices) - 1)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

"""
Solution 2:
Reservior Sampling

Proof: https://leetcode-cn.com/problems/random-pick-index/solution/398-sui-ji-shu-suo-yin-shui-tang-chou-ya-ud8b/

Time Complexity: O(n) for pick
Space complexity : O(1) for hashmap
"""


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        count = 0
        res_index = 0
        for index, num in enumerate(self.nums):
            if num == target:
                count += 1
                if random.randint(1, count) == count:
                    res_index = index

        return res_index


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
