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


"""
Solution 2:

Compare to the first question, this question doesn't guarantee that both nodes exist in the tree.
So we need to traverse the entire tree, which means we need to use post order traversal, only after we examine
the result from both left tree and right tree will we return the result.

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or not p or not q:
            return False
        self.count = 0
        res = self.search(root, p, q)

        return res if self.count == 2 else None

    def search(self, root, p, q):
        if not root:
            return None

        left = self.search(root.left, p, q)
        right = self.search(root.right, p, q)

        if left and right:
            return root

        if root == p or root == q:
            self.count += 1
            return root

        return left if left else right
