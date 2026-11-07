# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        # a node before the first node of the group
        group_prev = dummy

        while True:
            # find the kth node
            kth = group_prev
            for _ in range(k):
                kth = kth.next

                if not kth:
                    return dummy.next
        
            # save the next group start
            next_group = kth.next

            # save the original head = it becomes tail when reversed
            group_start = group_prev.next

            # reverse the current group
            prev = next_group
            current = group_start

            while current != next_group:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            
            # reconnect and advance
            group_prev.next = prev
            group_prev = group_start

