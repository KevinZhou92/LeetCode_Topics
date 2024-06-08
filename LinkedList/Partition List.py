"""
Solution 1:
Use dummy node to create two new list, and concatenate two list after partition


Key is to break the connection in original list to avoid loop
Time Complexity: O(n)
Space complexity : O(1)
"""
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None
        small_dummy = ListNode(-1)
        large_dummy = ListNode(-1)
        small_tail = small_dummy
        large_tail = large_dummy
        while head:
            if head.val < x:
                small_tail.next = head
                small_tail = small_tail.next
            else:
                large_tail.next = head
                large_tail = large_tail.next
            tmp = head.next
            head.next = None
            head = tmp

        if small_tail:
            small_tail.next = large_dummy.next
        
        return small_dummy.next
