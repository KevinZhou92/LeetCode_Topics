"""
Solution 1:

DFS
Preorder traversal
Return head, tail for each subtree and then connect them according to the requirements


Time Complexity: O(N)
Space complexity : O(N)
"""


class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # find the smallest
        # connect left, root, right
        if not root:
            return

        self.head = Node(None, None, None)
        head, tail = self.connectNode(root)
        self.head.right.left = tail
        if tail:
            tail.right = self.head.right

        return self.head.right

    def connectNode(self, root):
        if not root:
            return None, None

        if not self.head.right or root.val < self.head.right.val:
            self.head.right = root

        if not root.left and not root.right:
            return root, root

        lHead, lTail = self.connectNode(root.left)
        if lTail:
            lTail.right = root
            root.left = lTail
        rHead, rTail = self.connectNode(root.right)
        if rTail:
            root.right = rHead
            rHead.left = root

        head = lHead if lHead else root
        tail = rTail if rTail else root

        return head, tail


"""
Solution 1-2:

Simplified Version

Time Complexity: O(N)
Space complexity : O(N)
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # find the smallest
        # connect left, root, right
        if not root:
            return

        head, tail = self.connectNode(root)
        return head

    def connectNode(self, root):
        if not root:
            return None, None

        lHead, lTail = self.connectNode(root.left)
        if lTail:
            lTail.right = root
            root.left = lTail
        rHead, rTail = self.connectNode(root.right)
        if rTail:
            root.right = rHead
            rHead.left = root

        head = lHead if lHead else root
        tail = rTail if rTail else root

        head.left = tail
        tail.right = head

        return head, tail
