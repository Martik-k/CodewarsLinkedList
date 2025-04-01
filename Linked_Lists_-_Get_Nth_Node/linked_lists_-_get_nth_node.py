class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


def get_nth(node, index):
    '''
    >>> linked_list = Node(1, Node(2, Node(3, None)))
    >>> get_nth(linked_list, 0).data
    1
    >>> get_nth(linked_list, 1).data
    2
    >>> get_nth(linked_list, 2).data
    3
    >>> get_nth(linked_list, 3).data
    Traceback (most recent call last):
    IndexError
    >>> get_nth(linked_list, -1).data
    Traceback (most recent call last):
    IndexError
    >>> get_nth(None, 0) # Empty list
    Traceback (most recent call last):
    ValueError
    '''
    if node is None:
        raise ValueError
    
    if index < 0:
        raise IndexError
    
    current = node
    for _ in range(index):
        current = current.next
        if current is None:
            raise IndexError
    return current

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
