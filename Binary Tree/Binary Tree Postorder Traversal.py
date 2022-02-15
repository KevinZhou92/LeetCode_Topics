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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res

        self.dfs(root, res)

        return res

    def dfs(self, root, res):
        if not root:
            return
        self.dfs(root.left, res)
        self.dfs(root.right, res)
        res.append(root.val)


"""
Solution 2:
Iterative

Time Complexity: O()
Space complexity : O()
"""


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res

        stack = []
        cur = root
        prev = None
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if not cur.right or cur.right == prev:
                res.append(cur.val)
                prev = cur
                cur = None
            else:
                stack.append(cur)
                cur = cur.right

        return res


"""
Solution 2-1:
A more intuitive iterative approach

Time Complexity: O()
Space complexity : O()
"""


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res

        stack = [[root, 0]]
        while stack:
            cur = stack[-1]
            if cur[1] == 0:
                cur[1] = 1
                if cur[0].left:
                    stack.append([cur[0].left, 0])
            elif cur[1] == 1:
                cur[1] = 2
                if cur[0].right:
                    stack.append([cur[0].right, 0])
            else:
                res.append(cur[0].val)
                stack.pop()

        return res
