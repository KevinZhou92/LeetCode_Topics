"""
Solution 1:

Recursion.

Time consuming + Space Consuming

Time Complexity: O(nk)
Space complexity : O(n)
"""
class ListNode:
    def __init__(self, val):
        self.val = val
        
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if k == 1:
            return n
        
        head = tail = ListNode(1)
        for i in range(2, n + 1):
            tail.next = ListNode(i)
            tail = tail.next
        tail.next = head
        
        return self.findWinner(n, k - 1, head)
    
    def findWinner(self, numOfPlayers, k, head):
        if numOfPlayers == 1:
            return head.val
        
        count = k
        while count > 1:
            head = head.next
            count -= 1
        
        nextHead = head.next.next
        head.next = nextHead
        
        return self.findWinner(numOfPlayers - 1, k, nextHead)
    
"""
Solution 1-2:

Recursion

Joseph Ring(https://leetcode.cn/problems/find-the-winner-of-the-circular-game/solution/java-yue-se-fu-huan-xiang-jie-bao-zheng-v3pwo/)

Time Complexity: O(n)
Space complexity : O(n)
"""
