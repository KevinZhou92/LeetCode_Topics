"""
Solution 1:
DFS

# preorder, root, left, right
# inorder, left, root, right

!!! Note, be careful about index value, otherwise could end up in infinite loop

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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder, root, left, right
        # inorder, left, root, right
        if not preorder or not inorder:
            return None

        inorder_idx_map = {val: idx for idx, val in enumerate(inorder)}

        return self.build(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1, inorder_idx_map)

    def build(self, preorder, pre_start, pre_end, inorder, in_start, in_end, inorder_idx_map):
        if pre_start > pre_end:
            return None

        root = TreeNode(preorder[pre_start])
        root_idx = inorder_idx_map[preorder[pre_start]]
        ele_cnt = root_idx - in_start
        root.left = self.build(preorder, pre_start + 1, pre_start + ele_cnt,
                               inorder, in_start, in_start + ele_cnt - 1, inorder_idx_map)
        root.right = self.build(preorder, pre_start + ele_cnt + 1, pre_end,
                                inorder, in_start + ele_cnt + 1, in_end, inorder_idx_map)

        return root
