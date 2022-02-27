"""
Solution 1:

Iterative Approach, on level N-1, process nodes on leven N

The tricky part of this problem is that it's not a perfect binary tree, so we need to use additional
variables to represent the last none null node in level N.


Time Complexity: O(n)
Space complexity : O(1)
"""


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        leftMost = root
        lastNoneNullNode = None
        nextLeftMost = None
        while leftMost:
            nextLeftMost = self.getNextLeftMost(leftMost)
            cur = leftMost
            while cur:
                # connect node with same parent
                if cur.left:
                    if lastNoneNullNode:
                        lastNoneNullNode.next = cur.left
                    cur.left.next = cur.right
                    lastNoneNullNode = cur.left
                if cur.right:
                    if lastNoneNullNode:
                        lastNoneNullNode.next = cur.right
                    if cur.next:
                        cur.right.next = cur.next.left
                    lastNoneNullNode = cur.right
                cur = cur.next
            leftMost = nextLeftMost
            lastNoneNullNode = None

        return root

    def getNextLeftMost(self, cur):
        res = None
        while cur:
            if cur.left:
                res = cur.left
                break
            if cur.right:
                res = cur.right
                break
            cur = cur.next

        return res


"""
Solution 2:

BFS

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        queue = deque([root])
        while queue:
            size = len(queue)
            for index in range(size):
                cur = queue.popleft()
                if index != size - 1:
                    cur.next = queue[0]

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

        return root


"""
Solution 1-1:

Iterative Approach with dummy head on each level
https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/solution/bfsjie-jue-zui-hao-de-ji-bai-liao-100de-yong-hu-by/

Time Complexity: O(n)
Space complexity : O1)
"""


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        leftMost = root
        while leftMost:
            lastNoneNullNode = Node(None)
            head = lastNoneNullNode
            cur = leftMost
            while cur:
                # connect node with same parent
                if cur.left:
                    lastNoneNullNode.next = cur.left
                    lastNoneNullNode = cur.left
                if cur.right:
                    lastNoneNullNode.next = cur.right
                    lastNoneNullNode = cur.right
                cur = cur.next
            leftMost = head.next

        return root


"""
Solution 1-2:

Leetcode Solution
https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/solution/

Time Complexity: O(n)
Space complexity : O(1)
"""
