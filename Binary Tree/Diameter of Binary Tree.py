"""
Solution 1:

DFS

!!! Note, it's asking for max diameter between any two nodes, we need to keep track of global max and local max

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        localMax, globalMax = self.search(root)

        return globalMax

    def search(self, root):
        if not root:
            return 0, 0

        left, leftMax = self.search(root.left)
        right, rightMax = self.search(root.right)

        return max(left, right) + 1, max(left + right, leftMax, rightMax)
