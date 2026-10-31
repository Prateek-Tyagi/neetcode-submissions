# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        current = head

        while current:
            next_node = current.next # save  - saving reference to next node
            current.next = prev # reverse - point current of next to prev node
            
            prev = current # move pre  - setting prev to curernt as we need to point backward
            current = next_node # move current - moving  - moving current pointer to next node
        
        return prev
        