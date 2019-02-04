from node import Node


class Graph:
  def __init__(self, directed=False):
    self.directed = directed
    self.nodes = []
    self.edges = []

  def add_node(self, key):
    self.nodes.append(Node(key))

  def get_node(self, key):
    for node in self.nodes:
      if node.key == key:
        return node
    return None

  def add_edge(self, key_1, key_2):
    node_1 = self.get_node(key_1)
    node_2 = self.get_node(key_2)

    node_1.add_neighbor(node_2)
    self.edges.append('{}-{}'.format(key_1, key_2))

    if not self.directed:
      node_2.add_neighbor(node_1)
  
  def print(self):
    return list(map(lambda node: {node.key: node.neighbors}, self.nodes))