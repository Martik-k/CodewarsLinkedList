class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def stringify(node):
    result = []
    while node:
        result.append(str(node.data))
        node = node.next
    result.append('None')
    return ' -> '.join(result)


def remove_duplicates(head):
    if head is None or head.next is None:
        return head
    current = head
    while current.next.next is not None:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    if current.data == current.next.data:
        current.next = None
    return head

ex1 = Node(1)
ex2 = Node(3)
ex3 = Node(8)
ex4 = Node(8)
ex1.next = ex2
ex2.next = ex3
ex3.next = ex4
print(stringify(remove_duplicates(ex1)))


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
