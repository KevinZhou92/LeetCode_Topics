"""
Solution 1:

DFS. Same as #538

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        self.sum = 0
        self.traverse(root)
        return root

    def traverse(self, root):
        if not root:
            return

        self.traverse(root.right)
        self.sum += root.val
        root.val = self.sum
        self.traverse(root.left)
