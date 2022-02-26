"""
Solution 1:

BFS

!!! Note, it's very import we set pre to None(line #39) after iterating over all nodes in one level

Time Complexity: O()
Space complexity : O()
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        queue = deque([root])
        pre = None
        while queue:
            size = len(queue)
            for _ in range(size):
                cur = queue.popleft()
                cur.next = pre
                pre = cur
                if cur.right:
                    queue.append(cur.right)
                if cur.left:
                    queue.append(cur.left)
            pre = None

        return root


"""
Solution 2:

DFS

!! The tricky part is to connect nodes which have a different parent.
In order to to this, we need to pass the sibling of a node's parent to accomplish this

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        return self._connect(root, None)

    def _connect(self, root, parentSibling):
        if not root:
            return None

        if root.left:
            root.left.next = root.right

        if root.right:
            root.right.next = parentSibling.left if parentSibling else None

        self._connect(root.left, root.right)
        self._connect(root.right, root.right.next if root.right else None)

        return root


"""
Solution 2-1:
DFS Simplified

Time Complexity: O()
Space complexity : O()
"""


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        return self._connect(root, None)

    def _connect(self, root, parentSibling):
        if not root:
            return None

        root.next = parentSibling
        self._connect(root.left, root.right)
        self._connect(
            root.right, parentSibling.left if parentSibling else None)

        return root
