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


def linked_list_from_string(s):
    '''
    >>> s = "1 -> 2 -> 3 -> None"
    >>> lst = linked_list_from_string(s)
    >>> stringify(lst) == "1 -> 2 -> 3 -> None"
    True
    '''
    list_s = s.split(' -> ')[:-1]
    if not list_s:
        return Node(None)

    list_int = list(map(int, list_s))

    result = Node(list_int.pop(0))
    current = result
    while list_int:
        value = list_int.pop(0)
        current.next = Node(value)
        current = current.next
    return result


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
