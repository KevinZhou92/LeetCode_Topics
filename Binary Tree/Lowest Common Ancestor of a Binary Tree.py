"""
Solution 1:

DFS

Try to search p and q in subtrees, if found, return the node. There are two cases:
1. Two nodes share a common ancestor
2. One node is the descendant of the other one 

Write the recursive call according to these two cases.

Time Complexity: O(n)
Space complexity : O(n)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        if root.val == p.val or root.val == q.val:
            return root

        leftRes = self.lowestCommonAncestor(root.left, p, q)
        rightRes = self.lowestCommonAncestor(root.right, p, q)

        if leftRes and rightRes:
            return root

        if leftRes:
            return leftRes

        if rightRes:
            return rightRes

        return None


"""
Solution 2:

Iterative Approach

1. BFS to traverse the tree, use an additional map to record each node's parent

Construct a parent list for p and q separately by the parents map we just built and then loop over the list,
both p and q should share some command ancestor, we need to find the last common ancestor

Time Complexity: O()
Space complexity : O()
"""


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        parent_map = {}
        queue = deque([root])
        while queue:
            size = len(queue)
            for _ in range(size):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                    parent_map[cur.left] = cur
                if cur.right:
                    queue.append(cur.right)
                    parent_map[cur.right] = cur
            if p in parent_map and q in parent_map:
                break

        p_parents = self.getAllParents(p, parent_map)
        q_parents = self.getAllParents(q, parent_map)

        index = 0
        res = None
        while index < len(p_parents) and index < len(q_parents):
            if p_parents[index] != q_parents[index]:
                break
            res = p_parents[index]
            index += 1

        return res

    def getAllParents(self, cur, parent_map):
        res = []
        while cur in parent_map:
            res.append(cur)
            cur = parent_map[cur]
        res.append(cur)

        return res[::-1]


"""
Solution 2-1:

Simplified Iteravice Solution

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        parent_map = {root: None}
        queue = deque([root])
        while queue:
            size = len(queue)
            for _ in range(size):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                    parent_map[cur.left] = cur
                if cur.right:
                    queue.append(cur.right)
                    parent_map[cur.right] = cur
            if p in parent_map and q in parent_map:
                break

        ancestors = set()
        while p in parent_map:
            ancestors.add(p)
            p = parent_map[p]

        while q not in ancstors:
            q = parent_map[q]

        return q


"""
Solution 3:

Get rid of the backtracking process in Solution 2-1.
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/

A little bit tricky to think of 


Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    BOTH_UNVISITED = 0
    LEFT_VISITED = 1
    RIGHT_VISITED = 2

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        stack = [[root, Solution.BOTH_UNVISITED]]
        firstNodeFound = False
        LCAIndex = None
        while stack:
            cur, cur_state = stack[-1]
            if cur_state != Solution.RIGHT_VISITED:
                if cur_state == Solution.BOTH_UNVISITED:
                    if cur == p or cur == q:
                        if not firstNodeFound:
                            firstNodeFound = True
                            LCAIndex = len(stack) - 1
                        else:
                            return stack[LCAIndex][0]

                    child_node = cur.left
                else:
                    child_node = cur.right

                stack[-1][1] += 1
                if child_node:
                    stack.append([child_node, Solution.BOTH_UNVISITED])

            else:
                if firstNodeFound and LCAIndex == len(stack) - 1:
                    LCAIndex -= 1
                stack.pop()

        return None
