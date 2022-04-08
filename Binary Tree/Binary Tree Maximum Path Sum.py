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
        self.findMax(root)

        return self.globalMax

    def findMax(self, root):
        if not root:
            return float('-inf')

        leftMax = self.findMax(root.left)
        rightMax = self.findMax(root.right)
        self.globalMax = max(self.globalMax, leftMax, rightMax, leftMax + root.val,
                             rightMax + root.val, leftMax + root.val + rightMax, root.val)

        return max(leftMax + root.val, rightMax + root.val, root.val)


class Solution2:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.globalMax = float('-inf')
        self.findMax(root)

        return self.globalMax

    def findMax(self, root):
        if not root:
            return 0

        # If max left sum is 0, we will just abandon it
        leftMax = max(self.findMax(root.left), 0)
        rightMax = max(self.findMax(root.right), 0)
        pathMaxSum = leftMax + root.val + rightMax

        self.globalMax = max(self.globalMax, pathMaxSum)

        return root.val + max(leftMax, rightMax)
