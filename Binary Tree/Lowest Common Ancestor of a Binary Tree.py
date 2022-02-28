"""
Solution 1:

DFS

Try to search p and q in subtrees, if found, return the node. There are two cases:
1. Two nodes share a common ancestor
2. One node is the descendant of the other one 

Write the recursive call according to these two cases.

Time Complexity: O(n)
Space complexity : O(n)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        if root.val == p.val or root.val == q.val:
            return root

        leftRes = self.lowestCommonAncestor(root.left, p, q)
        rightRes = self.lowestCommonAncestor(root.right, p, q)

        if leftRes and rightRes:
            return root

        if leftRes:
            return leftRes

        if rightRes:
            return rightRes

        return None
