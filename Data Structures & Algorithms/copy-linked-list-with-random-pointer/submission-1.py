"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_new = dict()
        dummy = head
        new_head = None
        while dummy:
            node_new = Node(dummy.val)
            if not new_head:
                new_head = node_new
            old_new[id(dummy)] = node_new
            dummy = dummy.next
        dummy = head
        while dummy:
            dummy_new = old_new[id(dummy)]
            if dummy.next:
                new_next = old_new[id(dummy.next)]
                dummy_new.next = new_next
            if dummy.random:
                new_rand = old_new[id(dummy.random)]
                dummy_new.random = new_rand
            dummy = dummy.next
        return new_head