# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head = ListNode(-1)
        flag = 0
        while l1 or l2:
            v1, v2 = l1.val if l1 else 0, l2.val if l2 else 0
            v0 = v1 + v2 + flag
            flag, curr = v0 // 10, v0 % 10
            dummy.next = ListNode(curr)
            dummy = dummy.next
            l1, l2 = l1.next if l1 else None, l2.next if l2 else None
        if flag == 1:
            dummy.next = ListNode(1)
        return head.next