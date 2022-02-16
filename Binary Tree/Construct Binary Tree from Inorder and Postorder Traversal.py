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


"""
Solution 2:
DFS

Use a index map to record the index and the value of the inorder node in the tree, this will make the search
in above solution to become O(1)

Time Complexity: O()
Space complexity : O()
"""


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        idx_map = {val: idx for idx, val in enumerate(inorder)}

        return self.build(0, len(inorder) - 1, inorder, 0, len(postorder) - 1, postorder, idx_map)

    def build(self, in_left, in_right, inorder, post_left, post_right, postorder, idx_map):
        if in_right < in_left:
            return None

        root = TreeNode(postorder[post_right])
        root_idx = idx_map[postorder[post_right]]
        offset = root_idx - in_left
        root.left = self.build(in_left, in_left + offset - 1, inorder,
                               post_left, post_left + + offset - 1, postorder, idx_map)
        root.right = self.build(root_idx + 1, in_right, inorder,
                                post_left + offset, post_right - 1, postorder, idx_map)

        return root
