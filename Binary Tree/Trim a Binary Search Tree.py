"""
Solution 1:

DFS
Trim subtree and then return root and maxNode in the subtree, then connect subtree

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None

        newRoot, maxNode = self.trim(root, low, high)
        return newRoot

    def trim(self, root, low, high):
        if not root:
            return None, None

        leftRoot, lMax = self.trim(root.left, low, high)
        rightRoot, rMax = self.trim(root.right, low, high)

        curRoot = root if root.val <= high and root.val >= low else None
        maxNode = None

        if not curRoot:
            if leftRoot:
                lMax.right = rightRoot
                curRoot = leftRoot
            else:
                curRoot = rightRoot
        else:
            curRoot.left = leftRoot
            curRoot.right = rightRoot

        if rMax:
            maxNode = rMax
        elif lMax:
            maxNode = lMax
        else:
            maxNode = curRoot

        return curRoot, maxNode


"""
Solution 1-2:

DFS
Let trim(node) be the desired answer for the subtree at that node. We can construct the answer recursively.

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val < low:
            return self.trimBST(root.right, low, high)

        if root.val > high:
            return self.trimBST(root.left, low, high)

        leftRoot = self.trimBST(root.left, low, high)
        rightRoot = self.trimBST(root.right, low, high)
        root.left = leftRoot
        root.right = rightRoot

        return root
