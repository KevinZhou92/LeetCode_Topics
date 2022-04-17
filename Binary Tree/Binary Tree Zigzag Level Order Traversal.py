"""
Solution 1:

BFS
We can either revert a level altogether, or utilize the queue, we can add to head or tail of a queue in O(1)


Time Complexity: O(N) + O(logN)(list revert at every level) -> O(N)
Space complexity : O()
"""


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        res = []
        leftToRight = True
        while queue:
            size = len(queue)
            curLevelNodes = []
            for _ in range(size):
                cur = queue.popleft()
                curLevelNodes.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            if not leftToRight:
                curLevelNodes = curLevelNodes[::-1]
            res.append(curLevelNodes)
            leftToRight = not leftToRight

        return res


"""
Solution 2:

DFS
PreOrder/InOrder/PostOrder


Time Complexity: O(N)
Space complexity : O(N)
"""


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        levelMap = defaultdict(deque)
        self.dfs(root, 0, levelMap)

        return [levelMap[level] for level in sorted(levelMap.keys())]

    def dfs(self, root, level, levelMap):
        if not root:
            return

        if level % 2 == 0:
            levelMap[level].append(root.val)
        else:
            levelMap[level].appendleft(root.val)

        self.dfs(root.left, level + 1, levelMap)
        self.dfs(root.right, level + 1, levelMap)


"""
Solution 2-2:

DFS Iterative
This is tricky, we need to modify the preorder traversal of a binary tree and we need to be sure what is the termination requirement.
We will always check if the node is none or not and we will decide if we should proceed or not.


Time Complexity: O(N)
Space complexity : O(N)
"""


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        levelMap = defaultdict(deque)
        stack = []
        curPair = [root, 0]
        # PreOrderTraversal
        while curPair[0] or stack:
            while curPair[0]:
                if curPair[1] % 2 == 0:
                    levelMap[curPair[1]].append(curPair[0].val)
                else:
                    levelMap[curPair[1]].appendleft(curPair[0].val)

                stack.append(curPair)
                curPair = [curPair[0].left, curPair[1] + 1]
            prePair = stack.pop()
            if not prePair:
                continue
            curPair = [prePair[0].right, prePair[1] + 1]

        return [levelMap[level] for level in sorted(levelMap.keys())]
