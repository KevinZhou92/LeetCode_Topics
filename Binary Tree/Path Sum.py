"""
Solution 1:
DFS

!!!Note the criteria for a leaf node is the left child and right child are both none.

Time Complexity: O(n)
Space complexity : O(n) worst case, O(logn) on average
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right:
            return root.val == targetSum

        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)


"""
Solution 2:
BFS

!!! Note be careful with the target value at each level, when we add node to the queue, the target value is always
the preview target value minus the parent's value

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        queue = deque([[root, targetSum]])
        while queue:
            size = len(queue)
            for _ in range(size):
                curNode, target = queue.popleft()
                if not curNode.left and not curNode.right and target == curNode.val:
                    return True
                if curNode.left:
                    queue.append([curNode.left, target - curNode.val])
                if curNode.right:
                    queue.append([curNode.right, target - curNode.val])

        return False
