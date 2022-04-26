"""
Solution 1:

DFS
DFS around the tree nodes on perimeter.

Tricky Issue, need to revisit

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        left = []
        if root.left or root.right:
            left = [root.val]
        self.dfsLeft(root.left, left)
        right = []
        self.dfsRight(root.right, right)
        leaves = []
        self.dfsLeaves(root, leaves)

        return left + leaves + right

    def dfsLeft(self, root, left):
        if not root:
            return

        if not root.left and not root.right:
            return

        left.append(root.val)
        if root.left:
            self.dfsLeft(root.left, left)
        else:
            self.dfsLeft(root.right, left)

    def dfsRight(self, root, right):
        if not root:
            return

        if not root.left and not root.right:
            return

        if root.right:
            self.dfsRight(root.right, right)
        else:
            self.dfsRight(root.left, right)
        right.append(root.val)

    def dfsLeaves(self, root, leaves):
        if not root:
            return

        if not root.left and not root.right:
            leaves.append(root.val)

        self.dfsLeaves(root.left, leaves)
        self.dfsLeaves(root.right, leaves)
