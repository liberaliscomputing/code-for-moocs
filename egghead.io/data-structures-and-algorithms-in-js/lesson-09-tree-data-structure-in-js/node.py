class Node:
  def __init__(self, key):
    self.key = key
    self.children = []

  def add_child(self, key):
    child = Node(key)
    self.children.append(child)

    return child