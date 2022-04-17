"""
Solution 1:

DFS

Two steps:
1. Convert the tree to a linked list
2. Iteratd the list from smallest to biggest

Time Complexity: O(n)
Space complexity : O(n)
"""


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.dummyNode = TreeNode()
        if not root:
            self.dummyNode.right = None
        head, tail = self.__connectNodes(root)
        self.dummyNode.val = head.val - 1
        self.dummyNode.right = head

    def next(self) -> int:
        cur = self.dummyNode.right
        next = cur.right
        self.dummyNode.right = next

        return cur.val

    def hasNext(self) -> bool:
        if not self.dummyNode.right:
            return False

        return True

    def __connectNodes(self, root):
        if not root:
            return None, None

        lHead, lTail = self.__connectNodes(root.left)
        rHead, rTail = self.__connectNodes(root.right)

        if lHead:
            lTail.right = root

        if rHead:
            root.right = rHead

        head = lHead if lHead else root
        tail = rTail if rTail else root

        return head, tail
