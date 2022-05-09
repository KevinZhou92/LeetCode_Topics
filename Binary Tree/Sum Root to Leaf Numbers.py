"""
Solution 1:

Top-Down DFS

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return
        self.sum = 0
        self.countSum(root, 0)

        return self.sum

    def countSum(self, root, parentVal):
        if not root:
            return

        if not root.left and not root.right:
            self.sum += parentVal * 10 + root.val
            return

        curVal = parentVal * 10 + root.val
        self.countSum(root.left, curVal)
        self.countSum(root.right, curVal)
