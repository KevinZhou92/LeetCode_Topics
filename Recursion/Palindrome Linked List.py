"""
Solution 1:

Recursion

PostOrder Recursion

This solution utilize the characteristic of recursion. The key idea is to compare from head 
and tail simultaneously. They way we can achieve this is by keeping a global pointer to the head,
and visit node in reverse order by doing post order recursion.

Time Complexity: O()
Space complexity : O()
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # the key here is to traverse the list from start and end simultaneously
        # we keep a global variable that tracks the head of the list
        self.frontPointer = head
        return self.check(head)

    def checkReversely(self, currentPointer):
        if not currentPointer:
            return True

        # find the tail, compare
        # if equal, move head pointer to next
        # return to upper level for next comparsion
        # else, return false
        if not self.checkReversely(currentPointer.next):
            return False
        if currentPointer.val != self.frontPointer.val:
            return False
        self.frontPointer = self.frontPointer.next

        return True


"""
Solution 2:

Iterative

Get the length of the linkedlist and then reverse the second half.

!!! Becare for the edge case, like if there is only 1 node in the linkedlist

Time Complexity: O(n)
Space complexity : O(1)
"""


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # need to change the linkedlist in place so that
        # we can traverse from front and back simultaneously
        if not head or not head.next:
            return True

        length = self.getLength(head)
        tail = self.getTail(head, length)
        return self.checkPalindrome(head, tail)

    def getLength(self, head):
        count = 0
        while head:
            count += 1
            head = head.next

        return count

    def checkPalindrome(self, head, tail):
        while head and tail:
            if head.val != tail.val:
                return False
            head = head.next
            tail = tail.next

        if head or tail:
            return False

        return True

    def getTail(self, head, length):
        count = length // 2 - 1
        pivot = head
        while count > 0:
            count -= 1
            pivot = pivot.next

        tail = pivot.next
        if length % 2 == 0:
            pivot.next = None

        prev = None
        while tail.next:
            next = tail.next
            tail.next = prev
            prev = tail
            tail = next

        tail.next = prev

        return tail


"""
Solution 2-2:

Tow Pointer

Note here we don't need to produce two perfecly structured linkedlist, which means we break the connection
between some nodes to generate two disconnected linkedlists.

We just need to make sure we break the original linkedlist evenly so that we compare from head and tail
correctly. We will use the node from the tail side as the anchor. As long as we finish iterating over the nodes
from the tail. We could call it as a palindrome

Time Complexity: O(n)
Space complexity : O(1)
"""


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # two pointer to find the mid pointer
        # then revert the linkedlist and check if it's palindrome
        if not head or not head.next:
            return True

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if fast:
            slow = slow.next

        tail = self.reverse(slow)
        return self.checkPalindrome(head, tail)

    def reverse(self, head):
        if not head:
            return None

        prev = None
        while head.next:
            next = head.next
            head.next = prev
            prev = head
            head = next
        head.next = prev

        return head

    def checkPalindrome(self, head, tail):
        while tail:
            if head.val != tail.val:
                return False
            head = head.next
            tail = tail.next

        return True
