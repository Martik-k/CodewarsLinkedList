class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


def push(head, data):
    '''
    >>> push(Node(1), 2).data == 2
    True
    >>> push(Node(1), 2).next.data == 1
    True
    '''
    if head is None:
        return Node(data)
    else:
        node = Node(data)
        node.next = head
    return node

def build_one_two_three():
    '''
    >>> build_one_two_three().data
    1
    >>> build_one_two_three().next.data
    2
    >>> build_one_two_three().next.next.data
    3
    >>> build_one_two_three().next.next.next
    '''
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.next = node2
    node2.next = node3
    return node1


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())