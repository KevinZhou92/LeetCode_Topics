"""
Solution 1:

DFS

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        leftCount = self.countNodes(root.left)
        rightCount = self.countNodes(root.right)
        return leftCount + rightCount + 1


"""
Solution 2:

DFS Improved

Time Complexity: O(logn * logn)
Space complexity : O(logn * logn

!!!!Bitwise operation will be calculated after plus or minus

https://leetcode.wang/leetcode-222-Count-Complete-Tree-Nodes.html)
https://labuladong.github.io/algo/2/19/45/
https://leetcode.cn/problems/count-complete-tree-nodes/solution/wan-quan-er-cha-shu-de-jie-dian-ge-shu-by-leetco-2/
"""


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left, right = 0, 0
        leftNode = root
        while leftNode.left:
            left += 1
            leftNode = leftNode.left

        rightNode = root
        while rightNode.right:
            right += 1
            rightNode = rightNode.right

        if left == right:
            return (1 << (left + 1)) - 1
        else:
            return self.countNodes(root.left) + self.countNodes(root.right) + 1
