class Queue {
  constructor() { 
    this.queue = []; 
  }

  enqueue(item) { 
    this.queue.unshift(item); 
  }

  dequeue() { 
    this.queue.pop(); 
  }

  peek() { 
    return this.queue[this.queue.length - 1]; 
  }

  get length() { 
    return this.queue.length;
  }

  isEmpty() { 
    return this.queue.length === 0; 
  }
}

module.exports = Queue;
