"""
Solution 1:

Recursion

Time Complexity: O(n!)
Space complexity : O(n)
"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        if not nums:
            return res

        # for permutation, we need to generate all possible orders of how
        # to place each number
        # create an array to indicate if current element is used
        visited = [0 for _ in range(len(nums))]

        # search for permutations
        self.search(nums, visited, [], res)

        return res

    # place each number in 1st, 2nd, 3rd.. place and
    # for remaining array, do the similar apprach
    # to generate all permutations
    def search(self, nums, visited, permutation, res):
        if len(permutation) == len(nums):
            res.append(copy.copy(permutation))
            return

        for index, val in enumerate(nums):
            if visited[index]:
                continue
            visited[index] = 1
            permutation.append(val)
            self.search(nums, visited, permutation, res)
            permutation.pop()
            visited[index] = 0
