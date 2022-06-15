"""
Solution 1:

DFS

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

"""
Solution 2:

Iterative
Use a deque to enque and deque each node pair and compare each of them.

Time Complexity: O(n)
Space complexity : O(n)
"""
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:        
        queue = deque([(p, q)])
        while queue:
            # pop corresponding node and compare value
            node1, node2 = queue.popleft()
            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            queue.append((node1.left, node2.left))
            queue.append((node1.right, node2.right))
        
        return True

"""
Solution 2-2:

Iterative Approach
Using a stack

Time Complexity: O(n)
Space complexity : O(n)
"""
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:        
        stack = [(p, q)]
        
        while stack:
            node1, node2 = stack.pop()
            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            stack.append((node1.left, node2.left))
            stack.append((node1.right, node2.right))
        
        return True