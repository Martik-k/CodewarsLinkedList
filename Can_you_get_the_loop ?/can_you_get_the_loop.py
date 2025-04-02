class Node:
    def __init__(self):
        self.next = None

def loop_size(node):
    slow = node.next
    fast = node.next.next

    while fast != slow:
        slow = slow.next
        fast = fast.next.next
        if fast is None or fast.next is None:
            return 0

    slow = node
    while slow != fast:
        slow = slow.next
        fast = fast.next

    count = 1
    slow = slow.next
    while slow != fast:
        count += 1
        slow = slow.next

    return count
