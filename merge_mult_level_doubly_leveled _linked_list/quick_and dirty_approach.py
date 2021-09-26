# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None

        current_node = head

        if current_node.child:
            self.flattten_child(current_node)

        while current_node.next:
            if current_node.child:
                self.flattten_child(current_node)
            if current_node.next:
                current_node = current_node.next
            else:
                break

        return head

    def flattten_child(self, node):
        curr_node = node
        tail = curr_node.next
        curr_node.next = curr_node.child
        curr_node.child = None

        if curr_node.next:
            curr_node.next.prev = curr_node

        while curr_node:
            if curr_node.child:
                self.flattten_child(curr_node)

            if curr_node.next:
                curr_node = curr_node.next
            else:
                break

        curr_node.next = tail
        if tail:
            tail.prev = curr_node
