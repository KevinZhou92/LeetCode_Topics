"""
Solution 1:

BFS

Time Complexity: O(n)
Space complexity : O(n)

Problem: TLE

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []
        if not root:
            return '[]'

        queue = deque([root])
        maxDepth = 0
        while queue:
            maxDepth += 1
            size = len(queue)
            for _ in range(size):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

        queue = deque([root])
        depth = 0
        while queue:
            depth += 1
            if depth > maxDepth:
                break
            size = len(queue)
            for _ in range(size):
                cur = queue.popleft()
                res.append(str(cur.val) if cur else 'null')
                if not cur:
                    queue.append(None)
                    queue.append(None)
                else:
                    queue.append(cur.left)
                    queue.append(cur.right)

        return '[' + ','.join(res) + ']'

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data or data == '[]':
            return None

        data = data[1:-1].split(',')

        root = TreeNode(int(data[0]))
        queue = deque([root])
        curIndex = 1
        while queue:
            size = len(queue)
            if curIndex >= len(data):
                break
            for offset in range(size):
                cur = queue.popleft()
                if not cur:
                    curIndex += 2
                    queue.append(None)
                    queue.append(None)
                else:
                    cur.left = TreeNode(
                        int(data[curIndex])) if data[curIndex] != 'null' else None
                    queue.append(cur.left)
                    curIndex += 1
                    cur.right = TreeNode(
                        int(data[curIndex])) if data[curIndex] != 'null' else None
                    queue.append(cur.right)
                    curIndex += 1

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


"""
Solution 1-2:

BFS

Without additional calculation for the depth of the tree.

Time Complexity: O(n)
Space complexity : O(n)
"""


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []
        if not root:
            return '[]'

        queue = deque([root])
        while queue:
            nonNull = False
            size = len(queue)
            for _ in range(size):
                cur = queue.popleft()
                res.append(str(cur.val) if cur else 'null')
                if cur:
                    if cur.left or cur.right:
                        nonNull = True
                    queue.append(cur.left)
                    queue.append(cur.right)

            if not nonNull:
                break

        return '[' + ','.join(res) + ']'

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data or data == '[]':
            return None

        data = data[1:-1].split(',')
        root = TreeNode(int(data[0]))
        queue = deque([root])
        curIndex = 1
        while queue:
            size = len(queue)
            if curIndex >= len(data):
                break
            for offset in range(size):
                cur = queue.popleft()
                if cur:
                    cur.left = TreeNode(
                        int(data[curIndex])) if data[curIndex] != 'null' else None
                    queue.append(cur.left)
                    curIndex += 1
                    cur.right = TreeNode(
                        int(data[curIndex])) if data[curIndex] != 'null' else None
                    queue.append(cur.right)
                    curIndex += 1

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
