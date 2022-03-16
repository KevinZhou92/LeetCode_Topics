"""
Solution 1:

DFS

Flatten left and right subtrees first and then connect the tail of left subtree to the head of right subtree

!!!Note: Be careful about edge case, for example, if there is no left subtree

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        self.flatten(root)

        return None

    def flattenTree(self, root):
        if not root:
            return None

        if not root.left and not root.right:
            return root

        leftTail = self.flattenTree(root.left)
        rightTail = self.flattenTree(root.right)
        if leftTail:
            leftTail.right = root.right
            root.right = root.left
        root.left = None

        return rightTail if rightTail else leftTail


"""
Solution 1-2:

Iterative approach


Time Complexity: O(n)
Space complexity : O(n)
"""
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        
        BOTH_UNVISITED = 0
        LEFT_VISITED = 1
        RIGHT_VISITED = 2
        
        tailNode = None  
        stack = [[root, BOTH_UNVISITED]]
        while stack:
            cur, state = stack[-1]
            if state == BOTH_UNVISITED:
                stack[-1][1] = LEFT_VISITED
                if cur.left:
                    stack.append([cur.left, BOTH_UNVISITED])
                tailNode = cur
            elif state == LEFT_VISITED:
                stack[-1][1] = RIGHT_VISITED
                if tailNode:
                    tailNode.right = cur.right
                if cur.right:
                    stack.append([cur.right, BOTH_UNVISITED])
                    tailNode = cur.right
                if cur.left:
                    cur.right = cur.left
                cur.left = None
            else:
                stack.pop()
        
        return root
                