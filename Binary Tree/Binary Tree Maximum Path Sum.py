"""
Solution 1:

DFS
Consider different edge cases
https://leetcode.com/problems/binary-tree-maximum-path-sum/solution/

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.globalMax = float('-inf')
        self.search(root)

        return self.globalMax

    def search(self, root):
        if not root:
            return float('-inf')

        leftMax = self.search(root.left)
        rightMax = self.search(root.right)
        self.globalMax = max(self.globalMax, leftMax, rightMax, leftMax + root.val,
                             rightMax + root.val, leftMax + root.val + rightMax, root.val)

        return max(leftMax + root.val, rightMax + root.val, root.val)
