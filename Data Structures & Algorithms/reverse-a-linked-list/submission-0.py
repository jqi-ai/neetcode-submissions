# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed_head = None
        pre_head = ListNode(-1, head)
        while pre_head.next != None:
            cur_head = pre_head.next
            cur_head_next = cur_head.next
            pre_head.next = cur_head_next
            cur_head.next = reversed_head
            reversed_head = cur_head
        return reversed_head