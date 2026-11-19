# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        while n > 0:
            first = first.next
            n -= 1
        if not first:
            return None
        second = ListNode(next=head)
        while first:
            first = first.next
            second = second.next
        second_next = second.next.next
        second.next = second_next
        return head