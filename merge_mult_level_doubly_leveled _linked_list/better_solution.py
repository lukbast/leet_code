# Definition for a Node.
class Node:
    def __init__(self, val, prev, nxt, child):
        self.val = val
        self.prev = prev
        self.next = nxt
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None

        curr_node = head
        while curr_node:
            if not curr_node.child:
                curr_node = curr_node.next
            else:
                tail = curr_node.child
                while tail.next:
                    tail = tail.next

                tail.next = curr_node.next
                if tail.next:
                    tail.next.prev = tail

                curr_node.next = curr_node.child

                curr_node.next.prev = curr_node
                curr_node.child = None

        return head
