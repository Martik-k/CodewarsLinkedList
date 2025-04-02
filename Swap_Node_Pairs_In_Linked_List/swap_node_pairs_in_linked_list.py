class Node:
    def __init__(self, next=None, data = None):
        self.next = next
        self.next.data = data


def swap_pairs(head):
    if head is None:
        return None

    result = Node()
    result.next = head

    current = head
    prev = result
    while current and current.next:
        next_pair_prev = current.next
        next_pair_current = next_pair_prev.next

        prev.next = next_pair_prev
        next_pair_prev.next = current
        current.next = next_pair_current

        prev = current
        current = next_pair_current

    return result.next

