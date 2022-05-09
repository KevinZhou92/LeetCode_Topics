"""
Solution 1:

DFS
If the leaf of a tree has 0 coins (an excess of -1 from what it needs), then we should push a coin from its parent onto the leaf. 
If it has say, 4 coins (an excess of 3), then we should push 3 coins off the leaf. 
In total, the number of moves from that leaf to or from its parent is excess = Math.abs(num_coins - 1). 
Afterwards, we never have to consider this leaf again in the rest of our calculation.

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.moves = 0
        self.moveCoins(root)

        return self.moves

    def moveCoins(self, root):
        if not root:
            return 0

        leftMoves = self.moveCoins(root.left)
        rightMoves = self.moveCoins(root.right)

        self.moves += abs(leftMoves) + abs(rightMoves)

        return leftMoves + rightMoves + root.val - 1
