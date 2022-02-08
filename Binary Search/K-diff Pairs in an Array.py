"""
Solution 1:
Sort + Brute Force search


Time Complexity: O(nlogn + n^2)
Space complexity : O(1)
"""


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        num_pairs = [(index, val) for index, val in enumerate(nums)]
        num_pairs = sorted(num_pairs, key=lambda pair: pair[1])

        visited = set()
        res = 0
        for i in range(len(num_pairs)):
            if num_pairs[i][1] in visited:
                continue
            target = num_pairs[i][1] + k
            for j in range(i + 1, len(num_pairs)):
                if num_pairs[j][1] > target:
                    break
                elif num_pairs[j][1] == target:
                    res += 1
                    break
            visited.add(num_pairs[i][1])

        return res


"""
Solution 2:
HashMap

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums_map = {}
        for num in nums:
            nums_map[num] = nums_map.get(num, 0) + 1

        res = 0
        for key, val in nums_map.items():
            if k > 0 and nums_map.get(key + k, 0):
                res += 1
            elif k == 0 and nums_map.get(key, 0) > 1:
                res += 1

        return res
