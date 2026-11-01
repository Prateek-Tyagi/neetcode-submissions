# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # this approach uses a min heap
        heap = []
        if not list:
            return None
        # push every first node of each list to min heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val,i, node))
        
        # declear a dummy node to start a new list
        dummy = ListNode(0)
        tail = dummy

        # pop from heap till its empty
        while heap:
            # popping gets you smallest node - value and its index
            value, i, node = heapq.heappop(heap)

            # add this smallest node to tail of next node and update tail
            tail.next = node
            tail = tail.next
            
            # if this is not last node, push next node to heap
            if node.next:
                heapq.heappush(heap,(node.next.val, i, node.next))

        # return the dummy next of the new list
        return dummy.next