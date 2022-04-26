"""
Solution 1:

DFS

Time Complexity: O(n^2)
Space complexity : O(n^2)
"""


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        return self.buildBst(preorder, 0, len(preorder) - 1)

    def buildBst(self, preorder, start, end):
        if start > end:
            return None

        if start == end:
            return TreeNode(preorder[start])

        root = TreeNode(preorder[start])
        leftCount = self.findLeftCount(preorder, start + 1, preorder[start])
        root.left = self.buildBst(preorder, start + 1, start + leftCount)
        root.right = self.buildBst(preorder, start + leftCount + 1, end)

        return root

    def findLeftCount(self, preorder, startIndex, targetValue):
        count = 0
        while startIndex < len(preorder):
            if preorder[startIndex] < targetValue:
                startIndex += 1
                count += 1
            else:
                break

        return count


"""
Solution 1-2:

DFS
Make use of the characteristic of a bst, always root-left-right and
The left subtree of a node contains only nodes with keys lesser than the node’s key.
The right subtree of a node contains only nodes with keys greater than the node’s key.
The left and right subtree each must also be a binary search tree.

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        self.index = 0
        return self.buildTree(preorder, float('-inf'), float('inf'))

    def buildTree(self, preorder, minVal, maxVal):
        if self.index >= len(preorder):
            return None

        curVal = preorder[self.index]
        if curVal <= minVal or curVal >= maxVal:
            return None

        root = TreeNode(preorder[self.index])
        self.index += 1
        root.left = self.buildTree(preorder, minVal, root.val)
        root.right = self.buildTree(preorder, root.val, maxVal)

        return root
