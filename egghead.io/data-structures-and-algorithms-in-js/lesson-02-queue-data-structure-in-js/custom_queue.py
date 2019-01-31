class CustomQueue:
  def __init__(self):
    self.queue = [];

  def enqueue(self, item):
    self.queue.insert(0, item)

  def dequeue(self):
    self.queue.pop()

  def peek(self):
    return self.queue[self.size() - 1]

  def size(self):
    return len(self.queue)

  def is_empty(self):
    return self.size() == 0