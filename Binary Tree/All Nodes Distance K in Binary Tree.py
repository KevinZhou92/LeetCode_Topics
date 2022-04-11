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
