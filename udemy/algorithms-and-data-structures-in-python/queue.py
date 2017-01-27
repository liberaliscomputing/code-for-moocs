class Queue(object):

	def __init__(self):
		self.queue = list()
		self.size = 0

	def is_empty(self):
		return self.size == 0

	def enqueue(self, data):
		self.queue.insert(0, data)
		self.size += 1

	def dequeue(self):
		if self.size == 0:
			return 'Queue is already empty.'
		self.size -= 1
		self.queue.pop(self.size)

	def peek(self):
		return self.queue[self.size - 1]

	def get_size(self):
		return self.size

	def get_items(self):
		return self.queue


if __name__ == '__main__':
	queue = Queue()