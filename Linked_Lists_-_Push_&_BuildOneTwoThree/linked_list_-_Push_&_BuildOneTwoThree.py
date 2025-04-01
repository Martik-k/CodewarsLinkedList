class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    
    def __repr__(self):
        return f'({self.data}, {self.next})'


def push(head, data):
    '''
    >>> push(Node(1), 2).data == 2
    True
    >>> push(Node(1), 2).next.data == 1
    True
    '''
    result = Node(data)
    while head:
        result.next = head
        head = head.next
    return result

def build_one_two_three():
    # Your code goes here.
    return Node(None)

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())