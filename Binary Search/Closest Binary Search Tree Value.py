"""
Solution 1: Binary Seach Tree, Binary Search

Time Complexity: O(logn)
Space Complexity: O(1)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        cur_node = root
        min_node = None
        diff = sys.maxsize
        while cur_node:
            if abs(cur_node.val - target) < diff:
                diff = abs(cur_node.val - target)
                min_node = cur_node
            if cur_node.val < target:
                cur_node = cur_node.right
            elif cur_node.val == target:
                return cur_node.val
            else:
                cur_node = cur_node.left
        
        return min_node.val
        