"""
Solution 1:

DFS
Bottom-up
Postorder Traversal
Invert child first, and then parent

Time Complexity: O(n)
Space complexity : O(n)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        self.invertTree(root.left)
        self.invertTree(root.right)

        root.left, root.right = root.right, root.left

        return root


"""
Solution 1:

BFS
Top-down

Time Complexity: O()
Space complexity : O()
"""


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        queue = deque([root])
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if not node:
                    continue
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)

        return root
