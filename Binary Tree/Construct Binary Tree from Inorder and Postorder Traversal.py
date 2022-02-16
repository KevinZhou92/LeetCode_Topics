"""
Solution 1:
DFS

Time Complexity: O(n^2)
Space complexity : O(h*n), where h is the height of the tree
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # inorder l root, r
        # postorder l,r, root
        if not inorder or not postorder:
            return None

        root_val = postorder[-1]
        index = self.findRootIndex(inorder, root_val)
        node = TreeNode(root_val)
        node.left = self.buildTree(inorder[:index], postorder[:index])
        node.right = self.buildTree(inorder[index + 1:], postorder[index:-1])

        return node

    def findRootIndex(self, inorder, target_val):
        for index, value in enumerate(inorder):
            if value == target_val:
                return index
