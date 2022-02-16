"""
Solution 1:
Bottom-Up DFS

Typical DFS.
Definition for the dfs would be find the unival subtrees in current tree, return the count and the actual uni value of subtree
Value cound be the actuall value for the node or None, none represents values in subtrees are different

Cases:
At every recursion, the initial res would be left subtree's count + right subtree's count
1. Leaf node, retutn 1, node.val
2. cur node has left node and right node:
    2.1 cur node's val equals left and right nodes' val, these nodes can combine and make a new substree, res + 1
    2.2 cur node's val doesn't equal left and right nodes' val, the res stay's the same as the initial result, and we will
    return res, None. The none would tell upper level node that the subtree is disconnected and we can't extend from the previous node
3. cur node has left node, no right node, in this case, we just check if cur node's val equals left node's val, if so, we can 
extend the left subtree to include cur node and add 1 to the result since we have a new subtree, otherwise we will return res, None, while none
simply tells the upper level node there is no chance you can connect with your subtree to create a new subtree with unival.
4. cur node has right node, no left node. Similar case like case 3


Time Complexity: O(n)
Space complexity : O(n)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)[0]

    def dfs(self, root):
        if not root:
            return 0, None

        if not root.left and not root.right:
            return 1, root.val

        left_cnt, left_val = self.dfs(root.left)
        right_cnt, right_val = self.dfs(root.right)
        res = left_cnt + right_cnt
        if root.left and root.right and left_val == root.val and left_val == right_val:
            return res + 1, left_val

        if root.left and not root.right and left_val == root.val:
            return res + 1, left_val
        if root.right and not root.left and right_val == root.val:
            return res + 1, right_val

        return res, None


"""
Solution 2-1:
!!Wrong Version!!

Time Complexity: O()
Space complexity : O()
"""


class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.isValidSubtree(root, 0)

        return self.res

    def isValidSubtree(self, root, parent_val):
        if not root:
            return True
        else:
            print(root.val)
        # For a boolean or expression, if the false statement is True, then we will not evaluate the second one
        if not self.isValidSubtree(root.left, root.val) or not self.isValidSubtree(root.right, root.val):
            return False

        self.res += 1

        return root.val == parent_val


"""
Solution 2-2:
Correct Version 

Time Complexity: O(n)
Space complexity : O(h) where h is the height of the tree
"""


class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.res = 0
        self.isValidSubtree(root, root.val)

        return self.res

    def isValidSubtree(self, root, parent_val):
        if not root:
            return True

        if not all([self.isValidSubtree(root.left, root.val), self.isValidSubtree(root.right, root.val)]):
            return False

        self.res += 1

        return root.val == parent_val
