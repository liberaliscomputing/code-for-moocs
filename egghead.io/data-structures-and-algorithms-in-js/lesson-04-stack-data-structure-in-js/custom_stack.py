class CustomStack:
  def __init__(self):
    self.stack = []

  def push(self, item):
    self.stack.append(item)

  def pop(self):
    self.stack.pop()

  def peek(self):
    return self.stack[self.size - 1]

  def size(self):
    return len(self.stack)

  def is_empty(self):
    return self.size() == 0