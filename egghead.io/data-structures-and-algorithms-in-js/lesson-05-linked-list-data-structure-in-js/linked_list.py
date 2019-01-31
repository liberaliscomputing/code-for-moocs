from node import Node


class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  def push(self, value):
    node = Node(value)

    if not self.head:
      self.head = node
      self.tail = node
      self.size += 1

      return node

    self.tail.succ = node
    self.tail = node
    self.size += 1

    return node

  def pop(self):
    if self.is_empty():
      return None

    node = self.tail

    if self.head == self.tail:
      self.head = None
      self.tail = None
      self.size -= 1

      return node

    curr = self.head
    penultimate = None
    while curr:
      if curr.succ == self.tail:
        penultimate = curr
        break

      curr = curr.succ

    penultimate.succ = None
    self.tail = penultimate
    self.size -= 1

    return node

  def get(self, index):
    if index < 0 or index > self.size - 1:
      return None

    if index == 0:
      return self.head

    curr = self.head
    i = 0
    while i < index:
      curr = curr.succ
      i += 1

    return curr

  def delete(self, index):
    if index < 0 or index > self.size - 1:
      return None

    curr = self.head

    if index == 0:
      self.head == self.head.succ
      self.size -= 1

      return curr

    prev = None
    i = 0
    while i < index:
      prev = curr
      curr = curr.succ
      i += 1
    
    prev.succ = curr.succ

    if not prev.succ:
      self.tail = prev

    self.size -= 1

    return curr

  def is_empty(self):
    return self.size == 0

  def print(self):
    values = []
    curr = self.head

    while curr:
      values.append(curr.value)
      curr = curr.succ

    return ' => '.join(map(str, values))