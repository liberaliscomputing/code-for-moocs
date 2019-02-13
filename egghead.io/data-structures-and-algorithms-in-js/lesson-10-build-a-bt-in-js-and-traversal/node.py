class Node:
  def __init__(self, data):
    self.data = data
    self.prev = None
    self.succ = None

  def add_node(self, data):
    node = Node(data)

    if data < self.data:
      self.prev = node
    else:
      self.succ = node
    
    return node