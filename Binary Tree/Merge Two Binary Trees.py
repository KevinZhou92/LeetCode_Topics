"""
Solution 1:

DFS

!!!Remember to check if the node exists or not

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return

        newVal = 0
        if root1:
            newVal += root1.val

        if root2:
            newVal += root2.val

        root = TreeNode(newVal)
        root.left = self.mergeTrees(
            root1.left if root1 else None, root2.left if root2 else None)
        root.right = self.mergeTrees(
            root1.right if root1 else None, root2.right if root2 else None)
        return root
