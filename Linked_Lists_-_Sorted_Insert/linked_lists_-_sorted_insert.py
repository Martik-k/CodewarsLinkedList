class Node():
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



def push(head, data):
    if head is None:
        return Node(data)
    else:
        node = Node(data)
        node.next = head
    return node


def build_one_two_three():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.next = node2
    node2.next = node3
    return node1


def sorted_insert(head, data):
    '''
    >>> ex1 = Node(1)
    >>> ex1.next = Node(2)
    >>> ex1.next.next = Node(3)
    >>> stringify(sorted_insert(ex1, 2.5)) == '1 -> 2 -> 2.5 -> 3 -> None'
    True
    '''
    add_node = Node(data)

    if head is None:
        return add_node

    if data <= head.data:
        add_node.next = head
        return add_node

    current = head
    while current.next is not None and current.next.data < data:
        current = current.next
    add_node.next = current.next
    current.next = add_node

    return head


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
