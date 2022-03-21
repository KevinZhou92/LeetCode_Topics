"""
Ref: https://leetcode-cn.com/problems/binary-tree-postorder-traversal/solution/acm-xuan-shou-tu-jie-leetcode-er-cha-shu-q9ep/
"""

"""
Solution 1:
DFS Recursion

Bottom-Up

Time Complexity: O(?), this is hard to measure, since list.extend() operation includes creating a new array
and copy
Space complexity : O(n)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return []

        res.append(root.val)
        res.extend(self.preorderTraversal(root.left))
        res.extend(self.preorderTraversal(root.right))

        return res


"""
Solution 1-1:
DFS Recursion

Top-Down

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res

        res = []
        self.dfs(root, res)

        return res

    def dfs(self, root, res):
        if not root:
            return

        res.append(root.val)
        self.dfs(root.left, res)
        self.dfs(root.right, res)


"""
Solution 2:
Iterative Approach

Use a stack

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res

        stack = [root]
        cur = root
        visited = set()
        while stack:
            cur = stack[-1]
            if cur not in visited:
                visited.add(cur)
                res.append(cur.val)
            if cur.left:
                stack.append(cur.left)
                cur.left = None
            elif cur.right:
                stack.append(cur.right)
                cur.right = None
            else:
                stack.pop()

        return res


"""
Solution 2-1:

Iterative Approach

Use a stack, use our brain to simulate the workflow of the stack.

For preorder traversal, everytime we need to go to a deeper level, we need to push the current node to 
stack to simulate the stack frame in a recursive call, and pop the top element from stack to simulate the
return statement in recursion call.


Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res

        stack = []
        cur = root
        while stack or cur:
            if cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop().right

        return res


"""
Solution 2-2:
A more intuitive iterative approach

Time Complexity: O(n)
Space complexity : O(n)

"""


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res

        # 0 not visited,
        # 1 visited left
        # 2 visited right
        stack = [[root, 0]]
        while stack:
            cur = stack[-1]
            if cur[1] == 0:
                cur[1] = 1
                res.append(cur[0].val)
                if cur[0].left:
                    stack.append([cur[0].left, 0])
            elif cur[1] == 1:
                cur[1] = 2
                if cur[0].right:
                    stack.append([cur[0].right, 0])
            else:
                stack.pop()
        return res


"""
Solution 3:

Morris Traversal
https://leetcode.com/problems/binary-tree-preorder-traversal/solution/

 we visit each predecessor exactly twice descending down from the node, 
 thus the time complexity is \mathcal{O}(N)O(N), where NN is the number of nodes, i.e. the size of tree.

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Morris Traversal
        res = []
        if not root:
            return res

        cur = root
        prev = None
        while cur:
            if cur.left:
                prev = cur.left
                # Here we can't use while prev.right and prev.right.right
                # Assue a tree is a linked list and only have left subtrees
                #       3
                #      /
                #     2
                #    /
                #   1
                # If current node is 1, prev.right.right will point to 3, which will
                # result in a dead loop
                while prev.right and prev.right != cur:
                    prev = prev.right

                if prev.right == cur:
                    prev.right = None
                    cur = cur.right
                else:
                    res.append(cur.val)
                    prev.right = cur
                    cur = cur.left
            else:
                res.append(cur.val)
                cur = cur.right

        return res
