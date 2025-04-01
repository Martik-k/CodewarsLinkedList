class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


def stringify(node):
    '''
    >>> stringify(Node(0, Node(1, Node(2, Node(3))))) == '0 -> 1 -> 2 -> 3 -> None'
    True
    >>> stringify(None) == 'None'
    True
    >>> stringify(Node(0, Node(1, Node(4, Node(9, Node(16)))))) ==  '0 -> 1 -> 4 -> 9 -> 16 -> None'
    True
    '''
    result = []
    while node:
        result.append(str(node.data))
        node = node.next
    result.append('None')
    return ' -> '.join(result)


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
