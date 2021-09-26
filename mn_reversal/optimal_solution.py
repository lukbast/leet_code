# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_between(head: ListNode, m: int, n: int) -> ListNode:
    curr_pos = 1
    curr_node = head
    start = head

    # find the beginning of the reversal
    while curr_pos < m:
        start = curr_node
        curr_node = curr_node.next
        curr_pos += 1

    new_list = None
    tail = curr_node

    while n >= curr_pos >= m:
        next = curr_node.next
        curr_node.next = new_list
        new_list = curr_node
        curr_node = next
        curr_pos += 1

    start.next = new_list
    tail.next = curr_node

    if m > 1:
        return head
    else:
        return new_list
