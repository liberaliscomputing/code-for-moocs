class Queue:
  def __init__(self):
    self.queue = [];

  def enqueue(self, item):
    self.queue.insert(0, item)

  def dequeue(self):
    self.queue.pop()

  def peek(self):
    return self.queue[len(self.queue) - 1]

  def length(self):
    return len(self.queue)

  def is_empty(self):
    return len(self.queue) == 0