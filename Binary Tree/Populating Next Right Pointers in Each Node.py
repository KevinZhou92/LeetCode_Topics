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


"""
Solution 3:

Iterative Approach, this is a perfect binary tree, which makes the problem easier
If we connect nodes on level N on level N-1, the nodes on level N will become a linkedlist

We only move on to the level N+1 when we are done establishing the next pointers for the level N. 
So, since we have access to all the nodes on a particular level via the next pointers, 
we can use these next pointers to establish the connections for the next level or the level containing their children.

Time Complexity: O(n)
Space complexity : O(1)
"""


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        leftMost = root
        while leftMost.left:
            cur = leftMost
            while cur:
                # nodes with same parent
                cur.left.next = cur.right
                # nodes with different parents
                if cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            leftMost = leftMost.left

        return root


"""
Solution 3-1:

Iterative Approach, no need to use a stack, make use of the next pointer, we will connect all nodes
at level N in level N-1


Time Complexity: O(n)
Space complexity : O(1)
"""


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        leftMost = root
        nextLeftMost = None
        while leftMost:
            nextLeftMost = None
            cur = leftMost
            # iterate nodes on same level to find the left most node in the next level
            while cur:
                if cur.left:
                    nextLeftMost = cur.left
                    break
                elif cur.right:
                    nextLeftMost = cur.right
                    break
                cur = cur.next

            cur = leftMost
            while cur:
                # nodes with same parent
                if cur.left:
                    cur.left.next = cur.right
                # nodes with different parent
                if cur.right and cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next

            leftMost = nextLeftMost

        return root
