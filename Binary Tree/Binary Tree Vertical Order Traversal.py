"""

The tricky part of this question with DFS solution is:
For example, 

Level
-2 -1   0     1   2
        3
       / \
      /   \
     /     \
    /       \
   /         \
  9           8
 / \         / \
4   0       1   7
     \     /
      2   5

If we are using preorder traversal(root-left right), then for the vertical level 1, which contains nodes 8 and 2, we will have a list
like [2, 8], because dfs will traverse left tree first, therefore produce incorrect result.

"""

"""
Solution 1:

BFS
https://leetcode.com/problems/binary-tree-vertical-order-traversal/solution/

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        vOrderMap = defaultdict(list)
        queue = deque([[root, 0]])
        while queue:
            size = len(queue)
            for _ in range(size):
                node, vLevel = queue.popleft()
                vOrderMap[vLevel].append(node.val)
                if node.left:
                    queue.append([node.left, vLevel - 1])
                if node.right:
                    queue.append([node.right, vLevel + 1])

        res = []
        minLevel, maxLevel = min(vOrderMap.keys()), max(vOrderMap.keys())
        for index in range(minLevel, maxLevel + 1):
            res.append(vOrderMap[index])

        return res
