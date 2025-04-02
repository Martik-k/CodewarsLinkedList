class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


def stringify(node):
    result = []
    while node:
        result.append(str(node.data))
        node = node.next
    result.append('None')
    return ' -> '.join(result)


def reverse(head, previous_node=None):
    """
    >>> ex1 = Node(1)
    >>> ex2 = Node(3)
    >>> ex3 = Node(8)
    >>> ex1.next = ex2
    >>> ex2.next = ex3
    >>> stringify(reverse(ex1)) == '8 -> 3 -> 1 -> None'
    True
    """
    if not head:
        return previous_node
    next_node = head.next
    head.next = previous_node
    return reverse(next_node, head)


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())