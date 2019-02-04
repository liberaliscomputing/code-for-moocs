class CustomQueue {
  constructor() { 
    this.queue = []; 
  }

  enqueue(item) { 
    this.queue.unshift(item); 
  }

  dequeue() { 
    return this.queue.pop(); 
  }

  peek() { 
    return this.queue[this.size - 1]; 
  }

  get size() { 
    return this.queue.length;
  }

  isEmpty() { 
    return this.size === 0; 
  }
}

module.exports = CustomQueue;
