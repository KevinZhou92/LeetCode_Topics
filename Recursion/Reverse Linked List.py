"""
Solution 1:

DFS

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        return self.reverse(head)[0]

    def reverse(self, head):
        if not head or not head.next:
            return head, head

        newHead, newTail = self.reverse(head.next)
        head.next = None
        newTail.next = head

        return newHead, head


"""
Solution 2:

Iterative
!!! Edge Cases, make sure you are aware of which node head is pointing to


Time Complexity: O(n)
Space complexity : O(1)
"""


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        prev = None
        while head:
            nextNode = head.next
            head.next = prev
            prev = head
            head = nextNode

        return prev
