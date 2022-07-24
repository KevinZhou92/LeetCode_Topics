"""
Solution 1:

Iterative

Time Complexity: O(n)
Space complexity : O(n)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return None

        head = dummy = ListNode(-1)
        addition = 0
        while l1 and l2:
            sumVal = l1.val + l2.val + addition
            newNode = ListNode(sumVal % 10)
            addition = sumVal // 10
            head.next = newNode
            head = newNode
            l1 = l1.next
            l2 = l2.next

        while l1:
            sumVal = l1.val + addition
            newNode = ListNode(sumVal % 10)
            addition = sumVal // 10
            head.next = newNode
            head = newNode
            l1 = l1.next

        while l2:
            sumVal = l2.val + addition
            newNode = ListNode(sumVal % 10)
            addition = sumVal // 10
            head.next = newNode
            head = newNode
            l2 = l2.next

        if addition != 0:
            newNode = ListNode(addition)
            head.next = newNode
            head = newNode

        return dummy.next


"""
Solution 1-2:

Concise Iterative Solution

Time Complexity: O(n)
Space complexity : O(n)
"""


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return None

        head = dummy = ListNode(-1)
        carry = 0
        while l1 or l2 or carry:
            sumVal = 0
            sumVal += l1.val if l1 else 0
            sumVal += l2.val if l2 else 0
            sumVal += carry
            newNode = ListNode(sumVal % 10)
            carry = sumVal // 10
            head.next = newNode
            head = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
