class ListNode:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_


def detect_cycle(head: ListNode):
    hare = head
    tortoise = head
    while True:
        hare = hare.next
        tortoise = tortoise.next
        if hare is None:
            break
        else:
            hare = hare.next

        if tortoise == hare:
            break

    p1 = head
    p2 = tortoise

    while p1 is not p2:
        p1 = p1.next
        p2 = p2.next

    return p1
