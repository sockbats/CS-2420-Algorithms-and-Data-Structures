class Stack:
    def __init__(self):
        self.the_stack = []

    def push(self, item):
        """Adds an item to the top of the stack"""
        self.the_stack.append(item)

    def pop(self):
        """If the stack has an item, removes and returns the top item of the stack"""
        if len(self.the_stack) == 0:
            raise IndexError
        return self.the_stack.pop()

    def top(self):
        """If the stack has an item, returns the top item of the stack"""
        if len(self.the_stack) == 0:
            raise IndexError
        return self.the_stack[-1]

    def size(self):
        """Returns the length of the stack"""
        return len(self.the_stack)

    def clear(self):
        """Empties the stack"""
        self.the_stack = []
