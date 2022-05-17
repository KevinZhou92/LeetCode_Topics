"""
Solution 1:

DFS

Time Complexity: O(logn)
Space complexity : O(H)
"""


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        res = None
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
            res = root
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
            res = root
        else:
            if not root.left:
                res = root.right
                root.right = None
            elif not root.right:
                res = root.left
                root.left = None
            else:
                nextNode = self.findRightMin(root.right)
                nextNode.right = self.deleteNode(root.right, nextNode.val)
                nextNode.left = root.left
                root.left, root.right = None, None
                res = nextNode

        return res

    def findRightMin(self, root):
        if not root:
            return None

        while root.left:
            root = root.left

        return root
