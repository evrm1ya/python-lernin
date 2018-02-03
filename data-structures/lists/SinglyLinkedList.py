from Node import NodeOne

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def faster_append(self, data):
        node = NodeOne(data)

        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.tail = node
            self.head = node

        self.size += 1

    def slow_append(self, data):
        node = NodeOne(data)

        if self.head == None:
            self.head = node
        else:
            current = self.head

            while current.next:
                current = current.next

            current.next = node

        self.size += 1

    def iter(self):
        current = self.head

        while current:
            val = current.data
            current = current.next
            yield val

    def delete(self, fn):
        '''Delete if fn(val) == True'''
        current = self.head
        previous = self.head

        while current:
            if fn(current.data):
                val = current.data
                previous.next = current.next

                if current == self.tail:
                    self.tail = previous

                self.size -= 1
                return val

            previous = current
            current = current.next


if __name__ == '__main__':
    sll = SinglyLinkedList()

    sll.slow_append('a')
    sll.slow_append('b')
    sll.slow_append('c')

    print(sll.head)
    print(sll.head.next)
    print(sll.head.next.next)
    print(sll.size)

    sll2 = SinglyLinkedList()
    sll2.faster_append('d')
    sll2.faster_append('e')
    sll2.faster_append('f')

    print(sll2.head)
    print(sll2.head.next)
    print(sll2.head.next.next)
    print(sll2.tail)
    print(sll2.size)

    for val in sll2.iter():
        print(val)

    sll3 = SinglyLinkedList()
    sll3.faster_append('a')

    def equals(string):
        def fn(data):
            return string == data

        return fn

    deleted1 = sll3.delete(equals('a'))
    print(deleted1)

    sll4 = SinglyLinkedList()
    sll4.faster_append('a')
    sll4.faster_append('b')
    sll4.faster_append('c')

    deleted2 = sll4.delete(equals('b'))
    print('deleted2', deleted2)
    print(sll4.head)
    print(sll4.head.next)
    print(sll4.tail)
    print(sll4.size)

    deleted3 = sll4.delete(equals('c'))
    print('deleted3', deleted3)
    print(sll4.head)
    print(sll4.tail)
