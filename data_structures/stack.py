class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def dispaly_all(self):
        for item in self.items:
            yield item


stack = Stack()
stack.push("RAZ")
stack.push("DVA")
stack.push("TRI")
stack.peek()
stack.dispaly_all()