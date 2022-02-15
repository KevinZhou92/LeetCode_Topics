"""
Solution 1:
DFS

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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res

        self.dfs(root, res)

        return res

    def dfs(self, root, res):
        if not root:
            return
        self.dfs(root.left, res)
        res.append(root.val)
        self.dfs(root.right, res)


"""
Solution 2:
Iterative Approach

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res

        stack = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right

        return res


"""
Solution 2-1:
A more intuitive iterative approach

Time Complexity: O()
Space complexity : O()
"""


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res

        # 0 - first time visiting
        # 1 - visited left subtree
        # 2 - visited right subtree
        stack = [[root, 0]]
        while stack:
            cur = stack[-1]
            if cur[1] == 0:
                cur[1] = 1
                if cur[0].left:
                    stack.append([cur[0].left, 0])
            elif cur[1] == 1:
                res.append(cur[0].val)
                cur[1] = 2
                if cur[0].right:
                    stack.append([cur[0].right, 0])
            else:
                stack.pop()

        return res
