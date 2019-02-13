from node import Node


class BinaryTree:
  def __init__(self, data):
    self.root = Node(data)

  def traverse(self, node, func, order):
    if node:
      if order == 'in':
        self.traverse(node.prev, func, 'in')
        func(node)
        self.traverse(node.succ, func, 'in')
      elif order == 'pre':
        func(node)
        self.traverse(node.prev, func, 'pre')
        self.traverse(node.succ, func, 'pre')
      elif order == 'post':
        self.traverse(node.prev, func, 'post')
        self.traverse(node.succ, func, 'post')
        func(node)