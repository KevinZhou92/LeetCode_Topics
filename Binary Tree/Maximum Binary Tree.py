"""
Solution 1:

DFS 
Find the max value in the array and use it as the root of the tree,
then construct left and subtree from left subarray and right subarray,
follow the same manner while building the left and right subtrees.

Time Complexity: O(n^2)
Space complexity : O(n)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        maxValIndex = self.getMaxValIndex(nums)
        root = TreeNode(nums[maxValIndex])
        root.left = self.constructMaximumBinaryTree(nums[:maxValIndex])
        root.right = self.constructMaximumBinaryTree(nums[maxValIndex + 1:])

        return root

    def getMaxValIndex(self, nums):
        maxVal, maxValIndex = nums[0], 0
        for index, val in enumerate(nums):
            if val > maxVal:
                maxVal = val
                maxValIndex = index

        return maxValIndex
