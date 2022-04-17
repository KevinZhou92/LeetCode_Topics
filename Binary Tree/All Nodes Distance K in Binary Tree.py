"""
Solution 1:

BFS
Convert the tree to a graph and then do bfs on the graph starting from the target node.

A classical bfs problem

Time Complexity: O(N)
Space complexity : O(N)
"""


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root or not target:
            return []

        parentsMap = {}
        self.traverse(root, None, parentsMap)
        res = []
        queue = deque([target])
        visited = set([target])
        distance = 0
        while queue:
            size = len(queue)
            if distance == k:
                res.extend([node.val for node in queue])
                break
            for _ in range(size):
                cur = queue.popleft()
                for neighbour in [cur.left, cur.right, parentsMap[cur]]:
                    if neighbour and neighbour not in visited:
                        queue.append(neighbour)
                        visited.add(neighbour)
            distance += 1

        return res

    def traverse(self, root, parent, parentsMap):
        if not root:
            return

        parentsMap[root] = parent
        self.traverse(root.left, root, parentsMap)
        self.traverse(root.right, root, parentsMap)


"""
Solution 2:

DFS

Find target node:
If node == target, then we should add nodes that are distance K in the subtree rooted at target.
If target is in the left branch of node, say at distance L+1, then we should look for nodes that are distance K - L - 1 in the right branch.
If target is in the right branch of node, the algorithm proceeds similarly.
If target isn't in either branch of node, then we stop.

Time Complexity: O(N)
Space complexity : O(N)
"""


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root or not target:
            return []

       # Case 1, current node is target, we need to find node that is k distance from the target node
       # Case 2, targe is on left subtree, we need to find node on right tree that are k distance from the target node
       # Case 3, targe is on right subtree, we need to find node on left tree that are k distance from the target node
        res = []
        self.dfs(root, target, 0, k, res)

        return res

    def dfs(self, root, target, distance, k, res):
        if not root:
            return -1

        if root == target:
            self.subtree_add(root, 0, k, res)
            return 1

        leftDis = self.dfs(root.left, target, distance + 1, k, res)
        rightDis = self.dfs(root.right, target, distance + 1, k, res)

        if leftDis != -1:
            if leftDis == k:
                res.append(root.val)
            else:
                self.subtree_add(root.right, leftDis + 1, k, res)
                return leftDis + 1

        if rightDis != -1:
            if rightDis == k:
                res.append(root.val)
            else:
                self.subtree_add(root.left, rightDis + 1, k, res)
                return rightDis + 1

        return -1

    def subtree_add(self, root, dis, k, res):
        if not root:
            return

        if dis == k:
            res.append(root.val)
            return

        self.subtree_add(root.left, dis + 1, k, res)
        self.subtree_add(root.right, dis + 1, k, res)
