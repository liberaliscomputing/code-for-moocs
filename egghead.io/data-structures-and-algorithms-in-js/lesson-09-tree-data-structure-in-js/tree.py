from node import Node


class Tree:
  def __init__(self, key):
    self.root = Node(key)

  def print(self):
    def traverse(node, func, depth):
      func(node, depth)

      if len(node.children):
        for child in node.children:
          traverse(child, func, depth + 1)
    
    def indent(node, depth):
      print(node.key 
        if depth == 0 
        else '{}{}'.format(' ' * depth, node.key)
      )
    
    traverse(self.root, indent, 0)