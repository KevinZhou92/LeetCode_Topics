"""
Solution 1:

DFS
1st Recursion to check if both nodes exist in tree
2nd Recursion to check the LCA of two nodes

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or not p or not q:
            return False

        pExists = self.findNode(root, p)
        qExists = self.findNode(root, q)
        if not (pExists and qExists):
            return None

        return self.search(root, p, q)

    def findNode(self, root, targetNode):
        if not root:
            return False

        if root == targetNode:
            return True

        left = self.findNode(root.left, targetNode)
        right = self.findNode(root.right, targetNode)

        return left or right

    def search(self, root, p, q):
        if not root:
            return None

        if root == p or root == q:
            return root

        left = self.search(root.left, p, q)
        right = self.search(root.right, p, q)

        if left and right:
            return root

        return left if left else right
