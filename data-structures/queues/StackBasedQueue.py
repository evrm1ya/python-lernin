class Queue:
    def __init__(self):
        # Inbound used to store elements added to queue
        self.inbound_stack = []

        # Elements can only be deleted from queue
        # through outbound stack
        self.outbound_stack = []

    def get_inbound_stack(self):
        return self.inbound_stack

    def get_outbound_stack(self):
        return self.outbound_stack

    def enqueue(self, data):
        self.inbound_stack.append(data)

    def dequeue(self):
        if not self.outbound_stack:
            while self.inbound_stack:
                self.outbound_stack.append(self.inbound_stack.pop())

        return self.outbound_stack.pop()

if __name__ == '__main__':
    q = Queue()

    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(7)
    print(q.get_inbound_stack())

    print(q.dequeue())
    print(q.get_inbound_stack())
    print(q.get_outbound_stack())
