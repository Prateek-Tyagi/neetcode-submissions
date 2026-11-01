# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the mid and divide the list into two
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        second_half = slow.next
        slow.next = None

        # reverse the second half of the list
        
        prev = None
        current = second_half

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        second_half = prev

        # merge both of the list alternativly.

        first = head
        second = second_half
        while second:
        # save the refernce to next part of list
            temp1 = first.next
            temp2 = second.next

            # assignment
            first.next = second
            second.next = temp1

            # moving first and second node
            first = temp1
            second = temp2


        