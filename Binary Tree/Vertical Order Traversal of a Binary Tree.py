"""
Solution 1:

DFS
https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/solution/

Time Complexity: O(nlog(n/k)) assume there are k columns
Space complexity : O(n)
"""


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        verticalTraversals = defaultdict(list)
        self.traversal(root, 0, 0, verticalTraversals)

        minCol, maxCol = min(verticalTraversals), max(verticalTraversals)
        for col in range(minCol, maxCol + 1):
            verticalTraversals[col].sort(
                key=lambda nodeComb: (nodeComb[1], nodeComb[0]))

        res = [[nodeComb[0] for nodeComb in verticalTraversals[col]]
               for col in range(minCol, maxCol + 1)]

        return res

    def traversal(self, root, row, col, verticalTraversals):
        if not root:
            return

        verticalTraversals[col].append((root.val, row))
        self.traversal(root.left, row + 1, col - 1, verticalTraversals)
        self.traversal(root.right, row + 1, col + 1, verticalTraversals)
