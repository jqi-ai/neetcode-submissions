# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_head = ListNode(-1, None)
        tracker = merged_head
        while list1 and list2:
            if list1.val < list2.val:
                list1_next = list1.next
                list1.next = None
                tracker.next = list1
                tracker = tracker.next
                list1 = list1_next
            else:
                list2_next = list2.next
                list2.next = None
                tracker.next = list2
                tracker = tracker.next
                list2 = list2_next
        if list1:
            tracker.next = list1
        if list2:
            tracker.next = list2
        return merged_head.next