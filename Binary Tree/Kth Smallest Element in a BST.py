"""
Solution 1:

DFS.

!!!Note that if a varible is None of if the value of the variable is 0

They will both return False for a statement like

if variable:

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        self.count = 0

        return self.findKth(root, k)

    def findKth(self, root, k):
        if not root:
            return None

        leftRes = self.findKth(root.left, k)
        self.count += 1
        if self.count == k:
            return root.val
        rightRes = self.findKth(root.right, k)

        return rightRes if leftRes is None else leftRes
