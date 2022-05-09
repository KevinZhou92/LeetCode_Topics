"""
Solution 1:

DFS to find inorder list and sort it.

Compare the sorted inorder list with the tree and fix the node

Time Complexity: O(nlogn)
Space complexity : O(n)
"""


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        inOrder = []
        self.traverse(root, inOrder)
        inOrder.sort()
        self.index = 0
        self.fixTree(root, inOrder)

    def traverse(self, root, res):
        if not root:
            return

        self.traverse(root.left, res)
        res.append(root.val)
        self.traverse(root.right, res)

    def fixTree(self, root, inOrder):
        if not root:
            return

        self.fixTree(root.left, inOrder)
        root.val = inOrder[self.index]
        self.index += 1
        self.fixTree(root.right, inOrder)


"""
Solution 1-2:

DFS

The key point here is to understand how to find two swapped nodes in ordered list

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        self.first = None
        self.second = None
        self.prev = None

        self.traverseTree(root)

        self.first.val, self.second.val = self.second.val, self.first.val

    def traverseTree(self, root):
        if not root:
            return

        self.traverseTree(root.left)
        if not self.prev:
            self.prev = root
        else:
            if self.prev.val > root.val:
                self.second = root
                if not self.first:
                    self.first = self.prev
                else:
                    return
            self.prev = root
        self.traverseTree(root.right)


"""
Solution 1-3:

Iterative Inorder Traversal


Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        self.first = None
        self.second = None
        self.prev = None
        stack = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if not self.prev:
                self.prev = cur
            else:
                if self.prev.val > cur.val:
                    self.second = cur
                    if not self.first:
                        self.first = self.prev
                    else:
                        break
                self.prev = cur
            cur = cur.right

        self.first.val, self.second.val = self.second.val, self.first.val


"""
Solution 1-4:

Morris Traversal

Time Complexity: O(n)
Space complexity : O(1)
"""


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        self.first = None
        self.second = None
        self.prev = None
        # morris traversal
        while root:
            if root.left:
                cur = root.left
                while cur.right and cur.right != root:
                    cur = cur.right

                if not cur.right:
                    cur.right = root
                    root = root.left
                else:
                    if not self.prev:
                        self.prev = root
                    else:
                        if self.prev.val > root.val:
                            self.second = root
                            if not self.first:
                                self.first = self.prev
                    cur.right = None
                    self.prev = root
                    root = root.right
            else:
                if not self.prev:
                    self.prev = root
                else:
                    if self.prev.val > root.val:
                        self.second = root
                        if not self.first:
                            self.first = self.prev
                self.prev = root
                root = root.right

        self.first.val, self.second.val = self.second.val, self.first.val
