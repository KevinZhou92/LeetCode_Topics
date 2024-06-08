"""
Solution 1:
Loop over two lists simultaneously and construct a new linkedlist

The key here is the order of two words are determined by the first different letter in two words

Time Complexity: O(n)
Space complexity : O(1)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-1)
        cur = head
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        
        while list1:
            cur.next = list1
            list1 = list1.next
            cur = cur.next

        while list2:
            cur.next = list2
            list2 = list2.next
            cur = cur.next 
        
        return head.next
        