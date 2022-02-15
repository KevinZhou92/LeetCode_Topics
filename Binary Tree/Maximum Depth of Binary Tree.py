"""
Solution 1:
Top-Down DFS

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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.ans = 0
        self.dfs(root, 1)

        return self.ans

    def dfs(self, root, depth):
        if not root:
            return

        if not root.left and not root.right:
            self.ans = max(self.ans, depth)

        self.dfs(root.left, depth + 1)
        self.dfs(root.right, depth + 1)


"""
Solution 1-1:
Botum-up DFS

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1


"""
Solution 2:
BFS Level Order Traversal

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([root])
        depth = 0
        while queue:
            depth += 1
            size = len(queue)
            for _ in range(size):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

        return depth
