import os
import sys
sys.path.append(
  '/'.join(os.getcwd().split('/')[:-1] + [
    'lesson-06-js-graph-data-structure'
  ])
)
sys.path.append(
  '/'.join(os.getcwd().split('/')[:-1] + [
    'lesson-02-queue-data-structure-in-js'
  ])
)

from graph import Graph
from custom_queue import  CustomQueue


class SearchGraph(Graph):
  def breadth_first_search(self, key, func):
    head = self.get_node(key)
    hist = { node.key: False for node in self.nodes }
    custom_queue = CustomQueue()
    custom_queue.enqueue(head)

    while not custom_queue.is_empty():
      curr = custom_queue.dequeue()

      if not hist[curr.key]:
        func(curr)
        hist[curr.key] = True
      
      for neighbor in curr.neighbors:
        if not hist[neighbor.key]:
          custom_queue.enqueue(neighbor)
  
  def depth_first_search(self, key, func):
    head = self.get_node(key)
    hist = { node.key: False for node in self.nodes }

    def traverse(node):
      if hist[node.key]: return

      func(node)
      hist[node.key] = True

      for neighbor in node.neighbors:
        traverse(neighbor)
    
    traverse(head)    