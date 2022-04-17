"""
Solution 1:

BFS
TLE, this approach is problem because we are enqueue all nodes in a full binary tree, even though the nodes are none.

Time Complexity: O(N)
Space complexity : O(N)
"""


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        res = float('-inf')
        queue = deque([root])
        while queue:
            size = len(queue)
            firstIndex = None
            lastIndex = None
            allNone = True
            for index in range(size):
                cur = queue.popleft()
                if not cur:
                    queue.append(None)
                    queue.append(None)
                else:
                    allNone = False
                    if firstIndex == None:
                        firstIndex = lastIndex = index
                    else:
                        lastIndex = index
                    queue.append(cur.left)
                    queue.append(cur.right)
            if firstIndex != None and lastIndex != None:
                res = max(res, lastIndex - firstIndex + 1)
            else:
                break

            if allNone:
                break

        return res


"""
Solution 2:

BFS utilizing the characteristic of a binary tree.

As we know, for a full binary tree, the number of nodes double at each level, since each parent node has two child nodes. Naturally, the range of our node index would double as well.

If the index of a parent node is C, accordingly we can define the index of its left child node as 2C and the index of its right child node as 2C + 1

We only need to check for non-null nodes, assign them a index and then find the max value.

Time Complexity: O()
Space complexity : O()
"""


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        res = float('-inf')
        queue = deque([[root, 0]])
        while queue:
            size = len(queue)
            headIndex = queue[0][1]
            for _ in range(size):
                cur, index = queue.popleft()
                if cur.left:
                    queue.append([cur.left, 2 * index])
                if cur.right:
                    queue.append([cur.right, 2 * index + 1])
            res = max(res, index - headIndex + 1)

        return res


"""
Solution 3:

DFS

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        levelMap = defaultdict(list)
        self.dfs(root, 0, 0, levelMap)
        res = float('-inf')
        for level in levelMap.keys():
            res = max(res, max(levelMap[level]) - min(levelMap[level]) + 1)

        return res

    def dfs(self, root, level, colIndex, levelMap):
        if not root:
            return

        levelMap[level].append(colIndex)
        if root.left:
            self.dfs(root.left, level + 1, 2 * colIndex, levelMap)
        if root.right:
            self.dfs(root.right, level + 1, 2 * colIndex + 1, levelMap)
