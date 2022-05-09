"""
Solution 1:

DFS
1. Check if current tree is a binary search tree
    1.1 Find maxVal, minVal from left and right tree, root should be between the maxVal and minVal from left and right trees
    1,2 Left and right tree should be bst as well
2. Count nodes of current bst
3. Find the largest binary search tree 

Time Complexity: O(n^3)
For each isBst call, we need O(n) time for find max and min values and there n nodes, so in total isBst will take O(n^2)


Space complexity : O(n)
"""


class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        if self.isBst(root):
            return self.countNodes(root)

        return max(self.largestBSTSubtree(root.left), self.largestBSTSubtree(root.right))

    def isBst(self, root):
        if not root:
            return True

        maxVal = self.findMax(root.left)
        minVal = self.findMin(root.right)

        if root.val <= maxVal or root.val >= minVal:
            return False

        return self.isBst(root.left) and self.isBst(root.right)

    def findMax(self, root):
        if not root:
            return float('-inf')

        leftMax = self.findMax(root.left)
        rightMax = self.findMax(root.right)

        return max(leftMax, rightMax, root.val)

    def findMin(self, root):
        if not root:
            return float('inf')

        leftMin = self.findMin(root.left)
        rightMin = self.findMin(root.right)

        return min(leftMin, rightMin, root.val)

    def countNodes(self, root):
        if not root:
            return 0

        left = self.countNodes(root.left)
        right = self.countNodes(root.right)

        return left + right + 1


"""
Solution 1-2:

DFS

For isBst, we use a topDown approach and don't repeatitively check the min max values from each subtrees, which reduce the complexity
from O(n^2) to O(n)

Time Complexity: O(n^2)
Space complexity : O(n)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        if self.isBst(root, float('-inf'), float('inf')):
            return self.countNodes(root)

        return max(self.largestBSTSubtree(root.left), self.largestBSTSubtree(root.right))

    def isBst(self, root, minVal, maxVal):
        if not root:
            return True

        if root.val <= minVal or root.val >= maxVal:
            return False

        return self.isBst(root.left, minVal, root.val) and self.isBst(root.right, root.val, maxVal)

    def findMax(self, root):
        if not root:
            return float('-inf')

        leftMax = self.findMax(root.left)
        rightMax = self.findMax(root.right)

        return max(leftMax, rightMax, root.val)

    def findMin(self, root):
        if not root:
            return float('inf')

        leftMin = self.findMin(root.left)
        rightMin = self.findMin(root.right)

        return min(leftMin, rightMin, root.val)

    def countNodes(self, root):
        if not root:
            return 0

        left = self.countNodes(root.left)
        right = self.countNodes(root.right)

        return left + right + 1


"""
Solution 1-3:

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
