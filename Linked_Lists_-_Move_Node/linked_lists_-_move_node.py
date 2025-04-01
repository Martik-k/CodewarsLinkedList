class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
def move_node(source, dest):
    '''
    >>> source = Node(1)
    >>> source.next = Node(2)
    >>> dest = Node(3)
    >>> dest.next = Node(4)
    >>> new_source = move_node(source, dest).source
    >>> new_source.data
    2
    >>> new_dest = move_node(source, dest).dest
    >>> new_dest.data
    1
    >>> new_dest.next.data
    3
    >>> new_dest.next.next.data
    4
    '''
    new_source = source.next
    new_dest = Node(source.data)
    new_dest.next = dest
    return Context(new_source, new_dest)


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
