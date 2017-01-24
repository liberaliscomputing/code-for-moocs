# -*- coding: utf-8 -*-

class Node(object):

	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList(object):

	def __init__(self):
		self.head = None
		self.size = 0

	def insert_start(self, data):
		node = Node(data)

		if not self.head:
			self.head = node
		else:
			node.next = self.head
			self.head = node

		self.size += 1

	def insert_end(self, data):
		node = Node(data)
		curr = self.head

		if not curr:
			self.head = node
		else:
			while curr.next:
				curr = curr.next
			curr.next = node

		self.size += 1

	def insert_at(self, data, index):
		if index == 0:
			self.insert_start(data)
		elif index > self.size:
			return 'Error: the index is out of range.'
		else:
			node = Node(data)
			prev = None
			curr = self.head
			i = 0

			while i < index:
				prev = curr
				curr = curr.next
				i += 1

			node.next = curr
			prev.next = node

			self.size += 1

	def delete_start(self):
		if self.head != None:
			if self.head.next:
				self.head = self.head.next
			else:
				self.head = None

			self.size -= 1

	def delete_end(self):
		if self.head != None:
			prev = None
			curr = self.head

			while curr.next:
				prev = curr
				curr = curr.next

			if not prev:
				self.head = None
			else:
				prev.next = None

			self.size -= 1

	def delete(self, data):
		if self.head != None:
			prev = None
			curr = self.head

			while curr.data != data:
				prev = curr
				curr = curr.next

			if not prev:
				self.head = None
			else:
				prev.next = curr.next

			self.size -= 1

	def traverse(self):
		curr = self.head

		while curr:
			print '{}'.format(curr.data)
			curr = curr.next

	def get_size(self):
		return self.size


if __name__ == '__main__':
	linked_list = LinkedList()