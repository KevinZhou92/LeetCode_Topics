"""
Solution 1:

DFS
Find the root val from the preorder and postorder list, then we will try to build left and right subtrees recursively
In this approach, we are trying to find the left subtree nodes from the preorder and postorder lists
preorder: root left right
postorder: left right root

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


"""
Solution 1-2:

DFS

Compare to first solution, we build a val to index map from the postOrder list before we get into the recursion, therefore we can avoid
having to iterate over the array over and over again to count the size of the left subtree in each recursion.

We can just find the corresponding left root val in the postOrder list and then count how many elements are in the left subtree, cause postOrder traversal
always follow left-right-root order.

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) != len(postorder):
            return None

        postOrderValToIndex = {
            val: index for index, val in enumerate(postorder)}

        return self.constructTree(preorder, 0, len(preorder) - 1, postorder, 0, len(postorder) - 1, postOrderValToIndex)

    def constructTree(self, preOrder, preStart, preEnd, postOrder, postStart, postEnd, postOrderValToIndex):
        if preStart == preEnd:
            return TreeNode(preOrder[preStart])

        if preStart > preEnd:
            return None

        root = TreeNode(preOrder[preStart])
        leftRootVal = preOrder[preStart + 1]
        leftTreeSize = postOrderValToIndex[leftRootVal] - postStart + 1

        root.left = self.constructTree(preOrder, preStart + 1, preStart + leftTreeSize,
                                       postOrder, postStart, postStart + leftTreeSize - 1, postOrderValToIndex)
        root.right = self.constructTree(preOrder, preStart + leftTreeSize + 1,
                                        preEnd, postOrder, postStart + leftTreeSize, postEnd, postOrderValToIndex)

        return root


"""
Solution 1-2:

DFS Wrong Version

I made lots of mistakes in this solution, the tricky thing is between line 123-130
I'm checking both preStart/preEnd and postStart/postEnd

Time Complexity: O()
Space complexity : O()
"""


class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) != len(postorder):
            return None

        preValToIndex = {val: index for index, val in enumerate(preorder)}
        postValToIndex = {val: index for index, val in enumerate(postorder)}

        return self.constructTree(preorder, 0, len(preorder) - 1, postorder, 0, len(postorder) - 1, preValToIndex, postValToIndex)

    def constructTree(self, preorder, preStart, preEnd, postorder, postStart, postEnd, preValToIndex, postValToIndex):
        if preStart == preEnd:
            return TreeNode(preorder[preStart])

        if postStart == postEnd:
            return TreeNode(postorder[postStart])

        if preStart > preEnd or postStart > postEnd:
            return None

        root = TreeNode(preorder[preStart])
        leftRootVal = preorder[preStart + 1]
        rightRootVal = postorder[postEnd - 1]

        leftRootIndex = postValToIndex[leftRootVal]
        rightRootIndex = preValToIndex[rightRootVal]

        root.left = self.constructTree(preorder, preStart + 1, rightRootIndex - 1,
                                       postorder, postStart, leftRootIndex, preValToIndex, postValToIndex)
        root.right = self.constructTree(preorder, rightRootIndex, preEnd, postorder,
                                        leftRootIndex + 1, postEnd - 1, preValToIndex, postValToIndex)

        return root


"""
Solution 1-3:

DFS Correct Version 1


Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) != len(postorder):
            return None

        preValToIndex = {val: index for index, val in enumerate(preorder)}
        postValToIndex = {val: index for index, val in enumerate(postorder)}

        return self.constructTree(preorder, 0, len(preorder) - 1, postorder, 0, len(postorder) - 1, preValToIndex, postValToIndex)

    def constructTree(self, preorder, preStart, preEnd, postorder, postStart, postEnd, preValToIndex, postValToIndex):
        if preStart == preEnd:
            return TreeNode(preorder[preStart])

        if preStart > preEnd:
            return None

        root = TreeNode(preorder[preStart])
        leftRootVal = preorder[preStart + 1]
        rightRootVal = postorder[postEnd - 1]

        leftRootIndex = postValToIndex[leftRootVal]
        rightRootIndex = preValToIndex[rightRootVal]

        root.left = self.constructTree(preorder, preStart + 1, rightRootIndex - 1,
                                       postorder, postStart, leftRootIndex, preValToIndex, postValToIndex)
        root.right = self.constructTree(preorder, rightRootIndex, preEnd, postorder,
                                        leftRootIndex + 1, postEnd - 1, preValToIndex, postValToIndex)

        return root


"""
Solution 1-4:

DFS Correct Version 2


!!! Most Important Thing is: if the leftRootVal and rightRootVal collide, we need to make a decision whether to 
use the value to build the left treenode or to build the right treenode

Time Complexity: O()
Space complexity : O()
"""


class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) != len(postorder):
            return None

        preValToIndex = {val: index for index, val in enumerate(preorder)}
        postValToIndex = {val: index for index, val in enumerate(postorder)}

        return self.constructTree(preorder, 0, len(preorder) - 1, postorder, 0, len(postorder) - 1, preValToIndex, postValToIndex)

    def constructTree(self, preorder, preStart, preEnd, postorder, postStart, postEnd, preValToIndex, postValToIndex):
        if postStart == postEnd:
            return TreeNode(postorder[postStart])

        if postStart > postEnd:
            return None

        root = TreeNode(preorder[preStart])
        leftRootVal = preorder[preStart + 1]
        rightRootVal = postorder[postEnd - 1]

        leftRootIndex = postValToIndex[leftRootVal]
        rightRootIndex = preValToIndex[rightRootVal]

        root.left = self.constructTree(preorder, preStart + 1, rightRootIndex - 1,
                                       postorder, postStart, leftRootIndex, preValToIndex, postValToIndex)
        root.right = self.constructTree(preorder, rightRootIndex, preEnd, postorder,
                                        leftRootIndex + 1, postEnd - 1, preValToIndex, postValToIndex)

        return root
