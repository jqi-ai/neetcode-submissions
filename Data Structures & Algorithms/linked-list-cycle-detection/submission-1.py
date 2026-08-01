# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pacman_slow = head
        pacman_fast = head
        while pacman_fast and pacman_fast.next and pacman_fast.next.next:
            pacman_slow = pacman_slow.next
            pacman_fast = pacman_fast.next.next
            if pacman_slow == pacman_fast:
                return True
        return False