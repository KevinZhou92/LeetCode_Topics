"""
Solution 1:

BFS

Build a map that has each node as key and each node's parent as value. Find all the leaf nodes,
find their parents, nullify the parent's left and right pointers and if the parent becomes a leaf node.
Add the new leaf node to a new list which will be iterated next turn. Do it until we cleaned all the nodes.

Time Complexity: O(n)
Space complexity : O(n)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        leafParent = {root: root}
        queue = deque([root])
        leafNodes = []
        while queue:
            cur = queue.popleft()
            if cur.left:
                leafParent[cur.left] = cur
                queue.append(cur.left)
            if cur.right:
                leafParent[cur.right] = cur
                queue.append(cur.right)
            if not cur.left and not cur.right:
                leafNodes.append(cur)

        res = []
        queue = deque(leafNodes)
        while queue:
            size = len(queue)
            curLeaves = []
            for _ in range(size):
                leaf = queue.popleft()
                curLeaves.append(leaf.val)
                parent = leafParent[leaf]
                if parent == leaf:
                    continue
                if parent.left == leaf:
                    parent.left = None
                if parent.right == leaf:
                    parent.right = None

                if not parent.left and not parent.right:
                    queue.append(parent)
            res.append(curLeaves)

        return res


"""
Solution 2:

DFS
Postorder Traversal.

This question is the opposite of a typicaly tree height problem.
A typical tree height problem is asking you to find the height of the tree from the root node.
However, this question asks us to remove leaf node first, so it want us to start from the leaf node.
All the leaf node will have height 0. So we need to calculate a node height from the leaf node and we will
pick the max height from left and right tree since a node only becomes a leaf node if its left child and right
chile are none.

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        leafMap = defaultdict(list)

        maxHeight = self.findMaxHeight(root, leafMap)
        res = []
        for height in range(0, maxHeight):
            res.append(leafMap[height])

        return res

    def findMaxHeight(self, root, leafMap):
        if not root:
            return 0

        leftHeight = self.findMaxHeight(root.left, leafMap)
        rightHeight = self.findMaxHeight(root.right, leafMap)
        maxHeight = max(leftHeight, rightHeight)
        leafMap[maxHeight].append(root.val)

        return maxHeight + 1
