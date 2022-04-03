"""
Solution 1:

DFS

!!!This problem is to find all duplicate subtrees, so this problem is check two areas:
1. Tree traversal(we can use preorder or postorder)
2. Tree serialization

Note that we need to add placeholde for none node, we also need to add delimeter between each node.

Time Complexity: O(n^2) string concatenation takes O(n)
Space complexity : O(n)
"""


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        if not root:
            return None

        res = []
        duplicateTrees = defaultdict(int)
        self.search(root, duplicateTrees, res)

        return res

    def search(self, root, duplicateTrees, res):
        if not root:
            return '#'

        leftPath = self.search(root.left, duplicateTrees, res)
        rightPath = self.search(root.right, duplicateTrees, res)

        path = leftPath + ',' + rightPath + ',' + str(root.val)
        if duplicateTrees.get(path) == 1:
            res.append(root)
        duplicateTrees[path] += 1

        return path


"""
Solution 1-2:

O(n) soultion: https://leetcode.com/problems/find-duplicate-subtrees/discuss/1424214/Python3-DFS-with-comments

Time Complexity: O()
Space complexity : O()
"""
