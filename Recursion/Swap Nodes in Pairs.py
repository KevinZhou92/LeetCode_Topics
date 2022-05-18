"""
Solution 1:

Recursion

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        nextNode = head.next
        head.next = self.swapPairs(nextNode.next)
        nextNode.next = head

        return nextNode


"""
Solution 2:

Iterative Approach

Time Complexity: O(n)
Space complexity : O(1)
"""


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy

        while head and head.next:
            firstNode = head
            secondNode = head.next

            prev.next = secondNode
            firstNode.next = secondNode.next
            secondNode.next = firstNode

            prev = firstNode
            head = firstNode.next

        return dummy.next
