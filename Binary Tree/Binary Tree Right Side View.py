"""
Solution 1:

DFS
Added a map to recorde how many nodes are at each level from left to right. Not very space efficient
We just need to know about the right most node


Time Complexity: O(n)
Space complexity : O(n)
"""
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        
        levelNodes = defaultdict(list)
        self.levelTraversal(root, 0, levelNodes)
        
        maxLevel = max(levelNodes.keys())
        for level in range(0, maxLevel + 1):
            res.append(levelNodes[level][-1])
            
        return res
    
    def levelTraversal(self, root, level, levelNodes):
        if not root:
            return
        
        levelNodes[level].append(root.val)
        self.levelTraversal(root.left, level + 1, levelNodes)
        self.levelTraversal(root.right, level + 1, levelNodes)

"""
Solution 2:

BFS
Alwasy add the right most node to the res at each level

Time Complexity: O(N)
Space complexity : O(N) precisely the diameter of the tree, max will be N/2
"""
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        
        queue = deque([root])
        while queue:
            size = len(queue)
            for index in range(size):
                cur = queue.popleft()
                if index == size - 1:
                    res.append(cur.val)
                    
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        
        return res