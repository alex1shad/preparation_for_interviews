class Stack:

    def __init__(self):
        self.stack = []

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, new_item):
        self.stack.append(new_item)

    def pop(self):
        if len(self.stack) != 0:
            last_item = self.stack.pop()
            return last_item
        else:
            print('Stack is empty')

    def peek(self):
        if len(self.stack) != 0:
            return self.stack[-1]
        else:
            print('Stack is empty')

    def size(self):
        return len(self.stack)
