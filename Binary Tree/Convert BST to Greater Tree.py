"""
Solution 1:

DFS. Inorder Traversal in right - root - left order

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        self.sum = 0
        self.convertTree(root)

        return root

    def convertTree(self, root):
        if not root:
            return

        self.convertTree(root.right)
        root.val += self.sum
        self.sum = root.val
        leftSum = self.convertTree(root.left)
