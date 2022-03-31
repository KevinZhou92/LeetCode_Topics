"""
Solution 1:

DFS

Time Complexity: O(n^2)
Space complexity : O(n)
"""


class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) != len(postorder):
            return None
        return self.constructTree(preorder, 0, len(preorder) - 1, postorder, 0, len(postorder) - 1)

    def constructTree(self, preorder, preStart, preEnd, postorder, postStart, postEnd) -> Optional[TreeNode]:
        if preStart > preEnd or postStart > postEnd:
            return None

        if preStart == preEnd:
            return TreeNode(preorder[preStart])

        if postStart == postEnd:
            return TreeNode(postorder[postStart])

        root = TreeNode(preorder[preStart])
        leftNodeCount = self.getLeftNodeCount(
            preorder, preStart + 1, postorder, postStart)
        root.left = self.constructTree(preorder, preStart + 1, preStart +
                                       leftNodeCount, postorder, postStart, postStart + leftNodeCount - 1)
        root.right = self.constructTree(
            preorder, preStart + 1 + leftNodeCount, preEnd, postorder, postStart + leftNodeCount, postEnd - 1)

        return root

    def getLeftNodeCount(self, preorder, preStart, postorder, postStart):
        preElements = set()
        postElements = set()

        while not preElements or not postElements or preElements != postElements:
            preElements.add(preorder[preStart])
            postElements.add(postorder[postStart])
            preStart += 1
            postStart += 1

        return len(preElements)
