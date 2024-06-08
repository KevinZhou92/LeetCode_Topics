"""
Solution 1:
PriorityQueue + Dummy Head

The tricky thing here is to understand how to write a custom comparator for PQ


Time Complexity: O(NlogK)
Space complexity : O(n) for create a new linked list, O(k) for priority queue
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class HeapNode:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        # Define comparison based on ListNode's value
        return self.node.val < other.node.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        dummy = ListNode(-1)
        tail = dummy
        
        pq = []
        for head in lists:
            if not head:
                continue
            heapq.heappush(pq, HeapNode(head))
        
        while pq:
            heap_node = heappop(pq)
            node = heap_node.node
            tail.next = node
            tail = tail.next
            if node.next:
                heapq.heappush(pq, HeapNode(node.next))
            
        return dummy.next
        