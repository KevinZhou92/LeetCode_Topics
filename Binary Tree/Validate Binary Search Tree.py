"""
Solution 1:

DFS

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        res, _, _ = self.validateBST(root)

        return res

    def validateBST(self, root):
        if not root:
            return True, None, None

        if not root.left and not root.right:
            return True, root.val, root.val

        leftValid, lMin, lMax = self.validateBST(root.left)
        rightValid, rMin, rMax = self.validateBST(root.right)
        if not leftValid or not rightValid:
            return False, None, None

        if lMax and lMax >= root.val:
            return False, None, None

        if rMin and rMin <= root.val:
            return False, None, None

        return True, lMin if lMin else root.val, rMax if rMax else root.val


"""
Solution 1-2:

DFS with range for each subtree
For each subtree, define the minimal value and max value for the subtree and then validate recursively

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.validateBST(root, float('-inf'), float('inf'))

    def validateBST(self, root, minVal, maxVal):
        if not root:
            return True

        if root.val <= minVal or root.val >= maxVal:
            return False

        return self.validateBST(root.left, minVal, root.val) and self.validateBST(root.right, root.val, maxVal)
