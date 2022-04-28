"""
Solution 1:

DFS
This question is different than validate bst.
Validate BST ask us to verify if the entire tree is a bst, but this problem ask us to find potential bst starting from 
any node and get the size of it

Time Complexity: O(N)
Space complexity : O(N)
"""


class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.maxSize = 0
        self.checkBst(root)

        return self.maxSize

    def checkBst(self, root):
        if not root:
            return True, float('inf'), float('-inf'), 0

        lBst, lMin, lMax, lSize = self.checkBst(root.left)
        rBst, rMin, rMax, rSize = self.checkBst(root.right)

        validBst = lBst and rBst and lMax < root.val and root.val < rMin
        if validBst:
            self.maxSize = max(self.maxSize, lSize + rSize + 1)

        if lBst:
            self.maxSize = max(self.maxSize, lSize)

        if rBst:
            self.maxSize = max(self.maxSize, rSize)

        return validBst, min(root.val, lMin, rMin), max(root.val, lMax, rMax), lSize + rSize + 1 if validBst else 0
