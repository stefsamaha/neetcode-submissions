"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if head is None:
            return None

        # original node -> copied node
        copies = {None: None}

        current = head

        # first pass: create all copied nodes
        while current is not None:
            copies[current] = Node(current.val)
            current = current.next

        current = head

        # second pass: connect next and random pointers
        while current is not None:
            copied_node = copies[current]

            copied_node.next = copies[current.next]
            copied_node.random = copies[current.random]

            current = current.next

        return copies[head]
        
