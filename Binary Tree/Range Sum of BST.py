"""
Solution 1:

Bottom-up DFS

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root or low > high:
            return 0

        leftSum = self.rangeSumBST(root.left, low, high)
        rightSum = self.rangeSumBST(root.right, low, high)
        rootSum = root.val if root.val >= low and root.val <= high else 0

        return leftSum + rightSum + rootSum
