import os
import sys
sys.path.append(
  '/'.join(os.getcwd().split('/')[:-1] + [
    'lesson-02-queue-data-structure-in-js'
  ])
)

from custom_queue import CustomQueue


class PriorityQueue:
  def __init__(self):
    self.high_priority_queue = CustomQueue()
    self.low_priority_queue = CustomQueue()

  def enqueue(self, item, is_high_priority=False):
    if is_high_priority:
      self.high_priority_queue.enqueue(item)
    else:
      self.low_priority_queue.enqueue(item)

  def dequeue(self):
    if not self.high_priority_queue.is_empty():
      self.high_priority_queue.dequeue()
    else:
      self.low_priority_queue.dequeue()

  def peek(self):
    if not self.high_priority_queue.is_empty():
      return self.high_priority_queue.peek()
    else:
      return self.low_priority_queue.peek()

  def length(self):
    return sum([
      self.high_priority_queue.size(),
      self.high_priority_queue.size()
    ])

  def is_empty(self):
    return (self.high_priority_queue.is_empty() and 
            self.high_priority_queue.is_empty())