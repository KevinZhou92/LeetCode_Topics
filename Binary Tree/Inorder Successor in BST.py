"""
Solution 1:

Iterative Inorder Traversal
Inorder of a BST is always ordered, return the first value that is grater than the target value

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        if not root:
            return None

        cur = root
        stack = []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if cur.val > p.val:
                return cur
            else:
                cur = cur.right

        return None


"""
Solution 1:

DFS
Note the return oder, if we find the successor node, we return it immediately


Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        if not root:
            return None

        left = self.inorderSuccessor(root.left, p)
        # Return immediately if we find the successor node
        if left:
            return left

        if root.val > p.val:
            return root
        right = self.inorderSuccessor(root.right, p)

        if right:
            return right

        return None
