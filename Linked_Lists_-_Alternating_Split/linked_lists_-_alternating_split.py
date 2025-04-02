class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

    
def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError

    first = head
    second = head.next

    prev = head
    cur = head.next
    while cur and cur.next:
        next_prev = cur.next
        next_cur = next_prev.next

        prev.next = next_prev
        cur.next = next_cur

        prev = next_prev
        cur = next_cur
    if cur:
        prev.next = None

    return Context(first, second)
