"""
Solution 1:

Iterative

Time Complexity: O(n + m)
Space complexity : O(1)
"""


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2

        if not list2:
            return list1

        dummy = ListNode(-1)
        head = dummy
        while list1 and list2:
            if list1.val > list2.val:
                head.next = list2
                list2 = list2.next
            else:
                head.next = list1
                list1 = list1.next
            head = head.next

        while list1:
            head.next = list1
            list1 = list1.next
            head = head.next

        while list2:
            head.next = list2
            list2 = list2.next
            head = head.next

        return dummy.next


"""
Solution 2:

Recursion

!!!Make sure you know where the pointer is pointing to

Time Complexity: O(n + m)
Space complexity : O(n + m)
"""


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2

        if not list2:
            return list1

        head = list1 if list1.val < list2.val else list2
        newList1 = list1.next if list1.val < list2.val else list1
        newList2 = list2 if list1.val < list2.val else list2.next
        head.next = self.mergeTwoLists(newList1, newList2)

        return head
