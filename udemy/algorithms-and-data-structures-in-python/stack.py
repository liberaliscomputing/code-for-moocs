class Stack(object):

	def __init__(self):
		self.stack = list()
		self.size = 0

	def is_empty(self):
		return self.size == 0

	def push(self, data):
		self.stack.insert(self.size, data)
		self.size += 1

	def pop(self):
		if self.size == 0:
			return 'Stack is already empty.'
		self.size -= 1
		self.stack.pop(self.size)

	def peek(self):
		return self.stack[self.size - 1]

	def get_size(self):
		return self.size

	def get_items(self):
		return self.stack


if __name__ == '__main__':
	stack = Stack()