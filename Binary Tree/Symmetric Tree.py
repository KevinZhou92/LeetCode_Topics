"""
Solution 1:
BFS
Use two quest to traverse left and right subtree, traverse left from left to right, traverse right from right to left
!!!Edge case for comparing two nodes:
1. left is none, right is not
2. right is none, left is not
3. left and right are both none
4. left and right are both not none


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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        l_queue = deque([root.left])
        r_queue = deque([root.right])
        while l_queue and r_queue:
            if len(l_queue) != len(r_queue):
                return False
            size = len(l_queue)
            for _ in range(size):
                leftNode = l_queue.popleft()
                rightNode = r_queue.popleft()
                if not leftNode and not rightNode:
                    continue
                if not leftNode or not rightNode:
                    return False     
                if leftNode.val != rightNode.val:
                    return False

                l_queue.append(leftNode.left)
                l_queue.append(leftNode.right)
                r_queue.append(rightNode.right)
                r_queue.append(rightNode.left)

        return True


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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.dfs(root.left, root.right)

    def dfs(self, leftNode, rightNode):
        if not leftNode and not rightNode:
            return True
        if not leftNode or not rightNode:
            return False

        if leftNode.val != rightNode.val:
            return False

        return self.dfs(leftNode.left, rightNode.right) and self.dfs(leftNode.right, rightNode.left)
