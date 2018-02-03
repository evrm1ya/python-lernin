# Container of data that links to one or more nodes

class NodeOne:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class NodeTwo:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.previous = None

if __name__ == '__main__':
    n1 = NodeOne({ "a": 1, "b": 2 })
    print(n1)

    n2 = NodeOne('a')
    n3 = NodeOne('b')

    n2.next = n3
    print(n2.next)
    print(n3.next)

    n4 = NodeTwo('c')
    n5 = NodeTwo('d')
    n6 = NodeTwo('e')

    n4.next = n5
    n5.previous = n4
    n5.next = n6
    n5.previous = n4
    n6.previous = n5

    print(n5)
    print(n5.next)
    print(n6.previous)
    print(n6)

