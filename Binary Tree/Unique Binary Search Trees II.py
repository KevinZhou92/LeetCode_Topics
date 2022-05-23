"""
Solution 1:

DFS

This solution can be easily retrieved if we are solving the first one using recursion
https://leetcode.com/problems/unique-binary-search-trees-ii/solution/
https://leetcode.cn/problems/unique-binary-search-trees-ii/solution/bu-tong-de-er-cha-sou-suo-shu-ii-by-leetcode-solut/

Time Complexity: O(Catlan Numbers)
Space complexity : O(Catlan Numbers)
"""


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.buildTrees(1, n)

    def buildTrees(self, start, end):
        if start > end:
            return [None]

        res = []
        for rootVal in range(start, end + 1):
            leftTrees = self.buildTrees(start, rootVal - 1)
            rightTrees = self.buildTrees(rootVal + 1, end)
            for lTree in leftTrees:
                for rTree in rightTrees:
                    root = TreeNode(rootVal)
                    root.left = lTree
                    root.right = rTree
                    res.append(root)

        return res
