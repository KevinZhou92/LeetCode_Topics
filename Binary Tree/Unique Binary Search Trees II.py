"""
Solution 1:

DFS

This solution can be easily retrieved if we are solving the first one using recursion
https://leetcode.com/problems/unique-binary-search-trees-ii/solution/


Time Complexity: O()
Space complexity : O()
"""


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n < 1:
            return [None]

        return self.buildTrees(1, n)

    def buildTrees(self, start, end):
        if start > end:
            return [None]

        if start == end:
            return [TreeNode(start)]

        res = []
        for rootVal in range(start, end + 1):
            root = TreeNode(rootVal)
            leftSubTrees = self.buildTrees(start, rootVal - 1)
            rightSubTrees = self.buildTrees(rootVal + 1, end)
            for leftSubTree in leftSubTrees:
                for rightSubtree in rightSubTrees:
                    root.left = leftSubTree
                    root.right = rightSubtree
                    res.append(root)
                    root = TreeNode(rootVal)

        return res
