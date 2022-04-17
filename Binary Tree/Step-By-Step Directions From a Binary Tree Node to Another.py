"""
Solution 1:

BFS
Enumerate all the possible path and find the shortest one


Time Complexity: O(N) ?
Space complexity : O(N)

TLE!!!
"""


class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        if not root:
            return None

        parentMap = {}
        self.dfs(root, None, parentMap)
        startNode = [node for node in parentMap.keys() if node.val ==
                     startValue][0]
        destNode = [node for node in parentMap.keys() if node.val ==
                    destValue][0]

        queue = deque([[startNode, [], set()]])
        res = None
        while queue:
            size = len(queue)
            for _ in range(size):
                curNode, path, visited = queue.popleft()
                for neighbor in [curNode.left, curNode.right, parentMap[curNode]]:
                    if neighbor and neighbor not in visited:
                        newPath = copy.copy(path)
                        if neighbor == curNode.left:
                            newPath.append('L')
                        elif neighbor == curNode.right:
                            newPath.append('R')
                        else:
                            newPath.append('U')
                        visited.add(neighbor)
                        queue.append([neighbor, newPath, visited])

                        if neighbor.val == destValue:
                            res = newPath
                            break

        return ''.join(res)

    def dfs(self, root, parent, parentMap):
        if not root:
            return

        parentMap[root] = parent
        self.dfs(root.left, root, parentMap)
        self.dfs(root.right, root, parentMap)


"""
Solution 1-2:

BFS Improved

We don't need to store a separate visited set for each path. BFS is usually used to solve shortest path problem, if a node is visited by a previous node,
we don't need to visit this node again, cause it will not be a shorter path than the previous node's path

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        if not root:
            return None

        parentMap = {}
        self.dfs(root, None, parentMap)
        startNode = [node for node in parentMap.keys() if node.val ==
                     startValue][0]
        destNode = [node for node in parentMap.keys() if node.val ==
                    destValue][0]

        queue = deque([[startNode, '']])
        visited = set([startNode])
        res = None
        while queue:
            size = len(queue)
            for _ in range(size):
                curNode, path = queue.popleft()
                if curNode.left and curNode.left not in visited:
                    visited.add(curNode.left)
                    queue.append([curNode.left, path + 'L'])
                if curNode.right and curNode.right not in visited:
                    visited.add(curNode.right)
                    queue.append([curNode.right, path + 'R'])
                if parentMap[curNode] and parentMap[curNode] not in visited:
                    visited.add(parentMap[curNode])
                    queue.append([parentMap[curNode], path + 'U'])

                if curNode.val == destValue:
                    res = path
                    break

        return ''.join(res)

    def dfs(self, root, parent, parentMap):
        if not root:
            return

        parentMap[root] = parent
        self.dfs(root.left, root, parentMap)
        self.dfs(root.right, root, parentMap)


"""
Solution 2:

DFS

Use LCA to solve the problem
https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/submissions/

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        if not root:
            return None

        self.path = None
        self.findPath(root, startValue, [])
        leftPath = self.path
        self.findPath(root, destValue, [])
        rightPath = self.path
        print(leftPath, rightPath)

        commonLength = self.findCommonLength(leftPath, rightPath)

        leftPath = leftPath[commonLength:]
        rightPath = rightPath[commonLength:]
        leftPath = ''.join(leftPath).replace("L", "U").replace("R", "U")
        rightPath = ''.join(rightPath)

        return leftPath + rightPath

    def findCommonLength(self, leftPath, rightPath):
        index = 0
        while index < len(leftPath) and index < len(rightPath):
            if leftPath[index] == rightPath[index]:
                index += 1
            else:
                break

        return index

    def findPath(self, root, targetValue, res):
        if not root:
            return

        if root.val == targetValue:
            self.path = copy.copy(res)
            return

        if root.left:
            res.append("L")
            self.findPath(root.left, targetValue, res)
            res.pop()

        if root.right:
            res.append("R")
            self.findPath(root.right, targetValue, res)
            res.pop()
