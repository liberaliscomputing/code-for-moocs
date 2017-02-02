# -*- coding: utf-8 -*-

class Node(object):
    
  def __init__(self, data):
    self.data = data
    self.next = None
        
class LinkedList(object):
    
  def __init__(self):
    self.head = None
    self.size = 0
  
  def insert(self, data, index=0):
    if index > self.size:
      return 'IndexError: list out of range'
    
    node = Node(data)
    curr = self.head
    prev = None

    for i in range(index):
      prev = curr
      curr = curr.next

    node.next = curr
    
    if not prev:
      self.head = node
    else:
      prev.next = node

    self.size += 1
      
  def delete(self, data):
    if self.size == 0:
      return 'LinkedList is empty.'

    curr = self.head
    prev = None
    
    while data != curr.data:
      prev = curr
      curr = curr.next

      if not curr:
        return 'No such item.'
        
    if not prev:
      self.head = curr.next
    else:
      prev.next = curr.next
        
    self.size -= 1
          
  def traverse(self):
    if self.size == 0:
      return 'LinkedList is empty.'
    
    curr = self.head

    while curr:
      print '{}'.format(curr.data)
      curr = curr.next
          
  def get_size(self):
    return self.size


if __name__ == '__main__':
	linked_list = LinkedList()