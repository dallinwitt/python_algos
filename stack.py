#Create a stack object that has the methods push, pop, peek, and get_stack

class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def get_stack(self):
        return self.items