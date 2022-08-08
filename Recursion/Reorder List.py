"""
Solution 1:

Reverse Second Half and Merge List
Two Pointers to Find the Mid Point and then revert the second half and then connect two list

Time Complexity: O(n)
Space complexity : O(1)
"""
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        secondHead = slow.next
        slow.next = None
        
        prev = None
        while secondHead and secondHead.next:
            nextNode = secondHead.next
            secondHead.next = prev
            prev = secondHead
            secondHead = nextNode
        secondHead.next = prev
        
        while head and secondHead:
            nextHead = head.next
            nextSecondHead = secondHead.next
            head.next = secondHead
            secondHead.next = nextHead
            head = nextHead
            secondHead = nextSecondHead
            
        return